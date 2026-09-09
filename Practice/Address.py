
class Address:
    def __init__(self , Street , city):
        self.set_street(Street)
        self.set_city(city)
        
    def set_street(self , Street):
        self.Street = Street    
        
    def set_city(self , city):
        self.city = city
            
         
    def show_address_details(self):
        return f"STreet nmae : {self.Street} | City : {self.city}"    
    
  
    
    
    
    
    
    
    
    
    