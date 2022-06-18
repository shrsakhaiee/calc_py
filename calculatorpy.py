from math import *
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui",None)
        self.ui.show()

        self.ui.btn0.clicked.connect(partial(self.number,"0"))
        self.ui.btn1.clicked.connect(partial(self.number,"1"))
        self.ui.btn2.clicked.connect(partial(self.number,"2"))
        self.ui.btn3.clicked.connect(partial(self.number,"3"))
        self.ui.btn4.clicked.connect(partial(self.number,"4"))
        self.ui.btn5.clicked.connect(partial(self.number,"5"))
        self.ui.btn6.clicked.connect(partial(self.number,"6"))
        self.ui.btn7.clicked.connect(partial(self.number,"7"))
        self.ui.btn8.clicked.connect(partial(self.number,"8"))
        self.ui.btn9.clicked.connect(partial(self.number,"9"))
        
        self.ui.btn_ac.clicked.connect(self.ac)
        self.ui.btn_dot.clicked.connect(self.number_dot)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_percent.clicked.connect(self.percent)
        self.ui.btn_eq.clicked.connect(self.eq)       

    def number(self,N):
        self.ui.textbox.setText(self.ui.textbox.text()+ N)
    def number_dot(self):
        for i in self.ui.textbox.text():
            if "." in self.ui.textbox.text():
                break
            else:
                self.ui.textbox.setText(self.ui.textbox.text()+".")
    def ac(self):
        self.ui.textbox.setText("")
    
    
    def sum(self):
        self.opp = "+"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def sub(self):
        self.opp = "-"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def mul(self):
        self.opp = "*"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")

    def div(self):
        self.opp = "/"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")


    def log(self):
        self.opp = "log"
        self.ui.textbox.setText("log ")

   
    def percent(self):
        self.opp = "%"
        self.num1 = float(self.ui.textbox.text())
        self.ui.textbox.setText("")       
        self.ui.textbox.setText(str(self.num1/100))

    def eq(self):
        if self.opp =="+":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1+self.num2))

        if self.opp =="-":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 - self.num2))

        if self.opp =="*":
            self.num2 = float(self.ui.textbox.text())
            self.ui.textbox.setText(str(self.num1 * self.num2))

        if self.opp =="/":
            self.num2 = float(self.ui.textbox.text())
            if self.num2 !=0:
                self.ui.textbox.setText(str(self.num1/self.num2))
            else:
                self.ui.textbox.setText("Can't divide by zero")

        if self.opp =="log":
            self.num = self.ui.textbox.text().split(" ")
            self.num1 = float(self.num[1])
            self.ui.textbox.setText(str(log(self.num1)))

            

app = QApplication([])
window = Main()
app.exec()