import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from typing import Sequence

def plot_results(
    infected: Sequence[float],
    *,
    figsize: tuple[int, int] = (10, 6),
    color: str = "#AA0000",
    linestyle: str = "dashed",
    marker: str = "o",
    xlabel: str = "Day",
    ylabel: str = "Number of Infected Cases",
    title: str = "Simulated Outbreak",
    label_fontsize: int = 16,
    title_fontsize: int = 20,
    grid_alpha: float = 0.2,
) -> Figure:
    """Plots the time series of infected cases."""
    
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.plot(infected, color=color, linestyle=linestyle, marker=marker)
    ax.set_xlabel(xlabel, fontsize=label_fontsize)
    ax.set_ylabel(ylabel, fontsize=label_fontsize)
    ax.set_title(title, fontsize=title_fontsize)
    ax.grid(alpha=grid_alpha)
    return fig
