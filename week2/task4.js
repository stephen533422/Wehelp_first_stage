function getNumber(index){
    let number=0
    for(let i=0; i<=index; i++){
        if(i==0){
            number=number+0;
        }
        else if(i%2==0){
            number=number-1;
        }
        else if(i%2==1){
            number=number+4;
        }
    }
    console.log(number);
}
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15