import random
from itertools import chain
from operator import itemgetter
from typing import List

import altair as alt
import pandas as pd
from vega_datasets import data


ESSAYER_BASE_CONFIG = {
    "width": "container",
    "height": "container",
    "config": {
        "background": None,
        "font": "Space Mono",
        "title": {
            "font": "Space Mono",
            "subtitleFont": "Space Mono",
            "fontWeight": "normal",
        },
        "axis": {
            "labelFont": "Space Mono",
            "titleFont": "Space Mono",
            "titleFontWeight": "normal",
            "titlePadding": 10,
        },
        "legend": {
            "labelFont": "Space Mono",
            "titleFont": "Space Mono",
            "titleFontWeight": "normal",
        },
        "text": {"font": "Space Mono"},
        "padding": 0,
    },
}


def essayer_light():
    config = ESSAYER_BASE_CONFIG.copy()
    config["config"]["mark"] = {"color": "black"}
    config["config"]["text"] = {"color": "black"}
    return config


def essayer_dark():
    config = ESSAYER_BASE_CONFIG.copy()
    config["config"]["group"] = {"strokeOpacity": 0}
    config["config"]["mark"] = {"color": "white"}
    config["config"]["text"] = {"color": "white"}
    config["config"]["title"]["color"] = "white"
    config["config"]["style"] = {
        "guide-label": {"fill": "white"},
        "guide-title": {"fill": "white"},
    }
    config["config"]["axis"].update(
        {"domainColor": "white", "gridColor": "#212121", "tickColor": "white"}
    )
    return config


alt.themes.register("essayer-light", essayer_light)
alt.themes.register("essayer-dark", essayer_dark)
THEMES = ["light", "dark"]

df = (
    pd.read_csv("assets/csv/ona18.csv", index_col=None)
    .rename(
        columns={
            "direct": "Direct",
            "fb": "Facebook",
            "goog": "Google Search",
            "gcs": "Google Chrome Suggestions",
            "goognews": "Google News",
            "twtr": "Twitter",
            "flipboard": "Flipboard",
            "outbrain": "Outbrain",
            "insta": "Instagram",
            "yahoo": "Yahoo",
            "date": "DATE",
        }
    )
    .melt("DATE", var_name="REFERRER", value_name="REFERRALS")
    .assign(
        **{"WEEKLY REFERRALS (BILLIONS)": lambda df: df["REFERRALS"] / 1e9}
    )
)

sort_order = (
    df.groupby("REFERRER")["REFERRALS"]
    .sum()
    .sort_values(ascending=False)
    .index.tolist()
)


def plot(theme: str):
    highlight = alt.selection(
        type="single", on="mouseover", fields=["REFERRER"], nearest=True
    )
    nearest = alt.selection(
        type="single",
        nearest=True,
        on="mouseover",
        fields=["REFERRER", "DATE"],
        empty="none",
    )

    base = (
        alt.Chart(df)
        .encode(
            x=alt.X("DATE:T", axis=alt.Axis(format="%b %y")),
            y="WEEKLY REFERRALS (BILLIONS):Q",
        )
        .properties(title="MOBILE VISITS TO NEWS SITES, BY SOURCE")
    )
    points = (
        base.mark_circle()
        .encode(opacity=alt.value(0))
        .add_selection(highlight)
        .add_selection(nearest)
    )
    lines = base.mark_line().encode(
        size=alt.condition(~highlight, alt.value(1), alt.value(3)),
        strokeDash=alt.StrokeDash(
            "REFERRER:N",
            legend=alt.Legend(
                orient="bottom", columns=4, direction="horizontal"
            ),
            sort=sort_order,
        ),
    )
    text = lines.mark_text(
        align="left", baseline="line-bottom", dx=5, dy=-5
    ).encode(
        text=alt.condition(nearest, "REFERRER:N", alt.value(" ")),
        size=alt.value(10),
    )

    chart = points + text + lines

    chart.save(f"assets/vega/ona18-{theme}.json")


for theme in THEMES:
    with alt.themes.enable(f"essayer-{theme}"):
        plot(theme)
