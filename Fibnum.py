#define fibonacci series

def fib(n):
    if n <= 2:
        return 1
    #starting with zero and one
    fn = 0
    sn=1
    print (fn)
    for i in range(1, n):
        #every number is the sum of the two preceding ones
        #0, 0+1=1, 1+1=2, 1+2=3, 2+3=5, 3+5=8, 5+8=13, 8+13=21, 13+21=34, 21+34=55, 34+55=89, 55+89=144, 89+144=233, 144+233=377, 233+377=610
        current = fn + sn
        fn = sn
        sn = current
        print (current)
    return "done"

# Prompt the user for input
n = int(input("Enter the number of iterations: "))

#0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610
print (fib(n))