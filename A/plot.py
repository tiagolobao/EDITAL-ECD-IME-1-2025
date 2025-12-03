import matplotlib.pyplot as plt
import numpy as np

# Create sample data
np.random.seed(42)
x = np.arange(1, 11)
y1 = np.random.randn(10).cumsum()
y2 = x ** 2

# Create figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line plot
axes[0, 0].plot(x, y1, 'o-', color='steelblue')
axes[0, 0].set_title('Line Plot with Markers')

# 2. Scatter plot
axes[0, 1].scatter(x, y2, s=50, c=y2, cmap='viridis')
axes[0, 1].set_title('Scatter Plot with Colormap')

# 3. Bar chart
axes[1, 0].bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5], color='lightcoral')
axes[1, 0].set_title('Bar Chart')

# 4. Histogram
data = np.random.randn(1000)
axes[1, 1].hist(data, bins=30, edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Histogram')

plt.tight_layout()  # Adjust spacing
plt.savefig("./temp.png")
