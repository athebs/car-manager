class CarManager:
    all_cars =[]
    total_cars = int
    welcome_choices = {
    "1. Add a car": "1",
    "2. View all cars": "2",
    "3. View total number of cars": "3",
    "4. See a car's details": "4",
    "5. Service a car": "5",
    "6. Update mileage": "6",
    "7. Quit": "7",}

    
    def __init__(self, id, make, model, year, mileage, services) -> None:
        self._id = id 
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
        return welcome_list
    

    # def welcome_page(choice): 

        

    
athena_car = CarManager("4444", "honda", "civic", 2004, 5000, "oil change" )
print(athena_car.show_welcome_message)