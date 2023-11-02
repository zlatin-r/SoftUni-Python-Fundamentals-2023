data = {}
command = input()

while command != "End":
    company_name, employee_id = command.split("->")

    if company_name not in data:
        data[company_name] = []

    if employee_id not in company_name:
        data[company_name].append(employee_id)

    command = input()

for company, employees in data.items():
    print(company.strip())
    for ID in employees:
        print(f"-- {ID.strip()}")


