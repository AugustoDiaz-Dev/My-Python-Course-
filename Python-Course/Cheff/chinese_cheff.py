from cheff import Cheff

class ChineseCheff(Cheff):
#We have to overwrite the function if we want to modify the inheritance.
    def make_special_dish(self):
        print("The cheff makes orange chicken")

    def make_fried_rice(self):
        print("The cheff makes fried rice")