import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine


plt.rcdefaults()

hostname = "127.0.0.1"
uname = "root"
pwd = ""
dbname = "movies"

engine = sqlalchemy.create_engine('mysql://root:@127.0.0.1:3306/movies')
df = pd.read_sql('movies',engine)
connection = engine.connect()


df = pd.read_sql_table('movies', engine)
plt.bar(df['Audiencescore'], df['RottenTomatoes'], width=0.5, align='edge', label='Audiencescore to RottenTomatoes')


plt.title('Audiencescore to RottenTomatoes') # Title, labels, and axis formatting
plt.xlabel('Audiencescore')
plt.ylabel('RottenTomatoes')
plt.xticks(rotation=-55, ha='left')
plt.yscale('log')
plt.grid(axis='y')
plt.legend()
plt.tight_layout()

formatter = matplotlib.ticker.ScalarFormatter()
formatter.set_powerlimits((0,25))
plt.gca().yaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_minor_locator(matplotlib.ticker.NullLocator())

plt.show()
