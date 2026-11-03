class Employee:

    # __employee_id: int
    # Constructor of class
    def __init__(self, employee_id, firstname, lastname, city, designation):
        self.__employee_id = employee_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__city = city
        self.__designation = designation

    # it is used to convert your object into string
    def __str__(self):
        return f'{self.__employee_id:<15} {self.__firstname:<15} {self.__lastname:<15} {self.__city:<15} {self.__designation:<15}'
