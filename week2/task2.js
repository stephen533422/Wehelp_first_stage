function calculateSumOfBonus(data){
    //console.log(data);
    //console.log(typeof(data));
    //console.log(data["employees"]);
    let sum=0;
    for(const i in data["employees"]){
        for(const key in data["employees"][i]){
            if(key === "salary"){
                if(typeof(data["employees"][i][key])!="number"){
                    var new_value=data["employees"][i][key].replace(",","");
                    new_value=new_value.replace("USD","");
                    new_value=parseInt(new_value,10);
                }
                else{
                    new_value=data["employees"][i][key];
                }
                sum=sum+new_value;
            }
        }
    }
    console.log(sum);
}
calculateSumOfBonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}); // call calculateSumOfBonus function