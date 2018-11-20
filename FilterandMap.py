'''
alpha=['a','b','d','e','f','i','l','m','n','o','p','q','u','a','w','x','y','z']

def vowels_data(apha):
    number=['a','e','i','o','u']
    if (apha in number):
        return True
    else:
        return False

vowels=filter(vowels_data,alpha)
print("The vowels are :")

for vowel in  vowels:
    print(vowel)

'''
'''
def calculate_square(n):
    return n*n

number=(1,2,3,4)

result=map(calculate_square,number)

print(result)

number1 = list(result)
print(number1)
'''
'''
import copy

list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=copy.copy(list1)
#list1.append([4,4,4])
list1[2][2]=[10]

print('old list',list1)
print('new list',list2)
'''
'''
list1=[1,2,3]
list2=list1
print(list1)
print(list2)

list1[0]=5

print(list1)
print(list2)

list1=[4,5,6]
print(list1)
'''
a=10000
b=10000
print(id(a))
print(id(b))





