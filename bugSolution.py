def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list) 
print(f"The average is: {average}") #This will print 0 instead of error 