# Week 5
## pre-processing:
*  透過終端機 Command Line 介⾯，連結到 MySQL 伺服器中進行管理。
```
cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
```
```
./mysql -u root -p
```
  輸入安裝時設定的 root 密碼

*  建立⼀個新的資料庫，取名字為 website。
```
CREATE DATABASE website;
```
*  使用資料庫```USE <name>```
```
USE website;
```
*  在資料庫中，建立會員資料表，取名字為 member。

|  欄位名稱    |  資料型態  |  額外設定                                 |  用途說明    |
|:---------    |:-----------|:------------------------------------------|:-------------| 
| id           |bigint      |主鍵、⾃動遞增                             |獨立編號      |
|name          |varchar(255)|不可為空值                                 |姓名          |
|username      |varchar(255)|不可為空值                                 |帳戶名稱      |
|password      |varchar(255)|不可為空值                                 |帳戶密碼      |
|follower_count|int unsigned|不可為空值，預設為 0                       |追蹤者數量    |
|time          |datetime    |不可為空值，預設為當前時間                 |註冊時間      |

```
CREATE TABLE member (    
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,    
    password VARCHAR(255) NOT NULL,    
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,    
    time DATETIME NOT NULL DEFAULT NOW()
    );
```
*  顯示資料表的內容```DESC <name>```
```
DESC member;
```
*  刪除資料庫或資料表
```
DROP DATABASE <name>
DROP TABLE <name>
```
## Task 3:
*  使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```sql
INSERT INTO member (name, username, password, follower_count) VALUES ("test","test","test", 0);
INSERT INTO member (name, username, password, follower_count) VALUES ("ann","ann222","ann", 5);
INSERT INTO member (name, username, password, follower_count) VALUES ("alex","alex123","alex", 10);
INSERT INTO member (name, username, password, follower_count) VALUES ("alice","alice777","alice", 20);
INSERT INTO member (name, username, password, follower_count) VALUES ("allen","allen666","allen", 30);
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-1.jpg)
*  使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```sql
SELECT * FROM member;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-2.jpg)
*  使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```sql
SELECT * FROM member ORDER BY time DESC;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-3.jpg)
*  使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。
```sql
SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-4.jpg)
*  使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```sql
SELECT * FROM member WHERE username = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-5.jpg)
*  使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```sql
SELECT * FROM member WHERE username = "test" AND password = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-6.jpg)
*  使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```sql
UPDATE member SET name = "test2" WHERE username = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task3-7.jpg)
***
## Task 4:
*  取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```sql
SELECT COUNT(*) FROM member;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task4-1.jpg)
*  取得 member 資料表中，所有會員 follower_count 欄位的總和。
```sql
SELECT SUM(follower_count) FROM member;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task4-2.jpg)
*  取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```sql
SELECT AVG(follower_count) FROM member;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task4-3.jpg)
***
## Task 5:
1. 在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。

|  欄位名稱  |  資料型態  |  額外設定                                 |  用途說明    |
|:---------  |:-----------|:------------------------------------------|:-------------| 
| id         |bigint      |主鍵、⾃動遞增                             |獨立編號      |
|member_id   |bigint      |不可為空值<br>外鍵對應 member 資料表中的 id|留言者會員編號|
|content     |varchar(255)|不可為空值                                 |留言內容      |
|like_count  |int unsigned|不可為空值，預設為 0                       |按讚的數量    |
|time        |datetime    |不可為空值，預設為當前時間                 |留言時間      |
```
CREATE TABLE message (    
    id BIGINT primary key auto_increment,
    member_id BIGINT NOT NULL,
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,    
    time DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY(member_id) REFERENCES member(id)
    );  
INSERT INTO message (member_id, content, like_count)
VALUES (1,"hi",6),
       (3,"hello",9),
       (4,"hihi",8),
       (2,"hey",1),
       (5,"yo",6),
       (1,"hi",6),
       (1,"hello",9),
       (5,"hihi",8),
       (2,"hey",1),
       (3,"yo",6);
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5.jpg)
*  使⽤ SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者的姓名。
```sql
SELECT member.name, message.content, message.like_count, message.time FROM member 
INNER JOIN message ON member.id = message.member_id;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5-1.jpg)
*  使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者的姓名。
```sql
SELECT member.name, message.content, message.like_count, message.time FROM member 
INNER JOIN message ON member.id = message.member_id WHERE username = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5-2.jpg)
*  使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
```sql
SELECT AVG(like_count) FROM member INNER JOIN message ON member.id = message.member_id WHERE username = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5-3.jpg)
