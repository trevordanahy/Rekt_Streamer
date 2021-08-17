from pydirectinput import keyDown, keyUp
from time import sleep


def do_dance(func):
    func()   


def Button_Press(button: str, delay: int) -> None:
    """Control button press and duration

    Args:
        button (str): key you wish to press ex: "w"
        delay (int): time you wish to hold the key down in sec.
    """
    keyDown(button)
    sleep(delay)
    keyUp(button)


def Shuffle_Hop() -> None:
    """Not Essential:
    For both this function, and Stroll(), I would consider moving
    the left/right/forward/back keys into a configuration file so 
    you can account for non-default keybindings.
    """

    """Move the player left to right then jump
    """
    Button_Press('a', 2)
    Button_Press('d', 2)
    Button_Press('space', 1)


def Stroll() -> None:
    """Move the character foward then backwards
    """
    Button_Press('w', 2)
    Button_Press('s', 2)


dance_list = {
    "shuffle hop": Shuffle_Hop,
    "stroll": Stroll
}
