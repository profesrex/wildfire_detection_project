import pandas as pd
import streamlit as st

from developer.training_history import show_training_history

MODELS_DIR = "./models/"
TRAINING_CSV_SUFFIX = "_training_history.csv"
EVALUATION_PATH = "./models/evaluation_predictions.csv"


def compute_false_negatives(evaluation_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes false negatives (predicted no_fire, actual fire) for each model.
    Returns a summary DataFrame with FN count, total positives, and FN rate per model.
    """
    models = {
        "MobileNet V3 Small": "pred_mobilenet_v3_small",
        "ResNet18": "pred_resnet18",
    }

    rows = []
    total_actual_fire = (evaluation_df["ground_truth"] == "fire").sum()

    for model_name, pred_col in models.items():
        fn = ((evaluation_df["ground_truth"] == "fire") & (evaluation_df[pred_col] == "no_fire")).sum()
        fn_rate = fn / total_actual_fire if total_actual_fire > 0 else 0.0
        rows.append(
            {
                "Model": model_name,
                "False Negatives": int(fn),
                "Total Actual Fire": int(total_actual_fire),
                "FN Rate": round(fn_rate, 4),
            }
        )

    return pd.DataFrame(rows)


def show_false_negatives(evaluation_df: pd.DataFrame):
    st.subheader("False Negatives (fire missed as no_fire)")

    fn_df = compute_false_negatives(evaluation_df)

    col1, col2 = st.columns(2)
    for i, row in fn_df.iterrows():
        col = col1 if i == 0 else col2
        with col:
            st.metric(
                label=row["Model"],
                value=f"{row['False Negatives']} FN",
                delta=f"{row['FN Rate'] * 100:.1f}% of actual fires missed",
                delta_color="inverse",
            )

    st.dataframe(fn_df, use_container_width=True, hide_index=True)

    # Bar chart comparing FN counts side by side
    chart_df = fn_df.set_index("Model")[["False Negatives"]]
    st.bar_chart(chart_df, height=300)


def main():
    st.title("ML Dashboard")

    st.header("Training History")
    show_training_history(MODELS_DIR, TRAINING_CSV_SUFFIX)

    st.header("Evaluation")
    evaluation_df = pd.read_csv(EVALUATION_PATH)

    show_false_negatives(evaluation_df)

    with st.expander("Show raw evaluation data"):
        st.dataframe(evaluation_df, use_container_width=True)


if __name__ == "__main__":
    main()
