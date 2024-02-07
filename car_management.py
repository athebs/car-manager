class CarManager:
    all_cars =[]
    total_cars = 0
    welcome_choices = {
    "1. Add a car": "1",
    "2. View all cars": "2",
    "3. View total number of cars": "3",
    "4. See a car's details": "4",
    "5. Service a car": "5",
    "6. Update mileage": "6",
    "7. Quit": "7",}

    
    def __init__(self, id, make, model, year, mileage, services) -> None:
        self._id = CarManager.total_cars + 1  
        CarManager.totalcars+= 1 
        self._make = make 
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services 
    
    # string to see what is going on 
    def __str__(self):
        return f"car id: {self._id}, model: {self._model}, make: {self._make}, year: {self._year}, mileage {self._mileage}, serives render:{self._services}"
   
    
    def show_welcome_message(self, welcome_list):
        welcome_list = list(CarManager.welcome_choices.keys)
        print(welcome_list)
        return welcome_list
    
    # function that adds to the count of cars by 1 
    def total_cars_incrementer(self):
        CarManager.total_cars += 1
        return CarManager.total_cars



        

    
athena_car = CarManager("4444", "honda", "civic", 2004, 5000, "oil change" )
print(CarManager.total_cars)
athena_car.total_cars_incrementer()
print(CarManager.total_cars)