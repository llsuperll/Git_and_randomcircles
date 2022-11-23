from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
import sys
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def initUI(self):
        self.resize(400, 400)
        self.setWindowTitle("Разноцветные окружности")
        self.button = QPushButton(self)
        self.button.move(0, 0)
        self.button.resize(90, 30)
        self.button.setText("Нажми меня")

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_round(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        r = randint(1, 200)
        qp.drawEllipse(randint(1, 400 - r), randint(1, 400 - r), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
