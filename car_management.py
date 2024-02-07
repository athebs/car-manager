welcome_choices = [
    "1. Add a car",
    "2. View all cars",
    "3. View total number of cars",
    "4. See a car's details",
    "5. Service a car",
    "6. Update mileage",
    "7. Quit"]


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
        return f"car id: {self._id}, model: {self._model}, make: {self._make}, year: {self._year}, mileage {self._mileage}, serives render:{self._services}"
   
    def __repr__(self):
        return str(self)
    
    # @classmethod
    def show_welcome_message(self):
        welcome_list = list(CarManager.welcome_choices.keys())
        return welcome_list
    # to add information to a list 

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
    # to add a model 
    @property 
    def model(self):
        return self._model 
    
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
        
        



    

#add make/model/year/milage by calling the input class methods 
def add_car():
    new_car = CarManager()
    new_car.input_make()
    new_car.input_model()
    new_car.input_year()
    new_car.input_mileage()

#view how many cars are there 
def view_cars():
    
    print (CarManager.all_cars)
#logic tree to figure out what you want to do 

    
#logic tree to figure out what you want to do 
def choice_welcome():
    print(welcome_choices)
    
    done = False
    while not done:
        user_choice =input("What do you need to do? Enter a number between 1-7: ", )      
        if user_choice == "1":
            add_car()
            print("Car has been added")
        elif user_choice == "2":
            view_cars()
        elif user_choice == "3":
            print("view all cars")
        elif user_choice == "4":
            print("see a car")
        elif user_choice == "5":
            print("Service a Car") 
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
