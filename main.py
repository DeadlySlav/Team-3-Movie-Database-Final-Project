#Team 3
#This code connects to the WAMP server and creates the tables below. The movies.csv file take the information within and stores it into the databases tables. 

import pandas as pd
from sqlalchemy import create_engine
hostname = "127.0.0.1"
uname = "root"
pwd = ""
dbname = "movies"
#Dylan and Suhad part
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))
df = pd.read_csv(r'C:\Users\dylan\Documents\movies.csv', index_col='Film', nrows=70);
connection = engine.connect()
df.to_sql('movies', con=engine, if_exists='append')
#Eric and Dylan part
engine.execute('CREATE TABLE movies_temp Like movies')
engine.execute(
    'INSERT INTO movies_temp SELECT DISTINCT Film, Genre, LeadStudio, Audiencescore, Profitability, RottenTomatoes, '
    'WorldwideGross, Year FROM movies')
engine.execute('DROP TABLE movies')
engine.execute('ALTER TABLE movies_temp RENAME TO movies')
connection.close()
