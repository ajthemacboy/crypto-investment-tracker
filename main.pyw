from PyQt5 import QtWidgets, QtCore
import urllib.request
import sys
import json
from layout import Ui_Dialog


class GUI(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        self.url = "https://www.bitstamp.net/api/ticker/"
        self.config = {
            "origprice": None,
            "holdings": None
        }

        self.update_price()

        self.box_variable_holdings.valueChanged.connect(self.update)
        self.box_variable_origprice.valueChanged.connect(self.update)
        self.check_variable_pin.clicked.connect(self.pin)
        self.button_static_updateprice.clicked.connect(self.update_button)
        self.button_static_close.clicked.connect(self.close)

        self.config_load()

        self.update()

    def update_price(self):
        with urllib.request.urlopen(self.url) as url:
            data = json.load(url)
            self.price = round(float(data['last']), 8)

        self.label_variable_currentprice.setText(str(self.price))

    def update(self):

        self.origworth      = round(float(self.box_variable_holdings.value()) * float(self.box_variable_origprice.value()), 8)
        self.currentworth   = round(float(self.box_variable_holdings.value() * self.price), 8)
        self.worthchange    = round(self.currentworth - self.origworth, 8)

        if   self.worthchange > 0:  self.worthchangestring = "+{}".format(abs(self.worthchange))
        elif self.worthchange < 0:  self.worthchangestring = "-{}".format(abs(self.worthchange))
        else:                       self.worthchangestring = "No change"

        self.label_variable_origworth.setText(str(self.origworth))
        self.label_variable_currentworth.setText(str(self.currentworth))
        self.label_variable_worthchange.setText(str(self.worthchangestring))

    def update_button(self):
        self.update_price()
        self.update()

    def pin(self):
        if self.check_variable_pin.isChecked():
            dialog.setWindowFlags(dialog.windowFlags() |   QtCore.Qt.WindowStaysOnTopHint)
            dialog.show()
        else:
            dialog.setWindowFlags(dialog.windowFlags() & ~ QtCore.Qt.WindowStaysOnTopHint)
            dialog.show()

    def config_load(self):
        try:
            with open("tracker.cfg", "r") as file:
                self.config = json.load(file)
                self.box_variable_origprice.setValue(self.config["origprice"])
                self.box_variable_holdings.setValue(self.config["holdings"])
        except:
            pass

    def config_save(self):
        with open("tracker.cfg", "w") as file:
            json.dump(self.config, file)

    def close(self):
        self.config["origprice"] = round(float(self.box_variable_origprice.value()), 8)
        self.config["holdings"]  = round(float(self.box_variable_holdings.value()), 8)
        self.config_save()
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    gui = GUI(dialog)

    dialog.show()
    sys.exit(app.exec_())
