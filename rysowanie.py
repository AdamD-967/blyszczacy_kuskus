import matplotlib.pyplot as plt

plt.figure()
plt.subplot(1, 2, 1)
plt.plot([0, 9, 9, 0, 0], [9, 9, 0, 0, 9])
plt.subplot(1, 2, 2)
plt.plot([2, 4], [4, 2], 'g*')
plt.show()