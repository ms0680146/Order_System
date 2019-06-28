# Order System
依據提供的資料(<a href="https://s3-ap-northeast-1.amazonaws.com/urmart-dev/%E6%B8%AC%E8%A9%A6%E8%B3%87%E6%96%99+-+order.csv">訂單</a> / <a href="https://s3-ap-northeast-1.amazonaws.com/urmart-dev/%E6%B8%AC%E8%A9%A6%E8%B3%87%E6%96%99+-+order_item.csv">訂單商品</a>)建立的Django專案
****
## Techniques
* 01 Python version 3.6
* 02 Django version 2.1
* 03 Sqlite3 (built-in django)
* 04 <a href="https://github.com/chartjs/Chart.js">Chart.js package</a>
* 05 Docker
* 06 <a href="https://dashboard.heroku.com/Heroku">Heroku</a>

## Functions
* 01 訂單免運比例圓餅圖  
* 02 畫出用戶及下訂行為的同類群組分析表(Cohort) (以天為週期)
* 03 最受用戶歡迎的商品前三名
* 04 單元測試
* 05 Docker環境下開發
* 06 部屬到Heroku上

## Results
成果網站連結:<br><br>
首頁: https://order-system-kai.herokuapp.com/home/ <br><br>
![](https://imgur.com/NACehVo.png)
免運比例圓餅圖: https://order-system-kai.herokuapp.com/piechart/ <br><br>
![](https://imgur.com/qnmIWmk.png)
同類群組分析表: https://order-system-kai.herokuapp.com/cohort/ <br><br>
![](https://imgur.com/IbfmrSi.png)
最受用戶歡迎的商品前三名: https://order-system-kai.herokuapp.com/barchart/ <br><br>
![](https://imgur.com/pAplB7M.png)
