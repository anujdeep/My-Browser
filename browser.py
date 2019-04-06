from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="Anuj Browser"
        self.left=60
        self.top=60
        self.width=1600
        self.height=1080
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("browser_12.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.browser=QWebEngineView()
        self.browser.setStyleSheet("""
        .QWebEngineView{
            border: 20px solid black;
            font -size:100px;
            border-radius: 10px;
            background-color: rgb(0, 255, 255);
            width:100%;
            }
        """)
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        navtb=QToolBar("navigation")
        navtb.setStyleSheet("""
        .QToolBar {
            margin:25px;
            border-radius: 10px;
            font-family:Verdana;
            font-size:30 px;
            background-color: rgb(160, 160, 160);
            }
        .QLineEdit{
            font-size:30 px;
            font-family:Verdana;
            }
        """)
        navtb.setIconSize(QSize(40, 40))
        self.addToolBar(navtb)
        back_btn=QAction(QIcon("arrow2.png"),"Back", self)
        back_btn.setToolTip("back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)
        navtb.addSeparator()
        forward_btn=QAction(QIcon("arrow1.png"),"Forward", self)
        forward_btn.setToolTip("forward to next page")
        forward_btn.triggered.connect(self.browser.forward)
        navtb.addAction(forward_btn)
        navtb.addSeparator()
        reload_btn=QAction(QIcon("refresh1.png"),"Reload", self)
        reload_btn.setToolTip("reload the page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)
        navtb.addSeparator()
        stop_btn=QAction(QIcon("cross.png"),"stop", self)
        stop_btn.setToolTip("stop page")
        stop_btn.triggered.connect(self.browser.stop)
        navtb.addAction(stop_btn)
        navtb.addSeparator()
        home_btn=QAction(QIcon("home.png"),"Home", self)
        home_btn.setToolTip("go to home page")
        home_btn.triggered.connect(self.home1)
        navtb.addAction(home_btn)
        navtb.addSeparator()
        
        self.textvalue=QLineEdit("https://www.google.com/")
        self.textvalue.returnPressed.connect(self.changepage)
        self.textvalue.resize(200, 600)
        navtb.addWidget(self.textvalue)
        self.browser.urlChanged.connect(self.url_change)
        navtb.addSeparator()
        navtb.addSeparator()
        utube=QAction(QIcon("Youtube1.png"), "youtube", self)
        navtb.addAction(utube)
        utube.setToolTip("youtube")
        utube.triggered.connect(self.youtube)
        navtb.addSeparator()
        fb=QAction(QIcon("fb1.png"), "facebook", self)
        navtb.addAction(fb)
        fb.setToolTip("facebook")
        fb.triggered.connect(self.facebook)
        navtb.addSeparator()
        gmail=QAction(QIcon("gmail1.jpg"), "gmail", self)
        navtb.addAction(gmail)
        gmail.setToolTip("gmail")
        gmail.triggered.connect(self.gmail)
        navtb.addSeparator()
        github=QAction(QIcon("Octocat.png"), "github", self)
        navtb.addAction(github)
        github.setToolTip("github")
        github.triggered.connect(self.github)
        self.show()
        
    @pyqtSlot()
    def github(self):
        self.browser.setUrl(QUrl("https://www.github.com"))
    def youtube(self):
        self.browser.setUrl(QUrl("https://www.youtube.com"))
    def facebook(self):
        self.browser.setUrl(QUrl("https://www.facebook.com"))
    def  gmail(self):
        self.browser.setUrl(QUrl("https://www.gmail.com"))
    def home1(self):
        self.browser.setUrl(QUrl("https://www.google.com"))
    def url_change(self, q):
        self.textvalue.setText(q.toString())
        self.textvalue.setCursorPosition(0)
        
    def changepage(self):
        q=QUrl(self.textvalue.text())
        if q.scheme()=="":
            q.setScheme("http")
        self.browser.setUrl(q)
         
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setApplicationName("My Browser")
    ex=App()
    sys.exit(app.exec_())
