import matplotlib.pyplot as plt

def withTwoPoint(pointA,pointB):
    vectorAB = [pointB[0] - pointA[0], pointB[1] - pointA[1]]
    cartesianEquation = calculateCartesianEquation(vectorAB, pointA)
    reducedEquation = calculateReducedEquation(cartesianEquation)
    guidingVector = [-cartesianEquation[2], cartesianEquation[0]]
    return (pointA, guidingVector, cartesianEquation, reducedEquation)

def withCartesianEquation(cartesianEquation):
    guidingVector = [-cartesianEquation[2], cartesianEquation[0]]
    reducedEquation = calculateReducedEquation(cartesianEquation)
    pointA = [2, reducedEquation[0]*2 + reducedEquation[2]]
    return(pointA, guidingVector, cartesianEquation, reducedEquation)

def withReducedEquation(reducedEquation):
    if reducedEquation[0] != 0:
        pointA = [2, reducedEquation[0]*2 + reducedEquation[2]]
        pointB = [4, reducedEquation[0]*4 + reducedEquation[2]]
    else:
        pointA = [2, reducedEquation[2]]
        pointB = [4, reducedEquation[2]]
    vectorAB = [pointB[0] - pointA[0], pointB[1] - pointA[1]]
    cartesianEquation = calculateCartesianEquation(vectorAB, pointA)
    guidingVector = [-cartesianEquation[2], cartesianEquation[0]]
    return (pointA, guidingVector, cartesianEquation, reducedEquation)

def withOnePointOneVector(pointC, vectorAB):
    cartesianEquation = calculateCartesianEquation(vectorAB, pointC)
    reducedEquation = calculateReducedEquation(cartesianEquation)
    guidingVector = [-cartesianEquation[2], cartesianEquation[0]]
    return (pointC, guidingVector, cartesianEquation, reducedEquation)



def calculateCartesianEquation(vectorAB, pointA):
    cartesianEquation = ["a","x","b","y","c"]
    cartesianEquation[0] = -vectorAB[1]
    cartesianEquation[2] = vectorAB[0]
    cartesianEquation[4] =  vectorAB[0]*(-pointA[1]) - vectorAB[1]*(-pointA[0])
    return cartesianEquation

def calculateReducedEquation(cartesianEquation):
    reducedEquation = ["m","x","p"]
    reducedEquation[0] = (-cartesianEquation[0])/ cartesianEquation[2]
    reducedEquation[2] = (-cartesianEquation[4])/ cartesianEquation[2]
    return reducedEquation


def message(pointA, guidingVector, cartesianEquation, reducedEquation):
    print()
    print()
    print("Fiche technique de la droite :")
    if cartesianEquation[2] <  0:
        if cartesianEquation[4] < 0:
            print("Equation cartésienne : " + str(cartesianEquation[0]) + str(cartesianEquation[1]) + " " + str(cartesianEquation[2]) + str(cartesianEquation[3]) + " " + str(cartesianEquation[4]))
        else:
            print("Equation cartésienne : " + str(cartesianEquation[0]) + str(cartesianEquation[1]) + " " + str(cartesianEquation[2]) + str(cartesianEquation[3]) + " + " + str(cartesianEquation[4]))
    else:
        if cartesianEquation[4] < 0:
            print("Equation cartésienne : " + str(cartesianEquation[0]) + str(cartesianEquation[1]) + " + " + str(cartesianEquation[2]) + str(cartesianEquation[3]) + " " + str(cartesianEquation[4]))
        else:
            print("Equation cartésienne : " + str(cartesianEquation[0]) + str(cartesianEquation[1]) + " + " + str(cartesianEquation[2]) + str(cartesianEquation[3]) + " + " + str(cartesianEquation[4]))
    if reducedEquation[2] < 0:
        print("Equation réduite : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " " + str(reducedEquation[2]))
    else:
        print("Equation réduite : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " + " + str(reducedEquation[2]))
    print("Vecteur directeur : u(" + str(guidingVector[0]) + ";" + str(guidingVector[1]) + ")" )
    print("Un point de la droite : A(" + str(pointA[0]) + ";" + str(pointA[1]) + ")")


plt.title("Droite")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

index = 0
while index == 0:
    print("Choissisez la méthode :")
    print("[1] - 2 points d'une même droite")
    print("[2] - 1 point et un vecteur directeur d'une même droite")
    print("[3] - 1 équation cartésienne")
    print("[4] - 1 équation réduite")
    print("Entrez le numéro de l'étape choisie :")
    methode = int(input(">>>"))

    if (methode == 1):

        print()
        pointA = input("Point A (x;y) : ").replace("(" , "").replace(")", "").replace("A", "").replace(",", ".").split(";")
        pointB = input("Point B (x;y) : ").replace("(" , "").replace(")", "").replace("B", "").replace(",", ".").split(";")
        try:
            for i in range(2):
                pointA[i] = int(pointA[i])
                pointB[i] = int(pointB[i])
        except ValueError:
             for i in range(2):
                pointA[i] = float(pointA[i])
                pointB[i] = float(pointB[i])

        pointA, guidingVector, cartesianEquation, reducedEquation = withTwoPoint(pointA, pointB)

        message(pointA, guidingVector, cartesianEquation, reducedEquation)

        pointB = [-2000, reducedEquation[0]*(-2000) + reducedEquation[2]]
        pointC = [2000, reducedEquation[0]*2000 + reducedEquation[2]]
        if reducedEquation[2] < 0:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " " + str(reducedEquation[2])))
        else:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " + " + str(reducedEquation[2])))
        plt.axis([0, 100, 0, 100])
        plt.legend()
        plt.show()

        index += 1
    elif (methode == 2):

        print()
        pointA = input("Point A (x;y) : ").replace("(" , "").replace(")", "").replace("A", "").replace(",", ".").split(";")
        vectorAB = input("Vecteur u (x;y) : ").replace("(" , "").replace(")", "").replace("u", "").replace(",", ".").split(";")
        try:
            for i in range(2):
                pointA[i] = int(pointA[i])
                vectorAB[i] = int(vectorAB[i])
        except:
            for i in range(2):
                pointA[i] = float(pointA[i])
                vectorAB[i] = float(vectorAB[i])

        pointA, guidingVector, cartesianEquation, reducedEquation = withOnePointOneVector(pointA, vectorAB)

        message(pointA, guidingVector, cartesianEquation, reducedEquation)

        pointB = [-2000, reducedEquation[0]*(-2000) + reducedEquation[2]]
        pointC = [2000, reducedEquation[0]*2000 + reducedEquation[2]]
        if reducedEquation[2] < 0:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " " + str(reducedEquation[2])))
        else:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " + " + str(reducedEquation[2])))
        plt.axis([0, 100, 0, 100])
        plt.legend()
        plt.show()

        index += 1
    elif (methode == 3):

        print()
        a = input("Valeur de a : ").replace(",", ".")
        b = input("Valeur de b : ").replace(",", ".")
        c = input("Valeur de c : ").replace(",", ".")
        try:
            cartesianEquation = [int(a), "x", int(b), "y", int(c)]
        except ValueError:
            cartesianEquation = [float(a), "x", float(b), "y", float(c)]

        pointA, guidingVector, cartesianEquation, reducedEquation = withCartesianEquation(cartesianEquation)

        message(pointA, guidingVector, cartesianEquation, reducedEquation)

        pointB = [-2000, reducedEquation[0]*(-2000) + reducedEquation[2]]
        pointC = [2000, reducedEquation[0]*2000 + reducedEquation[2]]
        if reducedEquation[2] < 0:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " " + str(reducedEquation[2])))
        else:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " + " + str(reducedEquation[2])))
        plt.axis([0, 100, 0, 100])
        plt.legend()
        plt.show()

        index += 1
    elif (methode == 4):

        print()
        m = input("Valeur de m : ").replace(",", ".")
        p = input("Valeur de p : ").replace(",", ".")

        try :
            reducedEquation = [int(m), "x", int(p)]
        except ValueError:
            reducedEquation = [float(m), "x", float(p)]
        
        pointA, guidingVector, cartesianEquation, reducedEquation = withReducedEquation(reducedEquation)

        message(pointA, guidingVector, cartesianEquation, reducedEquation)

        pointB = [-2000, reducedEquation[0]*(-2000) + reducedEquation[2]]
        pointC = [2000, reducedEquation[0]*2000 + reducedEquation[2]]
        if reducedEquation[2] < 0:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " " + str(reducedEquation[2])))
        else:
            plt.plot([pointA[0], pointB[0], pointC[0]], [pointA[1], pointB[1], pointC[1]], label = ("Equation : " + str(reducedEquation[0]) + str(reducedEquation[1]) + " + " + str(reducedEquation[2])))
        plt.axis([0, 100, 0, 100])
        plt.legend()
        plt.show()

        index += 1
    else:
        print()
        print("Saisie Incorect")
        print()