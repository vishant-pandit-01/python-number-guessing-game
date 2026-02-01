import random
print("🎯 Welcome to Number Guessing Game :-")

Name=input("enter your name :-")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    user_choice = int(input("enter your choice number between 1 to 100: "))
    attempts +=1

    if user_choice < secret_number:
        print("📉 Too low! Dobara try karo: ")
    elif user_choice > secret_number:
        print("📈 Too high! Dobara try karo: ")
    else:
        print("Congrats:-",Name, "Aapne ",attempts," Attempts m Right Number Choose kra h ")
        # print(f" congrats {Name} tumne {attempts} attempts mein sahi number guess kar liya h:") 
        break
