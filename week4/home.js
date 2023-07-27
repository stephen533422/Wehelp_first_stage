function checkForm(){
    let agree_checkbox = document.getElementById("agree_checkbox");
    if(!agree_checkbox.checked){
        alert("Please check the checkbox first");
        return false;
    }
    else{
        return true;
    }
}
