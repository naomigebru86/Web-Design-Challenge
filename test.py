import pandas as pd
file = pd.read_csv("resources/cities.csv")
file.to_html('data.html')