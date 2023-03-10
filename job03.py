n = int(input("entrez un nombre entier"))
x= 2
def multi(x,n):
    if n == 0:

        return 1
    else :
        result = x * multi(x,n-1)
        print(result)
        return result


multi(2,n)