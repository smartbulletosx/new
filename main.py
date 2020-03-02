import vk_api
import random
import time
import datetime

token = "a9943498c5e4ef6220587df537e9e9e7211e65181197a208402a2c1453a1d7ab7d250d5bbedd57345c164"

vk = vk_api.VkApi(token=token)

vk._auth_token()

admin_id = 160800192

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет" and id != admin_id:
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "ты хороший человек", "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()) + " " + str(id), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        print(E)
        time.sleep(1)


