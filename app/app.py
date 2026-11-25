
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Zomato Restaurant Analytics",
    page_icon="🍽️",
    layout="centered"
)

# --------------------------------------------------
# MODEL LOADING
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "zomato_kmeans_deployment.joblib"

@st.cache_resource
def load_model_package():
    return joblib.load(MODEL_PATH)

package = load_model_package()

model = package["model"]
preprocessor = package["preprocessor"]

# --------------------------------------------------
# APPLICATION HEADER
# --------------------------------------------------

st.title("🍽️ Zomato Restaurant Analytics")
st.subheader("Restaurant Clustering Prediction")

st.write(
    "Enter restaurant details below to predict its cluster "
    "using the trained K-Means machine learning model."
)

st.info(
    "This application groups restaurants based on their "
    "characteristics. Cluster labels represent groups, "
    "not restaurant quality rankings."
)

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

st.header("Restaurant Details")

cost = st.number_input(
    "Approximate Cost for Two (₹)",
    min_value=0,
    max_value=100000,
    value=800,
    step=100
)

average_rating = st.slider(
    "Average Restaurant Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

avg_pictures = st.number_input(
    "Average Pictures per Review",
    min_value=0.0,
    max_value=100.0,
    value=0.3,
    step=0.1
)

cuisine_count = st.number_input(
    "Number of Cuisines",
    min_value=1,
    max_value=50,
    value=4,
    step=1
)

collection_status = st.selectbox(
    "Collection Status",
    options=["Listed", "No Collection Recorded"]
)

# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("Predict Restaurant Cluster", type="primary"):

    input_data = pd.DataFrame({
        "Cost": [cost],
        "Average_Rating": [average_rating],
        "Avg_Pictures_Per_Review": [avg_pictures],
        "Cuisine_Count": [cuisine_count],
        "Collection_Status": [collection_status]
    })

    transformed_data = preprocessor.transform(input_data)

    transformed_data = pd.DataFrame(
    	transformed_data,
    	columns=preprocessor.get_feature_names_out()
    )

    prediction = model.predict(transformed_data)

    st.success("Prediction completed successfully!")

    st.metric(
        label="Predicted Cluster",
        value=f"Cluster {prediction[0]}"
    )

    st.write("### Submitted Restaurant Details")

    display_data = input_data.copy()

    display_data["Predicted_Cluster"] = prediction

    st.dataframe(
        display_data,
        width="stretch"
    )

    st.caption(
        "The cluster number is an identifier assigned by "
        "the clustering algorithm and does not indicate "
        "a ranking or rating."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Machine Learning Model: K-Means Clustering | "
    "Built using Python, Scikit-learn and Streamlit"
)
