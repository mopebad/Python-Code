# Global Scope

n = 10

my_str = "H"


def main():
    # Function Scope
    n = 5
    print(my_str)
    print(f"This is my number: {n}")
    local_str = "P"
    global another_str
    another_str = "E"


main()
print(n)

'''
Everything can see what is in the global scope, including from within the function.
However, we cannot see inside the function unless we are within the function.
'''
