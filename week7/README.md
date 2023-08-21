# week 7
## 建立API
### Python back-end
*  新增Endpoint
```python
@app.route("/api/member", methods=["GET"])
```
```python
@app.route("/api/member", methods=["PATCH"])
```
*  使用db_config 儲存 connect參數
```python
db_config = {
  'host': 'localhost',
  'user': 'root',
  'password': '1234',
  'database': 'website',
}
connection = mysql.connector.connect(**db_config)
```
*  回傳Response Body
```python
data={"id":userdata["id"], "name":userdata["name"], "username":userdata["username"]}
return_data={"data":data}
# jsonify() 轉換JSON格式
return flask.jsonify(return_data)
```
*  API接收PATCH Request，並回傳response
```python
# 使用get_json() 轉換JSON格式
newname=flask.request.get_json().get("name")
```
### Javascript front-end
*  JS使用fetch()獲取response
```JavaScript
// fetch 預設method為 GET
function getData(url){
    return fetch(url).then((response) => response.json());
}
// 使用method = PATCH 傳送request
// JSON.stringify() 傳送JSON格式
function patchData(url, data){
    return fetch(url, {
        method: "PATCH",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
        },
    }).then((response) => response.json());
}
```
*  也可使用XMLHttpRequest
```Javascript
//待補
```
