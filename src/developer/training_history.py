import streamlit as st
import pandas as pd
from .utils import get_suffix_paths


def get_training_history_df(dir_models="./models/", suffix_csv_file="_training_history.csv"):
    training_history_paths = get_suffix_paths(dir_path=dir_models, suffix=suffix_csv_file)

    if not training_history_paths:
        st.info("No training history files found.")
        return pd.DataFrame()

    history_dataframes = [pd.read_csv(path) for path in training_history_paths]

    df = (
        pd.concat(history_dataframes, ignore_index=True)
        .drop_duplicates(subset=["architecture", "epoch"])
        .sort_values(["architecture", "epoch"])
    )

    return df


def show_training_history(dir_models="./models/", suffix_csv_file="_training_history.csv"):
    df = get_training_history_df(dir_models=dir_models, suffix_csv_file=suffix_csv_file)

    if df.empty:
        return

    available_metrics = {
        "Train Loss": "train_loss",
        "Validation Loss": "val_loss",
        "Train Accuracy": "train_accuracy",
        "Validation Accuracy": "val_accuracy",
    }

    selected_metric_name = st.selectbox(
        "Wähle die Metrik, die du anzeigen möchtest:",
        options=list(available_metrics.keys()),
        index=0,
    )

    selected_column = available_metrics[selected_metric_name]

    # Both architectures shown as separate series for the selected metric
    plot_df = df.pivot(index="epoch", columns="architecture", values=selected_column).reset_index()

    # Rename columns to friendly labels
    plot_df.columns.name = None
    rename_map = {arch: f"{arch} — {selected_metric_name}" for arch in plot_df.columns if arch != "epoch"}
    plot_df = plot_df.rename(columns=rename_map)

    st.line_chart(
        data=plot_df,
        x="epoch",
        y=[col for col in plot_df.columns if col != "epoch"],
        width="stretch",
        height=500,
    )

    st.caption(f"Aktuell angezeigt: **{selected_metric_name}** — beide Modelle im Vergleich")
