from time import sleep
import dances
from threading import Timer
from pydirectinput import mouseDown, mouseUp

stopper = False
available_dances = dances.dance_list


def Cutoff():
    """Used to stop any func with rapid inputs
    """
    global stopper
    stopper = True


def Reset():
    """Resets stopper var to allow rapid inputs to occur
    """
    global stopper
    stopper = False


def Do_Alittle_Dance(dance_name: str = "shuffle hop", reps: int = 5) -> None:
    """Preforms dance move given by chat

    Args:
        dance_name (str, optional): Usr can choose to type dance name
        in while redeeming. Defaults to "shuffle hop".
        reps (int, optional): Number of times to dance. Defaults to 5 sec.
    """
    knows_dance = False

    
    """ 
    Use dict.get() with a default value to simplify some of the logic

        avaliable_dances.get(dance_name, VALUE) 

    will return VALUE if dance_name is not a valid key,

    which means that:

        available_dances.get(dance_name, available_dances.get("shuffle hop"))

    will return available_dances.get("shuffle hop") if dance_name is not a valid key
    """
    dance_func = available_dances.get(dance_name, available_dances.get("shuffle hop"))
    for _ in range(reps):
        dances.do_dance(dance_func)


def Mouse_Hold(mode: str = "rapid", hold_time: float = 5.0) -> None:
    """
    Briefly controls player's mouse. Two options rapid clicks or a click and hold

    Args:
        mode (str, optional): Chooses rapid clicking or click and hold.
        hold_time (float, optional): Time to hold control of mouse. Defaults to 5.0 sec.
    """
    if "rapid" in mode:
        Mouse_Rapid(hold_time)
    elif "hold" in mode:
        mouseDown()
        sleep(hold_time)
        mouseUp()
    else:
        Mouse_Rapid(hold_time)


def Mouse_Rapid(hold_time: float) -> None:
    """
    Clicks rapidly while timer is active

    Args:
        hold_time (float): [Set time clicking will occur in seconds]
    """
    global stopper
    t = Timer(hold_time, Cutoff)
    t.start()
    while stopper is False:
        mouseDown()
        mouseUp()
        sleep(0.01)
