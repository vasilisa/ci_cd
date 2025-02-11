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



# Read recipe inputs
dataset = dataiku.Dataset("transactions_joined_prepared")
df      = transactions_joined_prepared.get_dataframe()


# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_ny = df.loc[df["merchant_state"]=="New York"]

df_avg_purchase = df_ny[['card_age', 'purchase_year', 'purchase_amount']].groupby(['card_age', 'purchase_year'], as_index=False).mean()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
picture = plot_3d(df_avg_purchase, "purchase_year", "card_age", "purchase_amount", country)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
folder = dataiku.Folder("07joGq0S")
folder.upload_stream(f"{country}-3D.png", picture.getvalue())




# Write recipe outputs
output_dataviz = dataiku.Folder("aLYZh2F9")
output_dataviz_info = output_dataviz.get_info()
