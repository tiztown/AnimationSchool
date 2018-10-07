import MaxPlus
from PySide2 import QtWidgets, QtGui, QtCore

def MyGeo(geo):
    
    if geo == "cube":
		MaxPlus.Core.EvalMAXScript("Box isSelected:on width:20 length:20 height:20")
		
    elif geo == "sphere":
		MaxPlus.Core.EvalMAXScript("Sphere radius:15")
		
    elif geo == "torus":
		MaxPlus.Core.EvalMAXScript("Torus radius1:30 radius2:8")


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