# imoprt modules
import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# get the data
data = pd.read_csv("20 Buildings.csv")
# get information about the data
print(data.shape)
print(data.dtypes)
print(data.columns.values)
print(data.isna().sum())
print(data.head())

# get the sum of all workers
print(data["Working_days"].sum())
# show density of workering days
plt.figure(figsize=(10,5))
sns.distplot(data["Working_days"],color="g")
plt.tight_layout()
plt.show()

# get countplot for Floors_num
print(data["Floors_num"].value_counts())
# show countplot for Floors_num
plt.figure(figsize=(10,5))
sns.countplot(data["Floors_num"])
plt.tight_layout()
plt.show()

# get all profits
data["Profits"] = data["flat_sale_price"] - data["flat_cost"]
print("-"*100)
data["Profits"] = data["Profits"] * data["Flats_num"]
print(data["Profits"].head())
# get the sum of all profits
print(data["Profits"].sum())

# get the sum of all Flats_num
print(data["Flats_num"].sum())

# show the correnation between the data
plt.figure(figsize=(10,5))
plt.title("The heatmap for data")
sns.heatmap(data.corr(), annot=True, cmap='Greens')
plt.tight_layout()
plt.show()


