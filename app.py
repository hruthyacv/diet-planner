import streamlit as st
import random
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Diet Planner", layout="centered")

st.title("🥗 AI Diet + Fitness Planner")

# ---------- INPUT ----------
goal = st.selectbox("Goal", ["Weight Loss","Weight Gain","Maintenance"])
diet = st.selectbox("Diet Type", ["Vegetarian","Non-Vegetarian"])
activity = st.selectbox("Activity Level", ["Low","Moderate","High"])

age = st.number_input("Age",10,80,20)
weight = st.number_input("Weight (kg)",30,150,60)
height = st.number_input("Height (cm)",120,220,170)

# ---------- BACKGROUND ----------
veg_bg = "https://images.unsplash.com/photo-1512621776951-a57141f2eefd"
nonveg_bg = "https://images.unsplash.com/photo-1600891964599-f61ba0e24092"

bg_url = veg_bg if diet == "Vegetarian" else nonveg_bg

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{bg_url}");
    background-size: cover;
    background-position: center;
}}

[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45);
}}

.block-container {{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(14px);
    border-radius: 25px;
    padding: 2rem;
}}

h1,h2,h3,label,p {{
    color: white !important;
}}

.card {{
    padding:15px;
    border-radius:20px;
    background: rgba(255,255,255,0.1);
    margin-bottom:10px;
}}
</style>
""", unsafe_allow_html=True)

# ---------- CALCULATIONS ----------
def calories():
    bmr = 10*weight + 6.25*height - 5*age + 5
    mult = {"Low":1.2,"Moderate":1.55,"High":1.9}
    cal = bmr * mult[activity]
    if goal=="Weight Loss": cal-=300
    elif goal=="Weight Gain": cal+=300
    return int(cal)

def macros(c):
    return {
        "Protein": int(c*0.3/4),
        "Carbs": int(c*0.4/4),
        "Fats": int(c*0.3/9)
    }

# ---------- DATA ----------
veg_data = {
    "Breakfast": ["Moong Dal Chilla","Vegetable Upma","Poha","Greek Yogurt"],
    "Lunch": ["Dal Rice","Veg Pulao","Quinoa Khichdi"],
    "Dinner": ["Roti Sabzi","Paneer Salad","Tofu Stir Fry"],
    "Snacks": ["Makhana","Chana Salad","Fruits"]
}

nonveg_data = {
    "Breakfast": ["Egg Omelette","Boiled Eggs","Egg Toast"],
    "Lunch": ["Chicken Rice","Fish Curry","Grilled Chicken"],
    "Dinner": ["Chicken Curry","Egg Bhurji","Fish + Veg"],
    "Snacks": ["Chicken Soup","Eggs","Yogurt"]
}

ingredients = {
    "Moong Dal Chilla":["Moong dal","Carrot"],
    "Dal Rice":["Rice","Dal"],
    "Paneer Salad":["Paneer","Vegetables"],
    "Chicken Rice":["Chicken","Rice"],
    "Fish Curry":["Fish","Spices"],
    "Egg Omelette":["Egg","Oil"]
}

# ---------- PLAN ----------
def generate_day():
    data = veg_data if diet=="Vegetarian" else nonveg_data
    return {k: random.choice(v) for k,v in data.items()}

if "plan" not in st.session_state:
    st.session_state.plan = generate_day()

if st.button("Generate Plan"):
    st.session_state.plan = generate_day()

# ---------- DAILY ----------
st.subheader("🍽 Daily Plan")
for k,v in st.session_state.plan.items():
    st.markdown(f"<div class='card'><b>{k}</b>: {v}</div>", unsafe_allow_html=True)

# ---------- CALORIES ----------
c = calories()
st.subheader("🔥 Calories")
st.success(f"{c} kcal")

# ---------- MACROS (FIXED PIE CHART) ----------
st.subheader("📊 Macros")

m = macros(c)

col1,col2,col3 = st.columns(3)
col1.metric("Protein", f"{m['Protein']}g")
col2.metric("Carbs", f"{m['Carbs']}g")
col3.metric("Fats", f"{m['Fats']}g")

df = pd.DataFrame({
    "Nutrient": ["Protein","Carbs","Fats"],
    "Grams": [m["Protein"], m["Carbs"], m["Fats"]]
})

st.subheader("🥧 Macro Distribution")

fig = px.pie(
    df,
    names="Nutrient",
    values="Grams",
    hole=0.3
)

st.plotly_chart(fig)

# ---------- FITNESS ----------
st.subheader("🏋 Fitness Plan")

if goal=="Weight Loss":
    plan = ["10k Steps","Cardio","HIIT"]
elif goal=="Weight Gain":
    plan = ["Weight Training","High Protein","Low Cardio"]
else:
    plan = ["Balanced Workout","8k Steps","Stretch"]

for p in plan:
    st.markdown(f"<div class='card'>{p}</div>", unsafe_allow_html=True)

# ---------- WEEKLY PLAN ----------
st.subheader("📅 Weekly Plan")

for i in range(7):
    d = generate_day()
    st.markdown(
        f"<div class='card'><b>Day {i+1}</b><br>🍳 {d['Breakfast']}<br>🍛 {d['Lunch']}<br>🍽 {d['Dinner']}</div>",
        unsafe_allow_html=True
    )

# ---------- GROCERY ----------
st.subheader("🛒 Grocery List")

items = []
for meal in st.session_state.plan.values():
    items.extend(ingredients.get(meal,[]))

for i in list(set(items)):
    st.markdown(f"<div class='card'>• {i}</div>", unsafe_allow_html=True)