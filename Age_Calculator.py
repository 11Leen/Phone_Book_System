import datetime

def calculate_age(birthdate):
    today = datetime.date.today()  # تاريخ اليوم
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    # تعديل إذا الأيام سالبة
    if age_days < 0:
        age_months -= 1
        prev_month = (today.month - 1) if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days_in_prev_month = (datetime.date(prev_year, prev_month + 1, 1) - datetime.date(prev_year, prev_month, 1)).days
        age_days += days_in_prev_month

    # تعديل إذا الأشهر سالبة
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days


# إدخال تاريخ الميلاد
year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

birthdate = datetime.date(year, month, day)
years, months, days = calculate_age(birthdate)

print(f"You are {years} years, {months} months, and {days} days old.")

# عدد الأيام التي عاشها المستخدم
days_lived = (datetime.date.today() - birthdate).days
print(f"You have lived {days_lived} days so far.")
