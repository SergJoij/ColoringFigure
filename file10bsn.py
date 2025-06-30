from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSpinBox
from PyQt5.QtCore import QPoint
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

        self.label_red = QLabel(self)
        self.label_red.move(140, 20)
        self.label_red.setText("red")
        self.label_red.show()
        self.label_green = QLabel(self)
        self.label_green.move(300, 20)
        self.label_green.setText("green")
        self.label_green.show()
        self.label_blue = QLabel(self)
        self.label_blue.move(460, 20)
        self.label_blue.setText("blue")
        self.label_blue.show()

        self.box_red = QSpinBox(self)
        self.box_red.setMaximum(255)
        self.box_red.move(170, 20)
        self.box_red.valueChanged.connect(self.color_changed_red)
        self.box_red.show()

        self.box_green = QSpinBox(self)
        self.box_green.setMaximum(255)
        self.box_green.move(330, 20)
        self.box_green.valueChanged.connect(self.color_changed_green)
        self.box_green.show()

        self.box_blue = QSpinBox(self)
        self.box_blue.setMaximum(255)
        self.box_blue.move(490, 20)
        self.box_blue.valueChanged.connect(self.color_changed_blue)
        self.box_blue.show()

        self.pix = QPixmap(self.width - 100, self.height - 100)
        self.pix_color = QColor(255, 255, 255)
        self.pix.fill(self.pix_color)
        self.pix_x = 0
        self.pix_y = 60

        self.label_of_process = QLabel(self)
        self.label_of_process.move(20, self.height - 40)
        self.label_of_process.setMinimumWidth(160)
        self.label_of_process.setText("Нажмите кнопку 'Покрасить'")
        self.label_of_process.show()

        self.position_of_cursor = None

        self.InitWindow()
        self.paintEvent(self.InitWindow())

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setMinimumSize(self.width, self.height)

        self.box_red.setValue(self.red)
        self.box_green.setValue(self.green)
        self.box_blue.setValue(self.blue)

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.drawPixmap(self.pix_x, self.pix_y, self.pix)
        painter.end()

        painter.begin(self.pix)
        painter.setPen(self.outline_color)
        # рисует дугу
        # painter.drawArc(20, 20, 280, 107, 640, 5760)
        # рисует замкнутый сектор. Аналогичен методу drawArc(), но соединяет крайние точки дуги с центром окружности
        # painter.drawPie(20, 20, 120, 107, 80, 5760)

        # рисует замкнутую дугу. Аналогичен методу drawArc(), но соединяет крайние точки дуги прямой линией
        # painter.drawChord(500, 10, 120, 160, 0, 5760)  # окружность (5760 для замкнутой)

        # рисует замкнутую дугу за границей справа
        # painter.drawChord(500, 10, 120, 160, 0, 5760)  # окружность (5760 для замкнутой)
        # рисует замкнутую дугу за границей слева
        painter.drawChord(-20, 10, 120, 160, 0, 5760)  # окружность (5760 для замкнутой)
        # рисует прямоугольник
        # painter.drawRect(40, 77, 30, 98)
        # рисует многоугольник
        # painter.drawPolygon(QPoint(2, 7), QPoint(100, 130), QPoint(198, 24),
        #                    QPoint(211, 130), QPoint(259, 159), QPoint(232, 200), QPoint(240, 220), QPoint(300, 140),
        #                    QPoint(300, 190), QPoint(340, 100),
        #                    QPoint(246, 350), QPoint(240, 398), QPoint(126, 200), QPoint(80, 307), QPoint(30, 120))
        # рисует многоугольник за границей
        # painter.drawPolygon(QPoint(2, 7), QPoint(100, 130), QPoint(198, 24),
        #                     QPoint(211, 130), QPoint(259, 159), QPoint(232, 200), QPoint(240, 220), QPoint(300, 140),
        #                     QPoint(300, 190), QPoint(340, 100),
        #                     QPoint(246, 350), QPoint(240, 398), QPoint(126, 200), QPoint(80, 307), QPoint(-30, 120),
        #                     QPoint(1, 14))
        # jnk
        # painter.drawPolygon(QPoint(2, 7), QPoint(100, 130), QPoint(102, 132),
        #                     QPoint(103, 131), QPoint(105, 131), QPoint(106, 132), QPoint(106, 134), QPoint(105, 135),
        #                     QPoint(104, 136), QPoint(104, 138), QPoint(105, 139), QPoint(106, 140), QPoint(106, 141),
        #                     QPoint(105, 142),
        #                     QPoint(57, 130), QPoint(126, 200), QPoint(80, 307), QPoint(-30, 120),
        #                     QPoint(1, 14))
        # "Тяжелый случай"
        # painter.drawPolygon(QPoint(2, 7), QPoint(100, 130), QPoint(102, 132), QPoint(103, 131), QPoint(105, 131),
        #                     QPoint(106, 132),  QPoint(106, 151),  QPoint(105, 153),  QPoint(100, 152),
        #                     QPoint(99, 153), QPoint(99, 159),  QPoint(100, 160),  QPoint(101, 161),
        #                     QPoint(107, 162),  QPoint(107, 163),
        #                     QPoint(101, 163), QPoint(100, 164), QPoint(58, 164))
        # Чуть более "тяжелый случай"
        # painter.drawPolygon(QPoint(2, 7), QPoint(100, 130), QPoint(650, 132), QPoint(650, 131), QPoint(650, 131),
        #                     QPoint(650, 132),  QPoint(106, 151),  QPoint(105, 153),  QPoint(100, 152),
        #                     QPoint(99, 153), QPoint(99, 159),  QPoint(100, 160),  QPoint(101, 161),
        #                     QPoint(107, 162),  QPoint(107, 163),
        #                     QPoint(101, 163), QPoint(100, 164), QPoint(58, 164))
        # "крокозябра"
        # painter.drawPolygon(QPoint(2, 7), QPoint(100, 130), QPoint(198, 24),
        #                    QPoint(120, 130), QPoint(259, 159), QPoint(137, 200),
        #                    QPoint(246, 350), QPoint(240, 398), QPoint(126, 200), QPoint(80, 307), QPoint(30, 120))
        painter.end()
        # Поиск фигуры и закрашивание
        if self.my_button_is_clicked:
            self.shape_figure(painter)
        painter.begin(self)
        painter.drawPixmap(self.pix_x, self.pix_y, self.pix)
        painter.end()

    def on_click(self):
        self.label_of_process.setText("Идёт закраска фигуры")
        self.my_button_is_clicked = True
        self.update()

    def shape_figure(self, painter):
        image = self.pix.toImage()  # перевод в другой тип для прохождения
        painter.begin(self.pix)
        painter.setPen(QColor(self.red, self.green, self.blue))  # QColor(200, 12, 200)
        for i in range(0, self.pix.height()):
            k = 0
            for j in range(0, self.pix.width()):
                if image.pixelColor(j, i) == self.outline_color and j >= k and (self.is_peak_mod(image, j, i) != 2
                                                                                or k == 0):
                    # проверяем точку на близость к пику
                    first_in_line = False
                    if self.is_peak_mod(image, j, i) == 1:
                        if self.near_to_peak(image, j, i) and not self.inside_f(image, j + 1, i):
                            continue
                    # претендент на фигуру, которая выпала за левый край
                    if k == 0 and j != 0:
                        first_in_line = True
                    k = j
                    # фигура, которая выпала за левый край
                    if first_in_line and self.inside_f_mod(image, j - 1, i) \
                            and image.pixelColor(j - 1, i) != self.outline_color:
                        for z in range(j - 1, -1, -1):
                            painter.drawPoint(z, i)
                        if self.is_peak_mod(image, j, i) != 2:  # если точка не явл. пиком, то просто переводим j вперёд
                            continue
                    # Вымеряем толщину границы (идём, пока не найдём белый)
                    while image.pixelColor(k, i) == self.outline_color and k != self.pix.width() - 1:
                        k = k + 1
                    # Если фигура не завершена в рамках окна, то не закрашиваем
                    if k == self.pix.width() - 1 and image.pixelColor(k, i) != self.outline_color:
                        break
                    # проверяем точку на близость к пику
                    if self.is_peak(image, k - 1, i) == 1:
                        if self.near_to_peak(image, k - 1, i) and not self.inside_f(image, k, i):
                            continue
                    # Сохраняем положение возможной 1ой точки, если она внутри фигуры
                    if self.inside_f_mod(image, k, i):
                        start = k
                    else:
                        continue
                    # Ищем положение возможной 2ой точки
                    while image.pixelColor(k, i) != self.outline_color and k != self.pix.width() - 1:
                        k = k + 1
                    # Если фигура не завершена в рамках окна, то не закрашиваем (учтена граница в конце)
                    if k == self.pix.width() - 1 and image.pixelColor(k, i) != self.outline_color \
                            and not self.inside_f(image, k, i):
                        break
                    if k == self.pix.width() - 1 and image.pixelColor(k, i) != self.outline_color:
                        finish = k
                    else:
                        finish = k - 1
                    painter.drawLine(start, i, finish, i)
                    # Выходим на белый пиксель или на конец панели(идём, пока не найдём белый)
                    while image.pixelColor(k, i) == self.outline_color and k != self.pix.width() - 1:
                        k = k + 1
                    # выход
                    if k == self.pix.width() - 1:
                        break
                    # Проверяем, является ли найденная точка пиком
                    next_point = self.is_peak(image, k - 1, i)
                    # Далее
                    while next_point == 2 or (next_point == 1 and self.near_to_peak(image, k - 1, i)) \
                            or (self.inside_f_many(image, k, i)):
                        # проверяем точку на близость к пику
                        if self.is_peak_mod(image, k - 1, i) == 1:
                            if self.near_to_peak(image, k - 1, i) and not self.inside_f(image, k, i):
                                break
                        # Записываем старт после пика
                        start = k
                        while image.pixelColor(k, i) != self.outline_color and k != self.pix.width() - 1:
                            k = k + 1
                        # Если фигура не завершена в рамках окна, то не закрашиваем (учтена граница в конце)
                        if k == self.pix.width() - 1 and image.pixelColor(k, i) != self.outline_color \
                                and not self.inside_f(image, k, i):
                            break
                        if k == self.pix.width() - 1 and image.pixelColor(k, i) != self.outline_color:
                            finish = k
                        else:
                            finish = k - 1
                        painter.drawLine(start, i, finish, i)
                        # Выходим на белый пиксель или на конец панели(идём, пока не найдём белый)
                        while image.pixelColor(k, i) == self.outline_color and k != self.pix.width() - 1:
                            k = k + 1
                        next_point = self.is_peak_mod(image, k - 1, i)

        self.label_of_process.setText("Закраска фигуры завершается")
        # Новый обход, сверху вниз (возраст.)
        image = self.pix.toImage()
        for j in range(0, self.pix.width()):
            k = 0
            for i in range(1, self.pix.height()):
                if self.new_usl(image, j, i, -1) and i >= k:
                    k = i
                    while self.not_two_colors(image, j, k) and k < self.pix.height() - 1:
                        painter.drawPoint(j, k)
                        k = k + 1
        # Новый обход, снизу вверх (убыв.)
        image = self.pix.toImage()
        for j in range(0, self.pix.width()):
            k = self.pix.height() - 1
            for i in range(self.pix.height() - 2, -1, - 1):
                if self.new_usl(image, j, i, 1) and i <= k:
                    k = i
                    while self.not_two_colors(image, j, k) and k > 0:
                        painter.drawPoint(j, k)
                        k = k - 1
        # Новый обход, слева направо (возраст.)
        image = self.pix.toImage()
        for i in range(0, self.pix.height()):
            k = 0
            for j in range(1, self.pix.width()):
                if self.new_usl_side(image, j, i, -1) and j >= k:
                    k = j
                    while self.not_two_colors(image, k, i) and k < self.pix.width() - 1:
                        painter.drawPoint(k, i)
                        k = k + 1
        # # Новый обход, справа налево (убыв.)
        image = self.pix.toImage()
        for i in range(0, self.pix.height()):
            k = self.pix.width() - 1
            for j in range(self.pix.width() - 2, -1, -1):
                if self.new_usl_side(image, j, i, 1) and j <= k:
                    k = j
                    while self.not_two_colors(image, k, i) and k > 0:
                        painter.drawPoint(k, i)
                        k = k - 1
        painter.end()
        self.label_of_process.setText("Фигура закрашена")
        self.my_button_is_clicked = False

    def two_pixels(self, image, x, y):  # возвращает координаты 2 пикселей для проверки на пики
        # Этап 1: выясняем положение пикселя в окне
        if 0 < x < image.width() - 1 and 0 < y < image.height() - 1:
            sphere = 9
        elif y == 0:  # смотрим сверху (1-3)
            if 0 < x < image.width() - 1:  # если x просто сверху (2)
                sphere = 2
            elif x == 0:  # если х сверху слева
                sphere = 1
            else:  # если х сверху справа
                sphere = 3
        elif y == image.width() - 1:
            if 0 < x < image.width() - 1:  # если x просто снизу (6)
                sphere = 6
            elif x == 0:  # если х снизу слева
                sphere = 7
            else:  # если х снизу справа
                sphere = 5
        elif x == 0:  # если х просто слева
            sphere = 8
        else:  # если х просто справа
            sphere = 4
        # этап 2: выясняем местоположение соседних пискселей
        points = []
        if sphere == 9:  # если точка внутри окна
            # Добавляем точки
            for i in range(0, 3):
                for j in range(0, 3):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 1:  # если точка сверху слева
            if image.pixelColor(x + 1, y) == self.outline_color:
                points.append(x + 1)
                points.append(y)
            if image.pixelColor(x + 1, y + 1) == self.outline_color:
                points.append(x + 1)
                points.append(y + 1)
            if image.pixelColor(x, y + 1) == self.outline_color:
                points.append(x)
                points.append(y + 1)
        elif sphere == 2:
            for i in range(0, 3):
                for j in range(1, 3):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 3:  # если х сверху справа
            for i in range(0, 2):
                for j in range(1, 3):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 8:  # если х слева
            for i in range(1, 3):
                for j in range(0, 3):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 4:  # если х справа
            for i in range(0, 2):
                for j in range(0, 3):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 7:  # если х слева снизу
            for i in range(1, 3):
                for j in range(0, 2):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 6:  # если х снизу
            for i in range(0, 3):
                for j in range(0, 2):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        elif sphere == 5:  # если х слева снизу
            for i in range(0, 2):
                for j in range(0, 2):
                    if (i != 1 or j != 1) and image.pixelColor(x - 1 + i, y - 1 + j) == self.outline_color:
                        points.append(x - 1 + i)
                        points.append(y - 1 + j)
        return points

    def two_pixels_mod_side(self, image, x, y):
        # возвращает координаты 2 пикселей для проверки на пики (модиф)
        points = self.two_pixels(image, x, y)
        # проверяем пик на "остроту"
        if len(points) == 4 and (points[0] == x or points[2] == x):
            # находим точку равную данной по параметру x
            if points[0] == x and points[1] != y:
                number1 = 0
                number2 = 1
            else:
                number1 = 2
                number2 = 3
            # ищем
            step = points[number2] - y  # шаг
            i = y + step
            while image.pixelColor(x, i) == self.outline_color:  # проходим всю
                i = i + step

            new_points = self.two_pixels(image, x, i - step)
            # Удаляем лишнюю точку (которая над i-1)
            if len(new_points) == 4 and (new_points[0] == x or new_points[2] == x):
                new_points.pop(new_points.index(i - step * 2) - 1)  # в списке перед той, которая равна i-1 (т.е. х)
                new_points.remove(i - step * 2)
            points.pop(number2)
            points.pop(number1)
            points = points + new_points
        return points

    def two_pixels_mod(self, image, x, y):
        # возвращает координаты 2 пикселей для проверки на пики (модиф)
        points = self.two_pixels(image, x, y)
        # проверяем пик на "остроту"
        if len(points) == 4 and (points[1] == y or points[3] == y):
            # находим точку равную данной по параметру y
            if points[0] != x and points[1] == y:
                number1 = 0
                number2 = 1
            else:
                number1 = 2
                number2 = 3
            # ищем
            step = points[number1] - x  # шаг
            i = x + step
            while image.pixelColor(i, y) == self.outline_color:  # проходим всю
                i = i + step
            new_points = self.two_pixels(image, i - step, y)
            # Удаляем лишнюю точку (которая справа i-1)
            new_points.pop(new_points.index(i - step * 2) + 1)  # в списке перед той, которая равна i-1 (т.е. х)
            new_points.remove(i - step * 2)
            points.pop(number2)
            points.pop(number1)
            points = points + new_points
        return points

    def is_peak(self, image, x, y):  # поиск пиков
        two_pixels = self.two_pixels(image, x, y)
        if len(two_pixels) == 0:
            return 0  # и близко не пик
        # проверяем расположение этих пикселей
        elif len(two_pixels) >= 8:
            return 2
        elif len(two_pixels) == 4:
            if two_pixels[0] != two_pixels[2] and two_pixels[1] == two_pixels[3] != y:
                return 2  # пик!
            else:
                return 0
        elif len(two_pixels) == 2:
            return 2  # если точка одна, значит точно пик
        else:
            return 1  # мб рядом с пиком

    def is_peak_side(self, image, x, y):  # поиск бокового пика
        two_pixels = self.two_pixels(image, x, y)
        if len(two_pixels) == 0:
            return 0  # и близко не пик
        # проверяем расположение этих пикселей
        elif len(two_pixels) >= 8:
            return 2
        elif len(two_pixels) == 4:
            if two_pixels[0] == two_pixels[2] != x and two_pixels[1] != two_pixels[3]:
                return 2  # пик!
            else:
                return 0
        elif len(two_pixels) == 2:
            return 2  # если точка одна, значит точно пик
        else:
            return 1  # мб рядом с пиком

    def near_to_peak(self, image, x, y):  # поиск близких к пику
        i = y - 1
        while image.pixelColor(x, i) == self.outline_color:
            if self.is_peak(image, x, i) == 2:
                return True
            elif i != 0:
                i = i - 1
            else:
                break
        i = y + 1
        while image.pixelColor(x, i) == self.outline_color:
            if self.is_peak(image, x, i) == 2:
                return True
            elif i != self.pix.height() - 1:
                i = i + 1
            else:
                break
        return False

    def near_to_peak_mod(self, image, x, y):  # поиск близких к пику
        i = y - 1
        while image.pixelColor(x, i) == self.outline_color:
            if self.is_peak_mod(image, x, i) == 2:
                return True
            elif i != 0:
                i = i - 1
            else:
                break
        i = y + 1
        while image.pixelColor(x, i) == self.outline_color:
            if self.is_peak_mod(image, x, i) == 2:
                return True
            elif i != self.pix.height() - 1:
                i = i + 1
            else:
                break
        return False

    def near_to_peak_side_mod(self, image, x, y):  # поиск близких к боковому пику
        i = x - 1
        while image.pixelColor(i, y) == self.outline_color:
            if self.is_peak_side_mod(image, i, y) == 2:
                return True
            elif i != 0:
                i = i - 1
            else:
                break
        i = x + 1
        while image.pixelColor(i, y) == self.outline_color:
            if self.is_peak_side_mod(image, i, y) == 2:
                return True
            elif i != self.pix.width() - 1:
                i = i + 1
            else:
                break
        return False

    def is_peak_mod(self, image, x, y):  # поиск пиков
        # поиск пиков модифицированный
        # Позволяет выявлять не только острые пики, но и пики, длиною более 1 пикселя. Сверху/снизу.
        two_pixels = self.two_pixels_mod(image, x, y)
        if len(two_pixels) == 0:
            return 0  # и близко не пик
        # проверяем расположение этих пикселей
        elif len(two_pixels) == 4:
            if two_pixels[1] == two_pixels[3] != y and two_pixels[0] != two_pixels[1]:
                return 2  # пик!
            else:
                return 0
        elif len(two_pixels) == 2:
            return 2  # если точка одна, значит точно пик
        else:
            return 1  # мб рядом с пиком

    def is_peak_side_mod(self, image, x, y):  # поиск боковых пиков
        # поиск пиков боковых модифицированный
        # Позволяет выявлять не только острые пики, но и пики, длиною более 1 пикселя. Боковые, исп. для алгоритма
        # распознания точки внутри фигуры (inside_f)
        two_pixels = self.two_pixels_mod_side(image, x, y)
        if len(two_pixels) == 0:
            return 0  # и близко не пик
        # проверяем расположение этих пикселей
        elif len(two_pixels) == 4:
            if two_pixels[0] == two_pixels[2] != x and two_pixels[1] != two_pixels[3]:
                return 2  # боковой пик!
            else:
                return 0
        elif len(two_pixels) == 2:
            return 2  # если точка одна, значит точно пик
        else:
            return 1  # мб рядом с пиком

    def inside_f_neighboring_points(self, image, x, y):  # проверяем точки выше и ниже
        # Идём до точки, которая выше
        result1 = result2 = True
        k = y
        while image.pixelColor(x, k) == self.outline_color:
            k = k - 1
        # 1 точка - выше
        i = 0
        borders_count = 0
        while i < k:
            if image.pixelColor(x, i) == self.outline_color:
                while image.pixelColor(x, i) == self.outline_color and i < k:
                    i = i + 1
                borders_count = borders_count + 1
            else:
                i = i + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            result1 = False
        # Идём до точки, которая ниже
        k = y
        while image.pixelColor(x, k) == self.outline_color:
            k = k + 1
        # 2 точка - ниже
        i = self.pix.height() - 1
        borders_count = 0
        while i > k:
            if image.pixelColor(x, i) == self.outline_color:
                if self.is_peak_side_mod(image, x, i) != 2 and not self.near_to_peak_side_mod(image, x, i):
                    borders_count = borders_count + 1
                while image.pixelColor(x, i) == self.outline_color and i > k:
                    i = i - 1
            else:
                i = i - 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            result2 = False
        # Делаем вывод о переходности точки
        if result1 != result2:
            return True
        else:
            return False

    def inside_f_neighboring_points_side(self, image, x, y):
        result1 = result2 = True
        k = x
        while image.pixelColor(k, y) == self.outline_color:
            k = k - 1
        # 4: Слева направо, к точке
        zero_points = i = 0
        borders_count = 0
        while i < k:
            if image.pixelColor(i, y) == self.outline_color:
                if self.is_peak_mod(image, i, y) != 2 and not self.near_to_peak_mod(image, i, y):
                    borders_count = borders_count + 1
                while image.pixelColor(i, y) == self.outline_color and i < k:
                    i = i + 1
            else:
                i = i + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            result1 = False
        elif borders_count == 0:
            zero_points = zero_points + 1
        # Идём до точки, которая правее
        k = x
        while image.pixelColor(k, y) == self.outline_color:
            k = k + 1
        # 3: Справа налево, к точке
        i = self.pix.width() - 1
        borders_count = 0
        while i > k:
            if image.pixelColor(i, y) == self.outline_color:
                if self.is_peak_mod(image, i, y) != 2 and not self.near_to_peak_mod(image, i, y):
                    borders_count = borders_count + 1
                while image.pixelColor(i, y) == self.outline_color and i > k:
                    i = i - 1
            else:
                i = i - 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            result2 = False
        # рассматриваем ситуацию с нулями
        if borders_count == 0 or zero_points == 1:
            result2 = not result1
        # Делаем вывод о переходности точки
        if result1 != result2:
            return True
        else:
            return False

    def inside_f(self, image, x, y):  # проверяем нахождение точки внутри фигуры проходом с верха окна до точки
        # 1: Сверху вниз, к точке
        i = 0
        borders_count = 0
        while i != y:
            if image.pixelColor(x, i) == self.outline_color:
                while image.pixelColor(x, i) == self.outline_color and i != y:
                    i = i + 1
                borders_count = borders_count + 1
            else:
                i = i + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 != 0:
            return True
        else:
            return False

    def inside_f_mod(self, image, x, y):  # проверяем нахождение точки внутри фигуры проходом с верха окна до точки
        local_image = self.pix.toImage()  # возвращает изображение уже частично закрашенной фигуры
        zero_points = i = 0
        borders_count = 0
        while i != y:
            if image.pixelColor(x, i) == self.outline_color:
                if self.is_peak_side_mod(image, x, i) != 2 and (not self.near_to_peak_side_mod(image, x, i)
                                                                or self.inside_f_neighboring_points(image, x, i)):
                    borders_count = borders_count + 1
                while image.pixelColor(x, i) == self.outline_color and i != y:
                    i = i + 1
                    if image.pixelColor(x, i) == self.outline_color and self.near_to_peak_side_mod(image, x, i):
                        borders_count = borders_count - 1
            else:
                i = i + 1
        if local_image.pixelColor(x, 0) == QColor(self.red, self.green, self.blue):
            borders_count = borders_count + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            return False
        elif borders_count == 0:
            zero_points = zero_points + 1
        # 2: Снизу вверх, к точке
        i = self.pix.height() - 1
        borders_count = 0
        while i != y:
            if image.pixelColor(x, i) == self.outline_color:
                if self.is_peak_side_mod(image, x, i) != 2 and (
                        not self.near_to_peak_side_mod(image, x, i) or self.inside_f_neighboring_points(image, x, i)):
                    borders_count = borders_count + 1
                while image.pixelColor(x, i) == self.outline_color and i != y:
                    i = i - 1
                    if image.pixelColor(x, i) == self.outline_color and self.near_to_peak_side_mod(image, x, i):
                        borders_count = borders_count - 1
            else:
                i = i - 1
        if local_image.pixelColor(x, self.pix.height() - 1) == QColor(self.red, self.green, self.blue):
            borders_count = borders_count + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            return False
        elif borders_count == 0:
            zero_points = zero_points + 1
        # 3: Справа налево, к точке
        i = self.pix.width() - 1
        borders_count = 0
        while i != x:
            if image.pixelColor(i, y) == self.outline_color:
                if self.is_peak_mod(image, i, y) != 2 and (not self.near_to_peak_mod(image, i, y)
                                                           or self.inside_f_neighboring_points_side(image, i, y)):
                    borders_count = borders_count + 1
                while image.pixelColor(i, y) == self.outline_color and i != x:
                    i = i - 1
                    if image.pixelColor(i, y) == self.outline_color and self.near_to_peak_mod(image, i, y):
                        borders_count = borders_count - 1
            else:
                i = i - 1
        if local_image.pixelColor(self.pix.width() - 1, y) == QColor(self.red, self.green, self.blue):
            borders_count = borders_count + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if borders_count % 2 == 0 and borders_count != 0:
            return False
        elif borders_count == 0:
            zero_points = zero_points + 1
        # 4: Слева направо, к точке
        i = 0
        borders_count = 0
        while i != x:
            if image.pixelColor(i, y) == self.outline_color:
                if self.is_peak_mod(image, i, y) != 2 and (not self.near_to_peak_mod(image, i, y)
                                                           or self.inside_f_neighboring_points_side(image, i, y)):
                    borders_count = borders_count + 1
                while image.pixelColor(i, y) == self.outline_color and i != x:
                    i = i + 1
                    if image.pixelColor(i, y) == self.outline_color and self.near_to_peak_mod(image, i, y):
                        borders_count = borders_count - 1
            else:
                i = i + 1
        if local_image.pixelColor(0, y) == QColor(self.red, self.green, self.blue):
            borders_count = borders_count + 1
        # Делаем вывод о нахождении точки внутри фигуры из количества границ
        if (borders_count % 2 == 0 and borders_count != 0) or (borders_count == 0 and zero_points >= 2):
            return False
        else:
            return True

    def inside_f_many(self, image, x, y):
        k = x
        while image.pixelColor(k, y) != self.outline_color and k != self.pix.width() - 1:
            if not self.inside_f(image, k, y):
                return False
            k = k + 1
        return True

    def inside_f_many_to_start(self, image, x, y):
        k = x
        while image.pixelColor(k, y) != self.outline_color and k != 0:
            if not self.inside_f_mod(image, k, y):
                return False
            k = k - 1
        return True

    def color_changed_red(self):
        if QColor(self.box_red.value(), self.green, self.blue) != self.outline_color:
            self.red = self.box_red.value()
        elif self.box_red.value() == 255 and self.outline_color.red() == 255:
            self.box_red.setValue(self.box_red.minimum())
            self.red = self.box_red.value()
        elif self.box_red.value() == 0 and self.outline_color.red() == 0:
            self.box_red.setValue(self.box_red.maximum())
            self.red = self.box_red.value()
        else:
            self.box_red.setValue(self.box_red.value() + 1)
            self.red = self.box_red.value()
        self.label_of_process.setText("Нажмите кнопку 'Покрасить'")

    def color_changed_green(self):
        if QColor(self.red, self.box_green.value(), self.blue) != self.outline_color:
            self.green = self.box_green.value()
        elif self.box_green.value() == 255 and self.outline_color.green() == 255:
            self.box_green.setValue(self.box_green.minimum())
            self.green = self.box_green.value()
        elif self.box_green.value() == 0 and self.outline_color.green() == 0:
            self.box_green.setValue(self.box_green.maximum())
            self.green = self.box_green.value()
        else:
            self.box_green.setValue(self.box_green.value() + 1)
            self.green = self.box_green.value()
        self.label_of_process.setText("Нажмите кнопку 'Покрасить'")

    def color_changed_blue(self):
        if QColor(self.red, self.green, self.box_blue.value()) != self.outline_color:
            self.blue = self.box_blue.value()
        elif self.box_blue.value() == 255 and self.outline_color.blue() == 255:
            self.box_blue.setValue(self.box_blue.minimum())
            self.blue = self.box_blue.value()
        elif self.box_blue.value() == 0 and self.outline_color.blue() == 0:
            self.box_blue.setValue(self.box_blue.maximum())
            self.blue = self.box_blue.value()
        else:
            self.box_blue.setValue(self.box_blue.value() + 1)
            self.blue = self.box_blue.value()
        self.label_of_process.setText("Нажмите кнопку 'Покрасить'")

    def not_two_colors(self, image, x, y):  # условие для финальной закраски
        if image.pixelColor(x, y) != QColor(self.red, self.green, self.blue) and image.pixelColor(x, y) != self.outline_color:
            return True
        else:
            return False

    def new_usl(self, image, x, y, sign):  # условие для финальной закраски
        if image.pixelColor(x, y + sign) == QColor(self.red, self.green, self.blue) and self.not_two_colors(image, x, y):
            return True
        else:
            return False

    def new_usl_side(self, image, x, y, sign):  # условие для финальной закраски
        if image.pixelColor(x + sign, y) == QColor(self.red, self.green, self.blue) and self.not_two_colors(image, x, y):
            return True
        else:
            return False


top = 150
left = 150
width = 600
height = 500

r = b = 200
g = 12
app1 = QApplication(sys.argv)
window = Window(r, g, b, top, left, width, height, QColor(0, 0, 0))
window.show()
sys.exit(app1.exec())
