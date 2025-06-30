from PyQt5.QtGui import QPainter, QColor, QImage, QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGraphicsScene
from PyQt5.QtCore import QPoint
from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class Window(QMainWindow):
    def __init__(self, red, green, blue, w_top, w_left, w_width, w_height, o_col):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.title = "Color"
        self.top = w_top
        self.left = w_left
        self.width = w_width
        self.height = w_height
        self.outline_color = o_col

        self.button = QPushButton('Покрасить', self)
        self.my_button_is_clicked = False

        self.button.setToolTip('Раскрасить фигуру')
        self.button.move(20, 20)
        self.button.show()
        self.button.clicked.connect(self.on_click)

        self.button2 = QPushButton('TEST', self)
        self.button2.move(140, 20)
        self.button2.show()
        self.button2.clicked.connect(self.on_click1)

        self.pix = QPixmap(self.width + 200, self.height + 200)
        self.pix_color = QColor(255, 255, 255)
        self.pix.fill(self.pix_color)
        self.pix_x = 0
        self.pix_y = 60
        print(self.pix.width())
        # self.colorw2 = QPalette()

        self.InitWindow()
        self.paintEvent(self.InitWindow())

    def InitWindow(self):
        print("start InitWindow")
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setMinimumSize(self.width, self.height)
        #self.setFixedSize(self.size())
        self.show()
        print("end InitWindow")

    def paintEvent(self, event):
        print("start paintEvent")
        painter = QPainter(self)
        painter.begin(self)
        painter.drawPixmap(self.pix_x, self.pix_y, self.pix)
        #painter.drawPoint(0, 0)
        painter.drawLine(2, 2, 102, 2)
        painter.end()

        painter.begin(self.pix)
        painter.setPen(self.outline_color)
        painter.drawChord(20, 10, 200, 200, 0, 5760)  # окружность (5760 для замкнутой)

        painter.setPen(QColor(self.red, self.green, self.blue))
        painter.drawPoint(107, 10)
        painter.setPen(self.outline_color)

        # Поиск фигуры и закрашивание
        if self.my_button_is_clicked:
            image = self.pix.toImage()  # в другой тип для прохождения
            painter.setPen(QColor(self.red, self.green, self.blue))  # QColor(200, 12, 200)
            for i in range(0, self.pix.height()):
                for j in range(0, self.pix.width()):
                    if image.pixelColor(j, i) == self.outline_color:
                        print("yes, its true", str(i), str(j))
                        # Вымеряем толщину границы (идём, пока не найдём белый)
                        while image.pixelColor(j, i) == self.outline_color and j != self.pix.width():
                            j = j + 1
                        # Если фигура не завершена в рамках окна, то не закрашиваем
                        if j == self.pix.width():
                            break
                        # Сохраняем положение возможной 1ой точки
                        start = j
                        # Ищем положение возможной 2ой точки
                        while image.pixelColor(j, i) != self.outline_color and j != self.pix.width():
                            j = j + 1
                        # Если фигура не завершена в рамках окна, то не закрашиваем
                        if j == self.pix.width():
                            break
                        finish = j - 1
                        painter.drawLine(start, i, finish, i)
            self.my_button_is_clicked = False

        painter.end()
        painter.begin(self)
        painter.drawPixmap(self.pix_x, self.pix_y, self.pix)
        painter.end()
        print("end paintEvent")

    def on_click1(self):
        print('PyQt5 button click1')
        self.pix_x = 251
        self.pix_y = 60
        self.update()

    def on_click(self):
        print('PyQt5 button click1')
        self.my_button_is_clicked = True
        self.update()

    def change_inside(self, inside):
        if inside:
            inside = False
        else: inside = True
        return inside



top = 150
left = 150
width = 250
height = 280

r = b = 200
g = 12
# while True:
#     try:
#         r = int(input("red "))
#         g = int(input("green "))
#         b = int(input("blue "))
#     except:
#         print("Неправильное значение")
#     else:
#         if 0 <= r < 256 and 0 <= g < 256 and 0 <= b < 256:
#             break
#         else:
#             print("Неправильное значение")
#             continue
cw = (QColor(0, 0, 0))
game = (QColor(0, 0, 0))
if cw == game and game == QColor(0, 0, 0):
    print("yes")
app1 = QApplication(sys.argv)
window = Window(r, g, b, top, left, width, height, QColor(0, 0, 0))
window.show()
sys.exit(app1.exec())
