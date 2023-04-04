import os
import shutil
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from janela import Ui_MainWindow
import sys



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Atlas - File Organizer")
        
        self.file = ''
        self.connect_open_path()

    def connect_open_path(self):
        self.Button_Open.clicked.connect(self.open_path)
        self.Button_Organize.clicked.connect(self.organizer)
        
    def organizer(self):
        path = self.file
        files = os.listdir(path)
        
        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

                
            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)
                
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos Organizados")
        msg.exec_()

    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("Pasta"),
                                                '/home',
                                                QFileDialog.ShowDirsOnly |
                                                QFileDialog.DontResolveSymlinks)
    
        self.TXT_Path.setText(self.file)
        self.file = str(self.file)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
