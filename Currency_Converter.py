def currency_converter(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None

    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount

def show_rates(rates):
    print("\n💱 Current exchange rates (relative to USD):")
    for currency, value in rates.items():
        print(f"{currency} = {value:.2f}")

def update_rate(rates):
    currency = input("Enter currency code to update (USD, EUR, JOD, GBP): ").upper()
    if currency in rates:
        new_value = float(input(f"Enter new rate for {currency}: "))
        rates[currency] = new_value
        print(f"Rate for {currency} updated to {new_value:.2f}")
    else:
        print("Invalid currency code.")

# أسعار صرف ابتدائية
rates = {
    "USD": 1.0,
    "EUR": 0.9,
    "JOD": 0.71,
    "GBP": 0.8
}

# البرنامج الرئيسي
while True:
    print("\nOptions:")
    print("1 - Convert currency")
    print("2 - Show exchange rates")
    print("3 - Update exchange rate")
    print("4 - Exit")

    choice = input("Choose an option (1/2/3/4): ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (USD, EUR, JOD, GBP): ").upper()
        to_currency = input("To currency (USD, EUR, JOD, GBP): ").upper()

        result = currency_converter(amount, from_currency, to_currency, rates)

        if result is None:
            print("Invalid currency code.")
        else:
            print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

    elif choice == "2":
        show_rates(rates)

    elif choice == "3":
        update_rate(rates)

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, please try again.")
