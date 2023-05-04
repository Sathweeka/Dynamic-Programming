q1="""What is the name of Shahrukh Khan in the movie named 'Kabhi Khusi Kabhi Gham'?
a. Raj
b. Rahul
c. Kali
d. Rohan"""
q2=""" Which male actors were seen in the song 'Gali Mein Aaj Chand Nikla"?
a. Kunal Khemu
b. Ajay Devgan
c. Akkineni Nagarjuna
d. Rohan"""
q3="""What are two things you can never eat for breakfast?
a. Rice and Dal
b. Nuts and Fruits
c. Lunch and Dinner
d. Bread and Butter"""
q4="""Which is always coming but never arrives?
a. Past
b. Today
c. Yesterday
d. Tomorrow"""
q5="""What word is spelled incorrectly in every single dictionary?
a. Online
b. Prepare
c. Cloudy
d. Incorrectly"""

questions={q1:"b",q2:"c",q3:"c",q4:"d",q5:"d"}
name =input("Hi! Whats ur name")
print("Hello", name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this question (yes/no)")
    if flag1 == "yes":
        continue
    ans=input("enter your answer")
    if ans == questions[i]:
        print("Congrats! you got one point")
        score=score+1
        print("your current score is :",score)
    else:
        print("Wrong answer, you lost 1 mark")
        score=score-1
        print("your current score is :",score)
    flag2=input("Do you want to Quit? type(yes/no)")
    if flag2 == "yes":
        break
print("Your total score is",score)
print("Thank you...!")
