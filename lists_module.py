def create_int_list():
   
    n = int(input("Въведете брой елементи: "))
    result = []

    for i in range(n):
        num = int(input(f"Въведете число {i + 1}: "))
        result.append(num)

    return result


def intersection(list1, list2):

    result = []
    for element in list1:
        if element in list2 and element not in result:
            result.append(element)
    return result


def union(list1, list2):
   
    result = []

    for element in list1:
        if element not in result:
            result.append(element)

    for element in list2:
        if element not in result:
            result.append(element)

    return result


def difference(list1, list2):
  
    result = []
    for element in list1:
        if element not in list2:
            result.append(element)
    return result


def reverse_list(lst):

    result = []
    for i in range(len(lst) - 1, -1, -1):   # Iterate from last index to first step -1
        result.append(lst[i])
    return result


