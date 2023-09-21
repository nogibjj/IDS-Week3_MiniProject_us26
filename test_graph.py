import polars as pl
import plotly.express as px
import os


def visualization():

    data = pl.read_csv("World University Rankings 2023.csv")

    result1 = data.group_by("Location").agg(pl.col("University Rank").count())
    result2 = data.group_by("Location").agg(pl.col("Industry Income Score").mean())

    joined = result1.join(result2, left_on="Location", right_on="Location")

    fig = px.scatter(
        joined,
        x=joined["Industry Income Score"],
        y=joined["University Rank"],
        color=joined["Location"],
        size=joined["University Rank"],
    )
    fig.update_layout(
        title="Analysing Top Universities",
        xaxis_title="Mean of Industry Income Score",
        yaxis_title="Count of Top Universities",
    )
    # fig.show()

    if not os.path.exists("output_graph"):
        os.mkdir("output_graph")

    fig.write_image("output_graph/visualization.png")


visualization()
