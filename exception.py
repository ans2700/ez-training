'''
bug->any functionality which is not running as expected
error->syntax error,code mistake
exception->if not handled will cause error
>keywords:try,except,else,finally
'''
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print("divide by zero id not possible")
    n1=100
    n2=200
    print(n1+n2)
    a1=1000
    a2=2000
    print(a1+a2)
##
try:
    arr=[1,7,8,12,36]
    print(arr[8])
except Indexerror:
    print('cannot access index value')
else:
    print('no exception occured')
finally:
    print('finally wednesday is a last day of the week')
