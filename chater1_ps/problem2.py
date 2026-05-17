import pandas as pd

data = {
    'dish': ['paubhaji', 'Paneer', 'Matan', 'chiken'],
    'Price': [200, 110, 600, 900], # Changed 'price' to 'Price'
    'Category': ['Main', 'Main', 'Special', 'side']
}

df = pd.DataFrame(data)
print("--- Full Menu ---")
print(df)

# 4. Now 'Price' matches the dictionary key
print("\n--- Dishes cheaper than 160 ---")
cheap_dishes = df[df['Price'] < 160]
print(cheap_dishes)

# 5. Get the average price
avg = df['Price'].mean()
print(f"\nAverage Dish Price: {avg}")