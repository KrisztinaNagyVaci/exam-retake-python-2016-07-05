# Write unittests for this function:

import unittest

list1 = [1, 2, 3, 4]
number1 = 3

def filter_smaller_than_number(original_list, number):
  if type(original_list) != list:
    return []
  output = []
  for element in original_list:
    if element < number:
      output.append(element)
  return output

print(filter_smaller_than_number(list1, number1))

class MyTest(unittest.TestCase):
    def test_list_input_was_given(self):
        self.assertEqual(filter_smaller_than_number([1, 2, 3, 4], 3), [1, 2])

    def test_nonlist_input_was_given(self):
        self.assertEqual(filter_smaller_than_number('hello', 3), [])

    def test_input_number_is_smaller_than_any_list_elements(self):
        self.assertEqual(filter_smaller_than_number([3, 4, 5, 6], 2), [])


if __name__ == '__main__':
    unittest.main()
