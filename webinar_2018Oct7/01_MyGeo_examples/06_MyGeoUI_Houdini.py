from PySide2 import QtWidgets, QtCore, QtGui

def MyGeo(geo):
    
    if geo == "cube":
        print "Cube has been created"

    elif geo == "sphere":
    
        geo = hou.node('/obj/').createNode('geo')
        for n in geo.children():
            n.destroy()
        hou.node('/obj/geo1').createNode("sphere")
        
    elif geo == "torus":
        print "Torus has been created"


class MyGeoWnd(QtWidgets.QDialog):
    def __init__(self):
        super(MyGeoWnd, self).__init__()

        self.setWindowTitle("MyGeo")
        self.setFixedSize(400,50)

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
        
        self.checkbox = QtWidgets.QCheckBox("Say Hi")
        self.buttonsLayout.addWidget(self.checkbox)
        
        self.setLayout(self.buttonsLayout)
        
    def createSphere(self):
        MyGeo("sphere")
        
        if self.checkbox.isChecked():
                print "Hi"
        
    def createCube(self):
        MyGeo("cube")
        
        if self.checkbox.isChecked():
                print "Hi"
        
    def createTorus(self):
        MyGeo("torus")
        
        if self.checkbox.isChecked():
                print "Hi"
        

myWnd = MyGeoWnd()
myWnd.show()
