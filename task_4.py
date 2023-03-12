revenue = int(input("Введите выручку фирмы: "))
expenses = int(input("Введите издержки фирмы: "))
if revenue > expenses:
    print("Финансовый результат - прибыль.")
else:
    print("Финансовый результат - убыток.")

profit = revenue - expenses
print(f"Прибыль равна: {profit}")

print(f"Рентабельность выручки: {profit/revenue}")
employees = int(input("Введите количество сотрудников: "))
print(f"Прибыль фирмы в расчете на одного сотрудника: {profit/employees}")