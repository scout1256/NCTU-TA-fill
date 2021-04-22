import datetime as dt
import getpass
from _datetime import datetime
from calendar import monthrange
from time import sleep
import intervals as I
import pyautogui
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
td = dt.date.today()
ws = td.replace(day=1).isoweekday()  # 星期幾開始
we = monthrange(td.year, td.month)[1]  # 幾號結束

# 必填資料
Date = [x+1 for x in range(td.day, we)] + list(range(2, 6)) + []  # 排除的日期(ex.國定假日) 2 <= Date <= we
Sun = ['all']
Mon = [1, 3, 2, 'am']  # 星期一的上課節數
Tue = []
Wed = []
Thu = []
Fri = []
Sat = ['all']
# project = '110T...^......^...^......'  # 計畫編號選單的value(如果bs4找不到可能會用到)
# tt = 0  # 總時數(如果bs4找不到可能會用到)


def Del(j):
    driver.find_element(By.ID, "node_level-1-1").click()
    sleep(1)
    while True:
        for i in range(j):
            ProgressBar(i+1, j, length=j, unit='/', a=10, decimals=0, mom=j)
            pyautogui.click(x=439, y=262)
            pyautogui.press('enter')
            sleep(1)
        j = FindC()
        if j == 0:
            print()
            print('時數已刪除！')
            break


def FindC():
    soup = BeautifulSoup(driver.page_source, 'html.parser').find("div", class_="w2ui-footer-right")  # 取得COUNT
    if not soup.string is None:
        return int(soup.string.split(' ')[2])
    else:
        return 0


def ProgressBar(iteration, total, unit='s', mom='', a=1, b=0, prefix='', suffix='', decimals=1, length=50, fill='█', unfill='-', printEnd="\r", finish="\n"):
    """
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        unit        - Optional  : unit (Str)
        a           - Optional  : ax+b (Float)
        b           - Optional  : ax+b (Float)
        mom         - Optional  : 分母 (Float)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        unfill      - Optional  : bar unfill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        finish      - Optional  : finish move (Str)
    """
    if mom == 0:
        mom = ''
    percent = ("{0:." + str(decimals) + "f}").format(a*total/10*(iteration / float(total))+b)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + unfill * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}{unit}{mom} {suffix}', end = printEnd)
    if iteration == total:  # Print New Line on Complete
        print(finish, end='')


def AskManual():
    ans = input('*** go Manual?  ').lower()
    if not (ans == 'no' or ans == 'n'):
        pyautogui.hotkey('command', 'tab')
        return True
    else:
        return False


S = {1: I.closedopen("08:00", "08:50"), 2: I.closedopen("09:00", "09:50"), 3: I.closedopen("10:10", "11:00"), 4: I.closedopen("11:10", "12:00"), 5: I.closedopen("13:20", "14:10"), 6: I.closedopen("14:20", "15:10"), 7: I.closedopen("15:30", "16:20"), 8: I.closedopen("16:30", "17:20"), 9: I.closedopen("17:30", "18:20"),
     'all': I.closedopen("08:00", "18:20"),  # 可自定義區間
     'am': I.closedopen("08:00", "12:00"),
     'pm': I.closedopen("13:00", "18:20")}
tn, ans, P, project, pdata, Plist = 0, 1, [], '', '', [[]]
done = kill = manual = test = False
X = [(k+ws-1)%7 for k in range(2, we+1)]  # x座標
Y = [int((k+ws-1)/7) for k in range(2, we+1)]  # y座標
W = {l+1: [X[l-1], Y[l-1]] for l in range(1, we)}
We = [Sun, Mon, Tue, Wed, Thu, Fri, Sat]
print('\n\n\n\n\n')
print('Date 原始排除日期: ')
print(sorted(Date), end='\n\n')
print('We 上課節數: ')
print(*We, sep='\n', end='\n\n')
print('W 座標: ', W, sep='\n', end='\n\n')

for k in Date:  # 刪除排除日期
    del W[k]
print('W 剩餘座標: ', W, sep='\n', end='\n\n')

for k in range(7):
    T = I.closedopen("08:00", "12:00") | I.closedopen("13:00", "17:00")  # 初始化, 可調整填入時間的上下限
    Te = I.empty()  #初始化
    for l in range(len(We[k])):  # 去除上課時間
        T = T - S[We[k][l]]
    if not T.is_empty():
        for l in range(len(T)):  # 找出小於30 min的T
            if (datetime.strptime(T[l].upper, '%H:%M') - datetime.strptime(T[l].lower, '%H:%M')).seconds < 1800:
                Te = Te | T[l]
        T = T - Te  # 去除小於30 min
        for key, val in W.items():  # 將interval加入val
            if val[0] == k:
                for i in range(len(I.to_data(T))):
                    for j in range(1, 3):
                        val.append(int(I.to_data(T)[i][j].split(':')[0]))
                        val.append(int(I.to_data(T)[i][j].split(':')[1]))
print('W:')
for key, val in W.items():
    print(key, ':', val)
print()

for i in range(50):  # ProgressBar
    ProgressBar(i + 1, 50, unit='%', a=20, decimals=0, finish='')
    # sleep(0.06 - i * 0.0012)
    sleep(0.000024 * (i - 50) ** 2 + 0.01)
j = ' |'
for i in range(50):  # 作者資訊
    j += 'This program is writen by scout1256/0752525       '[i]
    print(ProgressBar(i + 1, 50, unit='%', a=20, decimals=0, unfill='█', finish='', mom=' '), '\r', j, sep='', end='\r')
    sleep(0.1)
print('\n')

'''------------------------------------------------------開始操作------------------------------------------------------'''
if ans != 'no' and ans != 'n':
    username = input('Username (特殊變數 "k" = kill, "m" = manual, "d" = developer, "" = d+k): ')
    if any(i in username.lower() for i in ['k', 'm', 'd', '']) and len(username) <= 3:  # 刪除 簽到單/時數
        if 'm' in username.lower():
            manual = True
        if 'k' in username.lower() or username == '':
            kill = True
        if 'd' in username.lower() or username == '':
            username = '0752525'
            password = 'YOUR_PASSWORD'
        else:
            username = input('Real Username: ')
            password = getpass.getpass()  # 問密碼
    else:
        password = getpass.getpass()  # 問密碼
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.random
    headers = {'user-agent': user_agent}
    driver = webdriver.Chrome()
    driver.get('https://pt-attendance.nctu.edu.tw/verify/userLogin.php')
    driver.set_window_size(1280, 777)
    screenWidth, screenHeight = pyautogui.size()
    print(screenWidth, 'x', screenHeight, end='\n\n')
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    for i in range(40):
        sleep(0.1)
        soup = BeautifulSoup(driver.page_source, 'html.parser').find("h1", class_="align-middle")
        if not soup is None and soup.string == '您目前的請核列表':
            break
    '''--------------------------------------------------尋找 Plist--------------------------------------------------'''
    for tr in BeautifulSoup(driver.page_source, 'html.parser').tbody.find_all("tr"):
        Plist.append([td.string for td in tr.find_all("td")])
    '''['109T212', '學生公費獎助學金', '勞動型', '時薪', '200', '54', '2020-04-02', '2020-04-30', 可能(候選value)]'''

    pyautogui.click(x=30, y=180, duration=0.5)
    sleep(0.1)
    '''-----------------------------------------------------kill-----------------------------------------------------'''
    if kill:  # 刪除 簽到單/時數
        print('\n', 'Killing all now!', sep='')
        driver.find_element(By.ID, "node_level-1-4").click()
        sleep(1)
        for i in range(len(BeautifulSoup(driver.page_source, 'html.parser').find_all("div", title="待審"))):
            pyautogui.click(x=389, y=300)  # 選簽到單
            # driver.find_element(By.ID, "w2ui-grid-select-check").click()  # 選簽到單
            pyautogui.click(x=426, y=500)
            sleep(0.5)
        driver.find_element(By.ID, "node_level-1-1").click()
        sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser').find("div", class_="w2ui-footer-right")
        if not soup.string == None:
            Del(int(soup.string.split(' ')[2]))
        print('簽到單/時數 已刪除！', end='\n\n')

    '''----------------------------------------------尋找project, tt----------------------------------------------'''
    driver.find_element(By.ID, "node_level-1-1").click()
    for i in range(20):
        sleep(0.1)
        if not BeautifulSoup(driver.page_source, 'html.parser').find("select", id='pno') is None:
            pdata = BeautifulSoup(driver.page_source, 'html.parser').find("select", id='pno').find_all("option")
            break
    for i in range(1, len(Plist)):
        if datetime.strptime(Plist[i][6], '%Y-%m-%d').date() <= td <= datetime.strptime(Plist[i][7], '%Y-%m-%d').date():
            for j in range(1, len(pdata)):
                if pdata[j].string.split(' ')[0].replace('	', '').replace('\n', '').replace(':', '') in Plist[i]:
                    if pdata[j].string.split(' ')[1].split('~')[0] == Plist[i][6]:  # 日期相等
                        Plist[0].append(i)
                        Plist[i].append(pdata[j].get('value'))
    if len(Plist[0]) == 1:  # 本月只有一個 Project
        project = Plist[Plist[0][0]][8]
        # noinspection PyTypeChecker
        tt = int(Plist[Plist[0][0]][5])
    else:  # 本月不只一個 Project
        pyautogui.hotkey('command', 'tab')
        for i in Plist[0]:
            print(f'{i}. {Plist[i]}')
        while True:
            ans = input(f'which Project do you wish to fill?  {Plist[0]}  ')
            if ans == '':
                ans = Plist[0][0]
            elif not int(ans) in Plist[0]:
                continue
            project = Plist[int(ans)][8]
            tt = int(Plist[int(ans)][5])
            pyautogui.hotkey('command', 'tab')
            break
    '''--------------------------------------------------確認時數--------------------------------------------------'''
    for key, val in W.items():  # 確認可填時數是否 >= tt
        # noinspection PyUnboundLocalVariable
        if tn >= tt:
            break
        for k in range(2, len(val), 4):
            if tn >= tt:
                break
            tn += int((60 * val[k + 2] + val[k + 3] - 60 * val[k] - val[k + 1]) / 30) / 2
    if tn < tt:
        pyautogui.hotkey('command', 'tab')
        print('Lack', tt - tn, 'hr!!!!!!!!!!!!!!!')
        ans = input('*** Should we proceed?  ').lower()
        pyautogui.hotkey('command', 'tab')
        print()

    '''-----------------------------------------------------Auto-----------------------------------------------------'''
    while not done and not manual and ans != 'no' and ans != 'n':
        '''--------------------------------------------------填寫時數--------------------------------------------------'''
        pyautogui.click(x=30, y=180, duration=0.1)
        sleep(0.1)
        Select(driver.find_element_by_name('workP')).select_by_value(project)  # 選擇計畫
        sleep(0.5)
        tn, c, cdata= 0, 0, 0  # 初始化, 填寫時數
        for key, val in W.items():  # days
            if tn == tt:
                break
            elif len(val) > 2:
                print('\n', 'Day ', key, sep='')
            for k in range(2, len(val), 4):  # intervals
                while True:
                    if tn + int((60*val[k+2]+val[k+3]-60*val[k]-val[k+1])/30)/2 > tt:
                        val[k+2] = int(tt-tn + val[k]+val[k+1]/60)
                        val[k+3] = (60*(tt-tn) + 60*val[k]+val[k+1]) % 60
                    tn += int((60*val[k+2]+val[k+3]-60*val[k]-val[k+1])/30)/2
                    c += 1
                    if cdata == c - 1:
                        print('interval: ', "%02d"%val[k], ':', "%02d"%val[k+1], '-', "%02d"%val[k+2], ':', "%02d"%val[k+3], sep='')  # 印出要執行的區間
                        print('..........Total time now is '+str(tn)+' hr / +'+str(int((60*val[k+2]+val[k+3]-60*val[k]-val[k+1])/30)/2)+' hr / count: '+str(c))
                    Select(driver.find_element_by_name('workP')).select_by_value(project)  # 選擇計畫
                    sleep(0.1)
                    driver.find_element(By.NAME, "workS").click()
                    sleep(0.1)
                    pyautogui.click(x=484 + 39*val[0], y=441 + 26*val[1], clicks= 2, interval=0.01, duration=0.2)  # date
                    pyautogui.moveTo(576, 595, 0.2)
                    pyautogui.dragTo(576 + 136 / 23 * val[k], 595, 0.1, button='left')  # hour
                    if not val[k+1] == 0:
                        pyautogui.moveTo(576, 619, 0.1)
                        pyautogui.dragTo(576 + 136 / 59 * val[k+1], 619, 0.1, button='left')  # min
                    sleep(0.1)
                    driver.find_element(By.NAME, "workE").click()
                    pyautogui.click(x=484+39*val[0], y=441+26*(val[1]+1), clicks= 2, interval=0.01, duration=0.2)
                    pyautogui.moveTo(576, 621, 0.1)
                    pyautogui.dragTo(576 + 136 / 23 * val[k+2], 621, 0.1, button='left')  # hour
                    if not val[k+3] == 0:
                        pyautogui.moveTo(576, 645, 0.1)
                        pyautogui.dragTo(576 + 136 / 59 * val[k+3], 645, 0.1, button='left')  # min
                    sleep(0.1)
                    pyautogui.scroll(-2)
                    pyautogui.click(x=398, y=808)  # 點儲存
                    pyautogui.scroll(2)
                    for i in range(20):  # 等待 COUNT 顯現
                        ProgressBar(i+1, 20)
                        cdata = FindC()
                        if cdata == c:
                            break
                        sleep(0.1)
                    print()
                    if not cdata == c:  # 填寫的時數未儲存, 重新填一次
                        cdata = None
                        c += -1
                        tn += -int((60*val[k+2]+val[k+3]-60*val[k]-val[k+1])/30)/2
                        continue
                    break
                if tn == tt:
                    break
            sleep(0.2)
        print()
        '''--------------------------------------------------填寫完成--------------------------------------------------'''
        sleep(1)
        if tn == tt:  # tt相符
            if cdata == c:  # COUNT相符, 送出表單
                driver.find_element(By.ID, "node_level-1-2").click()
                sleep(1.5)
                driver.find_element(By.ID, "grid_grid_check_all").click()
                driver.find_element(By.ID, "btnSubmit").click()
                pyautogui.press('enter')
                sleep(2.5)
                pyautogui.press('esc')
                driver.find_element(By.ID, "node_level-1-4").click()  # check if tt is right
                for i in range(30):
                    sleep(0.1)
                    if BeautifulSoup(driver.page_source, 'html.parser').find("div", title="待審") is None:
                        continue
                    for soup in BeautifulSoup(driver.page_source, 'html.parser').find_all("div", title="待審"):
                        if soup.parent.next_sibling.next_sibling.div.string == str(tn):
                            done = True
                            if len(BeautifulSoup(driver.page_source, "html.parser").find_all("div", title="待審")) == 1:
                                print('Well Done!!!!!!!!!!!!!!!!!!!!!!!!\n')
                            elif BeautifulSoup(driver.page_source, 'html.parser').find_all("div", title="待審").index(soup) == len(BeautifulSoup(driver.page_source, "html.parser").find_all("div", title="待審")):
                                print(f'Done!! 時數相符且待審: {len(BeautifulSoup(driver.page_source, "html.parser").find_all("div", title="待審"))}\n')
                        else:
                            pyautogui.moveTo(700, 500, 0.1)
                            pyautogui.scroll(2)
                            pyautogui.click(x=389, y=300)
                            pyautogui.click(x=426, y=500)
                            sleep(2)
                            Del(c)
                            pyautogui.hotkey('command', 'tab')
                    break
            else:  # COUNT不符, 應該可刪
                pyautogui.hotkey('command', 'tab')
                print('COUNT is wrong!', '*** Delete all??', sep='\n', end='  ')
                ans = input('# press Y to continue......  ').lower()
                if ans == 'y' or ans == 'yes':  # 刪掉現有的時數
                    pyautogui.hotkey('command', 'tab')
                    Del(cdata)
                    pyautogui.hotkey('command', 'tab')
                else:  # 不刪, 改手動
                    manual = AskManual()
        else:  # 刪除時數
            pyautogui.hotkey('command', 'tab')
            print('Lack', tt - tn, 'hr')
            ans = input('*** Should we delete all?   press Y to continue......  ').lower()
            if ans == 'yes' or ans == 'y':
                pyautogui.hotkey('command', 'tab')
                Del(c)
                pyautogui.hotkey('command', 'tab')
                # 重來
            else:
                # manual = AskManual()
                manual = done = True
        if not done and not manual:
            ans = input('*** Should we do this again?  ').lower()
            if ans == 'no' or ans == 'n':
                driver.quit()
                break
            else:
                pyautogui.hotkey('command', 'tab')
    else:  # 完成 or 手動 or 不要繼續
        if manual:
            print('\nOk, You`re MANUAL now!!!')
            pyautogui.hotkey('command', 'tab')
        elif done:
            pyautogui.hotkey('command', 'tab')
            sleep(3)
            driver.quit()  # 完成 or 不要繼續
        else:
            driver.quit()

# python3 差勤-助教\ v1.6.py
