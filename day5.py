# question 1

#CReate a 5*5 matrix of random integers(1-90)
import numpy as np
a=np.random.randint(1,90,size=(5,5))
b= a.reshape(5, 5)
print(b)


#FIND MEAN OF VALUE ROW AND COLUMN WISE
print(np.mean(b,axis=0))
print(np.mean(b,axis=1))

#REPLACE ALL EVEN NUMBERS WITH -1

modified_b = np.where(b%2==0,-1,b)
print(modified_b)


#SORT THE ARRAY ROW AND COLUMN WISE
print(np.sort(b,axis=0))
print(np.sort(b,axis=1))


#FIND ROW AND COLUMN WISE SUM SAPARETELY
print(np.sum(b,axis=0))
print(np.sum(b,axis=1))



#COUNT THE NUMBER OF -VE IN EAcH COLUMN
count_-ve = np.sum(np.where (b<0, 1,0), axis=0)
print(count_col)









# question ----2
#ques
#craete a 5*5 array(stock level)
import numpy as np
a=np.random.randint(size=(5,5))
stock= a.reshape(5, 5)
print(stock)


#create another 5*5 array(demand)
b=np.random.randint(size=(5,5))
demand= b.reshape(5, 5)
print(demand)



#compur:
#remaining stock=stock-demand

remaning = stock-demand
print(remaning)


#replace:
#negative values=0(out of stock)
replace_rem = np.where(remaning<0, 0, remaning)
print(replace_rem)

#find:
# total shortage 
total_shortage= np.sum(where(remaninig<0,remaninig * -1,0) axis=0 )
print(total_shortage)


#product with zero stock
product_shortage=np.sum(np.where(remaining==0,1,0),axis=0)
print(product_shortage)

#sort each row based on reamining stock
sorted=np.sort(replace_rem,axis=1)
print(sorted)





import pandas as pd
file_=pd.read_csv('student_data.csv')
print(file_)