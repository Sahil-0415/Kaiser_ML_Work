class Department:
    dept_id =1000
    def __init__(self , dept_name , loc):
        self.set_dept_name(dept_name)
        self.set_dept_loc(loc)
        
        Department.dept_id +=1
        self.dept_id = Department.dept_id
        
    def set_dept_loc(self , loc):
        self.loc = loc    
        
    def set_dept_name(self , dept_name):
        self.dept_name = dept_name
            
    def show_dept_details(self):
        return f"Dept_id : {self.dept_id} | Dept_Name : {self.dept_name} | Dept_Loc : {self.loc}"    
    
d1 = Department("IT" , "Nashik")
print(d1.show_dept_details())    
    
    
    
    
    
    
    
    
    