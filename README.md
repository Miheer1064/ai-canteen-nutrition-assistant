# 🍽️ AI Canteen Nutrition Assistant

An AI-powered university canteen nutrition assistant that helps students choose suitable food based on their nutritional goal, budget, dietary preference, and meal type.

The system combines a **rule-based nutrition recommendation engine** with a **locally running Llama model through Ollama**.

The recommendation engine selects suitable food items from the university canteen dataset, while the Generative AI component provides a natural-language explanation of the recommendations.

---

## 📌 Problem Statement

University students often have multiple food choices available in their canteen but may find it difficult to select meals that match their:

- Nutritional goals
- Budget
- Dietary preferences
- Meal requirements

This project addresses this problem by providing an AI-assisted food recommendation system that uses the university canteen menu and user preferences to recommend suitable food options and explain the recommendations using Generative AI.

---

## 🎯 Objectives

The main objectives of the project are:

- Recommend suitable canteen food based on user preferences.
- Consider different nutritional goals.
- Respect the user's maximum budget.
- Support vegetarian food preferences.
- Filter recommendations according to meal type.
- Rank food items using nutritional and health-related information.
- Provide an AI-generated explanation of the recommendations.
- Run the complete application locally.

---

# ⭐ Features

## Personalized Recommendations

Users can specify:

- Health goal
- Maximum budget
- Vegetarian preference
- Meal type
- Number of recommendations

## Nutrition-Based Recommendation Engine

The recommendation engine uses information such as:

- Calories
- Protein
- Carbohydrates
- Fat
- Health score
- Price

The system filters unsuitable food items and ranks the remaining options according to the selected nutritional goal.

## Goal-Based Recommendations

The application supports different nutritional goals.

### 💪 Muscle Gain

Places greater importance on:

- Protein
- Appropriate calorie content

### ⚖️ Weight Loss

Places greater importance on:

- Health score
- Lower calorie content
- Protein

### 🥗 Healthy Eating

Places greater importance on:

- Health score
- Protein
- Reasonable calorie content
- Affordability

## 🤖 Generative AI Nutrition Explanation

The selected recommendations are passed to a locally running Llama model through Ollama.

Llama generates a natural-language explanation including:

- Which recommendation best matches the user's goal
- Why the option is suitable
- How alternative recommendations compare
- A practical nutrition tip

## 💻 Local AI Execution

The application is designed to run locally using:

- Python
- Streamlit
- Pandas
- Ollama
- Llama

No external AI API is required for the Generative AI component.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Dataset processing |
| Streamlit | Web application interface |
| Requests | Communication with Ollama |
| Ollama | Local LLM runtime |
| Llama | Generative AI explanation |
| Git | Version control |
| GitHub | Repository and project management |

---

# 🏗️ System Architecture

The system consists of five main components:

1. University canteen dataset
2. Streamlit user interface
3. Recommendation engine
4. Ollama local LLM service
5. Llama Generative AI model

### Workflow

```text
              Student
                 |
                 v
       +-------------------+
       | Streamlit UI      |
       | User Preferences  |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Recommendation    |
       | Engine            |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Filter & Rank     |
       | Food Items        |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Recommended Foods |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Ollama            |
       | Local LLM Runtime |
       +---------+---------+
                 |
                 v
       +-------------------+
       | Llama             |
       | AI Explanation    |
       +---------+---------+
                 |
                 v
       Personalized
       Nutrition Explanation
