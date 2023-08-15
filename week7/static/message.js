function checkDel(){
    if(confirm("確認是否刪除此留言")){
        return true;
    }
    else{
        return false;
    }
}
function checkContent(){
    //console.log("Check");
    let content = document.getElementById("content");
    if(content.value===""){
        alert("請輸入留言內容");
        return false;
    }
    else{
        return true;
    }
}
function getData(url){
    return fetch(url).then((response) => response.json());
}
function patchData(url, data){
    return fetch(url, {
        method: "PATCH",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
        },
    }).then((response) => response.json());
}
function searchUser(username){
    //console.log("username=",username);
    let url = "/api/member?username=" + username
    getData(url)
    .then((responseJSON)=>{
        let searchName;
        if(responseJSON.data==null){
            searchName = "查無用戶";
            let result = document.querySelector(".search .result");
            result.textContent=searchName;
        }
        else{
            searchName = responseJSON.data.name;
            let result = document.querySelector(".search .result");
            result.textContent=searchName+"("+username+")";
        }
    })
    .catch((error)=>{
        console.log(`Error: ${error}`);
    });
}
function changeName(newname){
    let url = "/api/member"
    patchData(url, {"name": newname})
    .then((responseJSON)=>{
        if(responseJSON.ok){
            let result = document.querySelector(".rename .result");
            result.textContent="更新成功";
            let message_text = document.querySelector(".message .text");
            message_text.textContent = newname + "，歡迎登入系統"
        }
        else if(responseJSON.error){
            let result = document.querySelector(".rename .result");
            result.textContent="更新失敗";
        }
    })
    .catch((error)=>{
        console.log(`Error: ${error}`);
    });
}