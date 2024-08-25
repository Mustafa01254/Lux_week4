string = input("Enter a string to check if it is a palindrome: ")
length = len(string)
stack1 = []
stack2 = []

for n in range((length+1) // 2, length ):
    stack1.append(string[length - n - 1])
    stack2.append(string[n])
print(stack1)
print(stack2)
if (stack2 != stack1):
    print("It is not a palindrome")
else: print("It is a palindrome")    

 
