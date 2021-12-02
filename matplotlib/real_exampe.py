import matplotlib.pyplot as plt
import csv

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        years = list(range(2009, 2020))
        # android = [6.8, 67.22, 220.67, 451.62, 761.29, 1004.68, 1160.21, 1271.02]
        # ios = [24.89, 46.6, 89.27, 130.13, 150.79, 191.43, 225.85, 216.07]
        # microsoft = [15.03, 12.38, 8.76, 16.94, 30.71, 35.13, 26.74, 6.94]
        plt.bar(years, row['Android'], label='Android')
        # color='C0' by default
        plt.bar(years, row["ios"], label='iOS')
        # color='C1' by default
        # plt.plot(years, microsoft, label='Microsoft')  # color='C2' by default
        plt.legend()
        plt.show()
