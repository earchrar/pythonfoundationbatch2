from openpyxl import Workbook
from datetime import datetime 

class ExcelWorkBook: 
    def __init__(self,filename): 
        self.filename = filename
        self.workbook = Workbook()
        self.exclsheet = self.workbook.active

    def setheaders(self,headers):
        self.exclsheet.append(headers)

    def setrows(self,datarows):
        for row in datarows:
            rowwithtimestamp = row+[datetime.now().strftime("%d-%m-%Y %H:%M:%S")]
            self.exclsheet.append(rowwithtimestamp)

    def savefile(self):
        self.workbook.save(self.filename)
        print(f"Excel file saved as {self.filename}")

if __name__ == "__main__":
    headers = ["ID","Name","Email","Created_At"]

    users = [
        [1,"Kyaw Kyaw","kyawkyaw@gmail.com"],
        [2,"Naw Naw","nawnaw@gmail.com"],
        [3,"Zaw Zaw","zawzaw@gmail.com"],
        [4,"Aung Aung","aungaung@gmail.com"],
        [5,"Maung Maung","maungmaung@gmail.com"]
    ]

    excelworkbookObj = ExcelWorkBook("users.xlsx")
    excelworkbookObj.setheaders(headers)
    excelworkbookObj.setrows(users)
    excelworkbookObj.savefile()

