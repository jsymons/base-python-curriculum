def create_stack():
    return []


def push(stack, element):
    stack.insert(0, element)


def pop(stack):
    if not stack:
        return None

    return stack.pop(0)
