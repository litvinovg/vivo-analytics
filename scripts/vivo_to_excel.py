#pip install pandas xlsxwriter
import base64
import os
import re
import pandas as pd	
from datetime import datetime

username = ""
password = ""
vivoUrl = ""
now = datetime.now()
string_timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
excel_file = "VIVO-" + string_timestamp + ".xlsx"
powerBIDistributor = "RDBMS"
distributorPrefix = "/api/dataRequest/"
token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
headers = {"Authorization": f"Basic {token}"}

with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
  for distributorName in pd.read_csv(vivoUrl + distributorPrefix + powerBIDistributor, storage_options=headers)['name']:
    csv = pd.read_csv(vivoUrl + distributorPrefix + distributorName, storage_options=headers)
    print(f'Downloaded {distributorName}')
    csv.to_excel(writer, sheet_name=re.sub(r'[^a-zA-Z_]', '_', distributorName)[:31], index=False)
