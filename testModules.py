import triangles_module as tm
import lists_module as lm

print(tm.triangleAreaA_Ha(5, 12))  
print(tm.triangleAreaA_Ha(0, 10))
print(tm.triangleAreaA_Ha(7, -3))

print(tm.triangleArea(8, 15, 17))
print(tm.triangleType(5, 5, 5))

print(tm.trianglePerimeter(3, 4, 5))
print(tm.isExistsTriangle(1, 2, 3))


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(lm.intersection(list1, list2))
print(lm.union(list1, list2))
print(lm.difference(list1, list2))
print(lm.reverse_list(list1))
print(lm.reverse_list(['a', 'b', 'c', 'd']))
