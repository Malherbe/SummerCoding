from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            print(i ,"before")

        if next in ")]}":
            # Process closing bracket, write your code here
            top = opening_brackets_stack[-1]
            
            if next == ')' and top == '(' or \
            next == ']' and top == '[' or \
            next == '}' and top == '{':
            
                opening_brackets_stack.pop()
                #print(text[i], "after")
                pass
     
    # if not opening_brackets_stack:
    #     print(next,"contains valid parentheses.")
    # else:
    #     print(next, index,"contains invalid parentheses.")

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    # print(mismatch)

if __name__ == "__main__":
    main()

