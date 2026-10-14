drivers = ["Palou", "Power", "O'Ward", "Dixon", "Herta"]
wins = [5, 2, 3, 1, 2]
podiums = [10, 6, 8, 5, 7]
prize_money = [2500000, 1200000, 1800000, 900000, 1100000]

#Day1
total = 0
for x in wins:
    total=total+x
    print(sum)

for driver, win in zip(drivers, wins):
    if win >= 3:
        print(driver)
        
count=0
for x in podiums:
    if x>=7:
        count=count+1
        print(count)

def average_prize(prize_money):
    return sum(prize_money) / len(prize_money)

print(average_prize(prize_money))

highest_wins = 0
best_driver = ""

for driver, win in zip(drivers, wins):
    if win > highest_wins:
        highest_wins = win
        best_driver = driver

print("Driver:", best_driver)
print("Wins:", highest_wins)    

#day2

import numpy as np
drivers = np.array(["Palou", "Power", "O'Ward", "Dixon", "Herta"])
lap_times = np.array([59.8, 60.2, 59.5, 61.1, 60.0])
fuel_used = np.array([2.4, 2.5, 2.3, 2.7, 2.4])

print(np.mean(lap_times))
print(np.mean(fuel_used))
print(np.max(lap_times))

print(drivers[lap_times<60])
print(drivers[fuel_used>2.5])
order = np.argsort(lap_times)
print(drivers[order])

race_data = np.array([
    [59.8, 2.4],
    [60.2, 2.5],
    [59.5, 2.3],
    [61.1, 2.7],
    [60.0, 2.4]
])
print(race_data[:,0])
print(race_data[:,1])

print(np.mean(race_data,axis=0))

#day3
import pandas as pd
data = {
    "Driver": ["Palou", "Power", "O'Ward", "Dixon", "Herta", "Palou"],
    "Team": ["Ganassi", "Penske", "McLaren", "Ganassi", "Andretti", "Ganassi"],
    "Points": [250, 180, 210, 160, 190, 250],
    "Wins": [4, 2, 3, 1, 2, 4]
}
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.info())

print(df["Driver"][df["Points"]>190])
print(df.sort_values("Points",ascending=False))
print(df.groupby("Team")["Points"].sum())

    