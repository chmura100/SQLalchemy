import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('sqlite:///database.db')


stations_df = pd.read_csv("clean_stations.csv")
measures_df = pd.read_csv("clean_measure.csv")


stations_df.to_sql("stations", con=engine, if_exists="append", index=False)
measures_df.to_sql("measures", con=engine, if_exists="append", index=False)

print("✅ Dane zostały załadowane do bazy.")