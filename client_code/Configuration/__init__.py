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

    # # Any code you write here will run before the form opens.
    # self.location_dd.items = [(r['name'], r) for r in app_tables.locations.search()]

    # fig = anvil.server.call('create_fig')
    # self.plot_1.figure = fig

  def populate_carriers_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('populate_carriers')

  def populate_locations_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('populate_locations')