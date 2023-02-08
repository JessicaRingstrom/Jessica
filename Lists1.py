list1 = ["Heela", "Illari", "Anuka", "Riley", "Anna"]
list2 = list1.copy()
list2.reverse()
print(list2)
element1 = [list2[0]]
print(element1)
list1.insert(3, element1)
print(list1)
print(list1.count(element1))


numbers1 = ["3", "6", "8", "2", "4"]
numbers1.append("9")
print(numbers1)

numbers1 = ["3", "6", "8", "2", "4"]
numbers2 = ["9"]
numbers1.extend(numbers2)
print(numbers1)

numbers1 = ["3", "6", "8", "2", "4"]
numbers1.pop()
print(numbers1)

numbers1 = ["3", "6", "8", "2", "4"]
numbers1.remove("4")
print(numbers1)

numbers1 = ["3", "6", "8", "2", "4"]
number_of_elements = len(numbers1)
print(number_of_elements)