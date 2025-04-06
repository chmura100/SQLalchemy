from sqlalchemy import create_engine, text


engine = create_engine('sqlite:///database.db')


with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stations LIMIT 5")).fetchall()


print("📋 5 pierwszych stacji:")
for row in result:
    print(row)