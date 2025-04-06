from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String
engine = create_engine('sqlite:///database.db', echo=True)
meta = MetaData()

stations = Table(
    'stations', meta,
    Column('station', String, primary_key=True),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String),
)

measures = Table(
    'measures', meta,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('date', String),     
    Column('precip', Float),
    Column('tobs', Float)
)

meta.create_all(engine)
print("✅ Tabele zostały utworzone.")