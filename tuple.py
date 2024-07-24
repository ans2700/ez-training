#tuple:
'''
once put data can't be edited
smae as list but ()braces
tuple_name=(,,,,)
it is immutable
no append or replace functions
only one method called fetch()
'''
student=(101,'navya','cse','hyd')
#updating existing data with new data
#student[2]='ece'
print(student)
# initializing string
text = "navya"
# using naive method to get count
# of each element in string
freq={}
for i in text:
	if i in freq:
		freq[i]+=1
	else:
		freq[i]=1

# printing result
print("Count of all characters is:"+str(freq))
