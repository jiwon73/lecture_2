def div(a,b=2):
    return a/b

print('div(4)=',div(4))
print('div(6,3)=', div(6,3))

#위치인자와 키워드인자 혼용
print('div(a=200,b=5)=', div(a=200,b=5))
print('div(b=5,a=200)=', div(b=5,a=200))
#a/b로 계산됨, 키워드인자는 위치 바뀌어도 상관없음

#print('div(b=5,a=200)=', div(b=5,200))
#SyntaxError: positional argument follows keyword argument
#항상 위치인자 먼저 자리 정해주고, 키워드인자 자리 정하기