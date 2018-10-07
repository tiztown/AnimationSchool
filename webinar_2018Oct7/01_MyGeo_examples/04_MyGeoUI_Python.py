import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

def MyGeo(geo):
    
    if geo == "cube":
        cmds.polyCube(w=10, h=3, d=3, sx=10, sy=2, sz=2, ch=1)
    elif geo == "sphere":
        cmds.polySphere(r=1, sx=20, sy=20, ch=1)
    elif geo == "torus":
        cmds.polyTorus(r=1, sr=0.5, tw=0, sx=20, sy=20, ch=1)


class MyGeoWnd(QtWidgets.QDialog):
    def __init__(self):
        super(MyGeoWnd, self).__init__()
        
        self.setWindowTitle("MyGeo")
        self.setFixedSize(300,50)
        
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        
        self.buttonSphere = QtWidgets.QPushButton("Sphere")
        self.buttonCube = QtWidgets.QPushButton("Cube")
        self.buttonTorus = QtWidgets.QPushButton("Torus")
        
        self.buttonSphere.clicked.connect(self.createSphere)
        self.buttonCube.clicked.connect(self.createCube)
        self.buttonTorus.clicked.connect(self.createTorus)
        
        self.buttonsLayout.addWidget(self.buttonSphere)
        self.buttonsLayout.addWidget(self.buttonCube)
        self.buttonsLayout.addWidget(self.buttonTorus)
  
        self.setLayout(self.buttonsLayout)
        
    def createSphere(self):
        MyGeo("sphere")
        
    def createCube(self):
        MyGeo("cube")
        
    def createTorus(self):
        MyGeo("torus")
        

myWnd = MyGeoWnd()
myWnd.show()
        