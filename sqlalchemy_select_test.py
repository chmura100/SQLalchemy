from sqlalchemy import create_engine, text

# Połącz z bazą
engine = create_engine('sqlite:///database.db')

# Wykonaj SELECT
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()

# Wyświetl wynik
print("📋 5 pierwszych stacji:")
for row in result:
    print(row)