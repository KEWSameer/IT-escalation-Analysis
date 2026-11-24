import os
import re
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/escalations_clean.csv")
df.columns = ["issue", "date"]
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%y")

rules = {
"Intercom": r"intercom",
"AWS WorkSpaces": r"aws",
"Backoffice": r"backoffice|\bbo\b|gr8",
"VPN": r"vpn",
"Login and access": r"log in|logging in|login|password|otp|2fa|access|account",
}

def categorize(text):
t = str(text).lower()
for name, pattern in rules.items():
if re.search(pattern, t):
return name
return "Other"

df["category"] = df["issue"].apply(categorize)

plt.figure()
df["category"].value_counts().plot(kind="bar", title="Escalations by category")
plt.tight_layout()
plt.savefig("charts/by_category.png")

weekly = df.groupby([pd.Grouper(key="date", freq="W"), "category"]).size().unstack(fill_value=0)
weekly.plot(title="Weekly escalations by category")
plt.tight_layout()
plt.savefig("charts/weekly_trend.png")

print(df["category"].value_counts())