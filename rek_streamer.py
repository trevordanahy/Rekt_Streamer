from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from uuid import UUID
from your_stuff import your_id, your_secret, your_oa, your_username
import rekters

# Authentication Setup and Info
twitch = Twitch(your_id, your_secret)
twitch.authenticate_app([])
twitch.set_user_authentication(your_oa,
                               [AuthScope.CHANNEL_READ_REDEMPTIONS],
                               your_oa)
user_id = twitch.get_users(logins=[your_username])['data'][0]['id']


# Controllers
def Channel_Pt_Controller(uuid: UUID, data: dict) -> None:
    redeemer = data["data"]["redemption"]["user"]["display_name"]
    reward = data["data"]["redemption"]["reward"]["title"]
    command = data["data"]["redemption"]["user_input"]
    command = command.lower()
    print(redeemer + " Is going to rek you.")

    if reward == "Do a little dance":
        rekters.Do_Alittle_Dance(command, 5)
        print("\n press ENTER to close")
    elif reward == "Shoot'em Up":
        rekters.Mouse_Hold(command, 5)
        print("\n  press ENTER to close")
    else:
        print("That reward doesn't exist")
        print("\n press ENTER to close")

    rekters.Reset()


"""Not Essential:
It's good practice to wrap functions that run on init in a "main" conditional

This prevents the functions from being called accidentally if this file were 
ever to be imported into another script.
"""

if __name__ == "__main__":
    # Start pubsub
    pubsub = PubSub(twitch)
    pubsub.start()
    # We save the uuid provided to unlisten later
    uuid = pubsub.listen_channel_points(user_id, Channel_Pt_Controller)
    input("press ENTER to close")
    pubsub.unlisten(uuid)
    pubsub.stop()
