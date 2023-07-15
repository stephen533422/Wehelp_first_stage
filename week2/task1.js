function findAndPrint(messages){
    // console.log(messages)
    // console.log(typeof messages)
    for(const key in messages){
        if(messages[key].includes("18 years old")||messages[key].includes("college student")||
           messages[key].includes("legal age")||messages[key].includes("vote")){
            console.log(key);
        }
    }
}
findAndPrint({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
});