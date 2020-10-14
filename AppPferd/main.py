import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QComboBox
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtCore import QSize
from datetime import datetime


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Pyqt GRID/Title ->
        self.setMinimumSize(QSize(350, 300))
        self.setWindowTitle("Pferd App")

        # FormItem PyQt5 -> status
        self.status = 1

        # FormItem PyQt5 -> Ordem de produção
        self.LabelProduction_Order = QLabel(self)
        self.LabelProduction_Order.setText('Ordem de produção:')
        self.production_order = QLineEdit(self)

        # FormItem PyQt5 -> Artigo
        self.LabelArticle = QLabel(self)
        self.LabelMachine = QLabel(self)
        self.LabelArticle.setText('Artigo:')
        self.article = QLineEdit(self)

        # FormItem PyQt5 -> Máquina
        self.machine = QComboBox(self)
        self.LabelMachine.setText('Máquina:')
        machine_list = ['Guilhotina', 'Fatiadeira', 'Lixadeira']
        self.machine.addItems(machine_list)

        # GRID PyQt5 -> Máquina
        self.machine.move(80, 50)
        self.LabelMachine.move(80, 20)
        self.machine.resize(200, 32)
        self.LabelMachine.resize(200, 32)

        # GRID PyQt5 -> Ordem de produção
        self.production_order.move(80, 110)
        self.LabelProduction_Order.move(80, 80)
        self.production_order.resize(200, 32)
        self.LabelProduction_Order.resize(200, 32)

        # GRID PyQt5 -> Artigo
        self.article.move(80, 170)
        self.LabelArticle.move(80, 140)
        self.article.resize(200, 32)
        self.LabelArticle.resize(200, 32)

        # PtQt5 FORM -> Botão
        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(80, 220)

    def clickMethod(self):

        # PtQt5 Action -> GOTO def
        self.mysql()

    def production_order_error(self):

        # MessageBox PyQt5 -> Error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erro de gravação!")
        msg.setInformativeText("O campo Ordem de produção não pode ser nulo!")
        msg.setWindowTitle("ERRO!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def article_error(self):

        # MessageBox PyQt5 -> Error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erro de gravação!")
        msg.setInformativeText("O campo Artigo não pode ser nulo!")
        msg.setWindowTitle("ERRO!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def erro_conn(self):

        # MessageBox PyQt5 -> Error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erro de conexão!")
        msg.setInformativeText("Verifique a conexão e tente novamente!")
        msg.setWindowTitle("ERRO!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def Success(self):

        # MessageBox PyQt5 -> Error
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sucesso!")
        msg.setInformativeText("Gravação feita com sucesso!")
        msg.setWindowTitle("Sucesso!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def mysql(self):

            import mysql.connector

            # Mysql.Conn -> Parâmetros de conexão
            self.mydb = mysql.connector.connect(
                host="YOURIP",
                user="YOURUSERNAME",
                password="YOURPASSWD",
                database="YOUTDATABASE"
            )

            def now():
                return datetime.now()

            # FormStatic Vars -> Status & data
            self.date_control = now()

            try:
                self.mycursor = self.mydb.cursor()
            except :
                print ("Error code:")

            # Mysql.Query -> inserção de variáveis
            self.sql = "INSERT INTO app_production (machine, date_control," \
                  "production_order,article_number,status) VALUES (%s,%s,%s,%s,%s)"

            # Mysql.error -> Error/Null prevent
            if self.production_order.text() == '':
                self.production_order_error()
                return

            # Mysql.error -> Error/Null prevent
            if self.article.text() == '':
                self.article_error()
                return

            # Mysql.Query -> Insert
            val = (self.machine.currentText(), self.date_control, self.production_order.text(), self.article.text(), self.status)
            self.mycursor.execute(self.sql, val)

            self.mydb.commit()
            self.Success()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
