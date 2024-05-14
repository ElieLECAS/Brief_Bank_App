from sqlalchemy import create_engine

db_user = "test_alchemy"
db_password = "test_alchemy"
db_host = "localhost"
db_port = "5432"
db_name = "test_alchemy"

db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(db_url)

try:
    conn = engine.connect()
    print('Success!')
except Exception as ex:
    print('ex')