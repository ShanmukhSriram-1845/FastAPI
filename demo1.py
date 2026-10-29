# # # # # #statements
# # # # # """
# # # # # x = 50
# # # # # y = 70

# # # # # Result = y-x
# # # # # if Result >0 :
# # # # #     print("positive")
# # # # # else:
# # # # #     print("Negative") 
# # # # # """
# # # # # #Even and Odd
# # # # # """x = 13
# # # # # if x % 2 ==0 :
# # # # #     print("even")
# # # # # else:
# # # # #     print("Odd")
# # # # # """
# # # # # #Logical Operators
# # # # # """
# # # # # x = 21
# # # # # if x%2==0 and x%3==0:
# # # # #     print("This is divisble by 2 and 3")
# # # # # else:
# # # # #     print("Not divisible by 2 and 3")
# # # # # """
# # # # # #Nested If statements or #Conditional Statements
# # # # # """
# # # # # age = int(input())
# # # # # gender = input()

# # # # # if (gender=="male"):
# # # # #     if (age>=20):
# # # # #         print("he is eligible for License")
# # # # #     else:
# # # # #         print("he is not eligible for License")
# # # # # elif (gender=="female"):
# # # # #     if (age>=18):
# # # # #         print("she is eligible for License")
# # # # #     else:
# # # # #         print("She is Not Eligible")
# # # # # """
# # # # # #loop Statements
# # # # # #ForLoop
# # # # # """for i in range(10,0,-1):
# # # # #     print(i,end=" ")"""
# # # # # """for i in range(0,11):
# # # # #     print(i,end=" ")"""
# # # # # """for i in range(1,11):
# # # # #     print(f"5 * {i} =",5*i)"""

# # # # # #Prime Numbers
# # # # # """
# # # # # n = int(input())
# # # # # count=0
# # # # # for i in range(1,n+1):
# # # # #     if (n%i==0):
# # # # #         count+=1
# # # # # if (count==2):
# # # # #     print("Prime")
# # # # # else:
# # # # #     print("not prime")"""

# # # # # """for i in range(1,100):
# # # # #     n=i
# # # # #     count=0
# # # # #     for j in range(1,n+1):
# # # # #         if (n%j==0):
# # # # #             count+=1
# # # # #     if (count==2):
# # # # #         print(n)"""

# # # # # """for i in range(10,101,10):
# # # # #     print(i,end=" ")"""
# # # # # """
# # # # # for i in range(100,0,-10):
# # # # #     print(i,end=" ")
# # # # #     """
# # # # # """
# # # # # counter=0
# # # # # for i in range(1,15):
# # # # #     n=i
# # # # #     count=0
# # # # #     for j in range(1,n+1):
# # # # #         if (n%j==0):
# # # # #             count+=1
# # # # #     if (count==2):
# # # # #         counter+=1
# # # # # print(counter) """

# # # # # #In 1 to 10 How many even numbers using F string method
# # # # # """counter1=0
# # # # # counter2=0
# # # # # for i in range(1,21):
# # # # #     if (i%2==0):
# # # # #         counter1+=1
# # # # #     else:
# # # # #         counter2+=1
# # # # # print(f"Even numbers= {counter1}")
# # # # # print(f"Odd numbers ={counter2}")"""

# # # # # # While Loop
# # # # # """
# # # # # n = int(input("Enter number:"))
# # # # # while(n<15):
# # # # #     print(n)
# # # # #     n+=1 """

# # # # # #Reverse While Loop
# # # # # """n = int(input())
# # # # # while(n>0):
# # # # #     print(n)
# # # # #     n-=1 """

# # # # # #1 to 10 Even number in While loop
# # # # # """n = 10
# # # # # while(n>0):
# # # # #     if (n%2==0):
# # # # #         print(n ,"even")
# # # # #     else:
# # # # #         print(n,"odd")
# # # # #     n-=1

# # # # # n = 1
# # # # # while(n<=10):
# # # # #     if (n%2==0):
# # # # #         print(n ,"even")
# # # # #     else:
# # # # #         print(n,"odd")
# # # # #     n+=1 """

# # # # # #Strings
# # # # # #Covering concepts (Indexing, Slicing)
# # # # # """
# # # # # Name = "Shanmukh"
# # # # # Name1 = 'Shanmukh'
# # # # # char = 'A'
# # # # # print(Name[0:7:2])
# # # # # print(Name[:5])
# # # # # print(Name[2:])
# # # # # print(Name[::3])
# # # # # print(Name[::-2])"""

# # # # # #Length
# # # # # """
# # # # # Name = "Shanmukh"
# # # # # print(len(Name))
# # # # # n = len(Name)
# # # # # print(n) """

# # # # # #Contactenation of Strings
# # # # # """ Name = "Shanmukha"
# # # # # Name1 = 'Sriram'
# # # # # fullName = Name +" , " +Name1
# # # # # print(fullName)
# # # # # print("Hi"*2) #Repeatation
# # # # # print("Shanmukha" in fullName)
# # # # # print("Sriram" not in fullName)

# # # # # #Upper & Lower ***
# # # # # print(Name.upper())
# # # # # Name = Name.upper()
# # # # # print(Name)
# # # # # print(Name.lower())

# # # # # #Title() ***
# # # # # Text = "We are aware of fraudulent recruitment activities that may involve individuals impersonating Comcast recruiters or employees."
# # # # # print(Text.title())

# # # # # #Captilize()
# # # # # Name2 = "varma"
# # # # # print(Name2.capitalize())

# # # # # #Strip() -- (L strip() & R Strip()) ***
# # # # # print(Text.strip())
# # # # # print(Text.lstrip())

# # # # # #replace()
# # # # # text1 = "My *name *is *Shannu"
# # # # # print(text1.replace("Shannu","Varma"))

# # # # # #split()

# # # # # print(text1.split("*"))
# # # # # x = text1.split("*")
# # # # # print(type(x))

# # # # # text2 = "I love Cricket"
# # # # # print(text2.split(" "))
# # # # # print(Text.split(" "))
# # # # # words = Text.split(" ")
# # # # # print(words)
# # # # # print(words[0:6])

# # # # # #join ()
# # # # # word = ['Ball', 'Bat', 'Cricket']
# # # # # print(",".join(word))
# # # # # Text = "We are aware of fraudulent recruitment activities that may involve individuals impersonating Comcast recruiters or employees."
# # # # # words = Text.split(" ")
# # # # # print(words)
# # # # # print(" ".join(words))

# # # # # #find()
# # # # # name = "shanmukmh"
# # # # # print(name.find("k"))

# # # # # #count()
# # # # # print(name.count("h"))

# # # # # #startswith & endswith
# # # # # print(name.startswith("sh"))
# # # # # print(name.endswith("kh"))

# # # # # #isalpha & isdigit & isaplhanum &isspace
# # # # # print(name.isalpha())
# # # # # print(name.isdigit())
# # # # # print(name.isalnum())
# # # # # print(name.isspace())

# # # # # #islower & isupper
# # # # # print(name.isupper())
# # # # # print(name.islower())

# # # # # #string programs
# # # # # #len of string
# # # # # Age = "22"
# # # # # print(len(Age))

# # # # # #Reverse String
# # # # # Name2 = "Shanmukh"
# # # # # print(Name2[5::-1])"""

# # # # # #Take one word and place some portion as caps and smalls and find how many captial letters
# # # # # """Name3 = "SRiram"
# # # # # count = 0
# # # # # for i in Name3:
# # # # #     if i.isupper():
# # # # #         count+=1
# # # # # print(count)"""

# # # # # """Name3 = "cricket"
# # # # # Owel = "AEIOUaeiou"
# # # # # count = 0
# # # # # for i in Name3:
# # # # #     if i in Owel:
# # # # #         count+=1
# # # # # print(count) 

# # # # # #count the letters in a word      
# # # # # Name3 = "cricket"
# # # # # count = 0
# # # # # for i in Name3:
# # # # #     print(i,Name3.count(i))

# # # # # #aplhabets and number counting
# # # # # count1=0
# # # # # count2=0
# # # # # str = "Var*ma123"
# # # # # for i in str:
# # # # #     if i.isalpha():
# # # # #         count1+=1
# # # # #     elif i.isdigit():
# # # # #         count2+=1
# # # # #     else:
# # # # #         continue
# # # # # print(count1,count2)

# # # # # #break, Continue, Pass
# # # # # for i in range(1,11):
# # # # #     pass
# # # # # for i in range(1,11):
# # # # #     print(i)
# # # # #     if i ==5:
# # # # #         break
# # # # # for i in range(1,11):
# # # # #     if i==7:
# # # # #         continue
# # # # #     print(i)

# # # # # #switch statement
# # # # # day = "monday"
# # # # # match day:
# # # # #     case "tuesday":
# # # # #         print("It is tuesday")
# # # # #     case "wednesday":
# # # # #         print("it is wednesday")
# # # # #     case "monday":
# # # # #         print("it is saturday")"""

# # # # # #List
# # # # # #A list is built-in python data type used to store mulitple items in a single variable
# # # # # #Characterstics of Lists : 1. It is mutable, 2. Allows duplicate items, 3. can store different data types
# # # # # names = ["Java", "Python","C++", "C", "SQL",1,6.7]
# # # # # print(names)
# # # # # print(type(names))
# # # # # #Indexing
# # # # # print(names[1])
# # # # # #slicing
# # # # # print(names[0:4])
# # # # # #Update
# # # # # names[0] = "JavaScript"
# # # # # print(names)
# # # # # #append
# # # # # names.append("DynamoDB")
# # # # # print(names)
# # # # # #extend
# # # # # names.extend(["MongoDB", "C#"])
# # # # # print(names)
# # # # # #insert
# # # # # """
# # # # # names.insert(5,8000)
# # # # # print(names)
# # # # # #Remove
# # # # # names.remove("C#")
# # # # # print(names)
# # # # # #pop
# # # # # names.pop()
# # # # # print(names)
# # # # # #clear
# # # # # #names.clear()
# # # # # #index
# # # # # print(names.index(True))
# # # # # #count()
# # # # # print(names.count("C"))
# # # # # """
# # # # # #sort
# # # # # names.sort()
# # # # # print(names)
# # # # # #reverse()
# # # # # names.reverse()
# # # # # print(names)
# # # # # #len()
# # # # # print(len(names))
# # # # # #Max
# # # # # print(max(names))
# # # # # #sum()
# # # # # l=[1,2,3,4,8,9]
# # # # # print(sum(l))

# # # # # print(names,end =" ")
# # # # # for i in names:
# # # # #     print(i)


# # # # # tup=(9,0,8,"hi","hi")
# # # # # print(tup)

# # # # name="varma"
# # # # x=set()   #step 1 ->v  answer=v ; x={v}    step 2-> answer=va ; x={v,a}   step 3 answer=var; x={v,a,r}.....
# # # # answer=""
# # # # for i in name:

# # # #     x.add(i)
# # # # print(x)


# # # name = input("Enter name: ")

# # # result = ""
# # # seen = set()

# # # for char in name :
# # #    if char not in seen:
# # #         result += char
# # #         seen.add(char)

# # # print("remove dupicates:", result)

# # 
# # print my name 5 times
# # name = (input())

# # for i in range(0,6):
# #     print(name)

# """

# for i in range(1,11):
#     print(f"5 * {i} = {5*i}")


# answer = 0
# for i in range(1,101):
#     answer +=i

# print(answer)

# result = 0
# while result<=20:
#     print(result)
#     result+=1


# for i in range(1,11):
#     print(f"{i}**2 = {i*i}")


# for i in range(5,0,-1):
#     print(i)

# print("Start")


# number = int(input())

# while number !=0:
#     print(f"You are enter {number} please try again")
#     number = int(input())
# print("You have entered Zero")
# print("Thank you")
# """

# # password = "934518"
# # count = 0
# # blocked= False
# # user = input("Enter the password:")

# # while password!=user:
# #     if count>=3:
# #         print("You execeeded maximum limit")
# #         blocked = True
# #         break
# #     count+=1
# #     user = input("Enter the password:")

# # if blocked:
# #     print("You are blocked")
# # else:
# #     print("You login successufully")


# # number = int(input())

# # while number !=0:
# #     print(f"You are enter {number} please try again")
# #     number = int(input())
# # print("You have entered Zero")
# # print("Thank you")

# # Factorial program
# # number = int(input())
# # answer = 1

# # for i in range(number,0,-1):
# #     answer*=i

# # print(answer)

# # Count digits in an integer without converting into string
# # number = int(input())
# # count = 0
# # while number!=0:
# #     number=int(number/10)
# #     count +=1

# # print(count)

# #Reverse a number using loop
# # number = int(input())
# # answer = 0
# # while number:
# #   answer = (answer*10)+(number%10)  # Formuala 
# #   number = int((number/10))
# # print(answer)

# # Sum of digits using loop

# # number = 5832
# # answer = 0
# # while number:
# #   answer = answer+ (number%10)
# #   number = int(number/10)

# # print(answer)

# # Count the vowels in a string using a loop.
# # word  = input()
# # vowels = "aeiouAEIOU"
# # count = 0
# # for i in word:
# #   if i in vowels:
# #     count+=1
# # print(count)


# # fibanocci series program upto 10 number

# # a,b = 0,1
# # for i in range(10):
# #    print(a, end = " ")
# #    a,b = b, a+b

# # # Dictonary
# # details = {"name": "Varma", "age": "22", "Gender": "Male"}
# # for key,val in details.items():
# #    print(key,val)

# #Print each character of a string on a seperate line
# # name = input()

# # for i in name:
# #     print(i)

# #Count the number of characters without using len()
# # name = input()
# # count = 0
# # for i in name:
# #     count+=1
# # print(count)


# # word  = input()
# # vowels = "aeiouAEIOU"
# # count = 0
# # for i in word:
# #   if i in vowels:
# #     count+=1
# # print(count)

# # Number of Consonants in a string
# # name = input()
# # vowels = "aeiouAEIOU"
# # count = 0
# # for i in name:
# #     if i not in vowels:
# #         count +=1
# # print(count)

# #Print a string in reverse using loop
# # word = input()
# # print(word[::-1]) #Normal reverse string
# name = input()
# length = len(name)-1
# reverse = ""
# for i in range(length,-1,-1):
#     reverse += name[i]

# print(reverse)

# #convert all lowercase letters to uppercase without using upper()

# We use 'chr' for converting ASCII number to Letter and 'Ord' for converting letter to ASCII
# ASCII = ord('b') - ord('a')
# print(ASCII)


# #convert all lowercase letters to uppercase without using upper()
# name = input()
# answer = ""
# for i in name:
#     if i.isupper() == False:
#         ascii_num = ord(i) - ord('a')
#         con_num = ord('A') + ascii_num
#         result = chr(con_num)
#         answer += result
#     else:
#         answer +=i
# print(answer)

# Count how many spaces are present in a string
name1 = "Count how many spaces are present in a string"
count = 0
for i in name1:
    if i == " ":
        count += 1
print(count)

# Check whether a string is a palindrome
name = input()
length = len(name)-1
reverse = ""
for i in range(length,-1,-1):
    reverse += name[i]
if reverse == name:
    print("It is a palindrome")
else:
    print("not a palindrome")