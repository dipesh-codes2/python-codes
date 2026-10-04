import random
number = random.randint(1,100)
attempts = 0

while True:

  guess_number = int(input("enter you guess number from 1 to 100 : "))
  attempts +=1

  if guess_number == number:
    print(f"correct!aapne {attempts} attempt me sahi guess kiya")
    break

  elif guess_number>number:
    print("too high")
  elif guess_number<number:
    print("too low")

