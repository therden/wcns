from ._anvil_designer import ConfigurationTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Configuration(ConfigurationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def populate_carriers_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call("populate_carriers")
