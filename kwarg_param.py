def kwarg_param(**kwargs):
    print('인자의 개수: ', len(kwargs)) 
    print('인자들:', kwargs)
    print('key값은',kwargs.keys())
    print('key값은',kwargs.values())

kwarg_param(first='a',second='b',third='c')
