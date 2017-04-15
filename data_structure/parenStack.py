def match(p):
    stack = []
    for i in p:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            p = stack.pop()
    if len(stack) != 0:
        return False
    return True

if __name__ == "__main__":
    string = "(((((())))))"
    print(match(string))