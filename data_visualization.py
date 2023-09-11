import polars as pl
import plotly.express as px

data = pl.read_csv('/Users/udyansachdev/Downloads/World University Rankings 2023.csv')

result1 = data.groupby("Location").agg(pl.col("University Rank").count())
result2 = data.groupby("Location").agg(pl.col("Industry Income Score").mean())

joined = result1.join(result2, left_on="Location", right_on="Location")

fig = px.scatter(joined, x= joined['Industry Income Score'], y=joined["University Rank"], color=joined["Location"],
                 size=joined['University Rank'])
fig.update_layout(
    title="Analysing Top Universities",
    xaxis_title="Mean of Industry Income Score",
    yaxis_title="Count of Top Universities")
fig.show()
