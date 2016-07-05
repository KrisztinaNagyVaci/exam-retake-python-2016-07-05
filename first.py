# Create a function that takes a list as a parameter,
# and returns a boolean it should return True if none of the elements are
# even, False otherwise
# It should raise an error if the parameter is not a list

list1 = [1, 2, 3, 4]
list2 = [1, 3, 5]
nonlist = 'I am a string'

def returnTrueifElementsEven(input_list):
    if type(input_list) != list:
        raise TypeError('The argument is not a list')
    list_of_evens = []
    for element in input_list:
        if element % 2 == 0:
            list_of_evens.append(element)
    if len(list_of_evens) == 0:
        return True
    else:
        return False

print(returnTrueifElementsEven(list1))
