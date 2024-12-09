def is_correct_bracket_sequence(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if len(stack) == 0:
                return False
            top = stack.pop()
            if (
                (top == "(" and char != ")")
                or (top == "[" and char != "]")
                or (top == "{" and char != "}")
            ):
                return False
    return len(stack) == 0


s = input()
print("yes" if is_correct_bracket_sequence(s) else "no")
