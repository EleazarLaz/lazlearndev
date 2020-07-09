"""
My ninth python assignment on pirple.com.
This assignment is about using classes in Python
"""


# Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = False
        self.trips_since_maintenance = 0

    def print_vehicle(self):
        print("Vehicle make: " + self.make)
        print("Model: " + self.model)
        print("Year Produced: " + str(self.year))
        print("Weight: " + str(self.weight) + "kg")
        print()

    def check_trips_since_maintenance(self):
        print(self.make + " " + self.model + " has gone for " + str(self.trips_since_maintenance) + " trip(s)")

    def check_maintenance(self):
        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True
            print("Please go for repair")
        else:
            self.needs_maintenance = False
            print("Ride on man, it's not yet time for repair")

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False


class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_driving = False

    def drive(self):
        self.is_driving = True
        print(self.make + " " + self.model + " is on a trip")
        self.trips_since_maintenance += 1

    def stop(self):
        self.is_driving = False
        print("Trip ended")


class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.is_flying = False
        self.is_landing = False

    def fly(self):
        self.is_flying = True
        print(self.make + " " + self.model + " is flying")
        self.trips_since_maintenance += 1
        if self.needs_maintenance:
            self.is_flying = False
            print("Cant fly until it's repaired")

    def land(self):
        if self.is_landing:
            print(self.make + " " + self.model + " is not on air")
        else:
            self.is_landing = True
            print(self.make + " " + self.model + " has landed")


# creating the first car
car1 = Cars("Toyota", "V6", 2016, 300)
car1.drive()
car1.drive()
car1.drive()
car1.drive()
car1.drive()
car1.stop()
print()  # for a space

# creating the second car
car2 = Cars("Volvo", "C200", 2002, 350)
car2.drive()
car2.drive()
car2.drive()
car2.drive()
car2.stop()
print()  # for a space

# creating the third car
car3 = Cars("Honda", "Accord", 2010, 475.50)
car3.drive()
car3.drive()
car3.drive()
car3.drive()
car3.drive()
car3.drive()
car3.drive()
car3.stop()
print()  # for a space

# Now let me print out the cars
print("FIRST CAR".upper())
car1.print_vehicle()
car1.check_trips_since_maintenance()
car1.check_maintenance()
print()

print("SECOND CAR")
car2.print_vehicle()
car2.check_trips_since_maintenance()
car2.check_maintenance()
print()

print("THIRD CAR")
car3.print_vehicle()
car3.check_trips_since_maintenance()
car3.check_maintenance()
print()
print()

my_plane = Planes("Liberator", "B-24", 1924, 800)
my_plane.fly()
my_plane.land()

my_plane.fly()
my_plane.land()

my_plane.fly()
my_plane.land()

my_plane.fly()
my_plane.land()
print()

my_plane.print_vehicle()
my_plane.check_trips_since_maintenance()


