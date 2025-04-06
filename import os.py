import os
print(os.path.abspath("database.db"))
engine = create_engine('sqlite:///./database.db')
