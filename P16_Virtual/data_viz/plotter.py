import matplotlib.pyplot as plt
from typing import List

def plot_histogram(data: List[float], title:str = "Histogram", xlabel: str = "Values", 
                   ylabel:str = "Frequency", bins: int = 5, color: str = "skyblue"):
    plt.figure(figsize=(8,6))
    plt.hist(data, bins = bins, color = color, edgecolor="black")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis='y', alpha=0.8)
    plt.show()