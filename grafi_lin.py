import matplotlib.pyplot as plt;

x = [1, 2, 3, 4, 5, 6, 7]
y=  [100, 95, 110, 105, 120, 115, 130]

plt.plot(x, y, marker="o", color="r")

plt.title("Estoque Diário")
plt.xlabel("Dias")
plt.ylabel("Quantidade")
plt.legend(["Estoque"])
plt.grid(True)
plt.show()

