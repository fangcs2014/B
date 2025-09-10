import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np

# 创建图形和坐标轴
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

# 添加地图特征
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAKES, alpha=0.5, facecolor='lightblue')
ax.add_feature(cfeature.RIVERS, edgecolor='lightblue')

# 添加经纬网格
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')
gl.top_labels = False
gl.right_labels = False
gl.xlabel_style = {'size': 10}
gl.ylabel_style = {'size': 10}

# 设置标题
plt.title('World Map with Coordinates', fontsize=16)

# 设置显示范围（全球）
ax.set_global()

# 添加一些重要的经纬线
ax.axhline(0, color='red', linestyle='--', linewidth=1, label='Equator')
ax.axhline(23.5, color='orange', linestyle='--', linewidth=1, label='Tropic of Cancer')
ax.axhline(-23.5, color='orange', linestyle='--', linewidth=1, label='Tropic of Capricorn')
ax.axvline(0, color='blue', linestyle='--', linewidth=1, label='Prime Meridian')

# 添加图例
plt.legend(loc='lower left')

# 显示图形
plt.tight_layout()
plt.show()