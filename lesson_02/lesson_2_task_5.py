def month_to_season(month):
    if month in [1, 2, 12]:
        return "Winter"
    if month in [3, 4, 5]:
        return "Spring"
    if month in [6, 7, 8]:
        return "Summer"
    if month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
