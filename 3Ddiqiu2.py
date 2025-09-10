import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和3D轴
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 生成球面坐标
u = np.linspace(0, 2 * np.pi, 100)  # 经度参数
v = np.linspace(0, np.pi, 50)       # 纬度参数

# 计算球面坐标
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# 绘制地球表面
ax.plot_surface(x, y, z, color='lightblue', alpha=0.6, rstride=2, cstride=2)

# 添加经纬网格
u_grid = np.linspace(0, 2 * np.pi, 13)
v_grid = np.linspace(0, np.pi, 7)

for u_val in u_grid:
    x = np.cos(u_val) * np.sin(v)
    y = np.sin(u_val) * np.sin(v)
    z = np.cos(v)
    ax.plot(x, y, z, color='gray', alpha=0.5, linewidth=0.5)

for v_val in v_grid:
    u = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(u) * np.sin(v_val)
    y = np.sin(u) * np.sin(v_val)
    z = np.cos(v_val) * np.ones_like(u)
    ax.plot(x, y, z, color='gray', alpha=0.5, linewidth=0.5)

# 设置轴范围和标签
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_box_aspect([1, 1, 1])  # 保持纵横比

# 设置标题
plt.title('3D地球模型 - Matplotlib', fontsize=14)

# 显示图形
plt.show()