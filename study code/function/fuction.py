def apply(x):
    return x * 10

def twice(a, x):
    return a(a(x))

def main():
    print(twice(apply, 10))

main()