import requests


def ask_ollama(
    recommendations,
    goal,
    budget,
    vegetarian,
    meal_type
):

    food_information = ""

    for i, (_, row) in enumerate(
        recommendations.iterrows(),
        start=1
    ):

        food_information += f"""
Food {i}:
Name: {row['item']}
Stall: {row['stall']}
Price: ₹{row['price_inr']:.0f}
Calories: {row['total_calories_kcal']:.0f} kcal
Protein: {row['protein_g']:.1f} g
Carbohydrates: {row['carbs_g']:.1f} g
Fat: {row['fat_g']:.1f} g
Health Score: {row['health_score_10']:.1f}/10
Vegetarian: {row['vegetarian']}
Meal Type: {row['meal_type']}
"""

    prompt = f"""
You are an AI university canteen nutrition assistant.

The student has these preferences:

Goal: {goal}
Maximum budget: ₹{budget}
Vegetarian: {"Yes" if vegetarian else "No"}
Meal type: {meal_type}

The recommendation algorithm has already selected
the following foods:

{food_information}

Your job is NOT to select different foods.

Instead:

1. Identify the best option among the recommended foods.
2. Explain why it is suitable for the student's goal.
3. Briefly compare the other options.
4. Mention price, protein, calories and health score when useful.
5. Keep the explanation simple and practical.
6. Do not make medical claims.
7. Do not invent nutritional information.

Give the response in this format:

Best Choice:
[food name]

Why:
[2-3 sentences]

Other Good Options:
- [food] — [short reason]
- [food] — [short reason]

Tip:
[one practical sentence]
"""

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result["response"]

    except requests.exceptions.ConnectionError:

        return (
            "❌ Could not connect to Ollama.\n\n"
            "Make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        return (
            "❌ Ollama took too long to respond. "
            "Please try again."
        )

    except Exception as e:

        return f"❌ Ollama error: {str(e)}"
