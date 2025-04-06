from sqlalchemy import create_engine, text

# Połączenie z bazą danych
engine = create_engine("sqlite:///./database.db")
conn = engine.connect()

# 📌 1. Pięć pierwszych stacji
print("📍 5 pierwszych stacji:")
stations = conn.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()
for row in stations:
    print(row)

# 📌 2. Liczba wszystkich pomiarów
print("\n📊 Liczba wszystkich pomiarów:")
count = conn.execute(text("SELECT COUNT(*) FROM measures")).fetchone()
print(count[0])

# 📌 3. Ile pomiarów było w 2017 roku?
print("\n📅 Liczba pomiarów z 2017 roku:")
count_2017 = conn.execute(text("SELECT COUNT(*) FROM measures WHERE date LIKE '2017%'")).fetchone()
print(count_2017[0])

# 📌 4. Średnia temperatura w 2017
print("\n🌡️ Średnia temperatura w 2017 roku:")
avg_temp_2017 = conn.execute(text("SELECT AVG(tobs) FROM measures WHERE date LIKE '2017%'")).fetchone()
print(round(avg_temp_2017[0], 2))

# 📌 5. Wszystkie dane z jednej wybranej stacji
print("\n🏝️ Pomiar ze stacji 'USC00519397' (WAIKIKI):")
wai = conn.execute(text("SELECT * FROM measures WHERE station = 'USC00519397' LIMIT 5")).fetchall()
for row in wai:
    print(row)