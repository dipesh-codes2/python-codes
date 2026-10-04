print("QUIZ GAME")
score = 0
a = input("what type of programming language is python : ").lower()
if a == "case sensitive":
    print("correct")
    score +=1

else:
    print("incorrect")

b = input("which brackets are used to create a list in python :  ").lower()
if b == "square":
    print("correct")
    score +=1

else:
    print("incorrect")

c = int(input("what is the result of 10+5 : "))
if c == 15:
    print("correct")
    score +=1

else:
    print("incorrect")

d = input("which function is used to display output in  :  ").lower()
if d == "print":
    print("correct")
    score +=1

else:
    print("incorrect")

e = input("how is data stored in a dictionary in python : ").lower()
if e == "key value pairs":
    print("correct")
    score +=1

else:
    print("incorrect")

print("your score is ", score)










