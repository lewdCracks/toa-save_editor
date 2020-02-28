from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from bs4 import BeautifulSoup as BS


class Updater(object):
    def __init__(self):
        self._app_version = 5
        self._data_version = 4

        self.root = Tk()
        self.root.withdraw()
        self.update()
        self.root.destroy()
    
    def get_online_data(self):
        self.url = "https://raw.githubusercontent.com/lewdCracks/toa-save_editor/master/json_data/data.json"
        self.req = requests.get(self.url)
        if self.req.status_code == 200 and self.req.url == self.url:
            self.json_data = json.loads(self.req.content)
            self.data_version = float(self.json_data['version_info']['data_version'])
            self.app_version = float(self.json_data['version_info']['app_version'])
            self.app_name = self.json_data['version_info']['app_name']
            self.app_link = self.json_data['version_info']['app_link']
            return True
        else:
            return False
    
    def get_download_url(self, url):
        self.req = requests.get(url)
        if self.req.status_code == 200 and self.req.url == url:
            self.soup = BS(self.req.content, features='html.parser')
            self.download_url = self.soup.find(class_='input').get('href')
            return True, self.download_url
        else:
            return False, None

    def update(self):
        self.resp = self.get_online_data()
        if self.resp:
            if self.app_version > self._app_version:
                self.choice = tkinter.messagebox.askquestion("Auto-Update", f"Your save editor is out of date would you like to request an update?.\n{self._app_version} < {self.app_version}")
                if self.choice == 'yes':
                    self.resp, self.dl_url = self.get_download_url(self.app_link)
                    if self.resp:
                        self.req = requests.get(self.dl_url)
                        if self.req.status_code == 200 and self.req.url == self.dl_url:
                            with open(self.app_name, 'wb+') as self.data:
                                self.data.write(self.req.content) 
                                self.data.close()
                            self.choice = tkinter.messagebox.showinfo("Auto-Update", f"Update complete!\nYou can delete the old version of your save editor whenever you want.")
                            self.newapp_path = os.path.join(os.getcwd(), self.app_name)
                            subprocess.Popen(self.newapp_path)
                            sys.exit(0)

                        else:
                            tkinter.messagebox.showerror("Link Request Error.", f"Media fire redirected therefore the download link could not be parsed.\n.{self.dl_url} != {self.req.url}")         
                    else:
                        tkinter.messagebox.showerror("Link Request Error.", f"Media fire redirected therefore the download link could not be parsed.\n.{self.dl_url} != {self.req.url}")         
                        self.root.destroy()
                else:
                    pass
            else:
                print('Editor is up to date.')

            if self.data_version > self._data_version:             
                self.choice = tkinter.messagebox.askquestion("Auto-updater.", f"Your json data is out of date would you like to update it?.\nVersions: {self._data_version} < {self.data_version}")
                if self.choice == 'yes':
                    json.dump(self.json_data, open('data.json', 'w+'), indent=4)
                else:
                    pass
            else:
                print('JSON data is up to data.')

        else:
            tkinter.messagebox.showerror("Version Request Error.", "Github redirected therefore version data could not be parsed.\nAnother request will be made on the next launch.")
            self.root.destroy()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 627)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(37, 37, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bar.setObjectName("search_bar")
        self.gridLayout.addWidget(self.search_bar, 0, 0, 1, 2)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 0, 2, 1, 1)
        self.max_skill_btn = QtWidgets.QPushButton(self.centralwidget)
        self.max_skill_btn.setObjectName("max_skill_btn")
        self.gridLayout.addWidget(self.max_skill_btn, 0, 3, 1, 1)
        self.unlock_cgi_btn = QtWidgets.QPushButton(self.centralwidget)
        self.unlock_cgi_btn.setObjectName("unlock_cgi_btn")
        self.gridLayout.addWidget(self.unlock_cgi_btn, 0, 4, 1, 1)
        self.list_values = QtWidgets.QListWidget(self.centralwidget)
        self.list_values.setObjectName("list_values")
        self.gridLayout.addWidget(self.list_values, 1, 0, 2, 2)
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setObjectName("refresh_btn")
        self.gridLayout.addWidget(self.refresh_btn, 1, 2, 1, 1)
        self.max_perks_btn = QtWidgets.QPushButton(self.centralwidget)
        self.max_perks_btn.setObjectName("max_perks_btn")
        self.gridLayout.addWidget(self.max_perks_btn, 1, 3, 1, 1)
        self.unlock_achievements_btn = QtWidgets.QPushButton(self.centralwidget)
        self.unlock_achievements_btn.setObjectName("unlock_achievements_btn")
        self.gridLayout.addWidget(self.unlock_achievements_btn, 1, 4, 1, 1)
        self.description_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description_box.setDocumentTitle("")
        self.description_box.setPlainText("")
        self.description_box.setObjectName("description_box")
        self.gridLayout.addWidget(self.description_box, 2, 2, 1, 3)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 3, 0, 1, 1)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")
        self.gridLayout.addWidget(self.open_btn, 3, 1, 1, 1)
        self.value_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.value_bar.setObjectName("value_bar")
        self.gridLayout.addWidget(self.value_bar, 3, 2, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # buttons / bars / items
        self.open_btn.clicked.connect(self.open_save)
        self.search_bar.textChanged.connect(self.display_variables)
        self.list_values.itemClicked.connect(lambda param: self.item_handler(False))
        self.value_bar.textChanged.connect(self.update_variable)
        self.back_btn.clicked.connect(lambda param: self.update_path(True))
        self.save_btn.clicked.connect(self.save_dict_to_file)
        self.refresh_btn.clicked.connect(self.refresh_save)

        self.unlock_achievements_btn.clicked.connect(lambda param: self.data_profile_handler(1))
        self.unlock_cgi_btn.clicked.connect(lambda param: self.data_profile_handler(2))
        self.max_skill_btn.clicked.connect(lambda param: self.data_profile_handler(3))
        self.max_perks_btn.clicked.connect(lambda param: self.data_profile_handler(4))

        # vars
        self.save = ''

        self.vars_ = {"save_location" : None, "profile_location" : None, "data_location" : None}
        self.val_handler = {}
        self.task_descriptors = {1 : 'Achievement Unlocker.', 2: "CGI & Event Unlocker.", 3 : "Max all skills.", 4 : "Max all perks.", 5 : "Variable Descriptions.", 6 : "Add missing variables."}
        
        self.path = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "save_editor_v5"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.save_btn.setText(_translate("MainWindow", "Save Variables"))
        self.max_skill_btn.setText(_translate("MainWindow", "Max Skills"))
        self.unlock_cgi_btn.setText(_translate("MainWindow", "CGI and Events"))
        self.refresh_btn.setText(_translate("MainWindow", "Refresh Save"))
        self.max_perks_btn.setText(_translate("MainWindow", "Max Perks"))
        self.unlock_achievements_btn.setText(_translate("MainWindow", "Achievements"))
        self.description_box.setPlaceholderText(_translate("MainWindow", "Variable Descriptions."))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.open_btn.setText(_translate("MainWindow", "Open Save"))
        self.value_bar.setPlaceholderText(_translate("MainWindow", "value:"))

    def open_save(self):
        try:
            self.savefile, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Save File", "", ".json Files (*.json)")
            self.profile = self.savefile.split('/')[:-1]
            self.profile.append('profile.json')

            self.vars_["save_location"] = self.savefile
            self.vars_["profile_location"] = '/'.join(self.profile)
            self.found = self.get_data_location()


            self.save = json.load(open(self.savefile))
            print(f"Save file has been successfully loaded.\nCurrent Save: {self.savefile}")
            self.path.append(self.save)

            if self.found:
                self.load_data_profile()
                self.data_profile_handler(6)
            else:
                pass

            self.display_variables()

        except Exception as error:
            print("Unknow error occured in 'open_save'.\nError:", error)
    
    def refresh_save(self):
        try:
            self.save = json.load(open(self.vars_["save_location"]))
            self.path.clear()

            self.path.append(self.save)

            self.search_bar.clear()
            self.value_bar.clear()
            self.display_variables()
        except Exception as error:
            os.system('cls')
            print(f"An error occured while trying to refresh save.\n\nError: {error}")

    def save_dict_to_file(self):
        try:
            json.dump(self.save, open(self.vars_['save_location'], "w+"), indent=4, skipkeys=True)
            print(f"Saved Changes to: {self.vars_['save_location']}\n")
        except Exception as error:
            os.system('cls')
            print(f"No save has been selected, unable to save variables.\n\nError: {error}")

    def profile_dict_to_file(self):
        try:
            json.dump(self.vars_['profile'], open(self.vars_['profile_location'], "w+"), indent=4, skipkeys=True)
            print(f"Saved Changes to: {self.vars_['profile_location']}\n")
        except Exception as error:
            print(f"No save has been selected, unable to save variables.\n\nError: {error}")

    def load_data_profile(self):
        try:
            print("Loading 'data.json'...")
            self.vars_['data'] = json.load(open(self.vars_['data_location']))
            print("Loading 'profile.json'...\n")
            self.vars_['profile'] = json.load(open(self.vars_['profile_location']))
            print("Successfully loaded 'data.json' & 'profile.json'!")
        except Exception as error:
            print("Json loader error.\n\nError:",error)
     
    def get_data_location(self): # method to parse 'data.json' location - if it is unable to find it, it will then ask the user for its location
        self.expected_location = os.path.join(os.getcwd(), "data.json")
        os.system("cls")

        if os.path.isfile(self.expected_location):
            self.vars_["data_location"] = self.expected_location
            print("Location of 'data.json' was found.")
            return True
            
        else:
            try:
                print("Could not parse to location of 'data.json' please select it's location.\n")
                self.path_to, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Please select the location of data.json", "", ".json Files (*.json)")

                if os.path.isfile(self.path_to) and 'data.json' in self.path_to:
                    self.vars_["data_location"] = self.path_to
                    print("Selected location of 'data.json' is valid.")
                    return True

                else:
                    self.vars_["data_location"] = None
                    print("No valid location was selected for 'data.json', some features may be unavailable.")
                    return False

            except Exception as error: 
                print('Unkown Error Occured: 1\n\n', error)
                return False
    
    def update_variable(self):
        try:
            os.system("cls")
            self.convert_to = type(self.path[-1][self.vars_['current_var']]) # gets variable type so I can cast it later

            try:
                os.system("cls")
                self.new_val = self.convert_to(self.value_bar.text())

                self.path[-1][self.vars_['current_var']] = self.new_val # sets the current var to the casted value bar text
                self.display_variables()
                print(f"[Updated]\n\nVariable '{self.vars_['current_var']}': {self.new_val}.")

            except Exception as error:
                os.system("cls")
                print(f"Couldn't edit variable!\n\nMost likely wrong variable type - expected: {self.convert_to}.\n\nError : {error}\n")

        except Exception as error:
            os.system("cls")
            print(f"Couldn't edit variable!\n\nMost likely no variable selected.\n\nError : {error}\n")
    
    def update_path(self, back):
        if not back:
            if self.val_handler[self.vars_['current_item'] + "_type"] == dict:
                self.path.append(self.path[-1][self.vars_['current_item']])
                self.display_variables()

            elif self.val_handler[self.vars_['current_item'] + "_type"] == list:
                os.system('cls')
                print("This variable is most likely a list meaning it can't be used to update the current path.")
                self.display_variables()

            else:
                print("Passed")

        elif len(self.path) > 1:
            self.path.remove(self.path[-1])
            self.display_variables()
        else:
            os.system('cls')
            print("Can't go back any futher.")

    def item_handler(self, back):
        self.item = self.list_values.currentItem().text().split(' :')[0]
        self.search_bar.clear()

        if self.val_handler[self.item]: # displays item & saves the item to dict
            self.vars_['current_var'] = self.item
            self.display_var = self.path[-1][self.item]
            self.value_bar.setText(str(self.display_var))
            self.data_profile_handler(5)

        elif not self.val_handler[self.item]: # saves the current item then goes to update_path for better handling
            self.vars_['current_item'] = self.item
            self.update_path(False)
        else:
            print("Unknow in item_handler.")

    
    def display_variables(self):
        self.val_handler.clear() # clears old values
        self.list_values.clear() # updates the list

        try:
            for self.value in self.path[-1].keys():
                if self.search_bar.text() in self.value:
                    if type(self.path[-1][self.value]) == str or type(self.path[-1][self.value]) == int or type(self.path[-1][self.value]) == bool: # checks the dict value types
                        self.list_values.addItem(f"{self.value} : {self.path[-1][self.value]}") 
                        self.val_handler[self.value] = True # if they aren't dict or list they are Editable

                    elif type(self.path[-1][self.value]) == list:
                        self.list_values.addItem(f"{self.value} : >")
                        self.val_handler[self.value] = False # if they are dict or list they are Non-Editable
                        self.val_handler[self.value + "_type"] = list # saves value type

                    elif type(self.path[-1][self.value]) == dict: # same as list
                        self.list_values.addItem(f"{self.value} : >")
                        self.val_handler[self.value] = False
                        self.val_handler[self.value + "_type"] = dict

                else:
                    pass

        except Exception as error:
            os.system('cls')
            print(f"Most likey no save file has been selected meaning there is nothing to search.\n\nError: {error}")
    
    def data_profile_handler(self, task):
        if self.vars_['data_location'] == None:
            os.system('cls')
            print(f"Could not complete task.\nTask description: {self.task_descriptors[task]}\nReason: missing 'data.json'\n")
        else:
            # re-assign for easy of use
            self.data = self.vars_['data']
            self.profile = self.vars_['profile']

            if task == 1: # achievements
                self.profile['achievements'] = self.data['achievements']
                self.profile_dict_to_file()

            elif task == 2: # events & cgi
                self.profile['events'] = self.data['events']
                self.profile['enemyKnowledge'] = self.data['enemyKnowledge']
                self.profile['cgSeen'] = self.data['cgSeen']
                self.profile['animatedCgSeen'] = self.data['animatedCgSeen']
                self.profile_dict_to_file()
            
            elif task == 3: # max skills
                self.save['player']['skills'] = self.data['skills-max']
                self.save_dict_to_file()
            
            elif task == 4: # max perk
                self.save['player']['perks'] = self.data['perks-max']
                self.save_dict_to_file()
            
            elif task == 5: # display description
                try:
                    self.description_box.setPlainText(str(self.data['descriptions'][self.vars_['current_var']]))
                except:
                    self.description_box.setPlainText("No description.")

            elif task == 6:
                print('\nAdding empty variables...')
                for self.key in self.data['skills'].keys():
                    if self.key in self.save['player']['skills'].keys():
                        pass
                    else:
                        self.save['player']['skills'][self.key] = 0

                for self.key in self.data['perks'].keys():
                    if self.key in self.save['player']['perks'].keys():
                        pass
                    else:
                        self.save['player']['perks'][self.key] = 0
                print("Successfully added variables!\n")
                self.save_dict_to_file()
            
            else:
                print("No known task was requested.\n")
            

if __name__ == "__main__":
    import os, time, sys, json, requests
    import tkinter.messagebox
    import subprocess
    Updater()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
