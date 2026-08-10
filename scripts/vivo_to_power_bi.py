#pip install pandas matplotlib
import base64
import re
import pandas as pd

username = ""
password = ""
vivoUrl = ""

powerBIDistributor = "RDBMS"
path = "/api/dataRequest/"
token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
headers = {"Authorization": f"Basic {token}"}

for distributorName in pd.read_csv(vivoUrl + path + powerBIDistributor, storage_options=headers)['name']:
  locals()[re.sub(r'[^a-zA-Z_]', '_', distributorName)] = pd.read_csv(vivoUrl + path + distributorName, storage_options=headers)

