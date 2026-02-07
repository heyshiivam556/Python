## Lists

fnds = ['apple','Rohan',57,True,'Shivam']
fnds[3] = 'rajkumar'
print(fnds)

nums = [1,3,43,12]
nums.sort()
print(nums)
# print(nums.sort()) X -can't directly sort and print  

nums.reverse()
print(nums)

#direct input in the list
fruits = []
fruits.append(input('enter a fruit: '))
fruits.append(input('enter a fruit: '))
fruits.append(input('enter a fruit: '))
fruits.append(input('enter a fruit: '))
fruits.append(input('enter a fruit: '))
print(fruits)
##Tuples

my_tuple = (1,2,3,4,6,7,8,0)
print(my_tuple.count(0)) #1 -no of occurance
print(my_tuple.index(0)) #7 -position of occurance

#unpacking tuple
abc = (1,2,3)
a,b,c = abc
print(a,b,c)

#no of digits 
nums = (1,0,3,4,2,4,0,0,2,0,7,0,2,0,6)
print('no of zeros:',nums.count(0))

