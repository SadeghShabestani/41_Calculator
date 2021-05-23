# This Python file uses the following encoding: utf-8
import sys
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


class Form:
    def __init__(self):
        super(Form, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_multi.clicked.connect(self.multi)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_mod.clicked.connect(self.mood)
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_dot.clicked.connect(self.dot)
        self.ui.btn_mo.clicked.connect(self.mo)
        self.ui.btn_ma.clicked.connect(self.ma)

        self.ui.btn_0.clicked.connect(self.num0)
        self.ui.btn_1.clicked.connect(self.num1)
        self.ui.btn_2.clicked.connect(self.num2)
        self.ui.btn_3.clicked.connect(self.num3)
        self.ui.btn_4.clicked.connect(self.num4)
        self.ui.btn_5.clicked.connect(self.num5)
        self.ui.btn_6.clicked.connect(self.num6)
        self.ui.btn_7.clicked.connect(self.num7)
        self.ui.btn_8.clicked.connect(self.num8)
        self.ui.btn_9.clicked.connect(self.num9)

    def equal(self):
        self.b = float(self.ui.tb_1.text())
        if self.op == "+":
            result = self.a + self.b
        elif self.op == "-":
            result = self.a - self.b

        elif self.op == "*":
            result = self.a * self.b

        elif self.op == "÷":
            result = self.a / self.b

        elif self.op == "%":
            result = self.a % self.b

        self.ui.tb_1.setText(str(result))

    def sum(self):
        self.op = "+"
        self.a = float(self.ui.tb_1.text())
        self.ui.tb_1.clear()

    def sub(self):
        self.op = "-"
        self.a = float(self.ui.tb_1.text())
        self.ui.tb_1.clear()

    def multi(self):
        self.op = "*"
        self.a = float(self.ui.tb_1.text())
        self.ui.tb_1.clear()

    def div(self):
        self.op = "÷"
        self.a = float(self.ui.tb_1.text())
        self.ui.tb_1.clear()

    def mood(self):
        self.op = "%"
        self.a = float(self.ui.tb_1.text())
        self.ui.tb_1.clear()

    def clear(self):
        self.ui.tb_1.clear()

    def dot(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + ".")

    def mo(self):
        self.ui.tb_1.setText("+" + self.ui.tb_1.text())

    def ma(self):
        self.ui.tb_1.setText("-" + self.ui.tb_1.text())

    def num0(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "0")

    def num1(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "1")

    def num2(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "2")

    def num3(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "3")

    def num4(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "4")

    def num5(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "5")

    def num6(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "6")

    def num7(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "7")

    def num8(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "8")

    def num9(self):
        self.ui.tb_1.setText(self.ui.tb_1.text() + "9")


if __name__ == "__main__":
    app = QApplication([])
    window = Form()
    sys.exit(app.exec_())
