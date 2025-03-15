import pandas as pd
import matplotlib.pyplot as plt  # ✅ Correct


df=pd.read_csv("cleaned_dataset.csv")
# def clean_time(timestamp):
#     return timestamp.astype(str).str[11:]
# df["Login Time"]=clean_time(df["Login Time"])
# df["Logout Time"]=clean_time(df["Logout Time"])
# df.to_csv("cleaned_dataset.csv",index=False)
# print(df.head())
df_sorted = df.sort_values(by="Count of Survey Attempts", ascending=False)

# Plot survey attempts distribution
# plt.hist(df["Count of Survey Attempts"], bins=20, edgecolor="black")
# plt.xlabel("Number of Survey Attempts")
# plt.ylabel("Frequency")
# plt.title("Distribution of Survey Attempts")
# plt.show()
login_attempts = df.groupby("Login Time")["Count of Survey Attempts"].sum()
logout_attempts = df.groupby("Logout Time")["Count of Survey Attempts"].sum()

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(login_attempts.index, login_attempts.values, marker="o", linestyle="-", label="Login Attempts")
plt.plot(logout_attempts.index, logout_attempts.values, marker="s", linestyle="--", label="Logout Attempts", alpha=0.7)

# Labels & Title
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Survey Attempts")
plt.title("Survey Attempts Based on Login & Logout Time")
plt.xticks(range(0, 24))  # Show all hours (0-23)
plt.legend()
plt.grid()

# Show plot
plt.show()