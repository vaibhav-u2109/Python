# num={1,2,3,4,5}
# print(num)
# set1={1,2,2,2,3,}#duplicate values are not allowed in set so its output will be {1,2,3}
# print(set1)

# emptyset=set()
# emptyset.add(1)
# emptyset.add(2)
# emptyset.add(3)
# print(emptyset)

#set methods
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))#it will return a new set which contains all the elements of both sets
print(set1.intersection(set2))#it will return a new set which contains only the common elements of both sets
print(set1.difference(set2))#it will return a new set which contains only the elements of set1 which are not present in set2