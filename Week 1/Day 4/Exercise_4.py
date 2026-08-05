from datetime import date

def calculate_age(birth_date, today):
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


today = date.today()

birth_date_passed = date(1995, 3, 15)
birth_date_not_passed = date(1995, 12, 25)

print(f"Today's date: {today}")

age1 = calculate_age(birth_date_passed, today)
print(f"Birth date: {birth_date_passed} -> Age: {age1}")

age2 = calculate_age(birth_date_not_passed, today)
print(f"Birth date: {birth_date_not_passed} -> Age: {age2}")
