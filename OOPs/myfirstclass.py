# class phone:
   
#     def show_details(self):
#         return f"details of phone"

# p1=phone()
# print(p1.show_details())   

class Phone:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand      # Attribute
        self.model = model      # Attribute

    def show_details(self):
        return f"Phone Brand: {self.brand}, Model: {self.model}"


# Object creation
p1 = Phone("Samsung", "S23")

# Accessing method
print(p1.show_details())
