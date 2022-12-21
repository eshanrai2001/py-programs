import random
asking = input("Give a range: ")
#check if user has typed a number and also if in string e.g "4", convert it in int.
if asking.isdigit():
  asking = int(asking)

  if asking<=0:
    print("Please enter number greater than 0 next time")
    quit()
  else:
   print("let's start")
else:
  print("Please enter number next time")
  quit()

random_number = random.randint(0,asking)
guesses=0
while True:
  guesses+=1
  user_guess = input("make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
     print("Please type a number next time") 
     continue
  if user_guess in range(0,asking):
   if user_guess == random_number:
     print("you got it correct")
     break
   elif user_guess > random_number:
    print("you are above the number")
   else: 
    print("you are below the number")
  else:
    print("please enter within the range")
print("you got it in ",guesses," guesses")
  



