from abc import ABC, abstractmethod


class Parent(ABC):  # abstract class
    @abstractmethod
    def education(self):    # abstract method
        pass


class Child(Parent):    # non-abstract class which can be instantiated
    def education(self):    # non-abstract method which can be invoked.
        print("Educated")


parent_object = Parent()    # Error as abstract base classes cannot be instantiated
child_object = Child()  # object can be created as it is non-abstract.
child_object.education()    # Prints Educated
