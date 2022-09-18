print("Hello and welcome to the game!")

answer = input("Do you want to play a tech quiz? ")

if answer.lower() != "yes":
    quit()
print("okay lets poop")
score = 0

answer = input("what des CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
    print("Current score: " + str(score))
else: 
    print("Incorrect!")

answer = input("what des GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
    print("Current score: " + str(score))
else: 
    print("Incorrect!")

answer = input("what des RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
    print("Current score: " + str(score))
else: 
    print("Incorrect!")
    
answer = input("what des PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
    print("Current score: " + str(score))
else: 
    print("Incorrect!")

print("You got " + str((score / 4) * 100) +"%")