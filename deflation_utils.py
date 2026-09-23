"""Deflation utilities for ECON 5200 labs."""

import pandas as pd


def deflate_series(nominal, cpi, base_year=2020):
    """Convert a nominal time series to real (constant-dollar) values.

    Parameters
    ----------
    nominal : pd.Series
        Nominal values indexed by date.
    cpi : pd.Series
        CPI values indexed by date, at the SAME frequency and with the SAME
        seasonal adjustment as `nominal`.
    base_year : int
        Year whose dollars to express values in. The base is that year's
        average CPI.

    Returns
    -------
    pd.Series
        Real values in base_year dollars, on the dates both inputs share,
        with no missing values.

    Raises
    ------
    ValueError
        If base_year is not present in the CPI index, or if the two series
        share no dates.
    """
    if not (cpi.index.year == base_year).any():
        raise ValueError(f"Base year {base_year} not found in CPI data.")

    common_dates = nominal.index.intersection(cpi.index)

    if len(common_dates) == 0:
        raise ValueError("Nominal and CPI series share no dates.")

    nominal_aligned = nominal.loc[common_dates]
    cpi_aligned = cpi.loc[common_dates]

    combined = pd.concat(
        [nominal_aligned.rename("nominal"),
         cpi_aligned.rename("cpi")],
        axis=1
    ).dropna()

    base_cpi = cpi[cpi.index.year == base_year].mean()

    real = combined["nominal"] / combined["cpi"] * base_cpi

    return real


def profile_dataframe(data, unit_col="name", time_col="date"):
    """Return a dictionary describing the structure and completeness of data."""

    profile = {}
    profile["shape"] = data.shape

    profile["n_units"] = data[unit_col].nunique()
    profile["n_periods"] = data[time_col].nunique()

    if profile["n_units"] > 1 and profile["n_periods"] > 1:
        profile["structure"] = "panel"
    elif profile["n_periods"] > 1:
        profile["structure"] = "time series"
    else:
        profile["structure"] = "cross-sectional"

    periods_per_unit = data.groupby(unit_col)[time_col].nunique()

    complete = periods_per_unit[
        periods_per_unit == profile["n_periods"]
    ]

    profile["complete_units"] = len(complete)

    profile["balanced"] = (
        profile["complete_units"] == profile["n_units"]
    )

    missing = {}

    for col in data.columns:
        missing[col] = data[col].isna().mean() * 100

    profile["missing"] = missing

    return profile