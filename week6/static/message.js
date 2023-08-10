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