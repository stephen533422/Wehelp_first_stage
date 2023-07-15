def find_and_print(messages):
    # print(type(messages))
    # messages is <dict>
    for key, value in messages.items():
        if ("18 years old") in value or "college student" in value or "legal age" in value or "vote" in value:
            print(key)
find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})
