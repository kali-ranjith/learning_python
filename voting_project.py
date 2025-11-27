print("*"*80)
print("\n \n \t \t \t \t Election 2026 \n \n")
print("*"*80)

paricipents = {
    "TVK":{ 
        "Canditade":"Vijay"

    },
    "DMK":{
         "canditade":"stalin"
     },
    "ADMK":{
         "candatade":"Palani samy"
     }
}

vote = {
    "TVK":0,
    "DMK":0,
    "ADMK":0
}


voters_information = []



try:
    while True:
        name = input("Enter your name : ")
        age = int(input("Enter your age : "))

        if age < 18:
            print("You're not able to Vote")
            continue

        j = 0
        for i in paricipents:
            j = j + 1
            print("select " + str(j) + " for " + str(i))

        choice = int(input())

        selected_party = list(vote.keys())[choice-1]

        voters_information.append({
            "name": name,
            "age": age,
            "vote": selected_party

        })

        vote[selected_party] += 1



        print("*"*30 , " Election Result ", "*"*30)


        print(vote)


        print(voters_information)


        print("*"*80)

except KeyboardInterrupt:
    print("\nVoting interrupted by user.")





