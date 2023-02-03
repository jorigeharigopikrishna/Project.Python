class Methods:
    def instance_method(self):
        print("This is an instance method")

    @staticmethod
    def static_method():
        print("This is a static method")

    @classmethod
    def class_method(cls):
        print("This is a class method")

types_of_methods = Methods()
types_of_methods.instance_method()
types_of_methods.class_method()
Methods.class_method()
Methods.static_method()
types_of_methods.static_method()
