# Week 5
## Task 3:
*  使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```sql
INSERT INTO member (name, username, password) VALUES ("test","test","test");
INSERT INTO member (name, username, password) VALUES ("ann","ann222","ann");
INSERT INTO member (name, username, password) VALUES ("alex","alex123","alex");
INSERT INTO member (name, username, password) VALUES ("alice","alice777","alice");
INSERT INTO member (name, username, password) VALUES ("allen","allen666","allen");
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
SELECT * FROM (SELECT *,ROW_NUMBER() OVER (ORDER BY time DESC) AS row_id FROM member)sorted LIMIT 1,3;
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
|  欄位名稱  |  資料型態  |  額外設定                                   |  用途說明      |
|:---------|:-----------|:------------------------------------------|:-------------| 
| id       |bigint      |主鍵、⾃動遞增                             |獨立編號      |
|member_id |bigint      |不可為空值<br>外鍵對應 member 資料表中的 id|留⾔者會員編號|
|content   |varchar(255)|不可為空值                                 |留⾔內容      |
|like_count|int unsigned|不可為空值，預設為 0                       |按讚的數量    |
|time      |datetime    |不可為空值，預設為當前時間                 |留⾔時間|
*  在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message。
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5.jpg)
*  使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。
```sql
SELECT member.name, message.content, message.like_count, message.time FROM member 
INNER JOIN message ON member.id = message.member_id;
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5-1.jpg)
*  使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者的姓名。
```sql
SELECT member.name, message.content, message.like_count, message.time FROM member 
INNER JOIN message ON member.id = message.member_id WHERE username = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5-2.jpg)
*  使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
```sql
SELECT AVG(like_count) FROM member INNER JOIN message ON member.id = message.member_id WHERE username = "test";
```
![image](https://github.com/stephen533422/wehelp_first_stage/blob/main/week5/pic/task5-3.jpg)
