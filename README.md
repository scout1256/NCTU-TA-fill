# NCTU-TA-fill

## 填寫 差勤-助教時數
##### 有沒有覺得在差勤系統填助教時數有點浪費生命？  
##### 今天有個懶鬼浪費好多時間幫大家寫了code  
##### 只要填好的必要的資料，就可以讓電腦自動幫你完成差勤助教的時數填寫喔！  
  
  
## python module 清單:
- selenium (以及下載相應的 webdriver)  
- pyautogui  
- intervals  
- bs4
- fake_useragent (optional) :  
    - 若不使用請＃ 以下  
      ```
      from fake_useragent import UserAgent
      ```
      ```
      ua = UserAgent(verify_ssl=False)
      user_agent = ua.random
      headers = {'user-agent': user_agent}
      ```
  
  
## 使用方法:
- 下載NCTU-TA-fill.py文件並用文字編輯開啟  
- 在第二區塊填寫必要的資料:  
  - project = ' 裡面的文字請在填寫時間區間的網頁 按右鍵,檢查 選擇相應的“選擇計畫編號”表單的"value" '  
    ```
    project = '110T212^334816^200^138336'
    ```
  - Date = [想排除的日期] + [今天之後的日期] + [國定假日]  
    Date 條件: 1< Date[i] <=月底 and Date[i]不得重複  
    Example:  假設今天28號, 任意一式皆可  
    ```
    Date = [] + [x+1 for x in range(td.day, we)] + list(range(2, 6))
    Date = [] + [29, 30] + [2, 3, 4, 5]
    Date = [] + [29, 30, 2, 3, 4, 5]
    Date = [] + [29, 2, 30, 3, 4, 5]
    Date = [3, 29, 4, 30, 5, 2]
    ```
  - Week = [想排除的節數]  
    可填入1, 2, 3, 4, 5, 6, 7, 8, 9, 'am', 'pm', 'all'
    ```
    Sun = ['pm']
    Mon = [2,4,6,8,'all']
    Tue = [2,4,6,8,'pm']
    Wed = []  # 可以空著, 但不能刪掉
    ...
    ```
- S字典:  
  - 可自定義時間區間(optional)
    ```
    S = {1: I.closedopen("08:00", "08:50"), 2: I.closedopen("09:00", "09:50"), 3: I.closedopen("10:10", "11:00"), 4: I.closedopen("11:10", "12:00"), 5: I.closedopen("13:20", "14:10"), 6: I.closedopen("14:20", "15:10"), 7: I.closedopen("15:30", "16:20"), 8: I.closedopen("16:30", "17:20"), 9: I.closedopen("17:30", "18:20"),
     'all': I.closedopen("08:00", "18:20"),  # 可自定義區間
     'am': I.closedopen("08:00", "12:00"),
     'pm': I.closedopen("13:00", "18:20")}
     ```
- 打開terminal  
- 鍵入```cd /Users/......./Downloads/.......```
- 鍵入```python3 THE_FILE_NAME.py```
- 程式運行時, 請勿移動/捲動滑鼠或新開其他程式
- 依指示操作即可
  - ```k``` : 刪除 簽到單/時數
  - ```m``` : 手動操作
  - ```km``` = ```k``` + ```m```


## 示範影片:


https://user-images.githubusercontent.com/71586456/115279930-e4ff8d80-a179-11eb-84bd-54d9f5c03dbe.mov




https://user-images.githubusercontent.com/71586456/115280285-5a6b5e00-a17a-11eb-8f63-913f8a36b1d9.mov




https://user-images.githubusercontent.com/71586456/115280109-21cb8480-a17a-11eb-8539-3e0083092fff.mov



###### markdown 學習中
