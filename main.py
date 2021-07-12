filas = {
    1: {"a": 5, "b": 3, "c": 7, "d": 0, "e": 7, "f": 0, "g": 0, "h": 0, "i": 0},
    2: {"a": 6, "b": 0, "c": 0, "d": 1, "e": 9, "f": 5, "g": 0, "h": 0, "i": 0},
    3: {"a": 0, "b": 9, "c": 8, "d": 0, "e": 0, "f": 0, "g": 0, "h": 6, "i": 0},
    4: {"a": 8, "b": 6, "c": 0, "d": 0, "e": 6, "f": 0, "g": 0, "h": 0, "i": 3},
    5: {"a": 4, "b": 0, "c": 0, "d": 8, "e": 0, "f": 3, "g": 0, "h": 0, "i": 1},
    6: {"a": 7, "b": 0, "c": 0, "d": 0, "e": 2, "f": 0, "g": 0, "h": 0, "i": 6},
    7: {"a": 0, "b": 6, "c": 0, "d": 0, "e": 0, "f": 0, "g": 2, "h": 8,  "i": 0},
    8: {"a": 0, "b": 0, "c": 7, "d": 4, "e": 1, "f": 9, "g": 0, "h": 4, "i": 5},
    9: {"a": 0, "b": 6, "c": 0, "d": 0, "e": 8, "f": 0, "g": 0, "h": 7, "i": 9}
}
soluciones=filas
comparacion=[]
#ingresar permite el ingreso de datos en el sudoku.
def ingresar():
    resp = "a"
    while resp != "x" and resp != "X":
        d1 = 0
        d2 = "p"
        d1 = int(input("Ingrese la columna del numero: "))
        d2 = input("Ingrese la fila del número: ")
        filas[d1][d2] = int(input("Ingrese el número: "))
        resp = input ("Si desea terminar presione x, sino cualquier tecla: ")
        print(resp)
#mostrar muestra el sudoku cómo está
def mostrar ():
    for i in filas:
        if (i - 1) % 3 == 0:
            print("_____________________________________")
        a = 1
        print("|  ", end="")
        for j in "abcdefghi":
            if filas[i][j] == 0:
                print("x", end="  ")
            else:
                print(filas[i][j], end="  ")
            if a % 3 == 0:
                print(end="|  ")
            a += 1
        print()
    print("_____________________________________")
#lista convierte las variables vacías en listas con [0]

def lista():
    for i in filas:
        for j in "abcdefghi":
            if filas [i][j] == 0:
                filas [i][j] = [0]
#limpiar borra las listas - NO SE USA
def limpiar():
    for i in filas:
        for j in "abcdefghi":
            if isinstance(filas[i][j], list) == True:
                filas[i][j] = 0#est#Esta no se usa
#posible mete en listas todos los números posibles para una celda en base a su cuadrado, fila y columna.
#si hay solo un número posible convierte la variable en int con ese número
def resolver():
    def posible(y,z):
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        n5 = 0
        n6 = 0
        n7 = 0
        n8 = 0
        n9 = 0
        if isinstance(filas[y][z], list) == True:
            guardar=filas[y][z]
            filas[y][z]=[]
            for k in filas:
                if filas[k][z] == 1:
                    n1 = 1
                if filas[k][z] == 2:
                    n2 = 2
                if filas[k][z] == 3:
                    n3 = 3
                if filas[k][z] == 4:
                    n4 = 4
                if filas[k][z] == 5:
                    n5 = 5
                if filas[k][z] == 6:
                    n6 = 6
                if filas[k][z] == 7:
                    n7 = 7
                if filas[k][z] == 8:
                    n8 = 8
                if filas[k][z] == 9:
                    n9 = 9

            for l in "abcdefghi":
                if filas[y][l] == 1:
                    n1 = 1
                if filas[y][l] == 2:
                    n2 = 2
                if filas[y][l] == 3:
                    n3 = 3
                if filas[y][l] == 4:
                    n4 = 4
                if filas[y][l] == 5:
                    n5 = 5
                if filas[y][l] == 6:
                    n6 = 6
                if filas[y][l] == 7:
                    n7 = 7
                if filas[y][l] == 8:
                    n8 = 8
                if filas[y][l] == 9:
                    n9 = 9
            if y <4:
                if z=="a" or z== "b" or z == "c":
                    for k in (1,2,3):
                        for l in ("abc"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
                if z=="d" or z=="e" or z=="f":
                    for k in (1, 2, 3):
                        for l in ("def"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
                if z=="g" or z=="h" or z=="i":
                    for k in (1,2,3):
                        for l in ("ghi"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9

            if 4 <= y <= 6:
                if z=="a" or z== "b" or z == "c":
                    for k in (4,5,6):
                        for l in ("abc"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
                if z=="d" or z=="e" or z=="f":
                    for k in (4,5,6):
                        for l in ("def"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
                if z=="g" or z=="h" or z=="i":
                    for k in (4,5,6):
                        for l in ("ghi"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
            if 7 <= y:
                if z == "a" or z == "b" or z == "c":
                    for k in (7,8,9):
                        for l in ("abc"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
                if z == "d" or z == "e" or z == "f":
                    for k in (7,8,9):
                        for l in ("def"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
                if z == "g" or z == "h" or z == "i":
                    for k in (7,8,9):
                        for l in ("ghi"):
                            if filas[k][l] == 1:
                                n1 = 1
                            if filas[k][l] == 2:
                                n2 = 2
                            if filas[k][l] == 3:
                                n3 = 3
                            if filas[k][l] == 4:
                                n4 = 4
                            if filas[k][l] == 5:
                                n5 = 5
                            if filas[k][l] == 6:
                                n6 = 6
                            if filas[k][l] == 7:
                                n7 = 7
                            if filas[k][l] == 8:
                                n8 = 8
                            if filas[k][l] == 9:
                                n9 = 9
            if n1 == 0:
                    filas[y][z].append(1)
            if n2 == 0:
                    filas[y][z].append(2)
            if n3 == 0:
                    filas[y][z].append(3)
            if n4 == 0:
                    filas[y][z].append(4)
            if n5 == 0:
                    filas[y][z].append(5)
            if n6 == 0:
                    filas[y][z].append(6)
            if n7 == 0:
                    filas[y][z].append(7)
            if n8 == 0:
                    filas[y][z].append(8)
            if n9 == 0:
                    filas[y][z].append(9)
            if len(filas[y][z]) == 0:
                filas[y][z] = guardar
            if len(filas[y][z]) == 1:
                filas[y][z] = filas[y][z][0]
    #comparar2 compara la lista xy con los elementos de todas las de su fila, columna y cuadrado.
    def comparar3 (lista1,lista2):
        comparacion3=[]
        if isinstance(lista1, list) and isinstance(lista2, list):
            for i in lista1:
                if i not in lista2:
                    comparacion3.append(i)
            if len(comparacion3) == 1:
                    lista1 = comparacion3[0]
                    int(lista1)
        return lista1
    def comparar2(x,y):
        comparacion = []
        if isinstance(filas[x][y], list):
            for k in filas:
                if k != x:
                    if isinstance(filas[k][y], list):
                        comparacion += filas[k][y]
                    else:
                        comparacion.append(filas[k][y])

        filas[x][y] = comparar3(filas[x][y], comparacion)
        comparacion = []

        if isinstance(filas[x][y], list):
            for j in "abcdefghi":
                if j != y:
                    if isinstance(filas[x][j], list):
                        comparacion += filas[x][j]
                    else:
                        comparacion.append(filas[x][j])
        filas[x][y] = comparar3(filas[x][y], comparacion)
        comparacion = []

        if isinstance(filas[x][y], list):
            if x < 4:
                if y == "a" or y == "b" or y == "c":
                    for k in (1, 2, 3):
                        for j in ("abc"):
                            if (k!= x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []
                if y == "d" or y == "e" or y == "f":
                    for k in (1, 2, 3):
                        for j in ("def"):
                            if (k != x or j != y):
                                if (isinstance(filas[k][j], list) == True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []

                if y == "g" or y == "h" or y == "i":
                    for k in (1, 2, 3):
                        for j in ("ghi"):
                            if (k!= x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []

            if 4 <= x <7:
                if y == "a" or y == "b" or y == "c":
                    for k in (4, 5, 6):
                        for j in ("abc"):
                            if (k != x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []
                if y == "d" or y == "e" or y == "f":
                    for k in (4, 5, 6):
                        for j in ("def"):
                            if (k != x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []

                if y == "g" or y == "h" or y == "i":
                    for k in (4, 5, 6):
                        for j in ("ghi"):
                            if (k != x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []

            if 4 <= x < 7:
                if y == "a" or y == "b" or y == "c":
                    for k in (7, 8, 9):
                        for j in ("abc"):
                            if (k != x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []

                if y == "d" or y == "e" or y == "f":
                    for k in (7, 8, 9):
                        for j in ("def"):
                            if (k != x or j != y) and (isinstance(filas[k][j], list) == True):
                                comparacion = comparacion + filas[k][j]
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []
                if y == "g" or y == "h" or y == "i":
                    for k in (7, 8, 9):
                        for j in ("ghi"):
                            if (k != x or j != y):
                                if (isinstance(filas[k][j],list)==True):
                                    comparacion = comparacion + filas[k][j]
                                else:
                                    comparacion.append(filas[k][j])
                filas[x][y] = comparar3(filas[x][y], comparacion)
                comparacion = []

    lista()
    for f in filas:
        for g in ("abdcefghi"):
            posible(f, g)
    for f in filas:
        for g in ("abcdefghi"):
            comparar2(f, g)
            for h in filas:
                for i in "abcdefghi":
                    posible (h, i)
    for i in range(2):
        for f in filas:
            for g in "abdcefghi":
                posible(f, g)

def comprobar(x,y):
    if isinstance (lista [x][y],list):
        comprobador=lista[x][y]
    if lista[x][y]==0:
        print ("El sudoku no tiene soluciones posibles")


#ingresar()
print("El sudoku ingresado es:")
mostrar()
lista ()
resolver()


mostrar()



