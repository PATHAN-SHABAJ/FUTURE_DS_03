
import pandas as pd
from pathlib import Path


df = pd.read_csv(Path("data/bank-full.csv"), sep=";")


total = len(df)
subscribed = (df["y"] == "yes").sum()
not_subscribed = (df["y"] == "no").sum()
conversion_rate = subscribed / total * 100


print(f"Total customers contacted: {total}")
print(f"Subscribed: {subscribed}")
print(f"Not subscribed: {not_subscribed}")
print(f"Conversion rate: {conversion_rate:.2f}%")


job_analysis = df.groupby("job")["y"].apply(
    lambda x: (x == "yes").mean() * 100
).sort_values(ascending=False)


print(job_analysis.round(2).to_string())


contact_analysis = df.groupby("contact")["y"].apply(
    lambda x: (x == "yes").mean() * 100
).sort_values(ascending=False)


print(contact_analysis.round(2).to_string())


previous_analysis = df.groupby("poutcome")["y"].apply(
    lambda x: (x == "yes").mean() * 100
).sort_values(ascending=False)

print("\nCONVERSION BY PREVIOUS OUTCOME")
print(previous_analysis.round(2).to_string())


df["subscribed"] = (df["y"] == "yes").astype(int)

overall = pd.DataFrame({
    "Metric": [
        "Total Customers",
        "Subscribed Customers",
        "Not Subscribed Customers",
        "Conversion Rate (%)"
    ],
    "Value": [
        total,
        int(subscribed),
        int(not_subscribed),
        round(conversion_rate, 2)
    ]
})

job_summary = df.groupby("job").agg(
    Customers=("subscribed", "size"),
    Subscribed=("subscribed", "sum"),
    Conversion_Rate=("subscribed", "mean")
).reset_index()

contact_summary = df.groupby("contact").agg(
    Customers=("subscribed", "size"),
    Subscribed=("subscribed", "sum"),
    Conversion_Rate=("subscribed", "mean")
).reset_index()

previous_summary = df.groupby("poutcome").agg(
    Customers=("subscribed", "size"),
    Subscribed=("subscribed", "sum"),
    Conversion_Rate=("subscribed", "mean")
).reset_index()

for table in [job_summary, contact_summary, previous_summary]:
    table["Conversion_Rate"] = (
        table["Conversion_Rate"] * 100
    ).round(2)


overall.to_csv("marketing_summary.csv", index=False)
job_summary.to_csv("conversion_by_job.csv", index=False)
contact_summary.to_csv("conversion_by_contact.csv", index=False)
previous_summary.to_csv(
    "conversion_by_previous_outcome.csv", index=False
)

