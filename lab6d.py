# Author: Mehtaash Kaur
# Date: 2026-11-04

# TO DO 1: Create function times_ten as instructed in readme.md file. 

# TO DO 2: Run the script.
def times_ten(start_index: int, end_index: int):
    result = {}
    for i in range(start_index, end_index + 1):
        result[i] = i * 10
    return result
my_dictionary = times_ten(2, 6)
print(my_dictionary)