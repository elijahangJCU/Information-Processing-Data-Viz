# Exercise 1 — Environment + first plot

import matplotlib.pyplot as plt

# Exercise 1

# y = [3, 7, 4, 9, 6]
#
# fig, ax = plt.subplots()
# ax.plot(y)
# plt.show()


# Exercise 2

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 1, 8, 7]
#
#
# fig2, ax2 = plt.subplots()
# ax2.plot(x, y)
# plt.show()
#
# plt.plot(x, y)
# plt.show()


# Exercise 3

# x = [10, 20, 30, 40]
# y = [1, 4, 9, 16]
# bad_x = [10, 20, 30]
#
# fig1, ax1 = plt.subplots()
# ax1.plot(x, y)
#
# fig2, ax2 = plt.subplots()
# ax2.plot(y)
#
# fig3, ax3 = plt.subplots()
# ax3.plot(bad_x, y[:3])
#
# plt.show()


# Exercise 4

# months = ["Jan","Feb","Mar","Apr","May"]
# sales = [12, 18, 7, 22, 15]
#
# height = [150, 160, 165, 170, 172, 180, 155, 168, 175, 162]
#
# study_hours = [1, 2, 3, 4, 5, 6]
# scores = [52, 55, 60, 63, 70, 78]
#
# fig1, ax1 = plt.subplots()
# ax1.plot(study_hours, scores)
# plt.show()
#
# fig2, ax2 = plt.subplots()
# ax2.scatter(study_hours, scores)
# plt.show()
#
# fig3, ax3 = plt.subplots()
# ax3.bar(months, sales)
# plt.show()
#
# fig4, ax4 = plt.subplots()
# ax4.hist(height, bins=5)
# plt.show()


# Exercise 5

# x = [1,2,3,4,5,6]
# baseline = [10,10,10,10,10,10]
# actual   = [8, 9, 11, 13, 12, 14]
# forecast = [14, 15, 16, 16, 17, 18]
#
# fig, ax = plt.subplots()
# ax.plot(x, baseline, linestyle='--', alpha=1, label='baseline')
# ax.plot(x, actual, linestyle='-', marker='o', alpha=1, label='actual')
# ax.plot(x, forecast, linestyle=':', alpha=0.5, label='forecast')
# ax.legend(loc='best')
# ax.set_title('Comparison between forecasted and actual')
#
# plt.show()


#  Exercise 6

# days = [1,2,3,4,5,6]
# inventory = [50, 50, 40, 40, 70, 70]
#
# fig, ax = plt.subplots()
# ax.plot(days, inventory, label='Inventory not stepped', color='red')
# ax.plot(days, inventory, drawstyle='steps-post', label="Inventory stepped", color='blue')
# ax.legend()
# ax.set_title('Inventory over time')
#
# plt.show()


# Exercise 7

# x = [0, 1, 2, 3, 4]
# y = [100, 102, 101, 103, 104]
#
# fig1, ax1 = plt.subplots()
# ax1.plot(x, y)
# plt.show()
#
# fig2, ax2 = plt.subplots()
# ax2.plot(x, y)
# ax2.set_ylim(0, 200)
# plt.show()


#  Exercise 8

# years = [2000, 2005, 2010, 2015, 2020]
# revenue = [2, 3, 5, 8, 13]
#
# fig, ax = plt.subplots()
# ax.plot(years, revenue)
# ax.set_xlabel('Year')
# ax.set_ylabel('Revenue')
# ax.set_title('Revenue vs Year')
# ax.set_xticks([2000, 2010, 2020])
# ax.tick_params(rotation=45)
# plt.tight_layout()
# plt.show()