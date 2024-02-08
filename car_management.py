
class CarManager:
    all_cars =[]
    total_cars = 0
    
   
    def __init__(self, make = None, model = None, year = None, mileage = None, services = []) -> None:

        # update total_cars and create ID for this care 
        CarManager.total_cars+= 1 
        self._id = CarManager.total_cars
        # update all_cars 
        self._make = make 
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.all_cars.append(self)
    
    # string to see what is going on 
    def __str__(self):
        return f"car id: {self._id}, model: {self._model}, make: {self._make}, year: {self._year}, mileage {self._mileage}"
    
    def __repr__(self):
        return str(self)
    # getter of make 
    @property
    def make(self): 
        return self._make  
    
    @make.setter 
    def make(self, new_make):
        self._make = new_make 
    
    # take input from the user sets self.make to new make 
    def input_make(self): 
        new_make = input("What is your Make?", )
        self.make = new_make
    # getter for model of the car 
    @property 
    def model(self):
        return self._model 
    # setter for model of the car 
    @model.setter
    def model_setter(self, new_model):
        self._model = new_model
    
    def input_model(self):
        new_model = input('What is your Model?', )
        self._model = new_model
    #to add a year 
    @property 
    def year(self):
        return self._year 
    
    @year.setter
    def year_setter(self, new_year):
        self._year = new_year

    def input_year(self):
        new_year = input('What year is your car?', )
        self._year = new_year
    # to add the milage 
    @property 
    def mileage(self):
        return self._mileage 
    
    @mileage.setter
    def mileage_setter(self, new_mileage):
        self._mileage = new_mileage

    def input_mileage(self):
        new_mileage = input('What is your car milage', )
        self._mileage = new_mileage
    
    @property
    def services(self):
        return self._services
    
    @services.setter
    def services_setter(self, updated_services): 
        self._services = update_services
        return updated_services
 


def add_car():
    new_car = InteractiveCarManager()
    new_car.make = InteractiveCarManager.input_make()
    new_car.model = InteractiveCarManager.input_model()
    new_car.year = InteractiveCarManager.input_year()
    new_car.mileage = InteractiveCarManager.input_mileage()
    return new_car

# Other functions and code remain the same...

        
def display_welcome():
    print("""----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit""")        

#add make/model/year/milage by calling the input class methods 
def add_car():
    new_car = CarManager()
    new_car.input_make()
    new_car.input_model()
    new_car.input_year()
    new_car.input_mileage()

#view how many cars are there 
def view_cars():
    print(CarManager.all_cars)

#view total number of cars 
def view_total_cars():
    print(f"Total cars present: {CarManager.total_cars}")

# print the return statment as it has all the details about the car 
def view_car_details():
    print(f"Car ID: {self._id}, Model: {self._model}, Make: {self._make}, Year: {self._year}, Mileage {self._mileage}")

# function to find the car ID
def car_finder():
    for id_values in CarManager.all_cars:
        print("hi")#TODO find a meaningfull to loop through 


# Car services 
def update_services():
    services_offered = ["1. Oil Change", "2. Brakes Pads Changed", "3. Tires Rotated"]
    user_choice ="""What do you need done? Please Enter a Number Between 1-3 
          if user
            {services_offered}"""
    if user_choice == "1":
        CarManager.services_setter.append(services_offered[0])
    # if user_choice == "2":
        
    # if user_choice == "3":
    #     view_total_cars()

    

    
#logic tree to figure out what you want to do 
def choice_welcome():
    done = False
    while not done:
        display_welcome()
        user_choice =input("What do you need to do? Enter a number between 1-7: ", )      
        if user_choice == "1":
            add_car()
            print("Car has been added")
        elif user_choice == "2":
            view_cars()
        elif user_choice == "3":
            view_total_cars()
        elif user_choice == "4":
            view_car_details()
        elif user_choice == "5":
            update_services()
        elif user_choice == "6":
            print("Upadate Milage") 
        elif user_choice == "7":
            done = True
            return "Goodbye!"
        else:
            print("Please Enter a Valid Repsonse")
                  
# honda = CarManager( "honda", "civic", 2004, 5000, "oil change" )
# ford = CarManager("ford" , "mustang", 2018, 679, ["change tires", "oil change"])
# new_car = CarManager()
print(choice_welcome())

print(car_finder)
