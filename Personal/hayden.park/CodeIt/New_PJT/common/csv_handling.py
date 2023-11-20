import pandas as pd
import os

root_path = os.path.dirname(__file__)

def get_csv_data(csv_filename):
    path = root_path+"\\csv_files\\"+csv_filename
    data = pd.read_csv(path)
    return data
