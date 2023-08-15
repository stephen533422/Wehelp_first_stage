function checkForm(){
    //console.log("Check");
    let name = document.getElementById("signupName");
    let username = document.getElementById("signupUsername");
    let password = document.getElementById("signupPassword");
    if(name.value===""){
        alert("請輸入姓名");
        return false;
    }
    else if(username.value===""){
        alert("請輸入帳號");
        return false;
    }
    else if(password.value===""){
        alert("請輸入密碼");
        return false;
    }
    else{
        return true;
    }
}

