def calculate_bmi(weight_in_kg, height_in_m):
    # Check if weight and height are positive numbers
    if weight <= 0 or height <= 0:
        return "Error: Weight and height must be positive numbers."

    # Calculate BMI
    bmi = weight / (height ** 2)

    return round(bmi, 2)

# Example usage:
weight_in_kg = 70  # weight in kilograms
height_in_m = 1.75  # height in meters

bmi = calculate_bmi(weight_in_kg, height_in_m)

print(f"BMI: {bmi}")
