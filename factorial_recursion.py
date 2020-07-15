def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1) #재귀함수

n=int(input('n='))

print('{}!={}'.format(n,factorial(n)))