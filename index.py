import random
print("🎯 Welcome to Number Guessing Game :-")

Name=input("enter your name :-")
right_number = random.randint(1, 100)
attempts = 0

while True:
    user_choice = int(input("enter your choice number between 1 to 100: "))
    attempts +=1

    if user_choice < right_number:
        print("📉 Too low! Dobara try karo: ")
    elif user_choice > right_number:
        print("📈 Too high! Dobara try karo: ")
    else:
        print("Congrats",Name, "tumne",attempts," Attempts m Right number guess kar lia h: ")
        
        # print(f" Congrats {Name} tumne {attempts} Attempts m Right Number guess kar lia h: ") 
        break
