### 要求三： SQL CRUD

1. 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

    ```
    INSERT member(name,username,password,follower_count) VALUES ( "Kimmy","test","test","100");
    INSERT member(name,username,password,follower_count) VALUES ( "Gina","gina1","ginap1","88");
    INSERT member(name,username,password,follower_count) VALUES ( "Paul","paul54","paul083","234");
    INSERT member(name,username,password,follower_count) VALUES ( "Wen","wen23593","wen0348","348");
    INSERT member(name,username,password,follower_count) VALUES ( "Lisa","lisa24","lisa245824","9483");
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午5 53 33" src="https://user-images.githubusercontent.com/94777104/151335688-a6b05c58-5dfb-4db7-b023-ec1098a2c2cc.png">
    
    ---

2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

    ```
    SELECT * FROM member;
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午5 55 53" src="https://user-images.githubusercontent.com/94777104/151335895-4adc9862-4534-4e23-98bb-06255356d655.png">

    ---
    
3. 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

    ```
    SELECT * FROM member ORDER BY time DESC;
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午5 58 32" src="https://user-images.githubusercontent.com/94777104/151336119-efee3040-a41f-44e7-9f86-7a89acfbe492.png">
    
    ---
    
 4. 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。

    ```
    SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午6 00 41" src="https://user-images.githubusercontent.com/94777104/151336583-8e4ab986-4a28-4731-aa12-804f4467b752.png">
    
    ---
    
5. 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

    ```
    SELECT * FROM member WHERE username = "test";
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午6 03 22" src="https://user-images.githubusercontent.com/94777104/151336901-56b9fd41-70e2-493e-a905-9d6ad9ca7748.png">
    
    ---
  
6. 使用 SELECT 指令取得欄位 username 是 test 且欄位 password 也是 test 的資料。

    ```
    SELECT * FROM member WHERE username = "test" AND password = "test";
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午6 05 35" src="https://user-images.githubusercontent.com/94777104/151337220-546193e8-87ce-4b1b-ad60-ebdb246cdb01.png">
    
    ---
    
7. 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
  
    ```
    UPDATE member SET name = "test2" WHERE username = "test";  
    ```

    <img width="950" alt="截圖 2022-01-27 下午6 07 51" src="https://user-images.githubusercontent.com/94777104/151337607-2fcbeefa-a447-4101-a84a-aa1eca0d7861.png">

---

### 要求四： SQL Aggregate Functions

1. 取得 member 資料表中，總共有幾筆資料（幾位會員）。

    ```
    SELECT COUNT(*) FROM member;
    ```

    <img width="950" alt="截圖 2022-01-27 下午6 13 14" src="https://user-images.githubusercontent.com/94777104/151338484-b9975079-1323-482b-aaf8-408c0e88845d.png">

    ---
  
2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。

    ```
    SELECT SUM(follower_count) FROM member;
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午6 15 50" src="https://user-images.githubusercontent.com/94777104/151338975-748486b7-36f0-4bf9-9398-fe741175e2de.png">

    ---
    
    
3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

    ```
    SELECT AVG(follower_count) FROM member;
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午6 15 50" src="https://user-images.githubusercontent.com/94777104/151339036-0967b87b-81f7-4e41-bc4a-efa3f6d61a78.png">
    
---

### 要求五：SQL JOIN

1. 在資料庫中，建立新資料表，取名字為 message 。
    * 建立資料表
    
      ```
      CREATE TABLE message (
      id BIGINT PRIMARY KEY AUTO_INCREMENT,
      member_id BIGINT NOT NULL,
      content VARCHAR(255) NOT NULL,
      time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (member_id) REFERENCES member(id)
      );
      ```
    
      <img width="950" alt="截圖 2022-01-27 下午6 21 46" src="https://user-images.githubusercontent.com/94777104/151339823-81c3457d-95a2-49d5-b0e7-a06d3c5ba830.png">

    
    * 新增資料
    
      ```
      INSERT message ( member_id , content ) VALUES ( 1 , "大家早安");
      INSERT message ( member_id , content ) VALUES ( 1 , "你有打疫苗了嗎？");
      INSERT message ( member_id , content ) VALUES ( 2 , "晚餐要吃什麼？");
      INSERT message ( member_id , content ) VALUES ( 4 , "新年快樂！");
      ```
      
      <img width="950" alt="截圖 2022-01-27 下午6 22 24" src="https://user-images.githubusercontent.com/94777104/151340355-b5508508-9935-4330-8be0-836672d850c7.png">

    ---
      
2. 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

    ```
    SELECT message.id, member.name , message.content, message.time 
    FROM message JOIN member ON message.member_id = member.id;
    ```
    
    <img width="950" alt="截圖 2022-01-27 下午6 27 26" src="https://user-images.githubusercontent.com/94777104/151340798-878991ef-933a-4f20-90c6-9e82faaeef90.png">
    
    ---
    
3. 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

   ```
   SELECT message.id , member.name , message.content , message.time 
   FROM message JOIN member ON message.member_id = member.id
   WHERE member.username = "test";
   ```
   
   <img width="950" alt="截圖 2022-01-27 下午6 28 51" src="https://user-images.githubusercontent.com/94777104/151341000-f6c8ea40-d8d0-48e0-828c-587dc084cb1b.png">

---
