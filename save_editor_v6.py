from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from subprocess import Popen
from bs4 import BeautifulSoup as BS
from datetime import datetime
import sys, os, json, logging, tkinter.messagebox, requests


LOG_FILENAME = "resources/logs/errors.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)

class BackEnd(object):
    def __init__(self):
        self.version = 6
        self.dev = "@illiw#2079"
        self.data = self.load_data("resources/data/appdata/data.json")
        self.dev = self.data['version_info']['dev']
 
        try:
            if self.data['ticks']['auto-update']:
                print("Updater work in progress...")
                # self.update()
            else:
                print("Auto-Updates are turned off, skipping to launch...")
                pass
        except Exception as error:
            self.log_error(error)

    def load_data(self, path):
        try:
            data = json.load(open(path))
            return data
        except Exception as error:
            self.log_error(error)
    
    def save_data(self, data, path):
        try:
            json.dump(data, open(path, "w+"), indent=4)
        except Exception as error:
            self.log_error(error)   

    def fetch_data(self):
        self.url = "https://raw.githubusercontent.com/lewdCracks/toa-save_editor/master/json_data/data.json"
        try:
            self.req = requests.get(self.url)
            if self.req.status_code == 200 and self.req.url == self.url:
                self.up_data = json.loads(self.req.content)
                return True, self.up_data
            else:
                return False, None
        except Exception as error:
            self.log_error(error)
            raise error

    def get_download_url(self, url):
        try:
            self.req = requests.get(url)
            if self.req.status_code == 200 and self.req.url == url:
                self.soup = BS(self.req.content, features='html.parser')
                self.download_url = self.soup.find(class_='input').get('href')
                return True, self.download_url
            else:
                return False, None
        except Exception as error:
            self.log_error(error)
            raise error
    
    def download_file(self, path):
        pass
    
    def update(self): # come back later - multiple files
        self.resp, self.new_data = self.fetch_data()
        print('Checking for updates...')
        try:
            if self.resp:
                if self.version < self.new_data['app_version']:
                    if self.ask_user("Auto-Updater", f"Your save editor is out of date would you like to request an update?.\n{self.version} < {self.new_data['app_version']}"):
                        pass
                else:
                    pass
                
                if self.data['data_version'] < self.new_data['data_version']:
                    pass
                else:
                    pass
                
        except Exception as error:
            self.log_error(error)

    def ask_user(self, head ,message):
        self.root = Tk()
        self.root.withdraw()
        self.c = tkinter.messagebox.askquestion(head, message)
        if self.c == 'yes':
            return True
        else:
            return False
        self.root.destroy()
    
    def show_user(self, head, message):
        self.root = Tk()
        self.root.withdraw()
        self.c = tkinter.messagebox.showinfo(head, message)
        if self.c == 'yes':
            return True
        else:
            return False
        self.root.destroy()
 
    def log_error(self, error):
        self.root = Tk()
        self.root.withdraw()
        logging.exception({error})
        tkinter.messagebox.showerror('Woops!', f"You ran into an error please report to {self.dev} on discord.\n\nError: {error}\n\nFull error log is available in logs folder.")
        self.root.destroy()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 655)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/tab_icons/main-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setItalic(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.items_tab = QtWidgets.QWidget()
        self.items_tab.setObjectName("items_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.items_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.all_item_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_item_label.sizePolicy().hasHeightForWidth())
        self.all_item_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.all_item_label.setFont(font)
        self.all_item_label.setTextFormat(QtCore.Qt.PlainText)
        self.all_item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.all_item_label.setOpenExternalLinks(False)
        self.all_item_label.setObjectName("all_item_label")
        self.gridLayout_2.addWidget(self.all_item_label, 0, 0, 1, 1)
        self.player_item_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_item_label.sizePolicy().hasHeightForWidth())
        self.player_item_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.player_item_label.setFont(font)
        self.player_item_label.setTextFormat(QtCore.Qt.PlainText)
        self.player_item_label.setAlignment(QtCore.Qt.AlignCenter)
        self.player_item_label.setOpenExternalLinks(False)
        self.player_item_label.setObjectName("player_item_label")
        self.gridLayout_2.addWidget(self.player_item_label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 545, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 13, 1)
        self.item_settings_label = QtWidgets.QLabel(self.items_tab)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.item_settings_label.setFont(font)
        self.item_settings_label.setTextFormat(QtCore.Qt.PlainText)
        self.item_settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_settings_label.setOpenExternalLinks(False)
        self.item_settings_label.setObjectName("item_settings_label")
        self.gridLayout_2.addWidget(self.item_settings_label, 0, 3, 1, 3)
        self.all_item_list = QtWidgets.QListWidget(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all_item_list.sizePolicy().hasHeightForWidth())
        self.all_item_list.setSizePolicy(sizePolicy)
        self.all_item_list.setMinimumSize(QtCore.QSize(200, 0))
        self.all_item_list.setObjectName("all_item_list")
        self.gridLayout_2.addWidget(self.all_item_list, 1, 0, 12, 1)
        self.player_item_list = QtWidgets.QListWidget(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_item_list.sizePolicy().hasHeightForWidth())
        self.player_item_list.setSizePolicy(sizePolicy)
        self.player_item_list.setMinimumSize(QtCore.QSize(200, 0))
        self.player_item_list.setObjectName("player_item_list")
        self.gridLayout_2.addWidget(self.player_item_list, 1, 1, 12, 1)
        self.item_filter_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_filter_bar.sizePolicy().hasHeightForWidth())
        self.item_filter_bar.setSizePolicy(sizePolicy)
        self.item_filter_bar.setObjectName("item_filter_bar")
        self.gridLayout_2.addWidget(self.item_filter_bar, 1, 3, 1, 1)
        self.item_dropdown = QtWidgets.QComboBox(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_dropdown.sizePolicy().hasHeightForWidth())
        self.item_dropdown.setSizePolicy(sizePolicy)
        self.item_dropdown.setObjectName("item_dropdown")
        self.gridLayout_2.addWidget(self.item_dropdown, 1, 4, 1, 2)
        self.grip_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grip_label.sizePolicy().hasHeightForWidth())
        self.grip_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.grip_label.setFont(font)
        self.grip_label.setObjectName("grip_label")
        self.gridLayout_2.addWidget(self.grip_label, 2, 3, 1, 1)
        self.grip_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grip_bar.sizePolicy().hasHeightForWidth())
        self.grip_bar.setSizePolicy(sizePolicy)
        self.grip_bar.setMinimumSize(QtCore.QSize(10, 0))
        self.grip_bar.setObjectName("grip_bar")
        self.gridLayout_2.addWidget(self.grip_bar, 2, 4, 1, 2)
        self.mag_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mag_label.sizePolicy().hasHeightForWidth())
        self.mag_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.mag_label.setFont(font)
        self.mag_label.setObjectName("mag_label")
        self.gridLayout_2.addWidget(self.mag_label, 3, 3, 1, 1)
        self.mag_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mag_bar.sizePolicy().hasHeightForWidth())
        self.mag_bar.setSizePolicy(sizePolicy)
        self.mag_bar.setMinimumSize(QtCore.QSize(10, 0))
        self.mag_bar.setObjectName("mag_bar")
        self.gridLayout_2.addWidget(self.mag_bar, 3, 4, 1, 2)
        self.dur_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dur_label.sizePolicy().hasHeightForWidth())
        self.dur_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.dur_label.setFont(font)
        self.dur_label.setObjectName("dur_label")
        self.gridLayout_2.addWidget(self.dur_label, 4, 3, 1, 1)
        self.dur_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dur_bar.sizePolicy().hasHeightForWidth())
        self.dur_bar.setSizePolicy(sizePolicy)
        self.dur_bar.setMinimumSize(QtCore.QSize(10, 0))
        self.dur_bar.setObjectName("dur_bar")
        self.gridLayout_2.addWidget(self.dur_bar, 4, 4, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(348, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 3, 1, 3)
        self.misc_items_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.misc_items_label.sizePolicy().hasHeightForWidth())
        self.misc_items_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.misc_items_label.setFont(font)
        self.misc_items_label.setTextFormat(QtCore.Qt.PlainText)
        self.misc_items_label.setAlignment(QtCore.Qt.AlignCenter)
        self.misc_items_label.setOpenExternalLinks(False)
        self.misc_items_label.setObjectName("misc_items_label")
        self.gridLayout_2.addWidget(self.misc_items_label, 7, 3, 1, 3)
        self.gold_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gold_label.sizePolicy().hasHeightForWidth())
        self.gold_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.gold_label.setFont(font)
        self.gold_label.setObjectName("gold_label")
        self.gridLayout_2.addWidget(self.gold_label, 8, 3, 1, 1)
        self.gold_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gold_bar.sizePolicy().hasHeightForWidth())
        self.gold_bar.setSizePolicy(sizePolicy)
        self.gold_bar.setMinimumSize(QtCore.QSize(10, 0))
        self.gold_bar.setObjectName("gold_bar")
        self.gridLayout_2.addWidget(self.gold_bar, 8, 4, 1, 2)
        self.food_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.food_label.sizePolicy().hasHeightForWidth())
        self.food_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.food_label.setFont(font)
        self.food_label.setObjectName("food_label")
        self.gridLayout_2.addWidget(self.food_label, 9, 3, 1, 1)
        self.food_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.food_bar.sizePolicy().hasHeightForWidth())
        self.food_bar.setSizePolicy(sizePolicy)
        self.food_bar.setMinimumSize(QtCore.QSize(10, 0))
        self.food_bar.setObjectName("food_bar")
        self.gridLayout_2.addWidget(self.food_bar, 9, 4, 1, 2)
        self.crystal_label = QtWidgets.QLabel(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crystal_label.sizePolicy().hasHeightForWidth())
        self.crystal_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.crystal_label.setFont(font)
        self.crystal_label.setObjectName("crystal_label")
        self.gridLayout_2.addWidget(self.crystal_label, 10, 3, 1, 1)
        self.crystal_bar = QtWidgets.QLineEdit(self.items_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crystal_bar.sizePolicy().hasHeightForWidth())
        self.crystal_bar.setSizePolicy(sizePolicy)
        self.crystal_bar.setMinimumSize(QtCore.QSize(10, 0))
        self.crystal_bar.setObjectName("crystal_bar")
        self.gridLayout_2.addWidget(self.crystal_bar, 10, 4, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(348, 203, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 11, 3, 1, 3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/images/tab_icons/items.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.items_tab, icon1, "")
        self.char_tab = QtWidgets.QWidget()
        self.char_tab.setObjectName("char_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.char_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stats_label = QtWidgets.QLabel(self.char_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stats_label.sizePolicy().hasHeightForWidth())
        self.stats_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.stats_label.setFont(font)
        self.stats_label.setTextFormat(QtCore.Qt.PlainText)
        self.stats_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stats_label.setOpenExternalLinks(False)
        self.stats_label.setObjectName("stats_label")
        self.gridLayout_6.addWidget(self.stats_label, 0, 3, 1, 2)
        self.race_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.race_dropdown.setObjectName("race_dropdown")
        self.gridLayout_6.addWidget(self.race_dropdown, 2, 2, 1, 1)
        self.appearance_label = QtWidgets.QLabel(self.char_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.appearance_label.sizePolicy().hasHeightForWidth())
        self.appearance_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.appearance_label.setFont(font)
        self.appearance_label.setTextFormat(QtCore.Qt.PlainText)
        self.appearance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.appearance_label.setOpenExternalLinks(False)
        self.appearance_label.setObjectName("appearance_label")
        self.gridLayout_6.addWidget(self.appearance_label, 0, 1, 1, 2)
        self.race_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.race_label.setFont(font)
        self.race_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.race_label.setAlignment(QtCore.Qt.AlignCenter)
        self.race_label.setObjectName("race_label")
        self.gridLayout_6.addWidget(self.race_label, 2, 1, 1, 1)
        self.eye_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.eye_dropdown.setObjectName("eye_dropdown")
        self.gridLayout_6.addWidget(self.eye_dropdown, 4, 2, 1, 1)
        self.job_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.job_dropdown.setObjectName("job_dropdown")
        self.gridLayout_6.addWidget(self.job_dropdown, 11, 4, 1, 1)
        self.hair_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.hair_label.setFont(font)
        self.hair_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.hair_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hair_label.setObjectName("hair_label")
        self.gridLayout_6.addWidget(self.hair_label, 3, 1, 1, 1)
        self.butt_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.butt_dropdown.setObjectName("butt_dropdown")
        self.gridLayout_6.addWidget(self.butt_dropdown, 6, 2, 1, 1)
        self.lip_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.lip_label.setFont(font)
        self.lip_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lip_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lip_label.setObjectName("lip_label")
        self.gridLayout_6.addWidget(self.lip_label, 5, 1, 1, 1)
        self.detail_search_bar = QtWidgets.QLineEdit(self.char_tab)
        self.detail_search_bar.setObjectName("detail_search_bar")
        self.gridLayout_6.addWidget(self.detail_search_bar, 1, 3, 1, 2)
        self.penis_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.penis_label.setFont(font)
        self.penis_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.penis_label.setAlignment(QtCore.Qt.AlignCenter)
        self.penis_label.setObjectName("penis_label")
        self.gridLayout_6.addWidget(self.penis_label, 7, 1, 1, 1)
        self.lip_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.lip_dropdown.setObjectName("lip_dropdown")
        self.gridLayout_6.addWidget(self.lip_dropdown, 5, 2, 1, 1)
        self.penis_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.penis_dropdown.setObjectName("penis_dropdown")
        self.gridLayout_6.addWidget(self.penis_dropdown, 7, 2, 1, 1)
        self.player_detail_list = QtWidgets.QListWidget(self.char_tab)
        self.player_detail_list.setObjectName("player_detail_list")
        self.gridLayout_6.addWidget(self.player_detail_list, 2, 3, 8, 2)
        self.fem_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.fem_label.setFont(font)
        self.fem_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fem_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fem_label.setObjectName("fem_label")
        self.gridLayout_6.addWidget(self.fem_label, 8, 1, 1, 1)
        self.hair_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.hair_dropdown.setObjectName("hair_dropdown")
        self.gridLayout_6.addWidget(self.hair_dropdown, 3, 2, 1, 1)
        self.fem_dropdown = QtWidgets.QComboBox(self.char_tab)
        self.fem_dropdown.setObjectName("fem_dropdown")
        self.gridLayout_6.addWidget(self.fem_dropdown, 8, 2, 1, 1)
        self.eye_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.eye_label.setFont(font)
        self.eye_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.eye_label.setAlignment(QtCore.Qt.AlignCenter)
        self.eye_label.setObjectName("eye_label")
        self.gridLayout_6.addWidget(self.eye_label, 4, 1, 1, 1)
        self.player_value_bar = QtWidgets.QLineEdit(self.char_tab)
        self.player_value_bar.setObjectName("player_value_bar")
        self.gridLayout_6.addWidget(self.player_value_bar, 10, 3, 1, 2)
        self.butt_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.butt_label.setFont(font)
        self.butt_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.butt_label.setAlignment(QtCore.Qt.AlignCenter)
        self.butt_label.setObjectName("butt_label")
        self.gridLayout_6.addWidget(self.butt_label, 6, 1, 1, 1)
        self.job_label = QtWidgets.QLabel(self.char_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.job_label.setFont(font)
        self.job_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.job_label.setAlignment(QtCore.Qt.AlignCenter)
        self.job_label.setObjectName("job_label")
        self.gridLayout_6.addWidget(self.job_label, 11, 3, 1, 1)
        self.por1_label = QtWidgets.QLabel(self.char_tab)
        self.por1_label.setText("")
        self.por1_label.setPixmap(QtGui.QPixmap("resources/images/portrait.png"))
        self.por1_label.setScaledContents(False)
        self.por1_label.setObjectName("por1_label")
        self.gridLayout_6.addWidget(self.por1_label, 9, 1, 1, 1)
        self.por2_label = QtWidgets.QLabel(self.char_tab)
        self.por2_label.setText("")
        self.por2_label.setPixmap(QtGui.QPixmap("resources/images/portrait2.png"))
        self.por2_label.setObjectName("por2_label")
        self.gridLayout_6.addWidget(self.por2_label, 9, 2, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/images/tab_icons/character.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.char_tab, icon2, "")
        self.skill_tab = QtWidgets.QWidget()
        self.skill_tab.setObjectName("skill_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.skill_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.skills_label = QtWidgets.QLabel(self.skill_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skills_label.sizePolicy().hasHeightForWidth())
        self.skills_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.skills_label.setFont(font)
        self.skills_label.setTextFormat(QtCore.Qt.PlainText)
        self.skills_label.setAlignment(QtCore.Qt.AlignCenter)
        self.skills_label.setOpenExternalLinks(False)
        self.skills_label.setObjectName("skills_label")
        self.gridLayout_3.addWidget(self.skills_label, 0, 0, 1, 1)
        self.perks_label = QtWidgets.QLabel(self.skill_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perks_label.sizePolicy().hasHeightForWidth())
        self.perks_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.perks_label.setFont(font)
        self.perks_label.setTextFormat(QtCore.Qt.PlainText)
        self.perks_label.setAlignment(QtCore.Qt.AlignCenter)
        self.perks_label.setOpenExternalLinks(False)
        self.perks_label.setObjectName("perks_label")
        self.gridLayout_3.addWidget(self.perks_label, 0, 1, 1, 1)
        self.skill_search_bar = QtWidgets.QLineEdit(self.skill_tab)
        self.skill_search_bar.setObjectName("skill_search_bar")
        self.gridLayout_3.addWidget(self.skill_search_bar, 1, 0, 1, 1)
        self.perk_search_bar = QtWidgets.QLineEdit(self.skill_tab)
        self.perk_search_bar.setObjectName("perk_search_bar")
        self.gridLayout_3.addWidget(self.perk_search_bar, 1, 1, 1, 1)
        self.skill_list = QtWidgets.QListWidget(self.skill_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skill_list.sizePolicy().hasHeightForWidth())
        self.skill_list.setSizePolicy(sizePolicy)
        self.skill_list.setMinimumSize(QtCore.QSize(200, 0))
        self.skill_list.setObjectName("skill_list")
        self.gridLayout_3.addWidget(self.skill_list, 2, 0, 1, 1)
        self.perk_list = QtWidgets.QListWidget(self.skill_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perk_list.sizePolicy().hasHeightForWidth())
        self.perk_list.setSizePolicy(sizePolicy)
        self.perk_list.setMinimumSize(QtCore.QSize(200, 0))
        self.perk_list.setObjectName("perk_list")
        self.gridLayout_3.addWidget(self.perk_list, 2, 1, 1, 1)
        self.sp_value_bar = QtWidgets.QLineEdit(self.skill_tab)
        self.sp_value_bar.setObjectName("sp_value_bar")
        self.gridLayout_3.addWidget(self.sp_value_bar, 3, 0, 1, 1)
        self.sp_desc_bar = QtWidgets.QLineEdit(self.skill_tab)
        self.sp_desc_bar.setObjectName("sp_desc_bar")
        self.gridLayout_3.addWidget(self.sp_desc_bar, 3, 1, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/images/tab_icons/skills-perks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.skill_tab, icon3, "")
        self.unlocker_tab = QtWidgets.QWidget()
        self.unlocker_tab.setObjectName("unlocker_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.unlocker_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.selected_list = QtWidgets.QListWidget(self.unlocker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_list.sizePolicy().hasHeightForWidth())
        self.selected_list.setSizePolicy(sizePolicy)
        self.selected_list.setMinimumSize(QtCore.QSize(200, 0))
        self.selected_list.setObjectName("selected_list")
        self.gridLayout_4.addWidget(self.selected_list, 1, 1, 1, 1)
        self.unlock_check_box = QtWidgets.QCheckBox(self.unlocker_tab)
        self.unlock_check_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.unlock_check_box.setObjectName("unlock_check_box")
        self.gridLayout_4.addWidget(self.unlock_check_box, 2, 1, 1, 1)
        self.not_selected_list = QtWidgets.QListWidget(self.unlocker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_selected_list.sizePolicy().hasHeightForWidth())
        self.not_selected_list.setSizePolicy(sizePolicy)
        self.not_selected_list.setMinimumSize(QtCore.QSize(200, 0))
        self.not_selected_list.setObjectName("not_selected_list")
        self.gridLayout_4.addWidget(self.not_selected_list, 1, 0, 1, 1)
        self.unlock_btn = QtWidgets.QPushButton(self.unlocker_tab)
        self.unlock_btn.setObjectName("unlock_btn")
        self.gridLayout_4.addWidget(self.unlock_btn, 2, 0, 1, 1)
        self.not_selected_label = QtWidgets.QLabel(self.unlocker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_selected_label.sizePolicy().hasHeightForWidth())
        self.not_selected_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.not_selected_label.setFont(font)
        self.not_selected_label.setTextFormat(QtCore.Qt.PlainText)
        self.not_selected_label.setAlignment(QtCore.Qt.AlignCenter)
        self.not_selected_label.setOpenExternalLinks(False)
        self.not_selected_label.setObjectName("not_selected_label")
        self.gridLayout_4.addWidget(self.not_selected_label, 0, 0, 1, 1)
        self.selected_label = QtWidgets.QLabel(self.unlocker_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_label.sizePolicy().hasHeightForWidth())
        self.selected_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.selected_label.setFont(font)
        self.selected_label.setTextFormat(QtCore.Qt.PlainText)
        self.selected_label.setAlignment(QtCore.Qt.AlignCenter)
        self.selected_label.setOpenExternalLinks(False)
        self.selected_label.setObjectName("selected_label")
        self.gridLayout_4.addWidget(self.selected_label, 0, 1, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/images/tab_icons/unlocker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.unlocker_tab, icon4, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.settings_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.current_saves_label = QtWidgets.QLabel(self.settings_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.current_saves_label.setFont(font)
        self.current_saves_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_saves_label.setObjectName("current_saves_label")
        self.gridLayout_5.addWidget(self.current_saves_label, 0, 0, 1, 2)
        self.backups_label = QtWidgets.QLabel(self.settings_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.backups_label.setFont(font)
        self.backups_label.setAlignment(QtCore.Qt.AlignCenter)
        self.backups_label.setObjectName("backups_label")
        self.gridLayout_5.addWidget(self.backups_label, 0, 2, 1, 1)
        self.logs_label = QtWidgets.QLabel(self.settings_tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.logs_label.setFont(font)
        self.logs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.logs_label.setObjectName("logs_label")
        self.gridLayout_5.addWidget(self.logs_label, 0, 3, 1, 2)
        self.saves_list = QtWidgets.QListWidget(self.settings_tab)
        self.saves_list.setObjectName("saves_list")
        self.gridLayout_5.addWidget(self.saves_list, 1, 0, 1, 2)
        self.backups_list = QtWidgets.QListWidget(self.settings_tab)
        self.backups_list.setObjectName("backups_list")
        self.gridLayout_5.addWidget(self.backups_list, 1, 2, 1, 1)
        self.logs_list = QtWidgets.QListWidget(self.settings_tab)
        self.logs_list.setObjectName("logs_list")
        self.gridLayout_5.addWidget(self.logs_list, 1, 3, 1, 2)
        self.backup_btn = QtWidgets.QPushButton(self.settings_tab)
        self.backup_btn.setObjectName("backup_btn")
        self.gridLayout_5.addWidget(self.backup_btn, 2, 0, 1, 2)
        self.load_backup_btn = QtWidgets.QPushButton(self.settings_tab)
        self.load_backup_btn.setObjectName("load_backup_btn")
        self.gridLayout_5.addWidget(self.load_backup_btn, 2, 2, 1, 1)
        self.current_save_label = QtWidgets.QLabel(self.settings_tab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.current_save_label.setFont(font)
        self.current_save_label.setAlignment(QtCore.Qt.AlignCenter)
        self.current_save_label.setObjectName("current_save_label")
        self.gridLayout_5.addWidget(self.current_save_label, 2, 3, 1, 1)
        self.current_save_bar = QtWidgets.QLineEdit(self.settings_tab)
        self.current_save_bar.setObjectName("current_save_bar")
        self.gridLayout_5.addWidget(self.current_save_bar, 2, 4, 1, 1)
        self.open_save_btn = QtWidgets.QPushButton(self.settings_tab)
        self.open_save_btn.setObjectName("open_save_btn")
        self.gridLayout_5.addWidget(self.open_save_btn, 3, 0, 1, 1)
        self.select_save_btn = QtWidgets.QPushButton(self.settings_tab)
        self.select_save_btn.setToolTipDuration(4)
        self.select_save_btn.setObjectName("select_save_btn")
        self.gridLayout_5.addWidget(self.select_save_btn, 3, 1, 1, 1)
        self.check_update_btn = QtWidgets.QPushButton(self.settings_tab)
        self.check_update_btn.setObjectName("check_update_btn")
        self.gridLayout_5.addWidget(self.check_update_btn, 3, 2, 1, 1)
        self.export_logs_btn = QtWidgets.QPushButton(self.settings_tab)
        self.export_logs_btn.setObjectName("export_logs_btn")
        self.gridLayout_5.addWidget(self.export_logs_btn, 3, 3, 1, 2)
        self.auto_update_check_box = QtWidgets.QCheckBox(self.settings_tab)
        self.auto_update_check_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.auto_update_check_box.setObjectName("auto_update_check_box")
        self.gridLayout_5.addWidget(self.auto_update_check_box, 4, 0, 1, 5)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/images/tab_icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.settings_tab, icon5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._save = {}
        self.logit_log = {}
        self.current_var = ''
        self.cvt = ''
        self.stats_details = ['name', 'level', 'baseStrength','baseEndurance', 'baseAgility', 'basePerception', 'magicPoints',
                             'baseMagic', 'baseCharisma', 'manaReserve', 'currentHealth', 'currentStamina', 'focus', 'fortune', 'skillPoints', 'perkPoints', 'willpower']
        self.femininity = ["MASCULINE","UNMASCULINE","ANDROGYNOUS","EFFEMINATE", "GIRLY", "FEMININE", "BITCH", "MALE", "FEMALE"]
        self.breast = ["LITTLE", "FLAT", "HANDFUL", "FUN"]
        self.bootyliciousness = ["Bubble", "Round", "Fat"]
        self.lipFullness = ["Thin", "Pouty", "Beestung", "Full"]
        self.eyeColor = ["Blue", "Teal", "Pink", "Golden"]
        self.hairColor = ["Black", "Brown", "Red", "Blonde", "Pink", "Mix"]
        self.race = ["Lowlander", "Highlander", "Mountainman", "Elfblood", "Orcblood"]
        self.jobCLASS = ["WARRIOR", "PALADIN", "THIEF", "RANGER", "MAGE", "ENCHANTRESS", "BITCH", "MARE", "BUNNY", "QUEEN", "PROSTITUTE", "SCHOOLGIRL", "LEWD_SCHOOLGIRL"]
        self.settings = util.load_data('resources/data/appdata/data.json')
        self.ticks = self.settings['ticks']
        self.obj_ticks = {self.auto_update_check_box: 'auto-update', self.unlock_check_box: 'unlock-update'}
        
        self.load_tick_states()
        self.locate_saves(True)
        self.load_save_data()
        self.load_unlocker_state()
        self.load_current_save(self.settings['misc']['current-save'])
        self.data_profile_handler(7)
        self.display_skills()
        self.display_perks()
        self.display_stats()

        if self.settings['ticks']['unlock-update']:
            self.run_unlocker()
        
        self.auto_update_check_box.clicked.connect(lambda param: self.tick_box(self.auto_update_check_box))
        self.unlock_check_box.clicked.connect(lambda param: self.tick_box(self.unlock_check_box))
        self.backup_btn.clicked.connect(self.backup_save)
        self.load_backup_btn.clicked.connect(self.load_backup)
        self.saves_list.itemDoubleClicked.connect(self.set_current_save)
        self.select_save_btn.clicked.connect(self.set_current_save)
        self.open_save_btn.clicked.connect(lambda param: self.locate_saves(False))
        self.selected_list.clicked.connect(lambda param: self.unlocker_selector(1))
        self.not_selected_list.clicked.connect(lambda param: self.unlocker_selector(0))
        self.unlock_btn.clicked.connect(self.run_unlocker)
        self.export_logs_btn.clicked.connect(self.export_logit)
        self.skill_search_bar.textChanged.connect(self.display_skills)
        self.perk_search_bar.textChanged.connect(self.display_perks)
        self.detail_search_bar.textChanged.connect(self.display_stats)
        self.skill_list.itemClicked.connect(lambda param: self.list_item_handler(self.skill_list, self.sp_value_bar,'s'))
        self.perk_list.itemClicked.connect(lambda param: self.list_item_handler(self.perk_list, self.sp_value_bar,'p'))
        self.player_detail_list.itemClicked.connect(lambda param: self.list_item_handler(self.player_detail_list, self.player_value_bar, 'c'))
        self.sp_value_bar.textChanged.connect(lambda param: self.save_current_var(self.sp_value_bar))
        self.player_value_bar.textChanged.connect(lambda param: self.save_current_var(self.player_value_bar))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Save Editor V6"))
        self.all_item_label.setText(_translate("MainWindow", "All Item(s)"))
        self.player_item_label.setText(_translate("MainWindow", "Players Item(s)"))
        self.item_settings_label.setText(_translate("MainWindow", "Item Settings"))
        self.item_filter_bar.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.grip_label.setText(_translate("MainWindow", "Grip"))
        self.mag_label.setText(_translate("MainWindow", "Magnitude"))
        self.dur_label.setText(_translate("MainWindow", "Durability"))
        self.misc_items_label.setText(_translate("MainWindow", "Misc Items"))
        self.gold_label.setText(_translate("MainWindow", "Gold"))
        self.food_label.setText(_translate("MainWindow", "Food"))
        self.crystal_label.setText(_translate("MainWindow", "Crystals"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.items_tab), _translate("MainWindow", "Items"))
        self.stats_label.setText(_translate("MainWindow", "Stats/Details"))
        self.appearance_label.setText(_translate("MainWindow", "Appearance"))
        self.race_label.setText(_translate("MainWindow", "Race"))
        self.hair_label.setText(_translate("MainWindow", "Hair Color"))
        self.lip_label.setText(_translate("MainWindow", "Lip Type"))
        self.detail_search_bar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.penis_label.setText(_translate("MainWindow", "Penis Size"))
        self.fem_label.setText(_translate("MainWindow", "Femininity"))
        self.eye_label.setText(_translate("MainWindow", "Eye Color"))
        self.player_value_bar.setPlaceholderText(_translate("MainWindow", "Value"))
        self.butt_label.setText(_translate("MainWindow", "Butt Size"))
        self.job_label.setText(_translate("MainWindow", "Job:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.char_tab), _translate("MainWindow", "Character"))
        self.skills_label.setText(_translate("MainWindow", "Skills"))
        self.perks_label.setText(_translate("MainWindow", "Perks"))
        self.skill_search_bar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.perk_search_bar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.sp_value_bar.setPlaceholderText(_translate("MainWindow", "Value"))
        self.sp_desc_bar.setPlaceholderText(_translate("MainWindow", "Short Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.skill_tab), _translate("MainWindow", "Skills/Perks"))
        self.unlock_check_box.setText(_translate("MainWindow", "Auto Unlock Selected on Update"))
        self.unlock_btn.setText(_translate("MainWindow", "Unlock Selected"))
        self.not_selected_label.setText(_translate("MainWindow", "Not Selected"))
        self.selected_label.setText(_translate("MainWindow", "Selected"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.unlocker_tab), _translate("MainWindow", "Unlocker"))
        self.current_saves_label.setText(_translate("MainWindow", "Current Saves"))
        self.backups_label.setText(_translate("MainWindow", "Back-ups"))
        self.logs_label.setText(_translate("MainWindow", "Logs"))
        self.backup_btn.setText(_translate("MainWindow", "Backup"))
        self.load_backup_btn.setText(_translate("MainWindow", "Load Backup"))
        self.current_save_label.setText(_translate("MainWindow", "Current Save:"))
        self.open_save_btn.setText(_translate("MainWindow", "Open"))
        self.select_save_btn.setToolTip(_translate("MainWindow", "Or double click a list item"))
        self.select_save_btn.setText(_translate("MainWindow", "Select"))
        self.check_update_btn.setText(_translate("MainWindow", "Check for Updates"))
        self.export_logs_btn.setText(_translate("MainWindow", "Export Logs"))
        self.auto_update_check_box.setText(_translate("MainWindow", "Auto-Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings"))

    def logit(self, event, details):
        try:
            self.logs_list.addItem(f'{event} : {details}')
            self.logs_list.scrollToBottom()
            self.logit_log[str(datetime.now())] = {event : details}
        except Exception as error:
            util.log_error(error)
    
    def export_logit(self):
        ts = str(datetime.now()).split(' ')[0]
        name = f'logit_{ts}_{ord(os.urandom(1))}.json'
        util.save_data(self.logit_log, f'resources/logs/{name}')
        util.show_user('Logit.', f'Action Log has been successfully saved!\n\nIt can be found at:\nresources/logs/{name}')
    
    def display_skills(self):
        try:
            self.display_list(self.skill_list, self._save['player']['skills'], search=self.skill_search_bar.text().upper(), display_value=True)
        except Exception as error:
            util.log_error(error)

    def display_perks(self):
        try:
            self.display_list(self.perk_list, self._save['player']['perks'], search=self.perk_search_bar.text().upper(), display_value=True)
        except Exception as error:
            util.log_error(error)
    
    def display_stats(self):
        try:
            self.player_detail_list.clear()
            for d in self.stats_details:
                if self.detail_search_bar.text() in d:
                    self.player_detail_list.addItem(f"{d} : {self._save['player'][d]}")
        except Exception as error:
            util.log_error(error)
    
    def add_combo_item(self, obj, data):
        try:
            obj.clear()
            for d in data:
                obj.addItem(d)
        except Exception as error:
            util.log_error(error)
        
    def save_current_var(self, obj): # type conversion
        try:
            self.val = obj.text()
            try:
                if self.cvt == 's':
                    self.typ = type(self._save['player']['skills'][self.current_var])

                    self._save['player']['skills'][self.current_var] = self.typ(self.val)

                if self.cvt == 'p':
                    self.typ = type(self._save['player']['perks'][self.current_var])

                    self._save['player']['perks'][self.current_var] = self.typ(self.val)

                if self.cvt == 'c':
                    self.typ = type(self._save['player'][self.current_var])

                    self._save['player'][self.current_var] = self.typ(self.val)
            except Exception as error:
                if type(error) == ValueError:
                    pass
                else:
                    util.log_error(error)

            self.logit('value-edit', f'{self.current_var} set to {self.val}')
            self.save_save()
        except Exception as error:
            util.log_error(error)
        
    def list_item_handler(self, obj, obj2, sp, split=' : '):
        try:
            self.items = obj.currentItem().text().split(' : ')
            self.current_var = self.items[0]
            obj2.setText(self.items[-1])
            self.data_profile_handler(6)
            self.cvt = sp
        except Exception as error:
            util.log_error(error)

    def unlocker_selector(self, n):
        try:
            if n == 1:
                self.settings['unlocker'][self.selected_list.currentItem().text()] = False
            else:
                self.settings['unlocker'][self.not_selected_list.currentItem().text()] = True

            util.save_data(self.settings, "resources/data/appdata/data.json")
            self.load_unlocker_state()
        except Exception as error:
            util.log_error(error)

    def set_current_save(self):
        try:
            txt = self.saves_list.currentItem().text()
            d = os.path.join(self.settings['misc']['toa-data-path'] , txt)
            self.settings['misc']['current-save'] = d
            self.current_save_bar.setText(txt)
            self.load_current_save(d)
            self.logit('set-save', d)
        except Exception as error:
            if type(error) == AttributeError:
                pass
            else:
                util.log_error(error)
        
        util.save_data(self.settings, "resources/data/appdata/data.json")
    
    def load_current_save(self, path):
        self._save = util.load_data(path)
    
    def save_save(self):
        util.save_data(self._save, self.settings['misc']['current-save'])
        self.logit('saved', self.settings['misc']['current-save'])

    def load_save_data(self):
        self.display_list(self.saves_list, self.get_path_list(self.settings['misc']['toa-data-path']))
        self.display_list(self.backups_list, self.get_path_list('resources/data/backups'))
        self.current_save_bar.setText(self.settings['misc']['current-save'])
    
    def backup_save(self):
        try:
            src = os.path.join(self.settings['misc']['toa-data-path'], self.saves_list.currentItem().text())
            dest = os.path.join('resources/data/backups', self.saves_list.currentItem().text())
            data = util.load_data(src)
            util.save_data(data,dest)
            util.show_user("BackUps.", "Backup completed succesfully!")
            self.logit('backed-up', self.saves_list.currentItem().text())
        except Exception as error:
            if type(error) == AttributeError:
                pass
            else:
                util.log_error(error)
        
        self.load_save_data()
    
    def load_backup(self):
        try:
            src = os.path.join('resources/data/backups', self.backups_list.currentItem().text())
            dest = os.path.join(self.settings['misc']['toa-data-path'], self.backups_list.currentItem().text())
            data = util.load_data(src)
            util.save_data(data,dest)
            util.show_user("BackUps.", "Loaded backup succesfully!")
            self.logit('loaded-backup', self.backups_list.currentItem().text())
        except Exception as error:
            if type(error) == AttributeError:
                pass
            else:
                util.log_error(error)

        self.load_save_data()   

    def load_unlocker_state(self):
        unlocker = self.settings['unlocker']
        t = []
        f = []
        for d in unlocker:
            if unlocker[d]:
                t.append(d)
            else:
                f.append(d)
        
        self.display_list(self.not_selected_list, f)
        self.display_list(self.selected_list, t)
        
    def load_tick_states(self):
        try:
            for t in self.obj_ticks:
                a = self.ticks[self.obj_ticks[t]]
                if a == True:
                    s = 2
                else:
                    s = 0
                t.setCheckState(s)
        except Exception as error:
            util.log_error(error)

    def tick_box(self, box):
        try:
            if box.checkState() == 0:
                state = False
            else:
                state = True

            self.ticks[ self.obj_ticks[box] ] = state

        except Exception as error:
            util.log_error(error)

        util.save_data(self.settings, "resources/data/appdata/data.json")
    
    def display_list(self, obj, data, search='', display_value=False):
        obj.clear()
        try:
            for d in data:
                if search in d:
                    if display_value:
                        obj.addItem(f"{d} : {data[d]}")
                    else:
                        obj.addItem(d)
        except Exception as error:
            util.log_error(error)

    
    def get_path_list(self, path):
        try:
            r = []
            for d in os.listdir(path):
                if 'save' in d:
                    r.append(d)
                else:
                    pass
            return r
        except Exception as error:
            util.log_error(error)

    def locate_saves(self, auto):
        try:
            expected_path = os.path.join(os.getcwd(), '.toa-data')
            if os.path.isdir(expected_path) and auto:
                self.settings['misc']['toa-data-path'] = expected_path
            else:
                if auto:
                    util.show_user("File path.", "You currently don't have your .toa-data folder path set, please select the folder in which your game files are located.")

                dirname = QtWidgets.QFileDialog.getExistingDirectory(None, "Select .toa-data folder.")
                self.settings['misc']['toa-data-path'] = dirname
        except Exception as error:
            util.log_error(error)
        
        util.save_data(self.settings, "resources/data/appdata/data.json")
    
    def run_unlocker(self):
        for d in self.settings['unlocker']:
            if self.settings['unlocker'][d]:
                self.data_profile_handler(self.settings['misc'][d])
                self.logit('unlocked', d)
        
    def data_profile_handler(self, task):
        try:
            prof_path = os.path.join(self.settings['misc']['toa-data-path'], 'profile.json')
            self.profile = util.load_data(prof_path)
            if task == 1: # achievements
                self.profile['achievements'] = self.settings['achievements']

            elif task == 2: # events
                self.profile['events'] = self.settings['events']
                self.profile['enemyKnowledge'] = self.settings['enemyKnowledge']
            
            elif task == 3: # cgi
                self.profile['cgSeen'] = self.settings['cgSeen']
                self.profile['animatedCgSeen'] = self.settings['animatedCgSeen']
            
            elif task == 4: # max skills
                self._save['player']['skills'] = self.settings['skills-max']
            
            elif task == 5: # max perk
                self._save['player']['perks'] = self.settings['perks-max']
                self.data_profile_handler(7)

            elif task == 6: # display description
                try:
                    self.sp_desc_bar.setText(str(self.settings['descriptions'][self.current_var]))
                except:
                    self.sp_desc_bar.setText("No description.")

            elif task == 7:
                for self.key in self.settings['skills'].keys():
                    if self.key in self._save['player']['skills'].keys():
                        pass
                    else:
                        self._save['player']['skills'][self.key] = 0

                for self.key in self.settings['perks'].keys():
                    if self.key in self._save['player']['perks'].keys():
                        pass
                    else:
                        self._save['player']['perks'][self.key] = 0
                
                if not 'magicPoints' in self._save['player']:
                    self._save['player']['magicPoints'] = 0
            
            else:
                print("No known task was requested.\n")
            
            self.save_save()
            util.save_data(self.profile, prof_path)
            self.load_current_save(self.settings['misc']['current-save'])
            
        except Exception as error:
            util.log_error(error)
            

if __name__ == "__main__":
    util = BackEnd()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
