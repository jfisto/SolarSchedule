import os.path
from solar_schedule.dirs import EXCEL_DIR
import pandas as pd
from pandas.io.excel import ExcelWriter




class ScheduleEngineer:
    def __init__(self):
        self.file_name = EXCEL_DIR / 'schedule.xlsx'

    def add_week_schedule(self, engineer_name,Mon=None,Tue=None,Wed=None,Thu=None,Fri=None,Sat=None,Sun=None):


        # Создаем DataFrame из списка
        df = pd.read_excel(self.file_name, sheet_name="schedule_test.db")
        print(df)
        year_header = "year"
        week_num = 4
        engineer_name = "Яцынина Т."

        df2 = pd.DataFrame({
            'Engineer': [engineer_name],
            'Week': [week_num],
            'Mon': [Mon],
            'Tue': [Tue],
            'Wed': [Wed],
            'Thu': [Thu],
            'Fri': [Fri],
            'Sat': [Sat],
            'Sun': [Sun],
        })
        print(df)
        print(df2)
        
        res = pd.concat([df, df2]).reset_index(drop=True)

        with ExcelWriter(self.file_name, mode="a" if os.path.exists(self.file_name) else "w", if_sheet_exists='replace') as writer:
            res.to_excel(writer, sheet_name="schedule_test.db", index=False)
        print(res)



        # # Создаем объект ExcelWriter
        # with pd.ExcelWriter('data.xlsx', engine='openpyxl', mode='a') as writer:
        #     # Записываем DataFrame в файл Excel
        #     df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=2)
        #
        #     # Получаем объект workbook и worksheet
        #     workbook = writer.book
        #     worksheet = writer.sheets['Sheet1']
        #
        #     # Объединяем ячейки A1 и B1 по их индексам
        #     worksheet.merge_cells(start_row=1, start_column=1, end_row=1, end_column=2)
        #
        #     # Сохраняем изменения
        #     writer.save()

    def edit_week_schedile(self):
        # if engineer_name is not None:
        #     df1.loc[(df1.Week != 2) & (df1.Engineer == engineer_name), 'Mon'] = new_value
        #     df1 = df1.reset_index(drop=True)
        pass

    def delete_week_schedule(self,engineer_name,week_num,Mon=None,Tue=None,Wed=None,Thu=None,Fri=None,Sat=None,Sun=None):
        # Чтение данных из листа пользователей
        df1 = pd.read_excel(self.file_name, sheet_name="schedule_test.db")
        print(df1)
        # Удаление данных к данным из листа пользователей новой записи о сотруднике
        print(f"list | {list(df1[df1.Engineer == engineer_name].index)}")
        if engineer_name is not None:
            print(f"Drope Enginer {engineer_name} on Week {week_num}: ")
            print(df1[(df1.Week != week_num) & (df1.Engineer == engineer_name)].reset_index(drop=True))
            print(df1)
        print(f"iskomeoe {df1}")
        # print(f"iskomeoe {res}")
        # for elem in list(df1[df1.Engineer == engineer_name].index):
        #     print(elem)
        #     if engineer_name is not None: # удаление конкретной недели
                # df1 = df1[(df1.Engineer == engineer_name) & (df1.Week == week_num)].reset_index(drop=True)





        # if engineer_name != None:
        #     for elem in list(df1[df1.Engineer == engineer_name ].index):
        #         df1 = df1.drop(index=elem)
        #         print(f"elem {elem} | df1 {df1[df1.Engineer == engineer_name].index} | {df1.Engineer}")

        # res = df1
        # Сохранение данных о новом пользователе без потерь содержимого других листов
        # with ExcelWriter(self.file_name,
        #                  mode="a" if os.path.exists(self.file_name) else "w",
        #                  if_sheet_exists='replace') as write:
        #     res.to_excel(write, sheet_name="engineer_test.db", index=False)

        # Тестирование записи
        # test_data_xlxs = pd.read_excel(self.file_name, sheet_name="engineer_test.db")
        # print("dd", test_data_xlxs)




if __name__ == '__main__':
    obj = ScheduleEngineer()
    # obj.add_week_schedule("Яцынина Т.",1,2,None,None,3,4,None)
    # obj.delete_week_schedule("Агеева В.",3,1,2,None,None,3,4,None)
    obj.delete_week_schedule("Яцынина Т.",3,1,2,None,None,3,4,None)