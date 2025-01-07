def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0 # Handle list of zeros
    average = total / len(numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") #This will print 0

my_numbers_with_zero = [10, 0, 20, 30]
result = calculate_average(my_numbers_with_zero)
print(f"The average is: {result}")

my_zero_list = [0,0,0,0]
result = calculate_average(my_zero_list)
print(f"The average is: {result}") #This will print 0