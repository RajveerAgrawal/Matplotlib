import pandas as pd
import matplotlib.pyplot as plt

url = 'https://drive.google.com/uc?id=1EcduqbDog6lNxb9tjCysvDgCFEpbRwVI'
data = pd.read_csv(url)

plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'], linestyle=':', marker='o', color='red', linewidth=3, markerfacecolor='black')
plt.title('Month-wise Profit of the Company')
plt.xlabel('Month')
plt.ylabel('Profit in dollars')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))
plt.plot(data['month_number'], data['facecream'], label='Face Cream', marker='o', linewidth=3)
plt.plot(data['month_number'], data['facewash'], label='Face Wash', marker='o', linewidth=3)
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste', marker='o', linewidth=3)
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap', marker='o', linewidth=3)
plt.plot(data['month_number'], data['shampoo'], label='Shampoo', marker='o', linewidth=3)
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer', marker='o', linewidth=3)
plt.title('Sales Data of All Products')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
bar_width = 0.35
index = data['month_number']
plt.bar(index - bar_width/2, data['facecream'], bar_width, label='Face Cream')
plt.bar(index + bar_width/2, data['facewash'], bar_width, label='Face Wash')
plt.title('Sales Comparison of Face Cream and Face Wash')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.xticks(index)
plt.legend()
plt.grid(True, axis='y')
plt.show()