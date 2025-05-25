import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv("output.csv")

# Sınıfları grupla ve say
summary = df.groupby("Class")["Count"].sum()

# Grafik çiz
plt.figure(figsize=(8, 5))
summary.plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Araç Tespit Sayıları")
plt.xlabel("Araç Türü")
plt.ylabel("Toplam Sayı")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle="--", alpha=0.7)

# Grafiği göster
plt.tight_layout()
plt.show()
