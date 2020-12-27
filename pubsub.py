from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from uuid import UUID
from your_stuff import dyll_id, dyll_secret, dyll_oa
import rekters

#Authentication
twitch = Twitch(dyll_id, dyll_secret)
twitch.authenticate_app([])
twitch.set_user_authentication(dyll_oa, [AuthScope.CHANNEL_READ_REDEMPTIONS], dyll_oa)
user_id = twitch.get_users(logins=['dyllbob'])['data'][0]['id']

#Controllers
def Channel_Pt_Controller(uuid: UUID, data: dict) -> None:
  redeemer = data["data"]["redemption"]["user"]["display_name"]
  reward = data["data"]["redemption"]["reward"]["title"]
  print(redeemer + " Is going to rekt you."

  if reward == "Do A Little Dance":
    rekters.Do_Alittle_Dance(rekters.shimmy, 5)
    print("press ENTER to close")
  elif reward = "Shoot'em Up":
    rekters.Shoot_em_Up()
    print("press ENTER to close")
  else :
    print("That reward doesn't exist")
    print("press ENTER to close")


# Start pubsub
pubsub = PubSub(twitch)
pubsub.start()
#We save the uuid provided to unlisten later
uuid = pubsub.listen_channel_points(user_id, Channel_Pt_Controller)
input("press ENTER to close")
pubsub.unlisten(uuid)
pubsub.stop()