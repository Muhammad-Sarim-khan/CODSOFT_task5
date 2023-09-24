import time

#predefining some questions for the quiz
Questions=["1)What does 'HTML' stand for?\nA) Hyper Text Markup Language\nB) High Tech Modern Language\nC) Hyperlink and Text Markup Language\nD) Home Tool Markup LanguageAnswer\n","2)Which company developed the Windows operating system?\nA) AppleB) Google\nC) Microsoft\nD) IBM\n","3)What does 'CPU' stand for in computing?\nA) Central Processing Unit\nB) Computer Peripheral Unit\nC) Control Processing Unit\nD) Central Peripheral Unit\n","4)Which programming language is often used for artificial intelligence and machine learning?\nA) Java\nB) Python\nC) C++\nD) Ruby\n","5)What is the term for a network security system that monitors and filters incoming and outgoing network traffic?\nA) Firewall\nB) Router\nC) Modem\nD) Hub\n","6)What is the term for a cryptographic protocol used to secure internet communication, often indicated by 'https://' in website URLs?\nA) SSL\nB) FTP\nC) TCP\nD) HTTP\n","7)Which programming language was developed by JetBrains and is commonly used for Android app development?\nA) C#\nB) Java\nC) Kotlin\nD) Swift\n","8)What is the maximum data transfer rate of USB 3.0?\nA) 480 Mbps\nB) 1 Gbps\nC) 5 Gbps\nD) 10 Gbps\n","9)What does the acronym 'IoT' stand for in technology?\nA) Internet of Things\nB) Internet of Thinkers\nC) Information on Technology\nD) Internet of Telecommunications\n","10)What is the name of the open-source, container orchestration platform developed by Google?\nA) Docker\nB) Kubernetes\nC) Apache Hadoop\nD) Node.js\n"]

# correct options of answers of the defined questions
Answers=["A","C","A","B","A","A","C","C","A","B"]

#function to get the answer from user and calculate the user's score
def quiz_game():
    #initializing increment=0 to check for the answer at the specific index number
    increment=0
    score=0
    for i in Questions:
        time.sleep(0.5)
        print(i)
        time.sleep(0.5)
        user_ans=input("Answer : ").capitalize()
        if user_ans==Answers[increment]:
            time.sleep(0.5)
            print("Correct!\n")
            score+=1
        else:
            time.sleep(0.5)
            print("Incorrect!")
            time.sleep(0.5)
            print("The correct answer is : ",Answers[increment],"\n")
        increment+=1
    #printing the total achieved score of user
    if score>5:
        time.sleep(0.5)
        print("WELL DONE! YOUR TOTAL SCORE IS",score,",","\nYOU ANSWERED",score,"QUESTIONS CORRECTLY!")
    elif score<=5:
        time.sleep(0.5)
        print("NOT BAD! YOUR TOTAL SCORE IS",score,",","\nYOU ANSWERED",score,"QUESTIONS CORRECTLY!")

#main Interface
while True:
    ask=input("WELCOME TO THE QUIZ GAME APPLICATION PRESS ENTER TO START THE QUIZ!")
    print("-------------------------------------------------------------------------------------------------")
    time.sleep(0.5)
    print("RULES : THERE ARE 10 QUESTIONS RELATED TO INFORMATION TECHNOLOGY.\nFOUR OPTIONS WILL BE PROVIDED FOR YOU TO SELECT WITH EACH QUESTION. EACH QUESTION CARRY 1 MARK.")
    time.sleep(0.5)
    print("-------------------------------------------------------------------------------------------------")
    if ask=="":
        time.sleep(0.5)
        quiz_game()
        time.sleep(0.8)
        ask2=input("DO YOU WANT TO PLAY AGAIN??ENTER 'y' TO PLAY AGAIN AND 'n' TO EXIT\n").lower()
        if ask2=='y':
            quiz_game()
            break
        else:
            time.sleep(0.4)
            print("THANKS FOR PLAYING!!")
            break
    else:
        print("INVALID INPUT! PLEASE PRESS ENTER TO CONTINUE...")

