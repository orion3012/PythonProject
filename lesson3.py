'''Ми вже вміємо створювати класи, але в реальності об’єкти
постійно взаємодіють. Так само можуть комунікувати між собою
і програмні об’єкти.
Оголосимо створення двох класів– авто й людини:'''
class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human): #Створимо метод, який реєструє пасажирів авто
        self.passengers.append(human)

    def print_passengers_names(self): #Додамо метод, що виводить імена пасажирів
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")
#
# '''Створимо об’єкти двох людей та авто, після чого
# викличемо методи реєстрації пасажирів та виведення їхніх імен'''
# nick = Human("Nick")
# kate = Human("Kate")
# bohdan = Human("Bohdan")
# car = Auto("Mercedes")
# car.add_passenger(nick)
# car.add_passenger(kate)
# car.print_passengers_names()

import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="a",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_pet(self):
        self.pet = Pet(species_list)


    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if self.home.pet_food < 10:
            manage = "pet_food"
        if manage == "fuel":
            print("I bought fuel")
            logging.info("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            logging.info("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            logging.info("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
        elif manage == "pet_food":
            print("I bought food for my pet")
            logging.info("I bought food for my pet")
            self.gladness += 5
            self.home.pet_food += 70
            self.money -= 30

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def play_with_pet(self):
        self.gladness += 10
        self.pet.hunger -= 15

    def feed_pet(self):
        self.gladness += 5
        self.pet.hunger += 50
        self.home.pet_food -= 30

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        logging.info(f"{day:=^50} \n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        logging.info(f"{human_indexes:^50} \n")
        print(f"Money – {self.money}")
        logging.info(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        logging.info(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        logging.info(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        logging.info(f"{home_indexes:^50} \n")
        print(f"Food – {self.home.food}")
        logging.info(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        logging.info(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        logging.info(f"{car_indexes:^50} \n")
        print(f"Fuel – {self.car.fuel}")
        logging.info(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")
        logging.info(f"Strength – {self.car.strength}")
        pet_indexes = f"{self.pet.species} pet indexes"
        print(f"{pet_indexes:^50}", "\n")
        logging.info(f"{pet_indexes:^50} \n")
        print(f"Hunger – {self.pet.hunger}")
        logging.info(f"Hunger – {self.pet.hunger}")



    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            logging.info("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            logging.info("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            logging.info("Bankrupt…")
            return False
        if self.pet and self.pet.hunger <= 0:
            print("Your pet died because of the hunger!")
            logging.info("Your pet died because of the hunger!")
            return False
        return True

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            logging.info("Settled in the house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
            logging.info(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
            logging.info(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print(f"I bought a pet {self.pet.species}")
            logging.info(f"I bought a pet {self.pet.species}")

        self.days_indexes(day)
        dice = random.randint(1, 5)
        if self.satiety < 20:
            print("I'll go eat")
            logging.info("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                logging.info("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                logging.info("So I will clean the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                logging.info("Let`s chill!")
                self.chill()
        elif self.money < 0:
            print("Start working")
            logging.info("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            logging.info("I need to repair my car")
            self.to_repair()
        elif self.pet.hunger <= 20:
            print("I need to feed my pet")
            logging.info("I need to feed my pet")
            self.feed_pet()
        elif dice == 1:
            print("Let`s chill!")
            logging.info("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Start working")
            logging.info("Start working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            logging.info("Cleaning time!")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            logging.info("Time for treats!")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Time to play with my pet!")
            logging.info("Time to play with my pet!")
            self.play_with_pet()

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }


class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            logging.info("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.pet_food = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]
        
species_list = {"Dog",
                "Cat",
                "Parrot",
                "Fish",
                "Snake"}

class Pet:
    def __init__(self, species_list):
        self.species=random.choice(list(species_list))
        self.hunger= 50



nick = Human(name="Nick")
for day in range(1, 800):
    if nick.live(day) == False:
        break



