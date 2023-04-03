import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


# @anvil.server.callable
# def populate_carriers():
#   import pandas as pd
#   with open(data_files['carriers.csv']) as file:
#     df = pd.read_csv(file)
#   for d in df.to_dict(orient="records"):
#     # d is now a dict of {columnname -> value} for this row
#     # We use Python's **kwargs syntax to pass the whole dict as
#     # keyword arguments
#     app_tables.carriers.add_row(**d) 

# @anvil.server.callable
# def populate_locations():
#   import pandas as pd
#   with open(data_files['locations.csv']) as file:
#     df = pd.read_csv(file)
#   for d in df.to_dict(orient="records"):
#     # d is now a dict of {columnname -> value} for this row
#     # We use Python's **kwargs syntax to pass the whole dict as
#     # keyword arguments
#     app_tables.carriers.add_row(**d) 