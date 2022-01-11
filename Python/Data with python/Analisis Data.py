
import pandas as pd

df.head(n)                      #to show te first n rows of data frame
df.tail(n)                      #Shows the bottom n rows of data frame
df.["xxx"]                      #To access a column

path='<xxx>'

df.to_csv(path)                 #to save the file changed


df.dtypes                       #Returns the data types of each column
df.describe()                   #Returns a statical summary
df.describe(include="all")      #provides full summary statics
df.info()                       #provides a concise summary of your dataframe

#Example 1
from dbmodule import connect

connection=connect('databasename','username','pswd')

cursor.execute('select * from mytable')
cursor = cursor.fetchall()

cursor.close()
connection.close()
#End 1

dataframe.dropna(subset=["price"], axis=0, inplace = True)     #to eliminate a missing value
axis=0                          #to drop the entire row
axis=1                          #to drow the entire column

dataframe.replace(missing_value, new_value)

#Example 1.1
df["normalized-losses"].mean()
df["normalized-losses"].replace(np.nan, mean)
#End 1.1

dataframe.dtypes()      #To identify data type
dataframe.astype()      #To convert data type

df["xxx"] = df["xxx"]/df["xxx"].max()
df["xxx"] = (df["xxx"]-df["xxx"].min())/(df["xxx"].max()-df["xxx"].min())
df["xxx"] = (df["xxx"]-df["xxx"].mean())/df["xxx"].std()

#Binning
bins = np.linspace(min(df["xxx"]),max(df["xxx"]))
group_names = ["low","Medium","High"]
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, inglude_lowest=True)

#Turning Categorical Variables into Quantitative Variables
pd.get_dummies(df["xxx"])


#EDA
#Descriptive Statistics
df.describe()
.value_counts()
sns.boxtplot(xxxxxxxx)

#GroupBy
dataframe.GroupBy()
#Example
df_test=df[['drive-wheels','body-style','price']]
df_grp=df_test.groupby(['drive-wheels','body-style'], as_index=False).mean()
df_grp
#End

df_pivot=df_grp.pivot(intex= 'drive-wheels',columns='body-style')

plt.pcolor(df_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

#Correlation
