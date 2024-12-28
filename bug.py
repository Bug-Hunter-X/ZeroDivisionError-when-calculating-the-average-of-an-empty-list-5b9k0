def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list) # ZeroDivisionError occurs here if my_list is empty
print(f"The average is: {average}")