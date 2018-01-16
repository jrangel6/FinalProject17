#introduction to game
input("Welcome! The goal is to win this game and escape the jungle. Complete the tasks to the best of your ability. Good Luck!")
#Using while statement and input function for players to select character
secret_word = 'Janessa Rangel' #Secret word that will reveal character stats
while True:
    answer = input("Choose your character. Pick wisely among Janessa Rangel, Clarissa Rangel, Caitlin Moy, and Henry Smolder: ")
    if answer == secret_word:
        print("OOH! You have chosen the most valuable player. Age: 25, Strengths: Twin Power, zoology, super-strength, super-speed. Weaknesses: None")
        break
    if answer != secret_word:#If statement when secret word is not entered and will reveal rest of character stats
        print("Well, unfortunatley, you did not choose the best player. However, these are the rest of the character stats:")
        print("Clarissa Rangel: Age is 25, Strengths include Twin Power, cartography, super-speed, Weaknesses include apple pie and bread")
        print("Caitlin Moy: Age is 28, Strengths include dancing combat and martial arts, Weaknesses include venom")
        print("Henry Smolder: Age is 27, Strengths include stamina and smoldering look, Weaknesses include cake and apple juice")
        break
#Printing the first task of the game to complete
print("*** Your first task is to collect water! You must journey through the Crocodile River and safely make it to the other side with your water." )
answer = input(str("To get across the river you: 1. Use your character's super-speed(if he/she has it) to collect the water or 2. Use a bow and arrow " ))
response = "1"
if answer == response:
    print("Congratulations! You have successfully completed the first task!")
if answer!= response:
    print("Quick! The crocodiles are trailing behind you! Hurry!")

print("That was a close one! Take a sip of water and prepare for your second task")

print("*** Uh-oh! The second task is a big one. There are two gigantic lions ready to attack. ")
answer = input(str("Who do you recruit for this task? a. The Twins or b. you and another character?"))
recruit = "a"
if answer == recruit:
    print("Alright! The Twin Power. Together, Janessa and Clarissa will fight the lions while you get to safe ground.")
if answer != recruit:
    print("What is your plan?")
plan = input(str("a. Make a run for it or b. Use a bow and arrow  "))
respo = "b"
if plan == respo:
    print("Way to go! You have moved on to the next level!")
else:
    print("Oh no. You have died. Don't worry though, you have two lives left.")

print("It is time to check your inventory.")

inventory = {'knife': 4, 'bow': 1, 'arrows': 150, 'change of clothes': 2, 'water bottle': 4, 'tent': 1, 'blanket': 5, 'binoculars': 2, 'hat(pith Helmet and Sun cap)': 2}
for k,v in inventory.items():
    print(f" {k} : {v} ")
print("*** Your third task requires you to stay up in the forest all night.")
print("Now that you have checked your inventory, which two items will help you face the freezing cold?")
answer = input(str("a. blanket and tent or b. hat and binoculars"))
item = "a"
if answer == item:
    print("Congratulations! Your task is to hide out. Exactly at midnight, you must run through the maze. Beware of insects lurking.")
if answer != item:
    print("Are you sure? Unfortunately, you have died. Try not to waste any more lives. You have three in total.")

print("The maze is a wonderful challenge. However, it is very difficult. You must journey through the maze and get to the market. Once at the market,you will meet your next task.")
answer = input(str("What do you do first to get through the maze? a. Grab as many weapons as you can  b. Make a run for it"))
maze = "a"
if answer == maze:
    print("Uh-Oh! You encounter a gigantic scorpion. What weapon do you use?")
if answer != maze:
    print("You are good so far. Keep going and try to be as quick as you can!")

answer = input(str("Are you Caitlin Moy?"))
response = "yes"
if answer == response:
    print("Your weakness is vemon. Beware of the scorpion.")
if answer != response:
    print(input(str("Insert weapon of choice:")))
weapon = input(str("Work hard and try to beat the scorpion. **Hint** In order to beat the scorpion, you must understand the scorpion. Which character understands animals? *Hit enter again*"))
print(input(str("""
1. Janessa Rangel
2. Clarissa Rangel
3.Cailtin Moy
4. Henry Smolder - """)))
response = "1"
if weapon == response:
    print(input(str("You have chosen wisely. Janessa has successfully advanced you to the next level.")))
if weapon != response:
    print(input(str("Try Again:")))
#Printing the fifth task
input("Yay! Your fifth task requires you to collect logs. Your inventory currently has zero logs. You have to collect 20 and make a fire.")
#using same list that created inventory to add another item in the list
inventory = {'knife': 4, 'bow': 1, 'arrows': 150, 'change of clothes': 2, 'water bottle': 4, 'tent': 1, 'blanket': 5, 'binoculars': 2, 'hat(pith Helmet and Sun cap)': 2, 'logs':0}
for k,v in inventory.items():
    print(f" {k} : {v} ")#printing the keys and values
def respond_to_numberq(number):#Defining a function
    if number == "5":#Uisng if and elif statements
        print("Oh no! You have been eaten by a bear!")
    elif number == "4":
        print("Congratulations! You have chosen the lucky section. Go and grab your logs!")
    elif number == "3":
        print("Oh no! You have entered the quick sand region. Retreat as fast as you can!")
    elif number == "2":
        print("Congratulations! You have chosen the lucky section. Go and grab your logs!")
    elif number == "1":
        print("Oh no! You have accidentally entered the bunny region. You can pet the bunnies but remember to stay focused on your task.")
#Calling the function
respond_to_numberq(input(str("Welcome to the Wild Jungle. The logs are scattered everywhere. Each section of the jungle is represented by a number (1-5). Choose a number to determine your fate.")))

answer = input(str("Have you died three times already? Y/N")).upper()
question = "Y"
if answer == question:
    print(input(str("Exit the program")))
if answer !=  question:
    print(input(str("Congratulations! You have moved on to the next level. Time to check your stats and inventory again.")))
#Creating a class to make health stats
class Stats(object):
    def __init__(self, name , health,):
        #Initializng a new instance of Stats class
        self.name = name
        self.health = health
        self.inventory  = inventory
Janessa = Stats('Janessa Rangel', 'Very healthy -- not dehyrated')
Clarissa = Stats('Clarissa Rangel', 'Healthy -- a bit dehyrdrated')
Caitlin = Stats('Caitlin Moy', 'Healthy')
Henry = Stats('Henry Smolder', 'Need to drink water')
#Printing to show the health of every character
print(Janessa.name)
print(Janessa.health)
print("-----")#Used to separate the objects
print(Clarissa.name)
print(Clarissa.health)
print("-----")
print(Caitlin.name)
print(Caitlin.health)
print("-----")
print(Henry.name)
print(Henry.health)

input("Alright! This is your final task! You have to journey across the ring of fire to win the game.")
answer = (input(str("To get across the ring of fire, you must travel through the fire. How do you plan to do this: a. I will swim in the water b. I will hop on top of each volcano because I am that cool.")))
response = "b"
if answer == question:
    print("Of course you are that cool! Be careful and win the game!")
if answer != question:
    print("Be careful and look out for creepy animals")

print("If you chose option a, you have unfortunately died, and lost the game. A shark ate you alive. If you chose b, then that was the quickest way to journey across the ring of fire. Congratulations. You have WON the game!")

answer =(input(str("Who is playing this game (insert real name)? --->")))

print(f"Well {answer}, I hope you had fun and ejoyed the game!")
















