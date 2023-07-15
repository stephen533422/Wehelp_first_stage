def calculate_sum_of_bonus(data):
    # data is <dict>
    # data["employees"] is <list>
    # data["employees"][0] is <dict>
    sum = 0
    for i in range(len(data["employees"])):
        salary = data["employees"][i]["salary"]
        rate = 1
        if type(salary) != int: 
            salary_TWD = salary.replace(",","")
            if "USD" in salary_TWD:
                salary_TWD = salary_TWD.strip("USD")
                rate = 30
            salary_TWD=int(salary_TWD) * rate
        else:
            salary_TWD = salary
        if data["employees"][i]["role"] == "Engineer":
            bonus = 0.04
        elif data["employees"][i]["role"] == "CEO":
            bonus = 0.1
        elif data["employees"][i]["role"] == "Sales":
            bonus = 0.05
        if data["employees"][i]["performance"] == "above average":
            bonus *= 1.2
        elif data["employees"][i]["performance"] == "average":
            bonus *= 1
        elif data["employees"][i]["performance"] == "below average":
            bonus *= 0.8
        sum = salary_TWD * bonus + sum
    print(int(sum))
calculate_sum_of_bonus({
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
}) # call calculate_sum_of_bonus function