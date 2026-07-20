n = 100

def print_local_variable(num: int) -> int:
    print(num)
    return num


num = print_local_variable(n)


print(num)
