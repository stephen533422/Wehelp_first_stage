def calculate_sum_of_bonus(data):
    # data is <dict>
    # data["employees"] is <list>
    # data["employees"][0] is <dict>
    sum = 0
    for i in range(len(data["employees"])):
        for key,value in data["employees"][i].items():
            if key == "salary":
                if type(value) != int: 
                    new_value = value.replace(",","")
                    new_value = new_value.strip("USD")
                    new_value=int(new_value)
                else: new_value = value
                sum += new_value
    print(sum)
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