import xlrd
import xlsxwriter

#open a file for reading and writing
f = open("simpletextfile.txt", "w+")
f.write("This is python demonstration\n This is entering text in second line"
        "\n Third line")
f.close()

#open a file for reading
f=open("simpletextfile.txt", "r")
print(f.read())
f.close()

#write to excel file
xlbook = xlsxwriter.Workbook("Tabledata.xlsx") #this will create your excel file
xlsheet = xlbook.add_worksheet("Table")
for i in range(0,3):
    for j in range(0,3):
        data = input("Enter the data to be given: ")
        xlsheet.write(i,j,data)
xlbook.close()

#read from excelfile
wb=xlrd.open_workbook("Tabledata.xlsx", 'r')
sheet = wb.sheet_by_index(0)
print(sheet.cell(0,2))