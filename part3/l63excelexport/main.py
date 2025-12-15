from openpyxl import Workbook
from datetime import datetime 

class ExcelWorkBook: 
    def __init__(self,filename): 
        self.filename = filename
        self.workbook = Workbook()
        self.exclsheet = self.workbook.active

    def setheaders(self,headers):
        self.exclsheet.append(headers)

    def setrows(self,row):
        rowwithtimestamp = row+[datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
        self.exclsheet.append(rowwithtimestamp)

    def savefile(self):
        self.workbook.save(self.filename)
        print(f"Excel file saved as {self.filename}")

if __name__ == "__main__":
    headers = ["ID","Name","Email","Created_At"]

    excelworkbookObj = ExcelWorkBook("users.xlsx")
    excelworkbookObj.setheaders(headers)

    initidx = 1 

    while True: 
        name = input("Enter Name (or type 'exit' to stop): ").strip()

        if name.lower() == "exit":
            break 

        email = input("Enter email: ").strip()

        excelworkbookObj.setrows([initidx,name,email])
        initidx += 1
        print("Row added: \n")

    excelworkbookObj.savefile()

