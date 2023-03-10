str_1 = input("entrez un mot ")
str_2 = input("entrez un autre mot ")
stars = 0


def replace(x, stars):

    if len(str_2) > len(str_1):
        return print("mot non remplaçable")

    if str_2[x] == "*" and stars == 0:
        stars += 1
    elif str_1[x] == str_2[x] and stars != 0:
        stars -= 1

    if x == len(str_2)-1:
        if len(str_1) == len(str_2) and stars == 0:
            print("mot ok")
            return 1
        elif str_2[x] == "*":
            return print("fin du mot remplacé par une étoile")
        else:
            return print("mot erroné")
    else:
      #  print("x :", x)
        return replace(x+1, stars)

replace(0, stars)