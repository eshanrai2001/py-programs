import sys
asking = input("do you want to play? ")
if asking.lower() != "yes":
  sys.exit("ok, letś play next time, Thank you!")
else:
  print("let's start the quiz")

score = 0
question1 = input("what does ram stands for?: ")
if question1.lower() == "random access memory":
  print("correct")
  score+=1
else:
  print("incorrect")


question2 = input("what does CPU stands for?: ")
if question2.lower() == "central processing unit":
  print("correct")
  score+=1
else:
  print("incorrect")

question3 = input("what does PSU stands for?: ")
if question3.lower() == "power supply unit":
  print("correct")
  score+=1
else:
  print("incorrect")

question4 = input("what does ROM stands for?: ")
if question4.lower() == "read only memory":
  print("correct")
  score+=1
else:
  print("incorrect")

question5 = input("what does JP stands for?: ")
if question5.lower() == "japan":
  print("correct")
  score+=1
else:
  print("incorrect")
  
print("you got: " + str(score) + " answers correct")
print("you did " + str((score/5)*100) + "%" + " answers correct")

