# week8
## 主題研究與實作
### CSS 選擇器的命名⽅式
* OOCSS
* SMACSS
* BEM
### 完善資料驗證程序
* front-end
* back-end
### AJAX 與 CORS
* CROS
  * same-origin policy 同源政策
    ```
    The same-origin policy is a critical security mechanism that restricts how a document or script 
    loaded by one origin can interact with a resource from another origin.
    限制不同來源的document或script與其他來源的互動
    ```
    ```
    It helps isolate potentially malicious documents, reducing possible attack vectors. For example, it 
    prevents a malicious website on the Internet from running JS in a browser to read data from a third-
    party webmail service (which the user is signed into) or a company intranet (which is protected from 
    direct access by the attacker by not having a public IP address) and relaying that data to the attacker.
    為了避免可能的惡意攻擊
    ```
  * same-origin 相同來源
![](https://www.appsecmonkey.com/_next/image?url=%2Fstatic%2Fimages%2Fsame-origin-policy%2Ffigure-1.jpg&w=1920&q=75)
    MDN example:
|URL 	|Outcome 	|Reason|
|---|---|---|
|http://store.company.com/dir2/other.html 	|Same origin 	|Only the path differs|
|http://store.company.com/dir/inner/another.html 	|Same origin 	|Only the path differs|
|https://store.company.com/page.html 	|Failure 	|Different protocol|
|http://store.company.com:81/dir/page.html 	|Failure 	|Different port (http:// is port 80 by default)|
|http://news.company.com/dir/page.html 	|Failure 	|Different host|
### 使⽤主鍵、索引優化資料庫查詢效率
* Primary key
* index
### 使⽤ Connection Pool 連結資料庫
* Connection Pool
### 了解並預防 Cross-Site Scripting (XSS) 攻擊
* XSS
