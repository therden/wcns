import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def send_text(sender, mobile_number, gateway, subject, msg):
  anvil.email.send(
    from_name=sender, to=f"{mobile_number}@{gateway}", subject=subject, text=msg
  )

  # anvil.email.send(from_name = "My App Support",
  # to = "6073420526@msg.fi.google.com",
  # subject = "Test SMS from LowPoint",
  # text = "This is a test - this is only a test.")


@anvil.server.callable
def populate_carriers():
  import pandas as pd

  with open(data_files["carriers.csv"]) as file:
    df = pd.read_csv(file)
  for d in df.to_dict(orient="records"):
    # d is now a dict of {columnname -> value} for this row
    # We use Python's **kwargs syntax to pass the whole dict as
    # keyword arguments
    app_tables.carriers.add_row(**d)
