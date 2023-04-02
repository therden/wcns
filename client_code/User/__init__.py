from ._anvil_designer import UserTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class User(UserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.carrier_dd.items = [(r['carrier'], r) for r in app_tables.carriers.search(tables.order_by('carrier'))]
    self.county_dd.items = [(r['county'], r) for r in app_tables.counties.search(tables.order_by('county'))]
    # Any code you write here will run before the form opens.
