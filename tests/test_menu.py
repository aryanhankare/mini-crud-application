
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
