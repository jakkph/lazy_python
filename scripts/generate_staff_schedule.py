import pandas as pd
import random
import datetime
from openpyxl import Workbook
import pandas as pd

start_date = pd.to_datetime("2023-06-02")
end_date = pd.to_datetime("2023-12-31")
date_range = pd.date_range(start_date, end_date, freq="D")
 
for i, date in enumerate(date_range):
    if date.strftime('%A') != day_off[staff]:
        worksheet.append([date.strftime('%d-%m-%Y'), random.choice(shift_times)])



days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
staff_names = [ "จารุวรรณ พลเพชร", "เสาวลักษณ์ บุญร่ม", "รักชนก สุดโกศล", "สุธาทิพย์ ทิมทัพ", "ดลฤดี โพธิ์ศรีมา", "เจนจิรา กิ้มเท่ง", "จุฑามาศ แก้วภู่", "อ้อมใจ", "กาญจนา", "ยุพาวรรณ พันใย", "เบญจมาศ สุวรรณโชติ", "ศศิวรรณ ทองย้อย", "ดิศราพร บุพศิริ", "ขวัญจิรา คำประเสริญ"]
shift_times = ["8:00 AM - 5:00 PM", "9:00 AM - 6:00 PM", "10:00 AM - 7:00 PM"]

day_off = {}

for staff in staff_names:
    day_off[staff] = random.choice(days_of_week)

workbook = Workbook()
date_range = pd.date_range(pd.to_datetime("2023-06-02"), pd.to_datetime("2023-12-31"), freq="D")

for staff in staff_names:
    worksheet = workbook.create_sheet(title=staff)
    worksheet.append(["Date", "Shift"])
    for date in date_range:
        if date.strftime('%A') != day_off[staff]:
            worksheet.append([date.strftime('%d-%m-%Y'), random.choice(shift_times)])

workbook.save("schedule.xlsx")
