
str="MangeshBhosale.83082259494"
str1="kapileshweri"
str3="Mangesh"

print(str[2])

print(str[0:7])  # if you want string in pyhton

print(str+str1)  #this is a concatenation operation

print(str3 in str)  # to check substring is present or not


var=str.split(".") # split function is used to split the string based on given parameter
print(var)

str4="   Mangesh Bhosale    "
print(str4.strip())  # strip function is used to remove unwanted spaces from starting and ending
print(str4.lstrip()) # lstrip function is used to remove unwanted spaces from starting
print(str4.rstrip() )  #rstrip function is used to removes unwant spaces from ending