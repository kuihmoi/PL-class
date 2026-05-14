import pandas as pd
import matplotlib.pyplot as plt
from typing import List

def validate_series(data: pd.Series, name: str) -> None:
    """Raise a descriptive error if data is not a non-empty Series"""
    if not isinstance(data, pd.Series):
        raise TypeError(
            f"{name} must be a pandas Series, got {type(data).__name__!r}"
        )
    if data.empty:
        raise ValueError(f"'{name}' is empty, nothing to plot")

def plot_bar_chart(data: pd.Series, title: str, xlabel: str, ylabel: str) -> None:
    validate_series(data)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(data.index.astype(str), data.values, color='steelblue', edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_line_chart(data: pd.Series, title: str, xlabel: str, ylabel: str) -> None:
    validate_series(data)
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        data.index.astype(str), data.values, 
        marker='o', color='tomato', linewidth=2,
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.5)
    plt.tight_layout()
    plt.show()