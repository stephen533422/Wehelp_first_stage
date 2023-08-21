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
* CROS ( Cross-Origin Resource Sharing 跨來源資源共享 )
  * same-origin policy 同源政策

    >The same-origin policy is a critical security mechanism that restricts how a document or script 
    loaded by one origin can interact with a resource from another origin.
    
    同源政策是重要的安全性機制，其限制一個origin的document或script，與另一個origin資源的互動。

    >It helps isolate potentially malicious documents, reducing possible attack vectors. For example, it 
    prevents a malicious website on the Internet from running JS in a browser to read data from a third-
    party webmail service (which the user is signed into) or a company intranet (which is protected from 
    direct access by the attacker by not having a public IP address) and relaying that data to the attacker.
    
    同源政策幫助隔離那些潛在的惡意文件，避免可能的惡意攻擊。例如，可以避免惡意網站在瀏覽器取得第三方網路郵件伺服器的資料(使用者已經登入的)，或公司內部網路(攻擊者沒有公開IP地址而無法直接存取)而中繼資料給攻擊者。
  * same-origin 相同來源
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_4_1.jpg)
    ( image credict: https://www.appsecmonkey.com/blog/same-origin-policy )<br/>
    MDN example:

    |URL 	|Outcome 	|Reason|
    |---|---|---|
    |http://store.company.com/dir2/other.html 	      |$\textcolor{green}{Same origin}$|Only the path differs|
    |http://store.company.com/dir/inner/another.html |$\textcolor{green}{Same origin}$|Only the path differs|
    |https://store.company.com/page.html 	           |$\textcolor{red}{Failure}$      |Different protocol|
    |http://store.company.com:81/dir/page.html 	     |$\textcolor{red}{Failure}$      |Different port (http:// is port 80 by default)|
    |http://news.company.com/dir/page.html 	         |$\textcolor{red}{Failure}$      |Different host|
  * 甚麼是CROS?
    >**Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.** CORS also relies on a mechanism by which browsers make a "preflight" request to the server hosting the cross-origin resource, in order to check that the server will permit the actual request. In that preflight, the browser sends headers that indicate the HTTP method and headers that will be used in the actual request.
  * 我們可以在⾃⼰的網⾴中，使⽤ fetch() 或是 XMLHttpRequest 連結到https://www.google.com/ 並取得回應嗎？
    ```.js
    fetch("https://www.google.com" )
      .then((response) => response.json())
      .then((json) => { console.log(json);})
    ```
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_4_2.jpg)
    會得到錯誤訊息( status: CORS error	)，仔細看會發現`No 'Access-Control-Allow-Origin' header is present on the request resource.`
  * 我們可以在⾃⼰的網⾴中，使⽤ fetch() 或是 XMLHttpRequest 連結到https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 並取得回應嗎？和上述的狀況，差別在哪裡？
    ```.js
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" )
      .then((response) => response.json())
      .then((json) => { console.log(json);})
    ```
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_4_3.jpg)
    可以發現有取得回應，查看Response Headers會發現有`Access-Control-Allow-Origin: *`
  * Access-Control-Allow-Origin
    fetch和XMLhttprequest都是會跟從同源政策<br/>
    如果我想發出跨來源請求的話，對方的伺服器必須在回應表頭(response header)裏加上`Access-Control-Allow-Origin`，並在`Access-Control-Allow-Origin`的設定裏，新增我的Origin(即是我的網址)，或者設定為萬用字符`*`，代表所有Origin都接受，這是在公共API裏常見的設定。
   * Refrerence
     https://ithelp.ithome.com.tw/articles/10253549
     https://www.appsecmonkey.com/blog/same-origin-policy
   ---
### 使⽤主鍵、索引優化資料庫查詢效率
* Primary key
* index
### 使⽤ Connection Pool 連結資料庫
* Connection Pool
### 了解並預防 Cross-Site Scripting (XSS) 攻擊
* XSS
