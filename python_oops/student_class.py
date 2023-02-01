class Student:
    """This is a Student class"""

    __specialization = "B.Tech"     # Private Class variable

    def __init__(self, name, course, college):
        self.__name = name      # Private instance variable
        self.__course = course  # Private instance variable
        self.__college = college    # Private instance variable

    # Custom Getter for name
    def get_name(self):
        return self.__name

    # Custom setter for name
    def update_name(self, name):
        self.__name = name

    # Custom Getter for course
    def get_course(self):
        return self.__course

    # Custom setter for course
    def update_course(self, course):
        self.__course = course

    # Custom Getter for college
    def get_college(self):
        return self.__college

    # Custom setter for college
    def update_college(self, college):
        self.__college = college

    def update_student_details(self, name, course, college):
        self.update_name(name)          # Calling another function within the class
        self.update_course(course)      # Calling another function within the class
        self.update_college(college)    # Calling another function within the class


student_ab = Student("Ab", "Course", "College-1")
print(student_ab.get_name())
print(student_ab.get_course())
print(student_ab.get_college())
student_ab.update_name("Cd")
student_ab.update_course("Course-2")
student_ab.update_college("College-2")
print(student_ab._Student__name)    # Accessing private instance variable
print(student_ab._Student__course)  # Accessing private instance variable
print(student_ab._Student__college)         # Accessing private instance variable
print(Student._Student__specialization)     # Accessing private class variable
student_ab.update_student_details("Ef", "Course-3", "College-3")
print(student_ab.get_name())
print(student_ab.get_course())
print(student_ab.get_college())