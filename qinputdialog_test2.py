from PyQt5.QtWidgets import *
import sys
from MyInputDialog2 import Ui_Dialog

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(MyDialog,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("输入对话框实验")

        #6个按钮
        self.nameButton.clicked.connect(self.inputName)
        self.sexButton.clicked.connect(self.inputSex)
        self.ageButton.clicked.connect(self.inputAge)
        self.dateButton.clicked.connect(self.inputDate2)  # Date Edit
        self.dateButton.clicked.connect(self.inputDate1)  #对话框
        self.HButton.clicked.connect(self.inputHeight)
        self.WButton.clicked.connect(self.inputWeight)
        #6个Label显示标签
        #label_name,label_sex,label_age,label_date,label_h,label_w
        #7个LineEdit编辑框用于输入信息，与上面按钮具有同样功能
        #namelineEdit,sexlineEdit,agelineEdit,datelineEdit,hlineEdit,wlineEdit,lovelineEdit


    def inputName(self):
        name2 = self.namelineEdit.text()
        name, ok = QInputDialog.getText(self, "用户名",
                                        "请输入新的名字:",
                                        QLineEdit.Normal, self.label_name.text())
        if ok:
            self.label_name.setText(name)
            self.namelineEdit.setText(name)
        else:
            self.label_name.setText(name2)

    def inputSex(self):
        list = []
        list.append("男")
        list.append("女")
        sex, ok = QInputDialog.getItem(self, "性别", "请选择性别", list)
        if ok:
            self.label_sex.setText(sex)
            self.sexlineEdit.setText(sex)

    def inputAge(self):
        age, ok = QInputDialog.getInt(self, "年龄","请输入年龄:",
                                      int(self.label_age.text()), 0, 150,4)

        if ok:
            self.label_age.setText(str(age))
            self.agelineEdit.setText(str(age))
    def inputDate1(self):
        dd, ok = QInputDialog.getText(self, "出生年月",
                                        "请输入新的出生年月:",
                                        QLineEdit.Normal, self.label_date.text())
        if ok:
            self.label_date.setText(dd)
            self.datelineEdit.setText(dd)
    def inputDate2(self):
        time = self.dateEdit.text()
        self.label_date.setText(str(time))

    def inputHeight(self):
        stature, ok = QInputDialog.getDouble(self, "身高",
                                             "请输入身高:",
                                             float(self.label_h.text()), -2300.0000, 2300.9999,4)
        if ok:
            self.label_h.setText(str(stature))
            self.hlineEdit.setText(str(stature))
    def inputWeight(self):
        stature, ok = QInputDialog.getDouble(self, "身高",
                                             "请输入身高:",
                                             float(self.label_w.text()), 0, 2300.00,2)
        if ok:
            self.label_w.setText(str(stature))
            self.wlineEdit.setText(str(stature))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MyDialog()
    main.show()
    sys.exit(app.exec_())