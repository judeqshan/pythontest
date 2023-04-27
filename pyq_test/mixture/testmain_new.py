from email.charset import QP
i=super
l=print
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import sys
z=sys.exit
r=sys.argv
from qlinedit_test import*
from test_import import*
class M(QMainWindow,Ui_MainWindow):
 def __init__(o,*args,**kwargs):
  i(M,o).__init__(*args,**kwargs)
  o.setupUi(o)
  o.pushButton_read.clicked.connect(o.a)
  o.pushButton_set.clicked.connect(o.Y)
  o.pushButton_setcombobox.clicked.connect(o.b)
  o.comboBox.addItems(["neg","positive"])
  o.pushButton_size_hint.clicked.connect(o.c)
 def Y(o):
  o.lineEdit.setText("11")
 def a(o):
  pass
  l(o.lineEdit.text())
 def b(o):
  pass
  o.comboBox.setCurrentIndex()
 def c(o):
  l(o.pushButton_size_hint.sizeHint())
  l(o.pushButton_read.sizeHint())
  l(o.label.sizeHint())
  ti=test_import()
  ti.test()
if __name__=="__main__":
 Q=QApplication(r)
 Q.setApplicationName("test")
 w=M()
 w.show()
 z(Q.exec_())
# Created by pyminifier (https://github.com/liftoff/pyminifier)
