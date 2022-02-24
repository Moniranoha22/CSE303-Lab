list1 = [10, 5, 8, 12, 3, 25]
list2 = [12, 5, 8, 16, 3, 20]

even_list = []
odd_list = []
for number in list1:

   if (number % 2 != 0 ):
       odd_list.append(number)

print(odd_list)
for number in list2:

   if (number % 2 == 0 ):
       even_list.append(number)

print(even_list)