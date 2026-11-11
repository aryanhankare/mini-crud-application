
from mysql.connector.errors import Error
from com.awm.mini_app.model.employee import Employee
from com.awm.mini_app.util.my_sql_connection import get_mysql_connection


class EmployeeController:

    def get_connection(self):
        connection = get_mysql_connection()

        if connection is None:
            print("Unable to connect to database. Please try again.")

        return connection

    def close_connection(self, cursor, connection):
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

    def display_employee(self, row):
        employee = Employee(
            employee_id=row[0],
            firstname=row[1],
            lastname=row[2],
            city=row[3],
            designation=row[4]
        )
        print(employee)

    def display_employee_header(self):
        print(
            f"{'Employee ID':<15} "
            f"{'First Name':<15} "
            f"{'Last Name':<15} "
            f"{'City':<15} "
            f"{'Designation':<15}"
        )

    def display_all_menu(self):
        while True:
            print('\n****Menu****')
            print('\t1. Display Employee Details')
            print('\t2. Create Employee Details')
            print('\t3. Update Employee Details')
            print('\t4. Delete Employee Details')
            print('\t5. Search Employee Details')
            print('\t6. Exit')

            try:
                choice = int(input('Enter your choice: '))

                match choice:
                    case 1:
                        self.get_all_employee()
                    case 2:
                        self.create_employee()
                    case 3:
                        self.update_employee()
                    case 4:
                        self.delete_employee()
                    case 5:
                        self.search_employee()
                    case 6:
                        print('Exiting the application.')
                        break
                    case _:
                        print('Invalid choice. Please enter a number from 1 to 6.')

            except ValueError:
                print('Invalid input. Please enter a valid number.')

    def get_all_employee(self):
        connection = None
        cursor = None

        try:
            connection = self.get_connection()

            if connection is None:
                return

            cursor = connection.cursor()
            cursor.execute('select * from employee')
            rows = cursor.fetchall()

            self.display_employee_header()

            for row in rows:
                self.display_employee(row)

        except Error as error:
            print(f'Error: {error}')

        finally:
            self.close_connection(cursor, connection)

    def create_employee(self):
        connection = None
        cursor = None

        try:
            connection = self.get_connection()

            if connection is None:
                return

            cursor = connection.cursor()

            firstname = input('Enter employee first name: ')
            lastname = input('Enter employee last name: ')
            city = input('Enter employee city: ')
            designation = input('Enter employee designation: ')

            query = '''
                INSERT INTO employee(firstname, lastname, city, designation)
                VALUES(%s, %s, %s, %s)
            '''

            cursor.execute(query, [firstname, lastname, city, designation])

            affected_rows = cursor.rowcount
            connection.commit()

            if affected_rows == 1:
                print('Employee successfully created.')

        except Error as error:
            print(f'Error: {error}')

        finally:
            self.close_connection(cursor, connection)

    def update_employee(self):
        connection = None
        cursor = None

        try:
            connection = self.get_connection()

            if connection is None:
                return

            cursor = connection.cursor()

            firstname = input('Update employee first name: ')
            lastname = input('Update employee last name: ')
            city = input('Update employee city: ')
            designation = input('Update employee designation: ')
            employee_id = int(input('Enter employee id: '))

            query = '''
                UPDATE employee
                SET firstname = %s, lastname = %s, city = %s, designation = %s
                WHERE employee_id = %s
            '''

            cursor.execute(
                query,
                [firstname, lastname, city, designation, employee_id]
            )

            affected_rows = cursor.rowcount
            connection.commit()

            if affected_rows > 0:
                print(f'Employee ID: {employee_id} updated successfully')
            else:
                print(f'Employee ID: {employee_id} not found')

        except Error as error:
            print(f'Error: {error}')

        except ValueError:
            print('Invalid employee id')

        finally:
            self.close_connection(cursor, connection)

    def delete_employee(self):
        connection = None
        cursor = None

        try:
            connection = self.get_connection()

            if connection is None:
                return

            cursor = connection.cursor()

            employee_id = int(input('Enter employee id: '))

            query = 'DELETE FROM employee WHERE employee_id = %s'
            cursor.execute(query, [employee_id])

            affected_rows = cursor.rowcount
            connection.commit()

            if affected_rows > 0:
                print(f'Employee ID: {employee_id} deleted successfully')
            else:
                print(f'Employee ID: {employee_id} not found')

        except Error as error:
            print(f'Error: {error}')

        except ValueError:
            print('Invalid employee id')

        finally:
            self.close_connection(cursor, connection)

    def search_employee(self):
        connection = None
        cursor = None

        try:
            connection = self.get_connection()

            if connection is None:
                return

            cursor = connection.cursor()

            employee_id = int(input('Enter employee id: '))

            query = 'SELECT * FROM employee WHERE employee_id = %s'
            cursor.execute(query, [employee_id])

            row = cursor.fetchone()

            if row is not None:
                self.display_employee_header()
                self.display_employee(row)
            else:
                print(f'Employee ID: {employee_id} not found')

        except Error as error:
            print(f'Error: {error}')

        except ValueError:
            print('Invalid employee id')

        finally:
            self.close_connection(cursor, connection)
