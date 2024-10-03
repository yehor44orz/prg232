str = input("Enter a string: ")

reversed_str2 = str[::-1]
print(reversed_str2)

def reverse_string(s):
    reversed = ""
    for char in s:
        reversed = char + reversed
    return reversed

reversed_str3 = reverse_string(str);
print(reversed_str3)
