"""http://paste.ubuntu.com/p/CsWrQWVTfK/"""

from PySide2 import QtWidgets, QtCore
from data_conn import mesaj_al, mesaj_gonder

class MainWindow(QtWidgets.QMainWindow):

    def build(self):
        self.setCentralWidget(QtWidgets.QWidget())


        self.build_widgets()
        self.build_layouts()
        self.build_events()
        self.reset_inputs()
        self.get_username()

    def build_widgets(self):

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.mesaj_al_callback)
        self.timer.start()

        self.text_input = QtWidgets.QLineEdit()
        self.text_input.setPlaceholderText("Mesaj")

        self.text_input2 = QtWidgets.QLineEdit()
        self.text_input2.setPlaceholderText("İsim")

        self.textedit = QtWidgets.QTextEdit()
        self.textedit.setReadOnly(True)

        self.button = QtWidgets.QPushButton()
        self.button.setText("Gönder")

        self.button2 = QtWidgets.QPushButton()
        self.button2.setText("Kullanici Degis")

        self.dialog = QtWidgets.QInputDialog()


    def build_layouts(self):
        self.layout2 = QtWidgets.QHBoxLayout()
        self.layout2.addWidget(self.text_input)
        self.layout2.addWidget(self.button)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.button2)
        self.main_layout.addWidget(self.textedit)
        self.main_layout.addLayout(self.layout2)
        self.centralWidget().setLayout(self.main_layout)

    def get_username(self):
        self.username = self.dialog.getText(self, "İsim", "İsim Girin")
        if self.username[1]:
            self.user = self.username[0]


    def reset_inputs(self):
        # self.text_input2.setText("")
        self.text_input.setText("")

    def build_events(self):
        self.text_input.returnPressed.connect(self.mesaj_gonder_callback)
        self.text_input.returnPressed.connect(self.reset_inputs)
        self.button.clicked.connect(self.mesaj_gonder_callback)
        self.button.clicked.connect(self.reset_inputs)
        self.button2.clicked.connect(self.get_username)


    def mesaj_gonder_callback(self):
        mesaj_gonder(self.user, self.text_input.text())

    def mesaj_al_callback(self):
        mesajlar_string = ""
        dic = mesaj_al()
        for i, j in dic.items():
            for k in reversed(j):
                #print(k['sender'], k['message'])
                mesajlar_string += k['sender'] + ": " + k['message'] + "\n"

        self.textedit.setText(mesajlar_string)




app = QtWidgets.QApplication()
window = MainWindow()
window.setStyleSheet("""
QWidget{
    background-color:pink;
    border-width: 1px;
    border-color: white;
    border-style: solid;
    color: black;
    }

""")
window.build()
window.show()
app.exec_()
