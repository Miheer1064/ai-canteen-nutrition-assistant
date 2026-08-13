import streamlit as st
import pandas as pd
import os
from src.recommendation_engine import recommend_foods
from src.ollama_service import ask_ollama
# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Canteen Nutrition Assistant",
    page_icon="🥗",
    layout="wide"
)


# ============================================================
# 2. LOAD DATA
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

CSV_FILE = os.path.join(
    BASE_DIR,
    "data",
    "university_canteen_sample_menu.csv"
)


@st.cache_data
def load_data():

    data = pd.read_csv(CSV_FILE)

    data.columns = data.columns.str.strip()

    numeric_columns = [
        "price_inr",
        "total_calories_kcal",
        "protein_g",
        "carbs_g",
        "fat_g",
        "health_score_10"
    ]

    for column in numeric_columns:
        data[column] = pd.to_numeric(
            data[column],
            errors="coerce"
        )

    text_columns = [
        "stall",
        "item",
        "description",
        "vegetarian",
        "meal_type"
    ]

    for column in text_columns:
        data[column] = (
            data[column]
            .astype(str)
            .str.strip()
        )

    data["vegetarian"] = (
        data["vegetarian"]
        .str.lower()
        .replace({
            "yes": "Yes",
            "no": "No",        })
    )

    return data


df = load_data()



# ============================================================
# 6. TITLE
# ============================================================

st.title(
    "🥗 AI Canteen Nutrition Assistant"
)

st.write(
    "Get personalized university canteen food "
    "recommendations using nutrition data and "
    "Generative AI."
)

st.divider()


# ============================================================
# 7. SIDEBAR
# ============================================================

st.sidebar.header(
    "🎯 Your Preferences"
)


goal = st.sidebar.selectbox(
    "Goal",
    [
        "Healthy Eating",
        "Muscle Gain",
        "Weight Loss"
    ]
)


budget = st.sidebar.number_input(
    "Maximum Budget (₹)",
    min_value=20,
    max_value=1000,
    value=150,
    step=10
)


vegetarian = st.sidebar.checkbox(
    "Vegetarian Only",
    value=True
)


meal_types = [
    "All"
] + sorted(
    df["meal_type"]
    .dropna()
    .unique()
    .tolist()
)


meal_type = st.sidebar.selectbox(
    "Meal Type",
    meal_types
)


top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# ============================================================
# 8. BUTTON
# ============================================================

recommend_button = st.sidebar.button(
    "🔍 Find Recommendations",
    width="stretch"
)


# ============================================================
# 9. GENERATE RECOMMENDATIONS
# ============================================================

if recommend_button:

    recommendations = recommend_foods(
        dataframe=df,
        goal=goal,
        budget=budget,
        vegetarian=vegetarian,
        meal_type=meal_type,
        top_n=top_n
    )


    # --------------------------------------------------------
    # NO RESULTS
    # --------------------------------------------------------

    if recommendations.empty:

        st.warning(
            "No food items match your preferences."
        )

        st.info(
            "Try increasing your budget or "
            "selecting 'All' for meal type."
        )


    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    else:

        st.success(
            f"Found {len(recommendations)} "
            "suitable food options!"
        )


        # ====================================================
        # RECOMMENDATION TABLE
        # ====================================================

        st.subheader(
            "🍽️ Recommended Foods"
        )

        display_columns = [
            "item",
            "stall",
            "price_inr",
            "vegetarian",
            "total_calories_kcal",
            "protein_g",
            "health_score_10",
            "meal_type"
        ]

        display_data = recommendations[
            display_columns
        ].copy()

        display_data.columns = [
            "Food",
            "Stall",
            "Price (₹)",
            "Vegetarian",
            "Calories",
            "Protein (g)",
            "Health Score",
            "Meal Type"
        ]

        st.dataframe(
            display_data,
            width="stretch",
            hide_index=True
        )


        # ====================================================
        # INDIVIDUAL FOOD CARDS
        # ====================================================

        st.subheader(
            "📊 Food Details"
        )

        for i, (_, row) in enumerate(
            recommendations.iterrows(),
            start=1
        ):

            with st.container(border=True):

                st.markdown(
                    f"### {i}. {row['item']}"
                )

                st.write(
                    f"🏪 **Stall:** {row['stall']}"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Price",
                        f"₹{row['price_inr']:.0f}"
                    )

                with col2:

                    st.metric(
                        "Calories",
                        f"{row['total_calories_kcal']:.0f} kcal"
                    )

                with col3:

                    st.metric(
                        "Protein",
                        f"{row['protein_g']:.1f} g"
                    )

                with col4:

                    st.metric(
                        "Health Score",
                        f"{row['health_score_10']:.1f}/10"
                    )


        # ====================================================
        # OLLAMA / GENAI EXPLANATION
        # ====================================================

        st.divider()

        st.subheader(
            "🤖 AI Nutrition Explanation"
        )

        st.write(
            "Llama analyzes the recommended foods "
            "and explains which option best matches "
            "your preferences."
        )


        with st.spinner(
            "🤖 Llama is analyzing your recommendations..."
        ):

            ai_response = ask_ollama(
                recommendations,
                goal,
                budget,
                vegetarian,
                meal_type
            )


        st.markdown(ai_response)


# ============================================================
# 10. DEFAULT MENU
# ============================================================

else:

    st.subheader(
        "📋 University Canteen Menu"
    )

    st.write(
        f"{len(df)} food items available."
    )

    display_columns = [
        "stall",
        "item",
        "price_inr",
        "vegetarian",
        "total_calories_kcal",
        "protein_g",
        "meal_type"
    ]

    st.dataframe(
        df[display_columns],
        width="stretch",
        hide_index=True
    )


# ============================================================
# 11. FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Canteen Nutrition Assistant | "
    "Recommendation Engine + Ollama Llama"
)
