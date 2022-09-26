# Import the required method
from zipfile import ZipFile
import csv
from pprint import pprint
with ZipFile('D:\docker-airflow\dags\ETL\PPR-ALL.zip', "r") as f:
    # Get the list of files
    file_names = f.namelist()
    print(file_names)
    # Extract the CSV file
    csv_file_path = f.extract(file_names[0])
    print(csv_file_path)

new_column_names = {
    "Date of Sale (dd/mm/yyyy)": "date_of_sale",
    "Address": "address",
    "Postal Code": "postal_code",
    "County": "county",
    "Price (€)": "price",
    "Description of Property": "description",
}
with open('D:\docker-airflow\ppr-all.csv', mode="r", encoding="windows-1252") as reader_csv_file:
    reader = csv.DictReader(reader_csv_file)
    # The new file is called "PPR-2021-Dublin-new-headers.csv"
    # and will be saved inside the "tmp" folder    
    with open("D:\docker-airflow\PPR-2021-Dublin-new-headers.csv",
                    mode="w",
                    encoding="windows-1252",
                ) as writer_csv_file:
        writer = csv.DictWriter(writer_csv_file, fieldnames=new_column_names)
        # Write header as first line
        writer.writerow(new_column_names)
        for row in reader:
	        # Write all rows in file
	        writer.writerow(row)
