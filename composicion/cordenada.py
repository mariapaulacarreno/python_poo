class coordenada:
    # Metodo constructor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Metodo de acceso 
    def getX(self):
        return self.__x

    def setX(self, X):
        self.__x = X

    def getY(self):
        return self.__y

    def setY(self, Y):
        self.__y = Y

    def mostrarcoordenada(self):
        print("(", self.__x, ",", self.__y, ")")