import sys
from PySide6.QtWidgets import QMainWindow, QApplication,  QDialog,  QVBoxLayout,QLabel
from solar_schedule import dirs_path
from action_to_db import ActionDB as ABD

from schedule_solar import Ui_MainWindow
from msg_editor_user import Ui_EditorEngineerDialog

class EditorEngineerDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui_dialog = Ui_EditorEngineerDialog()
        self.ui_dialog.setupUi(self)
        self.activate_elem()

    def activate_elem(self):
        self.ui_dialog.create_engineer.clicked.connect(self.on_push_create_engineer_btn_clicked)
        self.ui_dialog.delete_engineer.clicked.connect(self.on_push_delete_engineer_btn_clicked)

    def on_push_create_engineer_btn_clicked(self):
        try:
            surname_eng = self.ui_dialog.surname_engineer.text().strip()
            name_eng = self.ui_dialog.name_engineer.text().strip()
            second_name_eng = self.ui_dialog.second_name_engineer.text().strip()
            simpleName = f"{surname_eng} {name_eng[0]}."
            fullName = f"{surname_eng} {name_eng} {second_name_eng}"
            phone = None
            email_eng = self.ui_dialog.email_engineer.text().strip()
            job_eng = self.ui_dialog.job_engineer.text().strip()
            actionDB = ABD()
            actionDB.insert_into_db(simpleName,fullName,phone,email_eng,job_eng)
        except IndexError:
            print("Error: STRING IS EMPTY")

    def on_push_delete_engineer_btn_clicked(self):
        try:
            surname_eng = self.ui_dialog.surname_engineer.text().strip()
            name_eng = self.ui_dialog.name_engineer.text().strip()
            second_name_eng = self.ui_dialog.second_name_engineer.text().strip()
            simpleName = f"{surname_eng} {name_eng[0]}."
            fullName = f"{surname_eng} {name_eng} {second_name_eng}"
            phone = None
            email_eng = self.ui_dialog.email_engineer.text().strip()
            job_eng = self.ui_dialog.job_engineer.text().strip()
            actionDB = ABD()
            actionDB.delete_from_db(simpleName, fullName, phone, email_eng, job_eng)
        except IndexError:
            print("Error: STRING IS EMPTY")


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.info_btn_1.setChecked(True)
        self.activate_elem()

    # Function for activate interactive elements
    def activate_elem(self):
        self.ui.search_btn_1.clicked.connect(self.on_search_btn_clicked)

        self.ui.home_btn_1.clicked.connect(self.on_home_btn_1_toggled)
        self.ui.home_btn_2.clicked.connect(self.on_home_btn_2_toggled)

        self.ui.dashboard_btn_1.clicked.connect(self.on_dashborad_btn_1_toggled)
        self.ui.dashboard_btn_2.clicked.connect(self.on_dashborad_btn_2_toggled)

        self.ui.enginers_btn_1.clicked.connect(self.on_engineers_btn_1_toggled)
        self.ui.enginers_btn_2.clicked.connect(self.on_engineers_btn_2_toggled)

        self.ui.schedule_btn_1.clicked.connect(self.on_schedule_btn_1_toggled)
        self.ui.schedule_btn_2.clicked.connect(self.on_schedule_btn_2_toggled)

        self.ui.other_btn_1.clicked.connect(self.on_other_btn_1_toggled)
        self.ui.other_btn_2.clicked.connect(self.on_other_btn_2_toggled)

        # self.ui.profile_btn_2.clicked.connect(self.on_engineers_btn_1_toggled)
        # self.ui.profile_btn_1.clicked.connect(self.on_engineers_btn_2_toggled)

        self.ui.append_engineer.clicked.connect(self.on_push_append_engineer_btn_clicked)


    # Function of edit contents in Form

    def on_push_append_engineer_btn_clicked(self):
        dialog = EditorEngineerDialog()
        dialog.exec()

        layout = QVBoxLayout()

        N = 5

        # Динамическое создание и добавление виджетов QLabel
        for i in range(N):
            label = QLabel(f"Пример текстового виджета {i + 1}")
            layout.addWidget(label)



    # Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.search_lbl.setText(search_text)

    # Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    #     # Change QPushButton Checkable status when stackedWidget index changed
    # def on_stackedWidget_currentChanged(self, index):
    #     btn_list = self.ui.icon_only_widget.findChildren(QPushButton) + \
    #                self.ui.full_menu_widget.findChildren(QPushButton)
    #
    #     for btn in btn_list:
    #         if index in [5, 6]:
    #             btn.setAutoExclusive(False)
    #             btn.setChecked(False)
    #         else:
    #             btn.setAutoExclusive(True)

    #     # functions for changing menu page

    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_engineers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_engineers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_schedule_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_schedule_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_other_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_other_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

# class Dialog_Editor_Engineer(Q)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open(str(dirs.STYLE_DIR) + r"\style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindows()
    window.show()

    sys.exit(app.exec())


