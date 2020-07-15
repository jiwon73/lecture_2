def print_star(n=1):
    for _ in range(n):
        print("*****************")

print('위치인자로 3을 넣었을때')
print_star(3)
print('키워드인자로 4을 넣었을때')
print_star(n=4)
