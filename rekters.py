import time
import pynput.mouse as mouse
import pynput.keyboard as keyboard

mouse1 = mouse.Controller()
keyboard1 = keyboard.Controller()

def Do_Alittle_Dance(dance, reps:int) -> None:
  """"
  Takes a dance function and preforms x provided reps of the dance
  """
  for _ in range(reps):
    dance()

def shimmy() -> None:
  """
  In most shooting games this will lean the player left to right then jump.
  """
  keyboard1.press('q')
  time.sleep(0.5)
  keyboard1.release('q')
  keyboard1.press('e')
  time.sleep(0.5)
  keyboard1.release('e')
  keyboard1.press(keyboard.Key.space)
  time.sleep(0.5)
  keyboard1.release(keyboard.Key.space)

def Shoot_em_Up(time:int) -> None:
  """
  Presses the left mouse button, shooting for the time provided in most games
  """
  mouse1.press(mouse.Button.left)
  time.sleep(time)
  mouse1.release(mouse.Button.left)
