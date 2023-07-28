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
function squareCal(){
    let num = document.getElementById("square_num").value;
    if(parseInt(num)>0){
        location.href = "/square/" + num;
    }
    else{
        alert("Please enter a positive number");
    }
}
