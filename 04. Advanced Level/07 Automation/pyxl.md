# OPENPYXL NOTES — BEGINNER TO ADVANCED
# Python Excel Automation

## 1. INSTALLATION

pip install openpyxl

## 2. IMPORT

from openpyxl import Workbook, load_workbook

## 3. CREATE EXCEL FILE

wb = Workbook()
ws = wb.active
ws.title = "Students"

ws["A1"] = "Name"
ws["B1"] = "Marks"
ws["A2"] = "Faruk"
ws["B2"] = 90

wb.save("students.xlsx")

## 4. OPEN EXISTING EXCEL FILE

wb = load_workbook("students.xlsx")
ws = wb.active

print(ws["A1"].value)
print(ws["B2"].value)

## 5. CREATE WORKSHEET

ws2 = wb.create_sheet("Employees")
print(wb.sheetnames)

ws2["A1"] = "Employee Name"
wb.save("students.xlsx")

## 6. WRITE DATA USING APPEND

data = [
    ["ID", "Name", "Salary"],
    [1, "Faruk", 30000],
    [2, "Rahim", 40000],
    [3, "Karim", 50000]
]

for row in data:
    ws.append(row)

wb.save("data.xlsx")

## 7. READ ALL ROWS

for row in ws.iter_rows(values_only=True):
    print(row)

## 8. READ SPECIFIC RANGE

for row in ws.iter_rows(
    min_row=2,
    max_row=5,
    min_col=1,
    max_col=3,
    values_only=True
):
    print(row)

## 9. CELL ACCESS

print(ws["A1"].value)

ws["A1"] = "Updated Name"

ws.cell(row=1, column=1, value="ID")

## 10. ROW AND COLUMN COUNT

print(ws.max_row)
print(ws.max_column)

## 11. INSERT AND DELETE ROWS

ws.insert_rows(2)
ws.delete_rows(2, 1)

## 12. INSERT AND DELETE COLUMNS

ws.insert_cols(2)
ws.delete_cols(2, 1)

## 13. CELL FORMATTING

from openpyxl.styles import Font, PatternFill, Alignment

ws["A1"].font = Font(
    bold=True,
    size=14,
    color="FFFFFF"
)

ws["A1"].fill = PatternFill(
    fill_type="solid",
    fgColor="0000FF"
)

ws["A1"].alignment = Alignment(
    horizontal="center",
    vertical="center"
)

## 14. BORDER

from openpyxl.styles import Border, Side

thin = Side(style="thin", color="000000")

ws["A1"].border = Border(
    left=thin,
    right=thin,
    top=thin,
    bottom=thin
)

## 15. ROW HEIGHT AND COLUMN WIDTH

ws.row_dimensions[1].height = 30
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 15

## 16. MERGE CELLS

ws.merge_cells("A1:C1")
ws["A1"] = "Employee Report"

## 17. UNMERGE CELLS

ws.unmerge_cells("A1:C1")

## 18. EXCEL FORMULAS

ws["D1"] = "Total"
ws["D2"] = "=SUM(B2:C2)"
ws["D3"] = "=AVERAGE(B2:B10)"
ws["D4"] = "=MAX(B2:B10)"
ws["D5"] = "=MIN(B2:B10)"
ws["D6"] = "=COUNT(B2:B10)"
ws["D7"] = '=IF(B2>=50,"Pass","Fail")'

## 19. NUMBER FORMATTING

ws["B2"].number_format = "0.00"
ws["C2"].number_format = "0%"
ws["D2"].number_format = "#,##0.00"
ws["E2"].number_format = "YYYY-MM-DD"

## 20. FREEZE HEADER

ws.freeze_panes = "A2"

## 21. AUTO FILTER

ws.auto_filter.ref = ws.dimensions

## 22. HIDE ROW OR COLUMN

ws.row_dimensions[3].hidden = True
ws.column_dimensions["C"].hidden = True

## 23. DATA VALIDATION DROPDOWN

from openpyxl.worksheet.datavalidation import DataValidation

dv = DataValidation(
    type="list",
    formula1='"Pending,Approved,Rejected"'
)

ws.add_data_validation(dv)
dv.add("A2:A100")

## 24. CONDITIONAL FORMATTING

from openpyxl.formatting.rule import CellIsRule

red_fill = PatternFill(
    fill_type="solid",
    fgColor="FFC7CE"
)

ws.conditional_formatting.add(
    "B2:B100",
    CellIsRule(
        operator="lessThan",
        formula=["50"],
        fill=red_fill
    )
)

## 25. EXCEL TABLE

from openpyxl.worksheet.table import Table, TableStyleInfo

table = Table(
    displayName="EmployeeTable",
    ref="A1:C10"
)

style = TableStyleInfo(
    name="TableStyleMedium2",
    showRowStripes=True,
    showColumnStripes=False
)

table.tableStyleInfo = style
ws.add_table(table)

## 26. BAR CHART

from openpyxl.chart import BarChart, Reference

chart = BarChart()

data = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_row=10
)

categories = Reference(
    ws,
    min_col=1,
    min_row=2,
    max_row=10
)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, "E2")

## 27. WORK WITH DATES

from datetime import date, datetime

ws["A1"] = date.today()
ws["B1"] = datetime.now()

## 28. HYPERLINK

ws["A1"] = "GitHub"
ws["A1"].hyperlink = "https://github.com/"
ws["A1"].style = "Hyperlink"

## 29. COMMENTS

from openpyxl.comments import Comment

ws["A1"].comment = Comment(
    "Employee information",
    "Faruk"
)

## 30. LOAD LARGE EXCEL FILE

wb = load_workbook(
    "large.xlsx",
    read_only=True,
    data_only=True
)

ws = wb.active

for row in ws.iter_rows(values_only=True):
    print(row)

wb.close()

## 31. CREATE LARGE EXCEL FILE

wb = Workbook(write_only=True)
ws = wb.create_sheet("Data")

ws.append(["ID", "Name"])

for i in range(1, 10001):
    ws.append([i, f"User_{i}"])

wb.save("large_output.xlsx")

## 32. OPEN XLSM FILE

wb = load_workbook(
    "report.xlsm",
    keep_vba=True
)

ws = wb.active
ws["A1"] = "Updated"

wb.save("updated_report.xlsm")

## 33. FIND AND UPDATE DATA

for row in range(2, ws.max_row + 1):
    if ws.cell(row=row, column=1).value == 2:
        ws.cell(row=row, column=3).value = 50000
        break

wb.save("updated.xlsx")

## 34. SAVE EXCEL FILE

wb.save("output.xlsx")

## 35. IMPORTANT METHODS

Workbook()                 = Create workbook
load_workbook()             = Open workbook
wb.active                   = Active worksheet
wb.create_sheet()           = Create worksheet
wb.sheetnames               = List worksheet names
ws.append()                 = Add row
ws.cell()                   = Access cell
ws.iter_rows()              = Iterate through rows
ws.insert_rows()            = Insert rows
ws.delete_rows()            = Delete rows
ws.insert_cols()            = Insert columns
ws.delete_cols()            = Delete columns
ws.merge_cells()            = Merge cells
ws.freeze_panes             = Freeze panes
ws.auto_filter.ref          = Enable filter controls
wb.save()                   = Save workbook

## IMPORTANT NOTES

1. openpyxl মূলত XLSX এবং XLSM format-এর জন্য।
2. Formula লিখতে পারে, কিন্তু নিজে formula calculate করে না।
3. Read-only mode বড় file পড়তে উপকারী।
4. Write-only mode বড় file তৈরি করতে উপকারী।
5. VBA macro সংরক্ষণের জন্য keep_vba=True ব্যবহার করো।
6. গুরুত্বপূর্ণ file edit করার আগে backup রাখো।

END OF NOTES
