'''
collections
list,tuple,dicitionaries
list-> collection of different elements or objects
->ordered data
->operations:insert,delete(remove),append,update
->list is a mutable(can be changed) datastructure
->we can represent using sqaure brackets
syntax:list_name=[object1,obj2,obj3,.....,objn]
'''
'''operations'''
mobiles=['iphone','samsung','vivo']
print(mobiles)

#get indexed element
print(mobiles[-1])
print(mobiles[2])

#insert at a given position
mobiles.insert(2,'oppo')
print(mobiles)

#append happens at the end of list
mobiles.append('oneplus')
print(mobiles)

#pop deletes last element
mobiles.pop()
print(mobiles)

#indexed element is popped
mobiles.pop(0)
print(mobiles)

#remove removes specific data
mobiles.remove('vivo')
print(mobiles)

#insert- indexing starts from 0 but if we put a number greater than the last index it'll automatically take the last posiiton to fill in
mobiles.insert(1,'hello')
print(mobiles)

#delete the whole list->the elements will be removed but the list remains in the memory
mobiles.clear()
print(mobiles)

#ways to empty list
mobiles=['iphone','samsung','vivo']
#update the list to empty
mobiles=[]
print(mobiles)

#update the list->updates the element in that position to the desired one
mobiles=['iphone','samsung','vivo']
mobiles[1]='blackberry'
print(mobiles)

mobiles=['iphone','samsung','vivo','oppo','nothing']
print(mobiles[True])
print(mobiles[not True])

#iterate and print the elements
mobiles=['iphone','samsung','vivo','oppo','nothing']
count=1
for ele in mobiles:
    print(count,ele)
    count+=1
    
#iterate to find only even elements
mobiles=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        print(mobiles[i])
        
#using i variable only
mobiles=['iphone','samsung','vivo','oppo','nothing']
count=0
for i in range(0,len(mobiles)):
    print(mobiles[i])
    i+=2

#reverse the even elements only
mobiles=['iphone','samsung','vivo','oppo','nothing']
for i in range(0,len(mobiles)):
    if i%2==0:
        rev=mobiles[i]
        print(rev[::-1])
    else:
        print(mobiles[i])

#print the second half till the element k first and then print the rest as it is
'''
arr=[1,2,3,4,5]
k=4
[4,5,1,2,3]
'''
arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
#print(first+second)
first.extend(second)
print(first)
print(second)0569

#another approach
arr=[1,2,3,4,5]
k=3
#[5,4,3,1,2]
first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)

