my_array = [1, 2, 3, 'test', True, False, 0.1]
my_array[4]  
False
my_array.sort()
my_array = [7,6,5,4,3,2,1] 
my_array.sort()
my_array
[1, 2, 3, 4, 5, 6, 7]
sorted([7,6,3,8,1,0]) 
[0, 1, 3, 6, 7, 8]
my_array.insert(0, 999) 
my_array                
[999, 1, 2, 3, 4, 5, 6, 7]
my_array.insert(5, 7)   
my_array
[999, 1, 2, 3, 4, 7, 5, 6, 7]
my_array[0] = 9
my_array        
[9, 1, 2, 3, 4, 7, 5, 6, 7]
my_array.append(3) 
my_array
[9, 1, 2, 3, 4, 7, 5, 6, 7, 3]
my_array.remove(3) 
my_array
[9, 1, 2, 4, 7, 5, 6, 7, 3]
my_array.remove(7) 
my_array
[9, 1, 2, 4, 5, 6, 7, 3]
my_array[3] = 8
my_array        
[9, 1, 2, 8, 5, 6, 7, 3]
my_array[2] = None
my_array
[9, 1, None, 8, 5, 6, 7, 3]
del my_array[2] 
del my_array[2]
my_array        
[9, 1, 5, 6, 7, 3]
my_array.append(2, 8) 
my_array.insert(2, 8) 
my_array
[9, 1, 8, 5, 6, 7, 3]
max(my_array) 
9
min(my_array) 
1
my_array.sort() 
my_array        
[1, 3, 5, 6, 7, 8, 9]
import bisect
bisect.bisect(my_array, 5) 
3
bisect.bisect(my_array, 7) 
5
bisect.bisect(my_array, 9) 
7
bisect.bisect(my_array, 10) 
7
bisect.bisect(my_array, 19) 
7
bisect.bisect(my_array, 0)  
0
bisect.bisect(my_array, -1) 
0
bisect.bisect(my_array, 2)  
1
bisect.insert(my_array, 19) 
bisect.insort(my_array, 19) 
my_array                    
[1, 3, 5, 6, 7, 8, 9, 19]
bisect.bisect(my_array, 2)  
1
range(0,50) 
range(0, 50)
list(my_array) 
[1, 3, 5, 6, 7, 8, 9, 19]
two_dimentions = [[2,4], [5,7]] 
a = [1,2,3]   
b = a
a
[1, 2, 3]
b
[1, 2, 3]
b[0] = 999
a
[999, 2, 3]
b
[999, 2, 3]
a = [1,2,3] 
a
[1, 2, 3]
b
[999, 2, 3]
b = list(a) 
b[0] = 999
a
[1, 2, 3]
b
[999, 2, 3]
a = [1,2,3,4] 
a
[1, 2, 3, 4]
a[2], a[1], a[3] = a[3], a[2], a[1]
a
[1, 3, 4, 2]
a = [1,2,3,4] 
a[2], a[1], a[3] = a[1], a[2], a[0] 
a
[1, 3, 2, 1]