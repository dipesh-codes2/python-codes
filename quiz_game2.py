print("QUIZ GAME ......")

score = 0

print("what is the capital of india \n")

print("options..")
print("A. mumbai ")
print("B. new delhi ")
print("C. lucknow ")
print("D. kolkata \n")

a = input("enter  your choice : ")

if a.lower()=="b":
    
    print("correct\n")
    score +=1
    
else:
    print("incorrect")
    
print("NEXT QUESTION....")

print("which language is used to create web pages ")

print("options..")
print("A. python ")
print("B. c ")
print("C. html ")
print("D. java\n ")

a = input("enter  your choice : ")

if a.lower() == "c":
    print("correct\n")
    score +=1
    
else:
    print("incorrect")
    
print("NEXT QUESTION....")

    
print("what is the result of 5*4 ")

print("options..")
print("A. 20 ")
print("B. 45 ")
print("C. 67 ")
print("D. 54 \n")

b = input("enter  your choice : ")

if b.lower() == "a":
    print("correct\n")
    score +=1
    
else:
    print("incorrect")
    
print("NEXT QUESTION....")

print("which is the following is an input functon in python ")    

print("options..")
print("A. scanf()")
print("B. printf()")
print("C. len() ")
print("D. input()\n")

b = input("enter  your choice : ")

if b.lower() =="d":
    print("correct\n")
    score +=1
    
else:
    print("incorrect\n")
    
print("NEXT QUESTION....")

print("which symbol is used to comments in python  ")

print("options..")
print("A. // ")
print("B. # ")
print("C. /*/ ")
print("D. @ \n")

c = input("enter  your choice : ")

if c.lower() =="b" :
    print("correct\n")
    score +=1
    
else:
    print("incorrect")
    
if score == 5:
    print("very good")
    
elif score == 4:
    print("very good")
    
elif score == 3:
    print("good")
    
elif score == 2:
    print("not good")
    
if score <=2:
    print("bad")
    
print("your score is : ",score)