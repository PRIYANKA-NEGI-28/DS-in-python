#data structure and algorithm


#list 

lst=[1,2,3,4,"value","c",[2,3]]
#append()
lst.append("priyanka")
print(lst)

lst.append([8,9])
print(lst)


#extend ---(takes only irtrrable data)
lst.extend([8,9])
print(lst)

#insert
#lst.insert([index,value]) --- tu put in a specific place
lst.insert(2,"hello")
print(lst)


#pop()
lst.pop()
print (lst)

#remove -- jo number denge vo vala first occurance se remove kr dega 
lst.remove(2)
print(lst)

#index ---- what is the index of element
print(lst.index('value'))

#count---- how many times does this element exist
lst.count(3)


l=[1,6,5,9,0,8]
#sort()--- sort the same array we have 
#----or  sort only a type of value example integer
l.sort()
print(l)

#sum,max,min ------ lst.sum() -- error as function
#should written as an argument or assigned to a variable 
z=[2,7,9,8,5,34]

#sum
var=sum(z)
print(var)
or
#print(sum(z))

#max
var=max(z)
print(var)

#min
var=min(z)
print(var)

#sorted. ---- sort and make a new list internally
var=sorted(z)
print(var)






#TUPLES
#immutable

tp=(31,2,23,4)

#tp.sort() error bcz tuples are immutable
print(tp)
#a=sorted(tp)   sorted() makes a new list and doesnt interupt the main tuple
a=tuple(sorted(tp))  #tuple converts the list created by sorted() into a tuple
print(a)



#function 


p=(1,3,5,7,9,8,6,4,2,7,9,8,6,4,2)

#count() to count elements
print(p.count(7))

#index() to find the index of the element
print(p.index(7))

#len() to finc the length
print(len(p))

#sum() to find th  total
print(sum(p))


#max() min() to find the highest and lowest
print(max(p))
print(min(p))

#sorted() returns a list
print(sorted(p))


#take 2 list
#add the consecutive indices 
# answer should be a list always

size=int(input("Enter the size"))
lis1=[]
lis2=[]
i=1
while i<=size:
  a=int(input())
  lis1.append(a)
  i=i+1
print(lis1)
i=1
while i<=size:
  b=int(input())
  lis2.append(b)
  i=i+1
print(lis2)