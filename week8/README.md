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

    >The same-origin policy is a critical security mechanism that restricts how a document or script 
    loaded by one origin can interact with a resource from another origin.
    
    同源政策是重要的安全性機制，其限制一個origin的document或script，與另一個origin資源的互動。

    >It helps isolate potentially malicious documents, reducing possible attack vectors. For example, it 
    prevents a malicious website on the Internet from running JS in a browser to read data from a third-
    party webmail service (which the user is signed into) or a company intranet (which is protected from 
    direct access by the attacker by not having a public IP address) and relaying that data to the attacker.
    
    同源政策幫助隔離那些潛在的惡意文件，避免可能的惡意攻擊。例如，可以避免惡意網站在瀏覽器取得第三方網路
    郵件伺服器的資料(使用者已經登入的)，或公司內部網路(攻擊者沒有公開IP地址而無法直接存取)而中繼資料給攻擊者。
  * same-origin 相同來源
    
    ![](https://www.appsecmonkey.com/_next/image?url=%2Fstatic%2Fimages%2Fsame-origin-policy%2Ffigure-1.jpg&w=1920&q=75)<br/>
    ( image credict: https://www.appsecmonkey.com/blog/same-origin-policy )<br/>
    MDN example:

    |URL 	|Outcome 	|Reason|
    |---|---|---|
    |http://store.company.com/dir2/other.html 	      |`diff + Same origin `|Only the path differs|
    |http://store.company.com/dir/inner/another.html |`diff + Same origin `|Only the path differs|
    |https://store.company.com/page.html 	           |`diff - Failure `    |Different protocol|
    |http://store.company.com:81/dir/page.html 	     |`diff - Failure `　  |Different port (http:// is port 80 by default)|
    |http://news.company.com/dir/page.html 	         |`diff - Failure `    |Different host|

### 使⽤主鍵、索引優化資料庫查詢效率
* Primary key
* index
### 使⽤ Connection Pool 連結資料庫
* Connection Pool
### 了解並預防 Cross-Site Scripting (XSS) 攻擊
* XSS
