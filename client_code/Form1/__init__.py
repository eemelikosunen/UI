from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_draw_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the  Draw button")
    pass

  def button_mirror_screen_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the Mirror Screen button")
