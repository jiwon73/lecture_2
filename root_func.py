def get_root(a,b,c):
    r1 = (-b +(b**2-4*a*c)**(1/2))/(2*a)
    r2= (-b -(b**2-4*a*c)**(1/2))/(2*a)
    return r1, r2 #return [r1,r2] 이면 대가로로 리턴

root= get_root(1,5,6)
print(root) #여러개 값을 리터할 때 (-2,-3)으로 리턴, 소가로가 디폴트

#root1, root2=get_root(1,5,6)
#print('해는 ',root1,' 또는 ',root2)