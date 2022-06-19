from sqlalchemy import create_engine, MetaData
import yaml

# DB Connection definition loaded from a yaml file
cred = yaml.safe_load(open('config/db_cred.yml'))
engine = create_engine('mysql+pymysql://{0:}:{1:}@{2:}:{3:}/{4:}'.format(
    cred['mysql_user'], 
    cred['mysql_password'], 
    cred['mysql_host'],
    cred['mysql_port'],
    cred['mysql_db'],
))

meta = MetaData()
db_connection = engine.connect()