# Base / Parent class
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        return f"Brand: {self.brand}, Model: {self.model}"


# Child class (inherits Phone)
class SmartPhone(Phone):
    def __init__(self, brand, model, os):
        super().__init__(brand, model)
        self.os = os

    def show_os(self):
        return f"Operating System: {self.os}"


# Child of SmartPhone (multi-level inheritance)
class TouchScreenPhone(SmartPhone):
    def __init__(self, brand, model, os, screen_size):
        super().__init__(brand, model, os)
        self.screen_size = screen_size

    def show_touch_details(self):
        return (
            f"{self.brand} {self.model} | "
            f"OS: {self.os} | "
            f"Touch Screen: {self.screen_size} inches"
        )


# -------- Object Creation --------

basic_phone = Phone("Nokia", "3310")
print(basic_phone.show_details())

smart_phone = SmartPhone("Samsung", "S23", "Android")
print(smart_phone.show_details())
print(smart_phone.show_os())

touch_phone = TouchScreenPhone("Apple", "iPhone 15", "iOS", 6.1)
print(touch_phone.show_details())
print(touch_phone.show_os())
print(touch_phone.show_touch_details())
