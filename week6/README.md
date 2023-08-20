# week 6
## 使用Python連線MySQL
*  使用mysql.connector
```python
import mysql.connector
```
*  建立connection物件
```python
connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1234"
)
```
*  建立cursor物件
```python
cursor = connection.cursor()
```
*  執行MySQL語句
```python
cursor.execute()
cursor.executemany()
```
範例:
```python
create_stmt= ("CREATE DATABASE IF NOT EXISTS website")
cursor.execute(create_stmt)
use_stmt= ("USE website")
cursor.execute(use_stmt)
create_stmt= ("""
    CREATE TABLE IF NOT EXISTS member (
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,    
        password VARCHAR(255) NOT NULL,    
        follower_count INT UNSIGNED NOT NULL DEFAULT 0,    
        time DATETIME NOT NULL DEFAULT NOW())"""
)
cursor.execute(create_stmt)
```
*  提交變更
```python
connection.commit()
```
範例:
```python
insert_stmt = "INSERT INTO message (member_id, content) VALUES( %s, %s);"
user_data = (id, content)
cursor.execute(insert_stmt, user_data)
connection.commit()
```
*  獲取資料
```python
cursor.fetchone() # 獲取查詢結果的單筆資料
cursor.fetchmany(n) # 獲取查詢結果的n筆資料
cursor.fetchall() # 獲取查詢結果的所有資料
```
*  使用dictionary cursor 根據欄位取值
```python
# 建立cursor時設定dictionary = True
cursor = connection.cursor(dictionary = True)
```
```html
<!--根據欄位名稱取值-->
<span class="member_name">{{ message["name"] }}</span>: {{ message["content"] }} 
{% if message["member_id"] == member_id %}
<input name="message_id" type="hidden" value="{{ message['id'] }}">
<button type="submit">X</button>
{% endif %}
```
