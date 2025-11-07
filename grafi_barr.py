import matplotlib.pyplot as plt

x = ["Teclado", "Mouse", "Monitor", "WebCam"]
y = [50, 75, 30, 60] 

plt.bar(x, y, width = 0.50, color= "g")
plt.title("Armazenamento de Produtos")
plt.xlabel("Produtos")
plt.ylabel("Quantidade")
plt.legend(["Quantidade"])

plt.show()