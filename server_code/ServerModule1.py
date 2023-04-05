import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_files_table_data(rowname, column):
  bytes = app_tables.files.get(name=rowname)[column].get_bytes()
  return bytes.decode('utf-8')


@anvil.server.callable
def populate_carriers():
  csv_data = app_tables.files.get(name='carriers.csv')['data'].get_bytes().decode('utf-8')
  # print(csv_data)
  for each in csv_data[1:]:
    print(each)
    _, carrier, gateway = each[0], each[1], each[2]
    app_tables.carriers.add_row(carrier=carrier, gateway=gateway) 

@anvil.server.callable
def populate_locations():
  import pandas as pd
  with open(data_files['locations.csv']) as file:
    df = pd.read_csv(file)
  for d in df.to_dict(orient="records"):
    # d is now a dict of {columnname -> value} for this row
    # We use Python's **kwargs syntax to pass the whole dict as
    # keyword arguments
    app_tables.locations.add_row(**d) 