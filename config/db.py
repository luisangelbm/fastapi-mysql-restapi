from sqlalchemy import create_engine, MetaData

# create_engine("mysql+pymsql://root:password@localhost:3306/")
engine = create_engine("mysql+pymysql://root@localhost:3306/storedb")

meta = MetaData()
conn = engine.connect()