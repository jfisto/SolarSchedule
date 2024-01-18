import os.path
from solar_schedule.dirs import EXCEL_DIR
import pandas as pd
import uuid
from pandas.io.excel import ExcelWriter


###TODO: Запись, чтение и изменение DB нужно переделать. Работает не корректно
class ActionDB:
    def __init__(self):
        self.file_name = EXCEL_DIR / 'schedule.xlsx'

    def _select_from_db(self):
        file_name = EXCEL_DIR / 'schedule.xlsx'

        # Чтение данных из листа пользователей
        df1 = pd.read_excel(file_name, sheet_name="engineer_test.db")
        print(df1)




    def insert_into_db(self, simpleName=None, fullName=None, phone=None, email=None, jobName=None):


        # Чтение данных из листа пользователей
        df1 = pd.read_excel(self.file_name, sheet_name="engineer_test.db")

        df2 = pd.DataFrame({
            'uuid': [uuid.uuid4()],
            'SimpleName': [simpleName],
            'FullName': [fullName],
            'Phone': [phone],
            'Email': [email],
            'JobName': [jobName],
        })

        res = pd.concat([df1, df2]).reset_index(drop=True)
        # Альтернативный вариант записи без расхода памяти на df2(недостаток в том, что безвозвратно изменяется df1
        # res = df1._append({
        #     'SimpleName': 2222,
        #     'FullName': 3,
        #     'Phone': 4,
        #     'Email': 5555,
        #     'JobName': 6,
        # }, ignore_index=True)

        # print("res", res)

        # Сохранение данных о новом пользователе без потерь содержимого других листов
        with ExcelWriter(self.file_name, mode="a" if os.path.exists(self.file_name) else "w", if_sheet_exists='replace') as write:
            res.to_excel(write, sheet_name="engineer_test.db", index=False)

        # Тестирование записи
        self._select_from_db()

    def __update_note_to_db(self):
        pass

    def delete_from_db(self,simpleName=None, fullName=None, phone=None, email=None, jobName=None):


        # Чтение данных из листа пользователей
        df1 = pd.read_excel(self.file_name, sheet_name="engineer_test.db")

        # Добавление к данным из листа пользователей новой записи о сотруднике
        # print("df1",df1)
        if simpleName != None:
            for elem in list(df1[df1.SimpleName == simpleName].index):
                df1 = df1.drop(index=elem)
        elif fullName != None:
            for elem in list(df1[df1.FullName == fullName].index):
                df1 = df1.drop(index=elem)
        elif phone != None:
            for elem in list(df1[df1.Phone == phone].index):
                df1 = df1.drop(index=elem)
        elif email!= None:
            for elem in list(df1[df1.Email == email].index):
                df1 = df1.drop(index=elem)
        res = df1

        # Сохранение данных о новом пользователе без потерь содержимого других листов
        with ExcelWriter(self.file_name, mode="a" if os.path.exists(self.file_name) else "w", if_sheet_exists='replace') as write:
            res.to_excel(write, sheet_name="engineer_test.db", index=False)

        # Тестирование записи
        test_data_xlxs = pd.read_excel(self.file_name, sheet_name="engineer_test.db")
        print("dd", test_data_xlxs)

    def create_uuid_engineer(self):
        return uuid.uuid4()

if __name__ == '__main__':
    obj = ActionDB()
    # obj.delete_from_db()
    # obj.update_note_to_db()
    # obj._select_from_db()
    print(obj.create_uuid_engineer())
    # print(EXCEL_DIR)