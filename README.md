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
- fake_useragent (optional) :  
    - 若不使用請＃ 以下  
    ```
    ua = UserAgent(verify_ssl=False)  
    user_agent = ua.random  
    headers = {'user-agent': user_agent}  
    ```
  
  
## 使用方法:
- Release下載.py文件並用文字編輯開啟  
- 在第二區塊填寫必要的資料:  
  - project = ' 裡面的文字請在填寫時間區間的網頁 按右鍵,檢查 選擇相應的“選擇計畫編號”表單的"value" '  
- S字典:  
  - 可自定義時間區間(optional)  
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
