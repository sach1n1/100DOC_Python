import pandas as pd

squirrel_count = pd.read_csv("Squirrel_Data.csv")

color = pd.DataFrame()

fur_color = squirrel_count["Primary Fur Color"].value_counts().index.tolist()
fur_color_count = squirrel_count["Primary Fur Color"].value_counts().tolist()

color_dict = {
    'fur_color': fur_color,
    'fur_color_count': fur_color_count
}

color_dataframe = pd.DataFrame(color_dict)

color_dataframe.to_csv("squirrel_color.csv")
