import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt,QDateTime
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.date_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(700,300,700,250)
        self.time_label.setStyleSheet("font-size:150px;"
                                      "font-family:Arial;"
                                      "color:green;")
        self.setStyleSheet("background-color:black;")
        self.date_label.setStyleSheet("font-size:30px;"
                                      "font-family:Arial;"
                                      "color:green;")
        
        self.time_label.setAlignment(Qt.AlignCenter)
        self.date_label.setAlignment(Qt.AlignCenter | Qt.AlignBottom)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.date_label)
        self.setLayout(vbox)

        self.update_time()
        self.update_date()

    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

    def update_date(self):
        current_date=QDateTime.currentDateTime().toString("dd MMM yy")
        self.date_label.setText(current_date)
    
def main():
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()
# PyQt5 StopWatch