function func(...data){
    //console.log(data)
    //console.log(typeof data)
    let name=[]
    let tag=false
    for(const key in data){
        name.push(data[key][1])
    }
    for(const key in name){
        if(name.filter(x => x === name[key]).length === 1){
            tag=true
            console.log(data[key])
        }
    }
    if(tag === false){
        console.log("沒有")
    }
}
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有