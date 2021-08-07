print("Welcome!!")
person = input("Please enter your name for better experience: ")
print("Hey "+person+" Welcome!!")

score = 0
questions = 5

print(person+" Are you ready to play?? ")
ready = input()
if ready == "yes":
    question1 = input("What is the color of an apple?? ")
    if question1 =="red":
        score +=1
        print(person+" Your answer is Correct 👌👍")
    else:
        print(person+" Your answer is incorrect 😥😥")

    print("Note: Give your answer in integer only")
    question2 = int(input("How many letters are there in alphabets?? "))
    if question2 == 26:
        score +=1
        print(person+" Your answer is Correct 👌👍")
    else:
        print(person+" Your answer is incorrect 😥😥")

    question3 = input("Which planet is known as red planet?? ")
    if question3 =="mars":
        score +=1
        print(person+" Your answer is Correct 👌👍")
    else:
        print(person+" Your answer is incorrect 😥😥")

    question4 = input("In which direction soes the sun rise?? ")
    if question4 =="east":
        score +=1
        print(person+" Your answer is Correct 👌👍")
    else:
        print(person+" Your answer is incorrect 😥😥")

    question5 = input("Have you subscribe Code With Niranjan?? ")
    if question5 =="yes":
        score +=1
        print(person+" Very good 👌👍")
    else:
        score -=1
        print(person+" Go and subscribe now 😥😥")
        
    print("Very good try "+ person)
    print("Your details\nYour name: " + str(person) + "\nYour score: "+str(score))
    print("\nYou got "+str(score)+" Out of "+ str(questions))
    final_marks = (score/questions)*100
    print("You percentage is "+ str(final_marks)+ "%")

else:
    print("Ok")
    print("Come again Soon!!!")
    print("Closing!")
