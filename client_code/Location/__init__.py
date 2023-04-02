from ._anvil_designer import LocationTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Location(LocationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.location_dd.items = [(r['location'], r) for r in app_tables.locations.search()]

    fig = anvil.server.call('create_fig') 
    self.plot_1.figure = fig