str = input("Enter a string: ")

# example = "  hello WORLD  "

def test(str):
    print(str.strip())        # Output: "hello WORLD"
    print(str.capitalize())   # Output: "  hello world  "
    print(str.title())        # Output: "  Hello World  "
    print(str.upper())        # Output: "  HELLO WORLD  "
    print(str.lower())        # Output: "  hello world  "

test(str)
