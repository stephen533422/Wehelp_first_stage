# week8
## 主題研究與實作
### CSS 選擇器的命名⽅式
* OOCSS<br/>
  OOCSS(Object-Oriented CSS)的設計模式是鼓勵開發者設計出的CSS複用性能夠達到極致，最終目的是希望你可以藉由一套CSS來設計日後幾百幾千頁的頁面，而不用再去額外新增Class。其中最主要代表的框架就是Bootstrap。<br/>
  OOCSS 的設計裡面每一個 class 都是一個可以直接使用的 CSS 獨立個體。<br>
  其設計理念為二:
  * Separation of Structure from Skin：分離結構與樣式。結構像是元素的大小，樣式像是顏色等。
    ```css
    .btn {
      width: 20px;
      height: 100px;
      color: red;
      background-color: red;
    }
    ```
    可以改寫成
    ```css
    .btn-red {
      color: red;
      background-color: red;
    }
    .btn {
      width: 20px;
      height: 100px;
    }
    ```
    其中 OOCSS 中的結構與樣式的分離也有一個叫做 utilities 的觀念，也就是小工具，例如 padding、margin、border 及 width 等都可以作為一個小工具使用:
    ```css
    .pt-5 {
      padding-top: 5px;
    }
    
    .mt-5 {
      margin-top: 5px;
    }
    
    .border-all {
      border: 1px solid #000000;
    }
    
    .w-100 {
      width: 100%;
    }
    ```
  * Separation of Containers and Content：分離 HTML 與 CSS，意即盡量將可共用的樣式提取到單獨的 class 以供使用。
    ```css
    .header {
      color: yellow;
      width: 50px;
      height: 50px;
    }
    .content {
      color: red;
      width: 50x;
      height: 50px;
    }
    .footer {
      color: blue;
      width: 50px;
      height: 50px;
    }
    ```
    可以改寫成
    ```css
    .container {
      width: 50px;
      height: 50px;
    }
    
    .header {
      color: yellow;
    }
    .content {
      color: red;
    }
    .footer {
      color: blue;
    }
    ```
* SMACSS<br/>
  SMACSS(Scalable and Modular Architecture for CSS)指可擴展與模組化的設計模式。
  將結構分為五類:<br/>
  * Base: 所有網站的基礎架構，做全站設定為主，把最常用的東西全部先設定好。<br/>
    例如`margin: 0;`、`padding: 0;`、CSS Reset。
  * Layout: 主要用於共用的頁面，網站布局為主。<br/>
    主要的layout使用ID selectors，次要的layout使用class selectors。<br/>
    抽象語義化命名，抽象出共用樣式，通常 Layout 會有一個前綴詞 l-。<br/>
    例如:header、footer、nav。
    ```css
    #article {
      width: 80%;
      float: left;
    }
    #sidebar {
      width: 20%;
      float: right;
    }
    .l-fixed #article {
      width: 600px;
    }
    .l-fixed #sidebar {
      width: 200px;
    }
    ```
  * Module: 新增基底，再改換樣式(子模組)，很像前面OOCSS提到的「分離結構與樣式」。<br/>
    通常只用class來命名，不要使用ID selectors或tag，且要特別注意css的優先權。<br/>
    例如: `<button type="button" class="btn btn-red">red</button>`。
  * State: 用於新增狀態，通常與 Layout class 和 Module class 一起使用。<br/>
    例如:錯誤時添加個`.is-error`，成功時添加個`.is-success`的 class。
  * Theme: 主要用於設定網站主題的形式。<br/>
    例如:網頁的 dark mode。
* BEM<br/>
  BEM 是一種 CSS class 命名的設計模式，其由 Yandex 公司提出，將介面切割成許多獨立的區塊，以區塊（Block）、元素（Element）和修飾子（Modifier）來命名。<br/>
  優點是以元件觀念進行開發，具有重用性。它擁有 OOCSS 的架構清楚的美好，也沒有 SMACSS 複雜或令人混淆的部份。<br/>
  另外，由於 BEM 是功能導向的，因此不會像是 OOCSS 或 SMASS 可能會出現為了區別樣式而產生像是 .mt-15（翻譯：margin-top: 15px）這種讓人難以理解的 class 名稱。<br/>
  先看一個[官網](http://getbem.com/)的案例:
  ![](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_1_3.jpg)
  * 特色
    * Block name 描述他的功能、區塊的目的，而非狀態。
    * 不會添加樣式在裡面(例如：color, margin…等)。(因為要重複使用)
    * 使用BEM 的同時，不會使用 CSS 標籤選擇器和 ID 選擇器。
    * Block 命名方式：為單一單字`block`或使用1個破折號來連接過長的單字`block-name`。
    * Element 是 Block 中的组成成分。
    * Element 不能脫離 Block 單獨使用；但 Block 可以沒有 Element。
    * Element 命名方式:`block-name__element-name`。
    * Modifier name 定義了 Block 或 Element 的外觀，狀態或行為的實體。
    * 同一個 Block name 或 Element name 可以允許多組 Modifier name。
    * Modifier 命名方式：`block-name__element-name--modifier`。(原本的命名方式為1個底線 _，但因為閱讀性低而改良為現在的方式。)
    * 例外:並非所有的 CSS 命名方式都要如此，當某些 CSS 設定可重複使用時，就可以獨立出來，讓該設定被重複使用。
      ```css
      .clearfix{
          clear:both
      }
      .caps { 
          text-transform: uppercase; 
      } 
      ```
* Reference
  * https://hackmd.io/@YIHQx96xTI-K9vDjhzEfDA/S1TBmnon9
  * https://www.cythilya.tw/2018/06/05/css-methodologies/
  * https://ithelp.ithome.com.tw/articles/10236146
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
  * same-origin 相同來源<br/>
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
  * 如何開放我們⾃⼰開發的 API，讓別的網站透過 fecth() 或是 XMLHttpRequest 連結，
達到如同第 3 點的可能性。<br/>
      fetch和XMLhttprequest都是會跟從同源政策<br/>
      如果我想發出跨來源請求的話，對方的伺服器必須在回應表頭(response header)裏加上`Access-Control-Allow-Origin`，並在`Access-Control-Allow-Origin`的設定裏，新增我的Origin(即是我的網址)，或者設定為萬用字符`*`，代表所有Origin都接受，這是在公共API裏常見的設定。
* Refrerence
  * https://ithelp.ithome.com.tw/articles/10253549
  * https://www.appsecmonkey.com/blog/same-origin-policy
---
### 使⽤主鍵、索引優化資料庫查詢效率
* Primary key
* index
### 使⽤ Connection Pool 連結資料庫
* Connection Pool
### 了解並預防 Cross-Site Scripting (XSS) 攻擊
* XSS
