import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [pow(x,3) for x in x_values]

plt.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Blues, s=5)

plt.title('Pow of Numbers', fontsize=24)
plt.xlabel('Values', fontsize=20)
plt.ylabel('Pows', fontsize=20)

plt.axis([0, 5, 0, 150])

plt.tick_params(axis='both', which='major', labelsize='14')


plt.show()