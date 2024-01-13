#reverse a string

#using loops

print("Enter the String you want to reverse -")
s = str(input())

def reverse(s):
  str = ""
  for i in s:
      str = i + str
  return str

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

#using recursion

#if not equal to 0, the function is recursively called to cut the parts of string except the first character 
#first character will be concatenated to the end

print("Enter the string you want to reverse -")
s = str(input())

def reverse(s):
  if len(s) == 0:
     return s 
  else:
     return reverse(s[1:]) + s[0]
    
print("The orignal string is : ",end="")
print(s)

print("The reversed string is : ",end="")
print(reverse(s))
    
    