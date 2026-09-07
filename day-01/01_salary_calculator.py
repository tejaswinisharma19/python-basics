basic_salary = int(input())
hra = int(input())
ta = int(input())
professional_tax = int(input())

take_home_salary = basic_salary + hra + ta - professional_tax

print(take_home_salary)