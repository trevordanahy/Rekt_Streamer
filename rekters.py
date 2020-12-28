import time
from pydirectinput import mouseDown, mouseUp, keyDown, keyUp

def Do_Alittle_Dance(dance, reps:int) -> None:
  """"
  Takes a dance function and preforms x provided reps of the dance
  """
  for _ in range(reps):
    dance()


def shimmy() -> None:
  """
  In most shooting games this will move the player left to right then jump.
  """
  keyDown('a')
  time.sleep(1)
  keyUp('a')
  keyDown('d')
  time.sleep(1)
  keyUp('d')
  keyDown('space')
  time.sleep(.5)
  keyUp('space')


def Mouse_Hold(hold_time:int) -> None:
  """
  Presses the left mouse button, shooting for the time provided in most games
  """
  mouseDown()
  time.sleep(hold_time)
  mouseUp()
