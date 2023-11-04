import employee_info as info

def test_get_employees_by_age_range():
    lowerLimit = 20
    upperLimit = 30
    result = info.get_employees_by_age_range(lowerLimit,upperLimit)
    assert (result == [{'age': 25, 'department': 'Marketing', 'name': 'Jane', 'salary': 60000},
 {'age': 23, 'department': 'Marketing', 'name': 'Mary', 'salary': 56000}])

def test_calculate_average_salary():
    result = info.calculate_average_salary()
    assert (result == 60166.666666666664)

def test_get_employees_by_dept():
    dept = "Sales"
    result = info.get_employees_by_dept(dept)
    assert (result == [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}])