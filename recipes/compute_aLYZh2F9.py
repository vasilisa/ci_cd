# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import io

from dataviz import plot_3d

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
dataset = dataiku.Dataset("transactions_joined_prepared")

df      = dataset.get_dataframe()

country = "US"

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_ny = df.loc[df["merchant_state"]=="New York"]

df_avg_purchase = df_ny[['card_age', 'purchase_year', 'purchase_amount']].groupby(['card_age', 'purchase_year'], as_index=False).mean()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
picture = plot_3d(df_avg_purchase, "purchase_year", "card_age", "purchase_amount", country)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs

folder = dataiku.Folder("aLYZh2F9")
folder.upload_stream(f"{country}-3D.png", picture.getvalue())