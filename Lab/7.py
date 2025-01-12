class Employee:
    def __init__(self, emp_id, name, **kwargs):
        self.name = name
        self.id = emp_id

    def get_info(self):
        return self.id, self.name


class Manager(Employee):
    def __init__(self, emp_id, name, department, **kwargs):
        super().__init__(emp_id, name, **kwargs)
        self.department = department

    def get_info(self):
        return self.id, self.name, self.department

    def manage_project(self):
        print("Managing a project...")


class Technician(Employee):
    def __init__(self, emp_id, name, specialization, **kwargs):
        super().__init__(emp_id, name, **kwargs)
        self.specialization = specialization

    def get_info(self):
        return self.id, self.name, self.specialization

    def perform_maintenance(self):
        print("Performing maintenance...")


class TechManager(Manager, Technician):
    def __init__(self, emp_id, name, department, specialization, employee_list):
        super().__init__(emp_id, name, department=department, specialization=specialization)
        self.employee_list = employee_list

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_team_info(self):
        for i in self.employee_list:
            print(i.get_info())


tech_guy = Technician(1, "Billy", "Toilets")
management_guy = Manager(2, "Willy", "Medical")
another_management_guy = Manager(3, "Dilly", "Medical")

tech_guy.perform_maintenance()

management_guy.manage_project()

tech_manager = TechManager(0, "Boss", "Medical", "Drinking", [])

tech_manager.add_employee(tech_guy)
tech_manager.add_employee(management_guy)
tech_manager.add_employee(another_management_guy)

print(tech_manager.get_info())

tech_manager.get_team_info()