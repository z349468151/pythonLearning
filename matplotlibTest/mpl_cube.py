import matplotlib.pyplot as plt

x_value = [i for i in range(1, 10)]
y_value1 = [j ** 3 for j in x_value]
y_value2 = [k ** 2 for k in x_value]

plt.plot(x_value, y_value1, linewidth=5)
plt.plot(x_value, y_value2, c='c', linewidth=5)
plt.title("Cube Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
# plt.axis([0, 5001, 0, 125075015002])
plt.show()
