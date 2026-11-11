
from com.awm.mini_app.controller.employee_conrtoller import EmployeeController


def test_invalid_text_input(monkeypatch, capsys):
    controller = EmployeeController()

    inputs = iter(["abc", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller.display_all_menu()

    output = capsys.readouterr().out
    assert "Invalid input. Please enter a valid number." in output
    assert "Exiting the application." in output


def test_invalid_menu_choice(monkeypatch, capsys):
    controller = EmployeeController()

    inputs = iter(["9", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller.display_all_menu()

    output = capsys.readouterr().out
    assert "Invalid choice. Please enter a number from 1 to 6." in output


def test_display_employee_option(monkeypatch):
    controller = EmployeeController()
    called = []

    def fake_get_all_employee():
        called.append(True)

    monkeypatch.setattr(controller, "get_all_employee", fake_get_all_employee)

    inputs = iter(["1", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller.display_all_menu()

    assert len(called) == 1


from unittest.mock import MagicMock

from com.awm.mini_app.controller import employee_conrtoller


def test_create_employee(monkeypatch, capsys):
    # Create fake database objects
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor
    fake_cursor.rowcount = 1

    # Replace actual database connection
    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    # Simulate user input
    inputs = iter(["Aryan", "Hankare", "Kolhapur", "Developer"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller = employee_conrtoller.EmployeeController()
    controller.create_employee()

    # Check database operations
    fake_cursor.execute.assert_called_once()
    fake_connection.commit.assert_called_once()

    # Check employee details passed to SQL
    args = fake_cursor.execute.call_args[0]
    assert args[1] == ["Aryan", "Hankare", "Kolhapur", "Developer"]

    # Check cleanup
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()

    # Check success message
    output = capsys.readouterr().out
    assert "Employee successfully created." in output


def test_create_employee_when_database_unavailable(monkeypatch, capsys):
    # Simulate database connection failure
    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: None
    )

    controller = employee_conrtoller.EmployeeController()

    # The method should return before asking for employee details
    def unexpected_input(_):
        raise AssertionError("Input should not be requested")

    monkeypatch.setattr("builtins.input", unexpected_input)

    controller.create_employee()

    output = capsys.readouterr().out

    assert "Unable to connect to database" in output


def test_get_all_employee(monkeypatch, capsys):
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor

    fake_cursor.fetchall.return_value = [
        (1, "Aryan", "Hankare", "Kolhapur", "Developer"),
        (2, "Rahul", "Patil", "Pune", "Tester")
    ]

    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    controller = employee_conrtoller.EmployeeController()
    controller.get_all_employee()

    fake_cursor.execute.assert_called_once_with(
        "select * from employee"
    )

    fake_cursor.fetchall.assert_called_once()

    output = capsys.readouterr().out

    assert "Aryan" in output
    assert "Rahul" in output

    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()

def test_update_employee(monkeypatch, capsys):
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor
    fake_cursor.rowcount = 1

    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    inputs = iter(["Aryan", "Hankare", "Mumbai", "Developer", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller = employee_conrtoller.EmployeeController()
    controller.update_employee()

    # Check SQL execution
    fake_cursor.execute.assert_called_once()

    # Check values passed to SQL
    args = fake_cursor.execute.call_args[0]
    assert args[1] == ["Aryan", "Hankare", "Mumbai", "Developer", 1]

    # Check transaction
    fake_connection.commit.assert_called_once()

    # Check cleanup
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()

    # Check output
    output = capsys.readouterr().out
    assert "updated successfully" in output

def test_delete_employee(monkeypatch, capsys):
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor
    fake_cursor.rowcount = 1

    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    inputs = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller = employee_conrtoller.EmployeeController()
    controller.delete_employee()

    # Check SQL execution
    fake_cursor.execute.assert_called_once()

    # Check employee ID passed to SQL
    args = fake_cursor.execute.call_args[0]
    assert args[1] == [1]

    # Check transaction
    fake_connection.commit.assert_called_once()

    # Check cleanup
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()

    # Check output
    output = capsys.readouterr().out
    assert "deleted successfully" in output

def test_search_employee(monkeypatch, capsys):
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor
    fake_cursor.fetchone.return_value = (
        1, "Aryan", "Hankare", "Kolhapur", "Developer"
    )

    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    inputs = iter(["1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller = employee_conrtoller.EmployeeController()
    controller.search_employee()

    # Check SQL execution
    fake_cursor.execute.assert_called_once()

    # Check employee ID
    args = fake_cursor.execute.call_args[0]
    assert args[1] == [1]

    # Check result
    output = capsys.readouterr().out
    assert "Aryan" in output

    # Check cleanup
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()

def test_search_employee_not_found(monkeypatch, capsys):
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor
    fake_cursor.fetchone.return_value = None

    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    inputs = iter(["999"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller = employee_conrtoller.EmployeeController()
    controller.search_employee()

    # Check SQL parameter
    args = fake_cursor.execute.call_args[0]
    assert args[1] == [999]

    # Check not-found message
    output = capsys.readouterr().out
    assert "not found" in output.lower()

    # Check cleanup
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()

def test_delete_employee_not_found(monkeypatch, capsys):
    fake_connection = MagicMock()
    fake_cursor = MagicMock()

    fake_connection.cursor.return_value = fake_cursor
    fake_cursor.rowcount = 0

    monkeypatch.setattr(
        employee_conrtoller,
        "get_mysql_connection",
        lambda: fake_connection
    )

    inputs = iter(["999"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    controller = employee_conrtoller.EmployeeController()
    controller.delete_employee()

    # Check employee ID
    args = fake_cursor.execute.call_args[0]
    assert args[1] == [999]

    # Check transaction
    fake_connection.commit.assert_called_once()

    # Check output
    output = capsys.readouterr().out
    assert "not found" in output.lower()

    # Check cleanup
    fake_cursor.close.assert_called_once()
    fake_connection.close.assert_called_once()