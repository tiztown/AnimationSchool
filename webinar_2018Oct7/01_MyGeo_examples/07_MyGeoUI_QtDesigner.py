import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui

#Import extra module for opening UI file from file
from PySide2 import QtUiTools


def MyGeo(geo):
    
    if geo == "cube":
        cmds.polyCube(w=10, h=3, d=3, sx=10, sy=2, sz=2, ch=1)

    elif geo == "sphere":
        cmds.polySphere(r=1, sx=20, sy=20, ch=1)

    elif geo == "torus":
        cmds.polyTorus(r=1, sr=0.5, tw=0, sx=20, sy=20, ch=1)


class MyGeoWnd(QtCore.QObject):
    def __init__(self):
        super(MyGeoWnd, self).__init__()
            
        # read UI file
        ui_file = QtCore.QFile("C:/Users/RomanPC/Desktop/AnimationSchool_Webinar/01_MyGeo_examples/07_dialog.ui")   #Set file path
        ui_file.open(QtCore.QFile.ReadOnly)         #open file 
        loader = QtUiTools.QUiLoader()              #create QUiLoader instance to process file data
        self.window = loader.load(ui_file)          #read file data
        ui_file.close()                             #close file stream
        
        #define all buttons
        self.buttonSphere = self.window.findChild(QPushButton, 'buttonSphere') 
        self.buttonCube = self.window.findChild(QPushButton, 'buttonCube')
        self.buttonTorus = self.window.findChild(QPushButton, 'buttonTorus')
                
        self.buttonSphere.clicked.connect(self.createSphere)
        self.buttonCube.clicked.connect(self.createCube)
        self.buttonTorus.clicked.connect(self.createTorus)
        
        self.window.show()
        
        
    def createSphere(self):
        MyGeo("sphere")
        
    def createCube(self):
        MyGeo("cube")
        
    def createTorus(self):
        MyGeo("torus")
        

myWnd = MyGeoWnd()

        