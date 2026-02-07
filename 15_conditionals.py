a = int(input('enter a num:'))

if(a<18):
    print(f'num is less than 18 i.e {a}')
    print('if runned')
elif(a==18):
    print('num is equal to 18')
    print('elif runned')
else:
    print(f'num is more than 18 i.e {a}')
    print('else runned')

#greatest  of three numbers
a=5
b=16
c=12

if(a>b and a>c):
    print(f'{a} is greatest')
elif(b>a and b>c):
    print(f'{b} is greatest')
else:
    print(f'{c} is greatest')
    

