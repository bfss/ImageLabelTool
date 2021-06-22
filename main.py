# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen
from PySide6.QtCore import QRectF, QPointF

from ui_mainwindow import Ui_MainWindow


class MyItem(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super(MyItem, self).__init__(pixmap)

        self.ps = None
        self.es = None
        self.rect_list = list()

        self.draw = False

    def mousePressEvent(self, event):
        self.ps = event.pos()
        #self.draw = True

    def mouseReleaseEvent(self, event):
        self.es = event.pos()
        self.update()
        rect = QRectF(self.ps, self.es)
        self.rect_list.append(rect)
        self.draw = True

    def mouseMoveEvent(self, event):
        self.es = event.pos()
        self.update()
        self.draw = True

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        # Draw the already stored rect
        for rect in self.rect_list:
            painter.drawRect(rect)
        if self.draw:
            rect = QRectF(self.ps, self.es)
            
            painter.drawRect(rect)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pix = QPixmap("1.jpg")
        self.scene = QGraphicsScene()
        self.item = MyItem(self.pix)
        self.scene.addItem(self.item)

        self.ui.graphicsView.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
