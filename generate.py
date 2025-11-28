# generate_strong_data.py
import pandas as pd
import numpy as np
import random

# Seed for reproducibility
np.random.seed(42)

n_samples = 1000

data = []

for _ in range(n_samples):
    food_type = random.choice(['Dairy', 'Fruit', 'Bakery', 'Vegetable'])
    storage = random.choice(['Fridge', 'Room', 'Freezer'])
    packaging = random.choice(['Sealed', 'Open'])
    temperature = round(np.random.uniform(-5, 40), 1)
    humidity = round(np.random.uniform(10, 100), 1)
    age = np.random.randint(0, 30)  # days since production

    # Simple spoilage logic for labeling
    expired = 0
    if food_type == 'Dairy':
        if storage != 'Fridge' or temperature > 10 or age > 10 or packaging == 'Open':
            expired = 1
    elif food_type == 'Fruit':
        if storage == 'Room' and (temperature > 25 or humidity > 80 or age > 7):
            expired = 1
    elif food_type == 'Bakery':
        if storage == 'Room' and age > 3:
            expired = 1
    elif food_type == 'Vegetable':
        if storage == 'Room' and age > 5:
            expired = 1
    # Freezer generally preserves food
    data.append([food_type, storage, packaging, temperature, humidity, age, expired])

df = pd.DataFrame(data, columns=['Type','Storage','Packaging','Temperature','Humidity','Age','Expired'])
df.to_csv('strong_food_data.csv', index=False)
print("Dataset saved as strong_food_data.csv")
