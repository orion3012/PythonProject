import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.1
        self.gladness -= 5

    def to_freelance(self):
        print("I will do something for money")
        self.money += 20
        self.gladness -= 2

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 5

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.08
        self.money -= 10

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money <= 0:
            print("Broke...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:*^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_freelance()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
kate = Student(name="Kate")
bohdan = Student(name="Bohdan")
for day in range(3650):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
    if bohdan.alive == False:
        break
    bohdan.live(day)

# симулятор життя вуличного кота

# import random
# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 100
#         self.thirst = 100
#         self.rest = 100
#         self.happiness = 50
#         self.cleanliness = 100
#         self.alive = True
#
#     def to_hunt(self):
#         print("Time to hunt")
#         self.hunger += 10
#         self.rest -= 20
#         self.cleanliness -= 10
#
#     def to_look_for_water(self):
#         print("I will find some puddle")
#         self.thirst += 10
#         self.rest -= 10
#         self.cleanliness += 30
#
#     def to_sleep(self):
#         print("I will sleep")
#         self.happiness += 5
#         self.rest += 80
#
#     def to_play(self):
#         print("I want to play with others")
#         self.happiness += 5
#         self.hunger -= 15
#         self.rest -= 20
#         self.cleanliness -=20
#
#
#     def is_alive(self):
#         if self.hunger <= 0:
#             print("Died because of the hunger...")
#             self.alive = False
#         elif self.thirst <= 0:
#             print("Died because of the thirst...")
#             self.alive = False
#         elif self.rest <= 0:
#             print("Too tired to move...")
#             self.alive = False
#         elif self.happiness <= 0:
#             print("Depression...")
#         elif self.cleanliness <= 0:
#             print("Unhygienic...")
#             self.alive = False
#
#     def end_of_day(self):
#         print(f"Hunger = {self.hunger}")
#         print(f"Thirst = {self.thirst}")
#         print(f"Rest = {self.rest}")
#         print(f"Cleanliness = {self.cleanliness}")
#         print(f"Happiness = {self.happiness}")
#
#
#     def live(self, day):
#         day = "Day " + str(day) + " of " + self.name + " life"
#         print(f"{day:*^50}")
#         live_cube = random.randint(1, 4)
#         if live_cube == 1:
#             self.to_hunt()
#         elif live_cube == 2:
#             self.to_look_for_water()
#         elif live_cube == 3:
#             self.to_sleep()
#         elif live_cube == 4:
#             self.to_play()
#         self.end_of_day()
#         self.is_alive()
#
# milo = Cat(name="Milo")
# tuna = Cat(name="Tuna")
# charlie = Cat(name="Charlie")
# for day in range(3650):
#     if milo.alive == False:
#         break
#     milo.live(day)
#     if tuna.alive == False:
#         break
#     tuna.live(day)
#     if charlie.alive == False:
#         break
#     charlie.live(day)