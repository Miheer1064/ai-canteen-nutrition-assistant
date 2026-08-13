# AI Canteen Nutrition Assistant

An AI-powered university canteen nutrition assistant that recommends suitable food items based on a student's health goal, budget, dietary preference, and meal type.

The system combines a rule-based nutrition recommendation engine with a locally running Llama model through Ollama to provide personalized explanations for the recommended foods.

---

## 1. Problem Statement

Students often have many food options available in a university canteen but may find it difficult to choose meals that match their nutritional goals, budget, dietary preferences, and meal requirements.

This project provides a simple AI-assisted system that helps students make more informed food choices from the available university canteen menu.

---

## 2. Objectives

The main objectives of the project are:

- Recommend suitable canteen food items based on user preferences.
- Consider the student's nutritional goal.
- Respect the user's maximum budget.
- Support vegetarian food preferences.
- Filter recommendations according to meal type.
- Rank food items using nutritional and health-related information.
- Use Generative AI to explain why the recommended foods may be suitable.

---

## 3. Features

### Personalized Recommendations

Users can specify:

- Health goal
- Maximum budget
- Vegetarian preference
- Meal type
- Number of recommendations

### Nutrition-Based Ranking

The recommendation engine considers:

- Calories
- Protein
- Carbohydrates
- Fat
- Health score
- Food price

### AI Nutrition Explanation

The recommended foods are passed to a locally running Llama model through Ollama.

Llama explains:

- Which recommended food is the best option.
- Why it matches the selected goal.
- How the other recommendations compare.
- A practical nutrition tip.

### Local Execution

The complete application can run locally using Streamlit and Ollama.

---

## 4. Technologies Used

- Python
- Pandas
- Streamlit
- Requests
- Ollama
- Llama
- Git
- GitHub

---

## 5. System Architecture

The system consists of four major components:

1. Canteen food dataset
2. Recommendation engine
3. Streamlit user interface
4. Ollama/Llama AI explanation service

The overall workflow is:

Student Preferences  
↓  
Streamlit Interface  
↓  
Recommendation Engine  
↓  
Top Food Recommendations  
↓  
Ollama / Llama  
↓  
AI Nutrition Explanation

The detailed architecture diagram is available in:

`docs/architecture.png`

---

## 6. Recommendation Methodology

The recommendation engine first filters food items according to the user's:

- Budget
- Vegetarian preference
- Meal type

The remaining foods are assigned a recommendation score.

The score considers nutritional and health-related factors such as:

- Protein
- Health score
- Calories
- Price

Different weights are applied depending on the selected goal.

For example:

### Muscle Gain

Higher importance is given to protein and adequate calories.

### Weight Loss

Higher importance is given to health score, lower calorie content, and protein.

### Healthy Eating

Higher importance is given to health score, protein, lower calorie content, and affordability.

---

## 7. Generative AI Integration

The recommendation engine determines which foods are recommended.

The Llama model does not replace the recommendation engine.

Instead, the selected recommendations and their nutritional information are provided to Llama.

Llama then generates a natural-language explanation of the recommendations.

This creates a separation between:

**Recommendation Logic**

and

**Generative AI Explanation**

---

## 8. Project Structure

```text
ai-canteen-nutrition-assistant/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── app.py
│
├── src/
│   ├── recommendation_engine.py
│   └── ollama_service.py
│
├── data/
│   └── university_canteen_sample_menu.csv
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   └── screenshots/
│
├── outputs/
│
└── demo/
    └── demo.mp4
