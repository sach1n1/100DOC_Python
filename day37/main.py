import requests
import day37.config as config
from datetime import datetime

date = datetime.now().date().strftime("%Y%m%d")
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{config.USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{config.USERNAME}/graphs/{config.GRAPH_ID}"
update_pixel_endpoint = f"{pixel_endpoint}/{date}"


headers = {
    "X-USER-TOKEN": config.TOKEN
}


# Creating the graph
# graph_config = {
#     "id": f"{config.GRAPH_ID}",
#     "name": "Habit",
#     "unit": "random",
#     "type": "float",
#     "color": "shibafu"
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Adding a pixel
# pixel_params = {
#     "date": date,
#     "quantity": "5.6"
# }
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

# Updating a Pixel
# pixel_update_data = {
#     "quantity": "10.6"
# }
# response = requests.put(url=update_pixel_endpoint, json=pixel_update_data, headers=headers)

# Deleting a pixel
# response = requests.delete(url=update_pixel_endpoint, headers=headers)

# print(response.text)
