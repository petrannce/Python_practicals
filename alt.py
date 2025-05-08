

def double_numbers(numbers):
    numbers[:] = [num * 2 for num in numbers]
    return my_list

my_list = [1, 2, 3]
result = double_numbers(my_list)

print(my_list)  # Output: [2, 4, 6]