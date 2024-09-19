from datetime import date

def calculate_age_in_years(birth_year):
    today = date.today()

    # Check if birth_year is in the future
    if birth_year > today.year:
        return "Error: Birth year cannot be in the future."

    # Calculate age in years
    age_in_years = today.year - birth_year

    return age_in_years

# Example usage:
birth_year = 1997
age_in_years = calculate_age_in_years(birth_year)

print(f"Age in Years: {age_in_years}")
