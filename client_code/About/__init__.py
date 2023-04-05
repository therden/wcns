from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class About(AboutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # text = app_tables.files.get(name='about.md')['data'].get_bytes()
    # self.rich_text_1.content = text.decode('utf-8')
    self.rich_text_1 = get_files_table_data('about.md', 'data')
    self.rich_text_1 = anvil.server.call('get_files_table_data', 'about.md', 'data')

