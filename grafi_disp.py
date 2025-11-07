import matplotlib.pyplot as plt

x = [50, 120, 300, 80 ,20]
y = [80, 25, 10, 70, 150]

plt.scatter(x,y)
plt.title("Relação Preço e Quantidade")
plt.xlabel("Preço Unitario")
plt.ylabel("Quantidade")
plt.legend(["Quantidade"])
plt.show()