# Write unittests for this function:

def filter_smaller_than_number(original_list, number):
  if type(original_list) != list:
    return []
  output = []
  for element in original_list:
    if element < number:
      output.append(element)
  return output

