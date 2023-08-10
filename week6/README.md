# week 6
## 使用Python連線MySQL
*  使用mysql.connector
```python
import mysql.connector
```
*  建立connection物件
```python
connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234"
)
```
*  建立cursor物件
```python
cursor = connection.cursor()
```
*  執行MySQL語句
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
