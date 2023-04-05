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
    self.location_dd.items = [(r['name'], r) for r in app_tables.locations.search(tables.order_by('name'))]
    # Any code you write here will run before the form opens.

  def notify_by_text_checkbox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    text_components = [self.carrier_dd, self.cellphone_box, self.label_2, self.label_3]
    if self.notify_by_text_checkbox.checked:
      for each in text_components:
        each.visible = True
    else:
      for each in text_components:
        each.visible = False  
