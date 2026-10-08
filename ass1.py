#Create a list of 10 numbers, print the sum of last 4 elements from list, 
#find out diff. between max and min element
#insert item in a list at 6th position, this number must be 1/3 of no stored at 4th position.
num=[1,2,3,4,5,6,7,8,9,10]

print("Sum of last 4 digits: ",sum(num[-4::]))
print("Difference between max and min: ",max(num)-min(num))
num.insert(5,(num[4]//(1/3)))
#num.insert(5,66)
print(num)