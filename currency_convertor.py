def convert_currency(amount, from_currency, to_currency):
    # Exchange rates relative to 1 USD
    rates = {
        "USD": 1.0,
        "INR": 83.73,
        "EUR": 0.9
    }

    # Check if currencies are valid
    if from_currency not in rates or to_currency not in rates:
        return "Error: Unsupported currency."

    # Convert amount to USD
    amount_in_usd = amount / rates[from_currency]

    # Convert USD to target currency
    amount_in_target_currency = amount_in_usd * rates[to_currency]

    return amount_in_target_currency

# Example usage:
amount = -100
from_currency = "USD"
to_currency = "INR"

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
