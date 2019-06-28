import random
import time

class Turt:
    def __init__(self):
        self.size = 1
        self.color = "green"
        self.name = "Default"
        self.speed = "slow"
        self.shell = "intact"
        self.mood = "neutral"
        self.i = 0
        self.health = 10
        self.enemy_health = 10

    def feed(self):
        if self.mood == "full":
            print ("Looks like " + self.name + " is full. Feed him again later")
            time.sleep(1)
            self.new_friend()
        print ("""
-----------------------
Pick a snack!         
1. A leaf             
2. A carrot           
3. A small tomato     
4. A LARGE tomato     
5. Another turtle
6. Return to Main Menu     
-----------------------""")
        answer3 = input()
        if self.i<=3:
            if answer3 == "1":
                print ("CRONCH!")
                time.sleep(1)
                print ("He enjoyed his leaf")
                time.sleep(1)
                self.mood = "Content"
                self.i += 1
                self.feed()
            elif answer3 == "2":
                print ("Munch munch munch")
                time.sleep(1)
                print ("He loves carrots")
                time.sleep(1)
                self.mood = "Very Happy"
                self.i += 1
                self.feed()
            elif answer3 == "3":
                print ("Om nom nom")
                time.sleep(1)
                print ("A good small tomato")
                time.sleep(1)
                self.mood = "Content"
                self.i += 1
                self.feed()
            elif answer3 == "4":
                print ("How do eat???")
                time.sleep(1)
                print ("He's having trouble eating this one...")
                time.sleep(1)
                self.mood = "distressed"
                self.feed()
            elif answer3 == "5":
                print ("In this world it's eat or be eaten")
                self.mood = "BIG ANGRY"
                self.battle()
            elif answer3 == "6":
                self.new_friend()
            else:
                print ("That isn't a valid answer")
                time.sleep(1)
                self.feed()
        else:
            print ("Look's like he is all full!")
            time.sleep(1)
            self.mood = "full"
            self.new_friend()
        
    def look(self):
        print ("""
----------------------------------------------
What part of your turtle do you want to check?
1. His mood
2. His color
3. His name
4. His shell
5. Return to Main Menu
----------------------------------------------
""")
        answer4 = input()
        if answer4 == "1":
            print (self.name + "'s mood is " + self.mood)
            self.look()
        elif answer4 == "2":
            print (self.name + "'s color is " + self.color)
            self.look()
        elif answer4 == "3":
            print ("his name is " + self.name)
            self.look()
        elif answer4 == "4":
            print (self.name + "'s shell is " + self.shell)
            self.look()
        elif answer4 == "5":
            self.new_friend()
        else:
            print ("You are bad at numbers")
            self.look()

    def race(self):
        racers = ["Linda", "Speeds McGee", "Shell Shock", "Turts Biggem", "Carl", "Green Lightning"]
        opponent = random.choice(racers)
        if self.mood == "tired":
            print ("Your turtle looks pretty tired. Let him rest a while")
            self.new_friend()
        print ("We're off to the races!")
        print ("---- You're racing against " + opponent + " today! ----")
        time.sleep(1)
        print ("On your mark...")
        print (" ")
        time.sleep(1)
        print ("Get set...")
        print (" ")
        time.sleep(1)
        print ("GO!")
        print (" ")
        odds = []
        if self.mood == "full":
            self.speed = "very slow"
            for i in range(3):
                odds.append(opponent)
            for i in range(2):
                odds.append(self.name)
        else:
            for i in range(3):
                odds.append(opponent)
                odds.append(self.name)
        first_lap = random.choice(odds)
        time.sleep(2)
        print ("And in the first lap, " + first_lap + " has taken an early lead!")
        time.sleep(2)
        second_lap = random.choice(odds)
        print ("And in the second lap, " + second_lap + " is in the front!")
        time.sleep(2)
        print ("It's gonna be a photo finish!")
        time.sleep(2)
        winner = random.choice(odds)
        print ("And it looks like the winner is... " + winner + "!")
        time.sleep(1)
        if winner == self.name:
            print ("---- Congrats! Your turtle won! ----")
            self.mood = "tired"
        else:
            print ("---- Better luck next time! ----")
        self.speed = "slow"
        self.new_friend()

    def battle(self):
        time.sleep(2)
        print ("*battle music*")
        time.sleep(1)
        print ("A wild turtle has appeared!")
        while self.enemy_health > 0:
            print("""
----------------------
What will you do?
1. Fight!
2. Run!
----------------------
""")
            choice = input()
            if choice == "1":
                print ("""
----------------------
Choose your move!
1. Turtle Takedown
2. Big Bite
3. Shell Slam
----------------------
            """)
                move = input()
                if move == "1":
                    print (self.name + " used Turtle Takedown!")
                    time.sleep(1)
                    damage = random.randint(1, 10)
                    print (str(damage) + " damage!")
                    time.sleep(1)
                    self.enemy_health -= damage
                elif move == "2":
                    print (self.name + " used Big Bite!")
                    time.sleep(1)
                    damage = random.randint(1, 5)
                    print (str(damage) + " damage!")
                    time.sleep(1)
                    self.enemy_health -= damage
                elif move == "3":
                    print (self.name + " used Shell Slam!")
                    time.sleep(1)
                    damage = random.randint(1, 8)
                    print (str(damage) + " damage!")
                    time.sleep(1)
                    self.enemy_health -= damage
                else:
                    pass
                     
            elif choice == "2":
                run_chance = random.randint(1, 2)
                if run_chance == 1:
                    print ("You got away!")
                    time.sleep(2)
                    break
                else:
                    print ("You couldn't get away!")
                    time.sleep(2)
            else:
                print ("Your mistake got your turtle beat up... You should feel bad")
                time.sleep(1)
                self.mood = "beat up"
                self.shell = "broken"
            if self.enemy_health <= 0:
                print ("You defeated the Wild Turtle!")
                time.sleep(1)
                print ("Be more careful, your turtle could get hurt next time!")
                time.sleep(1)
                self.health = 10
                self.mood = "Victorious"
                break
            print ("---- Wild Turtle's turn! ----")
            time.sleep(1)
            wild_move = ["Turtle Takedown", "Big Bite", "Shell Slam"]
            print ("The wild turtle used " + random.choice(wild_move) + "!")
            time.sleep(1)
            wild_damage = random.randint(1, 8)
            print ("You took " + str(wild_damage) + " damage!")
            time.sleep(1)
            self.health -= wild_damage
            if self.health > 0:
                print ("Your health is " + str(self.health))
                time.sleep(1)
            else:
               # print ("Your turtle is hurt!")
               # time.sleep(1)
                self.mood = "beat up"
                self.shell = "broken"
                break
        self.new_friend()
                        
    def new_friend(self):
        if self.shell == "broken":
            print ("Oh no, " + self.name + " is hurt!")
            time.sleep(1)
            print ("Let's get you fixed up!")
            time.sleep(2)
            self.shell = "intact"
        if self.name == "Default":
            print ("Would you like to name your new turtle? (y/n)")
            answer1 = input()
            if answer1 == 'y':
                time.sleep(1)
                print ("Name your new turtle pal!")
                time.sleep(1)
                self.name = input()
            elif answer1 == "n":
                time.sleep(1)
                print ("We will give him a name for you")
                time.sleep(1)
                name_set = {"Durdle Turtle", "Danny Devito", "Jeff", "Lord Voldetort", "The Turtinator"}
                self.name = name_set.pop()
            else:
                time.sleep(1)
                print ("That's not a valid input, you egg. Whatever, I'm just gonna call him Steve")
                time.sleep(1)
                self.name = "Steve"
        print ("""
-------------------------------------------
What would you like to do with your turtle?
1. feed the turtle
2. check on the turtle
3. race your turtle
4. exit turtle simulator
Please input the number as listed above
-------------------------------------------""")
        a = input ()
        if a == "1":
            time.sleep(1)
            print ("Snack time!")
            time.sleep(1)
            self.feed()
        elif a == "2":
            time.sleep(1)
            print ("Let's check on your turtle")
            time.sleep(1)
            self.look()
        elif a == "3":
            time.sleep(1)
            self.race()
            time.sleep(1)
        elif a == "4":
            print ("Thanks for playing Turtle Simulator!")
            exit()
        else:
            print ("Thats not a valid input...")
        return a

turtle = Turt()
print (" ---- Welcome to Turtle Simulator! ----")
time.sleep(2)
turtle.new_friend()