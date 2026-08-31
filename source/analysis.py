import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

connection = psycopg2.connect(
    host="localhost",
    database="airflow",
    user="airflow",
    password="airflow",
    port=5432
)

query = "SELECT * FROM weather_data"

df = pd.read_sql(query, connection)

print(df)

df.info()
print("\nMissing values:", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

connection.close()

print ("\naverage temperature:", df["temperature"].mean())
print ("\nnumber of record:" , len(df))
print ("\ntemperature maximum:" , df["temperature"].max())


print("\nFirst record:", df["time"].min())
print("Last record:", df["time"].max())
print("Time range:", df["time"].max() - df["time"].min())

print("\n************\n")
print("Statistics:")
print (df["temperature"].describe())

plt.plot(df["time"], df["temperature"], marker="o")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()