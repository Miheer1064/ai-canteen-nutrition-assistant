import pandas as pd


# ============================================================
# NORMALIZATION
# ============================================================

def normalize(series):

    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series(
            1.0,
            index=series.index
        )

    return (
        (series - minimum)
        / (maximum - minimum)
    )


# ============================================================
# RECOMMENDATION ENGINE
# ============================================================

def recommend_foods(
    dataframe,
    goal="Healthy Eating",
    budget=150,
    vegetarian=True,
    meal_type="All",
    top_n=5
):

    data = dataframe.copy()

    # --------------------------------------------------------
    # BUDGET FILTER
    # --------------------------------------------------------

    data = data[
        data["price_inr"] <= budget
    ]

    # --------------------------------------------------------
    # VEGETARIAN FILTER
    # --------------------------------------------------------

    if vegetarian:

        data = data[
            data["vegetarian"].str.lower() == "yes"
        ]

    # --------------------------------------------------------
    # MEAL TYPE FILTER
    # --------------------------------------------------------

    if meal_type != "All":

        data = data[
            data["meal_type"] == meal_type
        ]

    # --------------------------------------------------------
    # NO RESULTS
    # --------------------------------------------------------

    if data.empty:
        return pd.DataFrame()

    # --------------------------------------------------------
    # PROTEIN SCORE
    # --------------------------------------------------------

    data["protein_score"] = normalize(
        data["protein_g"]
    )

    # --------------------------------------------------------
    # HEALTH SCORE
    # --------------------------------------------------------

    data["health_score"] = (
        data["health_score_10"] / 10
    )

    # --------------------------------------------------------
    # CALORIE SCORE
    # --------------------------------------------------------

    data["calorie_score"] = normalize(
        data["total_calories_kcal"]
    )

    data["calorie_inverse"] = (
        1 - data["calorie_score"]
    )

    # --------------------------------------------------------
    # PRICE SCORE
    # --------------------------------------------------------

    data["price_score"] = normalize(
        data["price_inr"]
    )

    data["price_inverse"] = (
        1 - data["price_score"]
    )

    # ========================================================
    # GOAL-BASED SCORING
    # ========================================================

    if goal == "Muscle Gain":

        data["recommendation_score"] = (
            data["protein_score"] * 55
            + data["health_score"] * 25
            + data["calorie_score"] * 10
            + data["price_inverse"] * 10
        )

    elif goal == "Weight Loss":

        data["recommendation_score"] = (
            data["health_score"] * 50
            + data["calorie_inverse"] * 25
            + data["protein_score"] * 15
            + data["price_inverse"] * 10
        )

    else:

        # Healthy Eating

        data["recommendation_score"] = (
            data["health_score"] * 55
            + data["protein_score"] * 20
            + data["calorie_inverse"] * 15
            + data["price_inverse"] * 10
        )

    # --------------------------------------------------------
    # SORT
    # --------------------------------------------------------

    data = data.sort_values(
        by="recommendation_score",
        ascending=False
    )

    # --------------------------------------------------------
    # TOP RESULTS
    # --------------------------------------------------------

    return data.head(top_n)
