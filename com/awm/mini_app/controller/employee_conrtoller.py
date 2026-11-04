from mysql.connector.errors import Error
from com.awm.mini_app.model.employee import Employee
from com.awm.mini_app.util.my_sql_connection import get_mysql_connection


class EmployeeController:
    def display_all_menu(self):
        while True:
            try:
                print('\n****Menu****')
                print('\t1. Display Employee Details')
                print('\t2. Create Employee Details')
                print('\t3. Update Employee Details')
                print('\t4. Delete Employee Details')

                choice: int = int(input('Enter your choice: '))
                match choice:
                    case 1:
                        self.get_all_employee()
                    case 2:
                        self.create_employee()
                    case 3:
                        self.update_employee()
                    case 4:
                        self.delete_employee()
                    case _:
                        print('Enter your choice from 1 to 4, exiting the menu.')
                        break
            except ValueError:
                print('Invalid choice, exiting the menu.')
                break

    def get_all_employee(self):
        connection = None
        cursor = None
        try:
            connection = get_mysql_connection()
            if connection is not None:
                # 2. Create cursor object
                cursor = connection.cursor()
                # 3. Execute the SQL query
                cursor.execute('select * from employee')
                # 4. Fetch the data
                rows = cursor.fetchall()
                print(f"{'Employee ID':<15} {'First Name':<15} {'Last Name':<15} {'City':<15} {'Designation':<15}")
                for row in rows:
                    employee = (Employee(employee_id=row[0], firstname=row[1], lastname=row[2], city=row[3],
                                         designation=row[4]))
                    print(employee)

        except Error as error:
            print(f'Error: {error}')

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()


    def create_employee(self):
        connection = None
        cursor = None
        try:
            # 1. Establish the connection
            connection = get_mysql_connection()
            # 2. Create cursor object
            cursor = connection.cursor()

            firstname = input('Enter employee first name: ')
            lastname = input('Enter employee last name: ')
            city = input('Enter employee city: ')
            designation = input('Enter employee designation: ')

            query = 'Insert into employee(firstname, lastname, city, designation) values(%s, %s, %s, %s)'

            # 3. Execute the SQL query
            cursor.execute(query, [firstname, lastname, city, designation])
            affected_rows = cursor.rowcount

            # 4. Commit
            connection.commit()
            if affected_rows == 1:
                print('Employee successfully created.')

        except Error as error:
            print(f'Error: {error}')

        finally:
            if cursor is not None:
                cursor.close()

            if connection is not None:
                connection.close()


def update_employee(self):
    print('In update employee menu.')


def delete_employee(self):
    print('In delete employee menu.')


controller = EmployeeController()
controller.display_all_menu()
