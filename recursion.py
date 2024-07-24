#recursion
'''
function re-using itself
to reduce the number of steps
big problem can be split into small parts
advantages:
->program execution is faster
->memory is not wasted
->reduce lines of codes
>works based on same set of sequence
>works on base condition.
>break cannot be used in recursion
>
'''
#factorial
m=5
fact=1
for i in range(1,m+1):
    fact=fact*i
print(fact)

#using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))

#n=10 sum of natural numbers
def sumOfNatural(n):
    if n==1:
        return 1
    else:
        return n+sumOfNatural(n-1)
n=int(input())
print(sumOfNatural(n))

#fib series 8:0 1 1 2 3 5 8 13 21
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
##sum of digit till it becomes a single digit
