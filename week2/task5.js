function findIndexOfCar(seats, status, number){
    let seats_left=[];
    const max_int=2**63-1;
    let min=max_int;
    let min_index=-1;
    for(const i in seats){
        if(status[i] && seats[i]-number>=0){
            seats_left.push(seats[i]-number);
        }
        else{
            seats_left.push(max_int);
        }
        if(seats_left[i]<min){
            min=seats_left[i];
            min_index=i;
        }
    }
    console.log(min_index);
}
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2