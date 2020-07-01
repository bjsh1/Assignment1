#1. Write a Python program to count the number of characters (character frequency) in a string.
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))


#2 Write a Python program to get a string made of the first 2 and the last 2 charsfrom a given a string. 
# If the string length is less than 2, return instead of the empty string.

your_string=input("Enter any string: ")
first_two= your_string[0:2]
last_two=your_string[-2:]

if len(your_string)<2:
    print("Empty String")
else:
    print(first_two+last_two)


#3. Write a Python program to get a string from a given string where all occurrences of 
# its first char have been changed to '$', except the first char itself.

character=input("Enter any character: ")
char=list(character)
value=char[0]
for index in range(1,(len(character))):
    if char[index]==char[0]:
        char[index]="$"
    value+=char[index]
print(value)



# 4. Write a Python program to get a single string from two given strings, separated 
# by a space and swap the first two characters of each string.

first_string=input("Enter your First string: ")
second_string=input("Enter your second string: ")

single_string=second_string[:2]+first_string[2:]+" "+first_string[:2]+second_string[2:]

print(single_string)


#5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

text=input("Enter your text here: ")

if len(text)>2:
    if text[-3:]=="ing":
        text+="ly"
    else:
        text+="ing"
print(text)



#6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

text=input("Enter your text: ")
#text="The lyrics is not that poor!"
#text="The lyrics is poor!"

if "not" in text:
    ind=text.index("not")
    for_replace=text[ind:-1]
    print(text.replace(for_replace,"good"))
else:
    print(text)


#7. Write a Python function that takes a list of words and returns the length of the longest one.

text=["pen",'pineapple','apple','applepen','penpineappleapplepen']
longest=text[0]

for num in range(len(text)):
    if len(text[num])>len(longest):
        longest=text[num]
print(longest,len(longest))



#8. Write a Python program to remove the n th index character from a nonempty string.
text=input("Enter any text here: ")
n=int(input("Enter the index number of a character you want to remove: "))
if len(text)>0:
    
    #print("You have removed %s from your text {text}".format{})
    print(text.replace(text[n],'',1))
else:
    print("you can't remove an empty string")



# 9. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

text=input("Enter your text: ")
new_text=text[-1]+text[1:-1]+text[0]
print(new_text)



# 10. Write a Python program to remove the characters which have odd index values of a given string.

text=input("Enter your text: ")
new_text=text[0::2]
print(text)
print(new_text)



# 11. Write a Python program to count the occurrences of each word in a given sentence.

text=input("Enter any sentence: ")
counts=dict()
word=text.split()
for ch in word:
    if ch in counts:
        counts[ch]+=1
         
    else:
        counts[ch]=1
print(counts)   



#12. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

text=input("Enter any text: ")
print(text.upper())
print(text.lower())



#13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

word=input("Enter any words: ")

items = [item for item in word.split(",")]
print(",".join(sorted(list(set(items)))))


#14. Write a Python function to create the HTML string with tags around the word(s).

text=input("Enter any text: ")
tag=input("Enter any html tag")
def html(text,tag):
    print("<%s>%s</%s>"%(tag,text,tag))

html(text,tag)


#15. Write a Python function to insert a string in the middle of a string.

def middle(text, word):
	return text[:2] + word + text[2:]

print(middle('[[]]', 'Python'))
print(middle('{{}}', 'PHP'))


#16. Write a Python program to sum all the items in a list.

items=[8,9,4,5,6,1,2]
sums=0
for item in items:
    sums+=item
print(sums)



#17. Write a Python program to multiplies all the items in a list.

items=[8,9,4,5,6,1,2]
muls=1
for item in items:
    muls*=item
print(muls)


#18. Write a Python program to get the largest number from a list.

items=[8,9,4,5,6,1,2]
maximum=items[0]
for num in items:
    if num>maximum:
        maximum=num
print("Maximum: ", maximum)



#19. Write a Python program to get the smallest number from a list.

items=[8,9,4,5,6,1,2]
mini=items[0]
for num in items:
    if num<mini:
        mini=num
print("Minimum: ", mini)



#20. Write a Python program to count the number of strings 
# where the string length is 2 or more and the first and last character are same from a given list of strings.

text=['abc','def','aba','dad']
count=0
for word in text:
    if len(word)>2 and word[0]==word[-1]:
        count+=1
print(count) 



#21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.

lists=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def arrange(data):
    return data[1]
lists.sort(key=arrange)
print(lists)



#22. Write a Python program to remove duplicates from a list.
lists=[5,8,9,7,6,1,3,2,4,5,6,9]

new_list=[]
for num in lists:
    if num not in new_list:
        new_list.append(num)        
print(new_list)



#23. Write a Python program to check a list is empty or not.

#lists=[2,5,6,8]
lists=[]
if len(lists)==0:
    print("List is empty")
else:
    print(lists)



#24. Write a Python program to clone or copy a list.

import copy
list1=[5,6,8,9,10]
list2=copy.deepcopy(list1)
print(list2)



#25. Write a Python program to check whether all dictionaries in a list are empty or not.

lists=[{},{},{}]
list2=[{5,6},{},{}]
print(all(not d for d in lists))
print(all(not d for d in list2))



#26. Write a Python program to insert a given string at the beginning of all items in a list.

value=input("Insert any value: ")
lists=['apple','pen','pineapple']
lists.insert(0,value)
print(lists)



#27. Write a Python program to replace the last element in a list with another list.

list1=['apple','pen','pineapple']
list2=[5,6,8,9,10]
value1=list1[-1]

lists=str(list1).replace(value1,str(list2))

print(lists)



#28. Write a Python script to add a key to a dictionary.

d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


#29. Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic={}

dic2.update(dic3)
dic1.update(dic2)
dic.update(dic1)

print(dic)



#30. Write a Python script to check whether a given key already exists in a dictionary.

key=int(input("Enter any key: "))

dic={3: 10, 9: 20, 1: 30, 4: 40, 8: 50, 6: 60}

if key in dic:
    print("Key exists")
else:
    print("Key doesn't exists")


#31. Write a Python program to iterate over dictionaries using for loops.

dic = {'Apple': 1, 'Pen': 2, 'Pineapple': 3,'Applepen':4} 
for key, value in dic.items():
     print(key, 'is', dic[key]) 


#32. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n=int(input("Input a number "))
dic = dict()

for x in range(1,n+1):
    dic[x]=x*x

print(dic) 


#33. Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are square of keys

dic=dict()
for x in range(1,16):
    dic[x]=x**2
print(dic)  



#34. Write a Python script to merge two Python dictionaries.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic={}

dic1.update(dic2)

print(dic1)


#35. Write a Python program to iterate over dictionaries using for loops.

dic = {'Apple': 1, 'Pen': 2, 'Pineapple': 3,'Applepen':4} 
for key, value in dic.items():
     print(key, 'is', dic[key]) 



#36. Write a Python program to sum all the items in a dictionary.

dic = {'x':100,'y':-54,'z':27,'a':-5,'b':24,'c':-4,'d':47}
print(sum(dic.values()))



#37. Write a Python program to multiply all the items in a dictionary.

dic = {'x':100,'y':54,'z':27,'a':5,'b':24,'c':4,'d':47}
mul=1
for key in dic:
    mul*=dic[key]
print(mul)



#38. Write a Python program to remove a key from a dictionary.
dic = {'a':1,'b':2,'c':3,'d':4}

if 'a' in dic: 
    del dic['a']
print(dic)


#39. Write a Python program to unpack a tuple in several variables.

values = (4, 8, 3) 

n1, n2, n3 = values

print(n1)
print(n2)
print(n3)


#40. Write a Python program to add an item in a tuple.

values = (4, 8, 3)  

values = values + (4, 6, 2, 8, 3, 1,)
print(values)



#41. Write a Python program to convert a tuple to a string.

values = ('p','e','n','p','i','n','e')
strings =  ''.join(values)
print(strings)



#42. Write a Python program to convert a list to a tuple.

values = [5,8,9,7,6,1,3,2,4,5,6,9]
tuples = tuple(values)

print(tuples)



#43. Write a Python program to remove an item from a tuple.

values = "w","r", "s", "o", "u", "r", "c", "e"

items = list(values) 

items.remove("c") 

values = tuple(items)
print(values)



#44. Write a Python program to slice a tuple.

values = ("w","r", "s", "o", "u", "r", "c", "e")
slice = values[3:5]
print(slice)



#45. Write a Python program to find the index of an item of a tuple.

values = ("w","r", "s", "o", "u", "r", "c", "e")
ind=values.index('s')
print(ind)


#46. Write a Python program to find the length of a tuple

values = ("w","r", "s", "o", "u", "r", "c", "e")
length=len(values)

print("Length: ", length)


                                                        #Functions

#1. Write a Python function to find the Max of three numbers.

def maximum(a, b, c): 
  
    if (a >= b) and (a >= c): 
        maxs = a 
  
    elif (b >= a) and (b >= c): 
        maxs = b 
    else: 
        maxs = c 
          
    return maxs 

print(maximum(4,5,6))



#2. Write a Python function to sum all the numbers in a list.

def sums(lists):
    list_sum=0
    for num in lists:
        list_sum+=num
    return list_sum

print(sums([4,5,6]))


#3. Write a Python function to multiply all the numbers in a list.
def mulss(lists):
    list_mult=1
    for num in lists:
        list_mult*=num
    return list_mult

print(mulss([4,5,6]))


#4. Write a Python program to reverse a string.

def revers_string(text): 
    str = "" 
    for i in text: 
        str = i + str
    return str

print(revers_string("Hello"))



#5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

n=int(input("Enter number : "))
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(n))



#6. Write a Python function to check whether a number is in a given range.

def test(n):
    if n in range(15,39):
        print( "{} is in the range".format(n))
    else :
        print("The number is not in range.")
test(25)



#7. Write a Python function that accepts a string and 
# calculate the number of upper case letters and lower case letters.

def test(sentence):
    dic={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in sentence:
        if c.isupper():
           dic["UPPER_CASE"]+=1
        elif c.islower():
           dic["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", sentence)
    print ("No. of Upper case characters : ", dic["UPPER_CASE"])
    print ("No. of Lower case Characters : ", dic["LOWER_CASE"])

test('The quick Brown Fox')



#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_elements(list1):
  lists = []
  for item in list1:
    if item not in lists:
      lists.append(item)
  return lists

print(unique_elements([1,2,3,3,3,3,4,5])) 



#9. Write a Python function that takes a number as a parameter and check the number is prime or not.

def test(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test(2))



#10. Write a Python program to print the even numbers from a given list.

def is_even(lists):
    even_num = []
    for num in lists:
        if num % 2 == 0:
            even_num.append(num)
    return even_num
print(is_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))



#11. Write a Python program to create a lambda function that adds 15 to a given 
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

adds = lambda a : a + 15
print(adds(10))
mults = lambda x, y : x * y
print(mults(12, 4))



#12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

def calculate(n):
 return lambda x : x * n
result = calculate(2)
print("Double the number of 15 =", result(15))
result = calculate(3)
print("Triple the number of 15 =", result(15))
result = calculate(4)
print("Quadruple the number of 15 =", result(15))
result = calculate(5)
print("Quintuple the number 15 =", result(15))



#13. Write a Python program to sort a list of tuples using Lambda.

lists=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lists.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(lists)

#14. Write a Python program to sort a list of dictionaries using Lambda.

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)


#15. Write a Python program to filter a list of integers using Lambda.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)



#16. Write a Python program to square and cube every number in a given list of integers using Lambda.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)



#17. Write a Python program to find if a given string starts with a given character using Lambda.

starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Applepen'))
starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Pineapplepen'))



#18. Write a Python program to check whether a given string is number or not using Lambda.

is_num = lambda q: q.replace('.','',1).isdigit()
print(is_num('26587'))

print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))



#19. Write a Python program to create Fibonacci series upto n using Lambda.


from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1]) 
print(fib(5)) 


#20. Write a Python program to find intersection of two given arrays using Lambda.

array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]

result = list(filter(lambda x: x in array1, array2)) 
print ("\nIntersection of the arrays: ",result)
