import xlsxwriter
from db.DB import DB

db = DB()
tests = db.getAllTestResults()

workbook = xlsxwriter.Workbook('example.xlsx', {'remove_timezone': True})  # создаем документ
worksheet = workbook.add_worksheet()  # создаем вкладку в документе
# форматирование
cellPass = workbook.add_format(dict(bg_color='#00ff00'))
cellFail = workbook.add_format(dict(bg_color='red', bold=True))
bold = workbook.add_format(dict(bold=True))
#cellSuccess = workbook.add_format(dict(bg_color='#00ff00'))
worksheet.set_column(1, 1, 44)  # Изменяет длину ячейки
worksheet.set_column(4, 4, 20)
worksheet.set_column(5, 6, 14)
date_format = workbook.add_format({'num_format': 'dd/mm/yy hh:mm:ss.000'})
# названия столбцов
worksheet.write('A1', '№', bold)
worksheet.write('B1', 'Название теста', bold)
worksheet.write('C1', 'Успех', bold)
worksheet.write('D1', 'Фиаско', bold)
worksheet.write('E1', 'Дата', bold)
# значения
for i, test in enumerate(tests):
    worksheet.write('A' + str(i + 2), i+1)
    worksheet.write('B' + str(i + 2), test['name'])
    if test['result']:
        worksheet.write('C' + str(i + 2), 1, cellPass)
    else:
        worksheet.write('D' + str(i + 2), 1, cellFail)
    worksheet.write('E' + str(i + 2), test['date_time'], date_format)
# подсчет сумм
worksheet.write('F1', 'Успешные', bold)
worksheet.write('G1', 'Неуспешные', bold)
worksheet.write('F2', '=SUM(C:C)', cellPass)
worksheet.write('G2', '=SUM(D:D)', cellFail)
# рисуем графики
chart = workbook.add_chart(dict(type='column'))
chart.add_series(dict(values='=Sheet1!$F2', data_labels={'value': True}))
chart.add_series(dict(values='=Sheet1!$G2', data_labels={'value': True}))
chart.set_title(dict(name='Results'))
chart.set_x_axis(dict(name='Test number'))
chart.set_y_axis(dict(name='Number of outcomes'))
chart.set_style(24)  # Стиль графиков
chart.set_plotarea(dict(
    border={'color': 'red', 'width': 2, 'dash_type': 'dash'},
    fill={'color': '#FFFFC2'}
))
worksheet.insert_chart('H7', chart)
# записать данные
workbook.close()
