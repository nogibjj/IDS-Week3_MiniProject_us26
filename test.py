from polar_stats import stats_mean, stats_median, stats_mode, stats_std
import polars as pl

data = pl.read_csv("World University Rankings 2023.csv")

# Calculating values for "No of student per staff"


def test_values():
    assert (stats_mean(data)) == 16.72500000000001
    assert (stats_median(data)) == 13.5
    assert (stats_mode(data)[0]) == 10.3
    assert (stats_std(data)) == 10.557828968365255


test_values()
