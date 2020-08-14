from sas7bdat import SAS7BDAT


with SAS7BDAT('whas500.sas7bdat', skip_header=False) as reader:
    df = reader.to_data_frame()


df.to_csv('whas500.csv')