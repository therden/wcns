from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

# from .Home import Home
from ..User import User
from ..Counties import Counties
from ..Test import Test
from ..About import About
from ..Login import Login

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # self.home_link.tag.form_to_open = Home()
    self.user_link.tag.form_to_open = User()
    self.counties_link.tag.form_to_open = Counties()
    self.test_link.tag.form_to_open = Test()
    self.about_link.tag.form_to_open = About()
    self.login_btn.tag.form_to_open = Login()

  def nav_link_click(self, **event_args):
    """A generalised click handler that you can bind to any nav link."""
    # Find out which Form this Link wants to open
    form_to_open = event_args['sender'].tag.form_to_open
    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

  def home_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Home')

  def login_btn_click(self, **event_args):
    open_form('Login')
    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)