import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.DataFrame({
    "Name": ["Abhimanyu","Adi","Anshika","Summit","Max","Vellentino","Shubh","Neeru"],
    "Marks":[40,50,45,33,12,34,47,29],
    "Class":["10th","12th","10th","12th","10th","12th","10th","12th"],
    "Fees":["Paid","Not Paid","Paid","Paid","Paid","Not Paid","Paid","Paid"]

    })

print(df.describe())
print(df[df["Marks"]>=45]["Name"])
print(df[df["Fees"]== "Not Paid"]["Name"])

print("Scholarship is given to ", df[df["Marks"]>df["Marks"].mean()]["Name"])

fig , ax = plt.subplots(1,2,figsize=(12,8))

ax[0].bar(df["Class"], df["Marks"], color="pink")
ax[0].set_title("Marks vs Class")
ax[0].set_xlabel("Class")
ax[0].set_ylabel("Marks")

ax[1].plot(df["Name"], df["Marks"], marker="o")
ax[1].set_title("Name vs Marks")
ax[1].set_xlabel("Name")
ax[1].set_ylabel("Marks")

plt.tight_layout()
plt.show()



