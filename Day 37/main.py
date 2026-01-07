import requests
import os
from dotenv import load_dotenv

load_dotenv()
from datetime import datetime

USERNAME = "mjc130"
TOKEN = os.getenv("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# graph_config = {
#     "id": "test1",
#     "name": "Tracking Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "shibafu",
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test1"

headers = {
    "X-USER-TOKEN": TOKEN
}

today=datetime.now()
print(today.strftime("%Y%m%d"))
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.5",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

#
# # pixel_editing_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test1/20260106"
# #
# # headers = {
# #     "X-USER-TOKEN": TOKEN
# # }
# #
# # pixel_config = {
# #     "quantity": "3",
# # }
# #
# # response = requests.put(url=pixel_editing_endpoint, json=pixel_config, headers=headers)
# # print(response.text)
#
#
#
# pixel_deleting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/test1/20260107"
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
#
#
# response = requests.delete(url=pixel_deleting_endpoint, headers=headers)
# print(response.text)