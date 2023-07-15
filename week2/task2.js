function calculateSumOfBonus(data){
    //console.log(data);
    //console.log(typeof(data));
    //console.log(data["employees"]);
    let sum=0;
    for(const i in data["employees"]){
        let salary = data["employees"][i]["salary"];
        rate = 1;
        if(typeof(salary) != "number"){
            var salary_TWD = salary.replace(",","");
            if(salary_TWD.includes("USD")){
                salary_TWD = salary_TWD.replace("USD","");
                rate = 30;
            }
            salary_TWD = parseInt(salary_TWD,10) * rate;
        }
        else{
            var salary_TWD = salary;
        }
        if(data["employees"][i]["role"] == "Engineer"){
            bonus = 0.04
        }
        else if(data["employees"][i]["role"] == "CEO"){
            bonus = 0.1
        }
        else if(data["employees"][i]["role"] == "Sales"){
            bonus = 0.05
        }
        if(data["employees"][i]["performance"] == "above average"){
            bonus *= 1.2
        }
        else if(data["employees"][i]["performance"] == "average"){
            bonus *= 1
        }
        else if(data["employees"][i]["performance"] == "below average"){
            bonus *= 0.8
        }
        sum = salary_TWD *bonus +sum;
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