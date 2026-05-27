import matplotlib.pyplot as plt

counts = [20, 40, 60, 80, 100]
no_sharing = [329.17, 555.38, 649.03, 791.54, 948.55]
sharing = [115.7, 164.53, 227.03, 255.18, 284.79]
kmeans = [116.04, 189.34, 219.59, 338.11, 322.27]

plt.figure(figsize=(8, 5))

plt.plot(counts, no_sharing, marker='o', markersize=8, linewidth=2, label='no_sharing')
plt.plot(counts, sharing, marker='s', markersize=8, linewidth=2, label='sharing')
plt.plot(counts, kmeans, marker='s', markersize=8, linewidth=2, label='kmeans')


plt.xlim(10, 110)
plt.ylim(0, 1000)

plt.xlabel('Number of Target points', fontsize=12)
plt.ylabel('Time (s)', fontsize=12)
plt.title('Simulation Time by Number of Target points', fontsize=14)
plt.xticks(counts)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()