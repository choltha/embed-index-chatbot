import pandas as pd
import numpy as np

datafile_path = "./data/structured-content-ada.csv"
df = pd.read_csv(datafile_path)
df["ada_embedding"] = df.ada_embedding.apply(eval).apply(np.array)