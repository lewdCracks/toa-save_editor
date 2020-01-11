from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 704)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 112, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 112, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 112, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(112, 112, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 11, 3, 1, 1)

        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setObjectName("open_btn")
        self.gridLayout.addWidget(self.open_btn, 11, 2, 1, 1)

        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 11, 1, 1, 1)

        self.value_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.value_bar.setObjectName("value_bar")
        self.gridLayout.addWidget(self.value_bar, 11, 6, 1, 1)

        self.description_box = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description_box.setObjectName("description_box")
        self.gridLayout.addWidget(self.description_box, 9, 4, 1, 3)

        self.unlock_achievements_btn = QtWidgets.QPushButton(self.centralwidget)
        self.unlock_achievements_btn.setObjectName("unlock_achievements_btn")
        self.gridLayout.addWidget(self.unlock_achievements_btn, 6, 6, 1, 1)

        self.search_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.search_bar.setObjectName("search_bar")
        self.gridLayout.addWidget(self.search_bar, 6, 1, 1, 3)

        self.unlock_encounters_btn = QtWidgets.QPushButton(self.centralwidget)
        self.unlock_encounters_btn.setObjectName("unlock_encounters_btn")
        self.gridLayout.addWidget(self.unlock_encounters_btn, 6, 5, 1, 1)

        self.path_label = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.path_label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.path_label.setFont(font)
        self.path_label.setObjectName("path_label")
        self.gridLayout.addWidget(self.path_label, 4, 1, 1, 1)
        self.variable_label = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.variable_label.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.variable_label.setFont(font)
        self.variable_label.setObjectName("variable_label")
        self.gridLayout.addWidget(self.variable_label, 4, 4, 1, 1)

        self.max_skill_btn = QtWidgets.QPushButton(self.centralwidget)
        self.max_skill_btn.setObjectName("max_skill_btn")
        self.gridLayout.addWidget(self.max_skill_btn, 6, 4, 1, 1)

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setObjectName("reset_btn")
        self.gridLayout.addWidget(self.reset_btn, 11, 5, 1, 1)

        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout.addWidget(self.add_btn, 11, 4, 1, 1)

        self.list_values = QtWidgets.QListWidget(self.centralwidget)
        self.list_values.setObjectName("list_values")
        self.gridLayout.addWidget(self.list_values, 9, 1, 2, 3)

        self.tag_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.tag_bar.setObjectName("tag_bar")
        self.gridLayout.addWidget(self.tag_bar, 10, 4, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # buttons / bars / items
        self.value_bar.returnPressed.connect(self.update_variable)
        self.max_skill_btn.clicked.connect(self.max_skills)
        self.unlock_achievements_btn.clicked.connect(self.unlock_achievements)
        self.unlock_encounters_btn.clicked.connect(self.unlock_events)
        self.reset_btn.clicked.connect(self.max_perks)
        self.add_btn.clicked.connect(self.add_empty)
        self.open_btn.clicked.connect(self.open_save)
        self.back_btn.clicked.connect(lambda param: self.update_path(True))
        self.save_btn.clicked.connect(self.save_dict_to_file)
        self.value_bar.textChanged.connect(self.update_variable)
        self.search_bar.textChanged.connect(lambda *param: self.display_variables(self.last_display, 2))
        self.list_values.itemDoubleClicked.connect(lambda param: self.update_path(False))

        # tags = dictionary path, which is added to search index but saved separately
        self.save = ''
        self.save_file = ''
        self.last_display = -1

        self.profile = []
        self.path = []
        self.current_var = ['']

        self.desciptions = {}
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Save Editor"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.open_btn.setText(_translate("MainWindow", "Open Save"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.value_bar.setPlaceholderText(_translate("MainWindow", "value:"))
        self.description_box.setPlaceholderText(_translate("MainWindow", "As you type/edit it will auto-save the description..."))
        self.unlock_achievements_btn.setText(_translate("MainWindow", "Unlock Achievements"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", "Search"))
        self.unlock_encounters_btn.setText(_translate("MainWindow", "Unlock Events"))
        self.path_label.setText(_translate("MainWindow", "PATHS: "))
        self.variable_label.setText(_translate("MainWindow", "VARIABLE EDITOR: "))
        self.max_skill_btn.setText(_translate("MainWindow", "Max Skills"))
        self.reset_btn.setText(_translate("MainWindow", "Max Perks"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.tag_bar.setPlaceholderText(_translate("MainWindow", "Tags - separate with commas ~"))
    
    def open_save(self):
        try:
            self.savefile, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Save File", "", ".json Files (*.json)")
            self.playerfile = self.savefile.split('/')[:-1] 
            self.playerfile.append('profile.json')
            self.save_file = self.savefile

            self.profile.append('/'.join(self.playerfile))
            
            self.save = json.load(open(self.savefile))
            self.path.append(self.save)

            self.display_variables(1, 1)
            self.last_display = 1
        except:
            pass
    
    def save_dict_to_file(self):
        try:
            json.dump(self.save, open(self.save_file, "w+"), indent=4, skipkeys=True)
            print(f"\n[!] Saved Changes to: {self.save_file}\n")
        except Exception as error:
            print(error)
    
    def save_external_to_file(self, prof_dic, target_file):
        try:
            json.dump(prof_dic, open(target_file, "w+"), indent=4)
            print(f"\n[!] Saved Changes to: {target_file}\n")
        except Exception as error:
            print(error)
    
    def load_external_json(self, target_file):
        try:
            return json.load(open(target_file))
            print(f"[!] Loaded external json: {target_file}")
        except Exception as error:
            print(error)
    
    def update_variable(self):
        try:
            self.convert_to = type(self.path[-1][self.current_var[0][-1]])
            self.path[-1][self.current_var[0][-1]] = self.convert_to(self.value_bar.text())
            self.display_variables(self.last_display, 1)
        except:
            try:
                self.convert_to = type(self.current_dic[self.current_var[1]])
                self.current_dic[self.current_var[1]] = self.convert_to(self.value_bar.text())
                self.display_variables(self.last_display, 1)
            except Exception as error:
                print(error)

    def unlock_achievements(self):
        if self.last_display > -1:
            try:
                if os.path.isfile(self.profile[0]):
                    self.dic = self.load_external_json(self.profile[0])
                    try:
                        self.achievements = self.load_external_json("data.json")['achievements']
                    except:
                        try:
                            self.path_to, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File Containing Achievements", "", ".json Files (*.json)")
                            self.achievements = self.load_external_json(self.path_to)['achievements']
                        except Exception as error: 
                            print('3', error)

                    self.dic['achievements'] = self.achievements

                    self.save_external_to_file(self.dic, self.profile[0])

                else:
                    pass
            except Exception as error:
                print(error)
        else:
            print(self.last_display)
    
    def unlock_events(self):
        if self.last_display > -1:
            try:
                if os.path.isfile(self.profile[0]):
                    self.dic = self.load_external_json(self.profile[0])
                    try:
                        self.events = self.load_external_json("data.json")['events']
                    except:
                        try:
                            self.path_to, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File Containing Events", "", ".json Files (*.json)")
                            self.events = self.load_external_json(self.path_to)['events']
                        except Exception as error: 
                            print('3', error)

                    self.dic['events'] = self.events

                    self.save_external_to_file(self.dic, self.profile[0])

                else:
                    pass
            except Exception as error:
                print(error)
        else:
            print(self.last_display)

        if self.last_display > -1:
            try:
                if os.path.isfile(self.profile[0]):
                    self.dic2 = self.load_external_json(self.profile[0])
                    try:
                        self.pervert = self.load_external_json("data.json")['enemyKnowledge']
                    except:
                        try:
                            self.path_to, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File Containing Toa pervert Characters", "", ".json Files (*.json)")
                            self.pervert = self.load_external_json(self.path_to)['enemyKnowledge']
                        except Exception as error: 
                            print('3', error)

                    self.dic2['enemyKnowledge'] = self.pervert

                    self.save_external_to_file(self.dic2, self.profile[0])

                else:
                    pass
            except Exception as error:
                print(error)
        else:
            print(self.last_display)
    
    def max_perks(self):
        if self.last_display > -1:
            try:
                self.current_path = os.path.join(os.getcwd(), "data.json")
                if os.path.isfile(self.current_path):
                    self.perks = self.load_external_json(self.current_path)['perks-max']
                    self.save['player']['perks'] = self.perks
                    self.save_dict_to_file()
                else:
                    try:
                        self.current_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File Containing Perks", "", ".json Files (*.json)")
                        self.perks = self.load_external_json(self.current_path)['perks-max']
                        self.save['player']['perks'] = self.perks
                        self.save_dict_to_file()

                    except Exception as error:
                        print('1',error)
            except:
                print('2', error)
        else:
            print(self.last_display)
 
    def max_skills(self):
        if self.last_display > -1:
            try:
                self.current_path = os.path.join(os.getcwd(), "data.json")
                if os.path.isfile(self.current_path):
                    self.skills = self.load_external_json(self.current_path)['skills-max']
                    self.save['player']['skills'] = self.skills
                    self.save_dict_to_file()
                else:
                    try:
                        self.current_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File Containing Skills", "", ".json Files (*.json)")
                        self.skills = self.load_external_json(self.current_path)['skills-max']
                        self.save['player']['skills'] = self.skills
                        self.save_dict_to_file()

                    except Exception as error:
                        print('1',error)
            except:
                print('2', error)
        else:
            print(self.last_display)
    
    def add_empty(self):
        if self.last_display > -1:
            try:
                self.current_path = os.path.join(os.getcwd(), "data.json")
                if os.path.isfile(self.current_path):
                    self.skills = self.load_external_json(self.current_path)['skills']
                    for self.key in self.skills.keys():
                        if self.key in self.save['player']['skills'].keys():
                            pass
                        else:
                            self.save['player']['skills'][self.key] = 0
                    self.save_dict_to_file()
                else:
                        print('[1-1]', "Couldn't resolve path to data.json")
            except:
                print('2', error)

            try:
                self.current_path = os.path.join(os.getcwd(), "data.json")
                if os.path.isfile(self.current_path):
                    self.skills = self.load_external_json(self.current_path)['perks']
                    for self.key in self.skills.keys():
                        if self.key in self.save['player']['perks'].keys():
                            pass
                        else:
                            self.save['player']['perks'][self.key] = 0
                    self.save_dict_to_file()
                else:
                        print('[1-2]', "Couldn't resolve path to data.json")
            except:
                print('2', error)
        else:
            print(self.last_display)

    def display_variables(self, typ, ref):
        self.list_values.clear()
        if ref == 1:
            if typ == 1:
                for self.value in self.path[-1].keys():
                    if str(type(self.path[-1][self.value])) == "<class 'int'>" or str(type(self.path[-1][self.value])) == "<class 'str'>" or str(type(self.path[-1][self.value])) == "<class 'bool'>":
                        self.list_values.addItem(f"{self.value} : {self.path[-1][self.value]}")
                    else:
                        self.list_values.addItem(f"{self.value} : >")
            elif typ == 2:
                for self.value in self.path[-1]:
                    if str(type(self.value)) == "<class 'dict'>":
                        for self.dvalue in self.value.keys():
                            self.list_values.addItem(f"{str(self.dvalue)} : {self.value[self.dvalue]}")
                    else:
                        pass
            else:
                pass
        elif ref == 2:
            if typ == 1:
                for self.value in self.path[-1].keys():
                    if str(type(self.path[-1][self.value])) == "<class 'int'>" or str(type(self.path[-1][self.value])) == "<class 'str'>" or str(type(self.path[-1][self.value])) == "<class 'bool'>":
                        if self.search_bar.text() in self.value:
                            self.list_values.addItem(f"{self.value} : {self.path[-1][self.value]}")
                        else:
                            pass
                    else:
                        if self.search_bar.text() in self.value:
                            self.list_values.addItem(f"{self.value} : >")
                        else:
                            pass
            elif typ == 2:
                for self.value in self.path[-1]:
                    if self.search_bar.text() in self.value:
                        if str(type(self.value)) == "<class 'dict'>":
                            for self.dvalue in self.value.keys():
                                self.list_values.addItem(f"{str(self.dvalue)} : {self.value[self.dvalue]}")
                        else:
                            pass
                    else:
                        pass   
        else:
            pass


    def update_path(self, back):
        if not back:
            self.item = self.list_values.currentItem().text().split(' :')[0]
            self.crnt_row = self.list_values.currentRow()
            try:
                if str(type(self.path[-1][self.item])) == "<class 'dict'>":
                    self.path.append(self.path[-1][self.item])
                    self.display_variables(1, 1)
                    self.last_display = 1
                elif str(type(self.path[-1][self.item])) == "<class 'list'>":
                    self.path.append(self.path[-1][self.item])
                    self.last_display = 2
                    self.display_variables(2, 1)
                else:
                    self.current_var[0] = [self.item]
                    self.display_var = self.path[-1][self.current_var[0][-1]]
                    self.value_bar.setText(str(self.display_var))
            except:
                for self.limit in range(len(self.path[-1])):
                    if self.item in self.path[-1][self.limit]:
                        self.current_var[0] = self.path[-1][self.limit]

                        if len(self.current_var) > 1:
                            self.current_var.remove(self.current_var[-1])
                        else:
                            pass
                        
                        self.current_var.append(self.item)

                        self.current_dic = self.current_var[0]
                        self.value_bar.setText(str(self.current_dic[self.current_var[1]]))
                        self.current_var[0] = self.current_dic[self.current_var[1]]
                        break
                    else:
                        pass

        elif len(self.path) > 1:
            self.path.remove(self.path[-1])
            self.display_variables(1, 1)
            self.last_display = 1
        else:
            print("Can't go back any futher.")
        


if __name__ == "__main__":
    import os
    import sys
    import json

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
