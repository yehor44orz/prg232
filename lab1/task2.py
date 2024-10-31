str = input("Enter a string: ")

# example = "  hello WORLD  "

def test(str):
    print(example.strip())        # Output: "hello WORLD"
    print(example.capitalize())   # Output: "  hello world  "
    print(example.title())        # Output: "  Hello World  "
    print(example.upper())        # Output: "  HELLO WORLD  "
    print(example.lower())        # Output: "  hello world  "

test(str)
