def reversed_list(lst1,lst2):
 lst1.sort()
 lst2.sort()
 if (lst1==lst2):
    print('equal')
 else:
    print('unequal')

reversed_list([1,4,3,2,5],[5,2,3,1,4])
