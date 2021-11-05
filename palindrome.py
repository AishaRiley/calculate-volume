s = input("Enter a string:")  ##abcdef

print(s[:])
print(s[0:5])
print(s[0:5:1])
print(s[::])


revstr=(s[::-1])

if revstr==s:
    print("Palindrome")
else:
    print("Not Palindrome")
