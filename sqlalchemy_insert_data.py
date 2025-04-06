import pandas as pd
from sqlalchemy import create_engine

# Połączenie z bazą
engine = create_engine('sqlite:///database.db')

# Załaduj dane z CSV
stations_df = pd.read_csv("clean_stations.csv")
measures_df = pd.read_csv("clean_measure.csv")

# Wrzuć dane do odpowiednich tabel
stations_df.to_sql("stations", con=engine, if_exists="append", index=False)
measures_df.to_sql("measures", con=engine, if_exists="append", index=False)

print("✅ Dane zostały załadowane do bazy.")