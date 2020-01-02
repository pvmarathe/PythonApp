# What is 7 to the power of 4?

7**4

#Split this string: into a list.
s = "Hi there Sam!"
s
ls = s.split()
ls


'''
Given the variables:

planet = "Earth"
diameter = 12742
Use .format() to print the following string:

The diameter of Earth is 12742 kilometers.
'''
planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers".format(planet,diameter))


# Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst
lst[3][1][2][0]


# Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d
d.keys()
d['k1']
d['k1'][3]['tricky'][3]['target'][3]

# What is the main difference between a tuple and a list

# A list is mutable while tuple is immutable


'''
Create a function that grabs the email website domain from a string in the form:

user@domain.com
So for example, passing "user@domain.com" would return: domain.com
'''


def subset_grab(some_str):
	return some_str.split('@')[1]

subset_grab('user@domain.com')

'''
Create a basic function that returns True if the word 'dog' is
contained in the input string. Don't worry about edge cases like
a punctuation being attached to the word dog, but do account for
capitalization.

'''
def findy(some_str):
	return 'dog' in some_str.lower().split()




'''
Create a function that counts the number of times the word "dog"
occurs in a string. Again ignore edge cases.
'''
​
def countDog(some_string):
    return some_string.split().count('dog')

countDog('This dog runs faster than the other dog dude!')


def countDog2(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count

countDog2('This dog runs faster than the other dog dude!')


'''Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:

seq = ['soup','dog','salad','cat','great']
should be filtered down to:

['soup','salad']
'''

seq = ['soup','dog','salad','cat','great']
list(filter (lambda element:element[0]!='s',seq))


'''
You are driving a little too fast, and a police officer stops you.
 Write a function to return one of 3 possible results: "No ticket",
  "Small ticket", or "Big Ticket". If your speed is 60 or less,
  the result is "No Ticket". If speed is between 61 and 80 inclusive,
  the result is "Small Ticket". If speed is 81 or more, the result is
   "Big Ticket". Unless it is your birthday (encoded as a boolean value
    in the parameters of the function) -- on your birthday, your speed
     can be 5 higher in all cases.
'''

def caught_speeding(speed,is_birthday):
    if is_birthday:
        speeding = speed - 5
    else speeding = speed

    if speeding > 80:
        return "Big Ticket"
    elif speeding > 60:
        return "Small Ticket"
    else:
        return "No Ticket"


caught_speeding(81,True)
caught_speeding(81,False)


caught_speeding
