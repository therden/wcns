from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

from datetime import datetime

from ..Home import Home
from ..User import User
from ..Location import Location
from ..Configuration import Configuration
from ..About import About


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    year = datetime.now().strftime('%Y')
    self.copyright.text = "Copyright " + year
    self.home_link.tag.form_to_open = Home()
    self.user_link.tag.form_to_open = User()
    self.locations_link.tag.form_to_open = Location()
    self.configuration_link.tag.form_to_open = Configuration()
    self.about_link.tag.form_to_open = About()
    
    anvil.users.login_with_form()
    self.user = anvil.server.call('get_user')
    if not self.user['administrator']:
      self.configuration_link.visible = False

  def nav_link_click(self, **event_args):
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open
    self.content_panel.clear()
    self.content_panel.add_component(form_to_open, item=dict())
   