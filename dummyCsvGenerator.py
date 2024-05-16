import pandas as pd

# Dummy veri setini oluşturma
data = {
    'Transaction': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Milk': [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    'Bread': [1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    'Butter': [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    'Cheese': [0, 1, 1, 0, 1, 1, 0, 0, 1, 1],
    'Eggs': [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

# Veri setini CSV dosyasına kaydetme
df.to_csv('dummy_dataset.csv', index=False)
