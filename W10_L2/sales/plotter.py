import matplotlib.pyplot as plt
from typing import List

def plot_bar_chart(data: pd.Series, title: str, xlablel: str, ylabel: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(data.index.astype(str), data.values, color='steelblue')