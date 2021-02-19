import matplotlib.pyplot as plt

snack_scores = [50, 35, 15]

slice_labels = ["cheese poofs", "peanuts", "pretzels"]

colors = ['#FF8C00', '#0000FF', '#006400']

plt.pie(snack_scores,labels=slice_labels, colors=colors)

plt.title("Tasha's favorite snacks", fontsize=26)

plt.savefig("tashasnacks.png")