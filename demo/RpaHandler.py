import xlrd
import os
from openpyxl import load_workbook


def readExcel():
    wb = load_workbook('D:\IdeaProjects\my_space\demo\保单号.xlsx')
    sheets = wb.worksheets
    sheet1 = sheets[0]
    max_rows = sheet1.max_row

    res = []

    for row in range(2, max_rows + 1):
        var1 = sheet1.cell(row, 1).value
        var2 = sheet1.cell(row, 2).value
        res.append([var1, var2])

    return res


path = "E:\FFOutput\屏幕录像"


def renameFile():
    file_list = os.listdir(path)
    file_list = [i.replace("格式工厂 屏幕录像", "").replace("_", "").replace(".mp4", "") for i in file_list]
    file_list.sort()
    data_list = readExcel()

    if len(file_list) == len(data_list):
        for index, i in enumerate(data_list):
            filename = file_list[index]

            old_name = "格式工厂 屏幕录像" + filename[:8] + "_" + filename[8:] + ".mp4"
            new_name = i[0] + ".mp4"
            os.rename(path + "\\" + old_name, path + "\\" + new_name)
    else:
        print("文件数量不正确")





