from sqlalchemy import create_engine, MetaData
import pymongo
import yaml

# MySQL
mysql_cred = yaml.safe_load(open('config/mysql_cred.yml'))

engine = create_engine('mysql+pymysql://{0:}:{1:}@{2:}:{3:}/{4:}'.format(
    mysql_cred['mysql_user'], 
    mysql_cred['mysql_password'], 
    mysql_cred['mysql_host'],
    mysql_cred['mysql_port'],
    mysql_cred['mysql_db'],
))

meta = MetaData()
db_connection = engine.connect()

# MongoDB
mongodb_cred = yaml.safe_load(open('config/mongodb_cred.yml'))

mongodb_engine = "mongodb://{0:}:{1:}@{2:}:{3:}".format(
    mongodb_cred['mongodb_user'],
    mongodb_cred['mongodb_password'],
    mongodb_cred['mongodb_host'],
    mongodb_cred['mongodb_port']
)

client = pymongo.MongoClient(mongodb_engine, serverSelectionTimeoutMS=5000)
db = client['{}'.format(mongodb_cred['mongodb_db'])]
collection = db['{}'.format(mongodb_cred['mongodb_collection'])]