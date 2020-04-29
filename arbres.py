class ArbreBinaire:
    valNode = 0
    leftNode = None
    rightNode = None

    #Constructeur
    def __init__(self):

    def getValNode(self):
        return self.valNode

    def setValNode(self, x):
        self.valNode = x

    def getLeftNode(self):
        return self.leftNode

    def setLeftNode(self, x):
        self.leftNode = x

    def getRightNode(self):
        return self.rightNode

    def setRightNode(self, x):
        self.rightNode = x

    def str(self):
        print("Noeud = ",self.valNode)
        print("Sous-noeud gauche = ", self.leftNode)
        print("Sous-noeud droit = ", self.rightNode)

a1 = ArbreBinaire()

a1.str()

