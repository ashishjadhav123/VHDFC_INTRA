import pandas as pd
import csv

file_path = 'D:\\Csv\\API Average Response Time Status Report_31-01-2022 17_49_51 PM.csv'
out_put_file = 'D:\\Csv\\Output\\Out_put.csv'

excel_df = pd.read_csv(file_path)

fields = list(excel_df)[:4]

out_put_data = []
row_count = len(excel_df.index)
for index in range(row_count):
    row_of_df = excel_df.iloc[index]
    if '0' not in str(row_of_df[str(list(excel_df)[5])]) or '0' not in str(row_of_df[str(list(excel_df)[6])]):
        out_put_data.append(list(row_of_df))

print(fields)
print(out_put_data)

with open(out_put_file,'w', newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(out_put_data)


