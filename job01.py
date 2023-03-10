nbr = int(input("entrez un nombre entier"))

def factorielle(arg):
    if arg == 1:
        return 1
    else :
        print(arg * factorielle(arg -1))
        return arg * factorielle(arg - 1)

factorielle(nbr)