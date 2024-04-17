from ._anvil_designer import MENUTemplate
from anvil import *

class MENU(MENUTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_draw_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the Draw button")
    pass

  def button_mirror_screen_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the Mirror Screen button")

  def button_open_file_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the Open file button")
    pass

  def button_favourite_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the favourite button")
    pass

  def button_settings_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the settings button")
    pass

  def button_log_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the Log Out button")
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the Select screen button")
    pass
