import matplotlib.pyplot as plt

x = ["Eletrônicos", "Vestuário", "Alimentos"]
y = [15000, 8000, 5000]

explode = [0.1, 0, 0]
cores = ['skyblue', 'lightgreen', 'gold']

fig = plt.figure(figsize=(6,4))

plt.pie(y, 
        labels = x, 
        autopct = '%1.1f%%', 
        explode = explode, 
        shadow = True,
        colors = cores)

plt.legend(x, 
           title = "Categorias", 
           loc ="upper right", 
           bbox_to_anchor = (1.3, 1))
plt.title("Valor total de estoque por categoria")
plt.show()