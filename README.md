# NCTU-TA-fill

## NYCU(NCTU)-差勤-助教  
##### 有沒有覺得在差勤系統填助教時數有點浪費生命？  
##### 今天有個懶鬼浪費好多時間幫大家寫了code  
##### 只要填好的必要的資料，就可以讓電腦自動幫你完成差勤助教的時數填寫喔！  
  
  
## python module 清單:  
- selenium (以及下載相應的 webdriver)  
- pyautogui  
- intervals  
- bs4
- fake_useragent(optional):  
    - 若不使用請＃ 以下  
    '''
      ua = UserAgent(verify_ssl=False)  
      user_agent = ua.random  
      headers = {'user-agent': user_agent}  
    '''
  
  
## 使用方法:  
- 去release下載.py文件並用文字編輯開啟  
- 在第二區塊填寫必要的資料:  
  - project = ' 裡面的文字請在填寫時間區間的網頁 按右鍵,檢查 選擇相應的“選擇計畫編號”表單的"value" '  
- S字典:  
  - 可自定義時間區間(optional)  
- 打開terminal  
- 鍵入cd /YOUR_FILE_PATH/BLA/BLA/BLA  
- 鍵入python3 THE_FILE_NAME  
- 依指示操作即可  
  
  
markdown 學習中
