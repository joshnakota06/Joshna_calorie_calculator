
import streamlit as st

# =========================================================
# JOSHNA CALORIE CALCULATOR
# =========================================================

st.set_page_config(
    page_title="Joshna Calorie Calculator",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# HIGH-CONTRAST CSS
# =========================================================
st.markdown("""
<style>
/* ---------- Main page ---------- */
.stApp {
    background: linear-gradient(135deg, #E8F5E9 0%, #E3F2FD 50%, #FFF3E0 100%);
    color: #17202A !important;
}

/* Force readable text everywhere */
html, body, [class*="css"], p, span, div, label, h1, h2, h3, h4, h5, h6 {
    color: #17202A !important;
}

/* Streamlit markdown text */
.stMarkdown, .stMarkdown p {
    color: #17202A !important;
}

/* ---------- Header ---------- */
.hero {
    background: linear-gradient(135deg, #4527A0, #1565C0);
    padding: 28px 20px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 22px;
    box-shadow: 0 10px 25px rgba(69, 39, 160, 0.28);
    animation: slideDown 0.8s ease;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 40px;
    font-weight: 800;
    margin: 0 0 8px 0;
}

.hero p {
    color: #FFFFFF !important;
    font-size: 16px;
    margin: 0;
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-25px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ---------- Input card ---------- */
.input-card {
    background: #FFFFFF;
    border: 2px solid #BBDEFB;
    border-radius: 20px;
    padding: 22px;
    margin: 15px 0;
    box-shadow: 0 8px 22px rgba(21, 101, 192, 0.12);
    animation: fadeUp 0.7s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ---------- Headings ---------- */
h2, h3 {
    color: #283593 !important;
    font-weight: 800 !important;
}

/* ---------- Input labels ---------- */
label {
    color: #17202A !important;
    font-weight: 700 !important;
}

/* ---------- Number input / selectbox ---------- */
div[data-baseweb="input"] {
    background: #FFFFFF !important;
    border: 2px solid #90CAF9 !important;
    border-radius: 10px !important;
}

div[data-baseweb="input"] input {
    color: #17202A !important;
    background: #FFFFFF !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border: 2px solid #90CAF9 !important;
    border-radius: 10px !important;
    color: #17202A !important;
}

div[data-baseweb="select"] span {
    color: #17202A !important;
}

/* ---------- Calculate button ---------- */
.stButton > button {
    width: 100%;
    min-height: 52px;
    border: none !important;
    border-radius: 14px !important;
    background: linear-gradient(90deg, #6A1B9A, #1565C0) !important;
    color: #FFFFFF !important;
    font-size: 17px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 20px rgba(21, 101, 192, 0.30);
    transition: 0.25s ease;
}

.stButton > button p {
    color: #FFFFFF !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.01);
    background: linear-gradient(90deg, #4A148C, #0D47A1) !important;
}

/* ---------- Result ---------- */
.result-card {
    background: linear-gradient(135deg, #00695C, #00897B);
    color: #FFFFFF !important;
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    margin: 20px 0;
    box-shadow: 0 10px 25px rgba(0, 105, 92, 0.30);
    animation: popIn 0.7s ease;
}

.result-card h2,
.result-card p {
    color: #FFFFFF !important;
}

.result-number {
    color: #FFFFFF !important;
    font-size: 42px;
    font-weight: 900;
}

@keyframes popIn {
    0% { opacity: 0; transform: scale(0.75); }
    70% { transform: scale(1.04); }
    100% { opacity: 1; transform: scale(1); }
}

/* ---------- Metric boxes ---------- */
.metric-card {
    background: #FFFFFF;
    border: 2px solid #80CBC4;
    border-radius: 16px;
    padding: 18px 10px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0, 105, 92, 0.12);
}

.metric-card .metric-title {
    color: #37474F !important;
    font-weight: 700;
}

.metric-card .metric-value {
    color: #00695C !important;
    font-size: 25px;
    font-weight: 900;
}

/* ---------- Interpretation ---------- */
.tip {
    background: #FFF8E1;
    border-left: 7px solid #FFB300;
    border-radius: 12px;
    padding: 18px;
    color: #4E342E !important;
    box-shadow: 0 5px 15px rgba(255, 179, 0, 0.12);
}

.tip b, .tip {
    color: #4E342E !important;
}

/* ---------- Info / warning ---------- */
div[data-testid="stAlert"] p {
    color: #17202A !important;
    font-weight: 600 !important;
}

/* ---------- Expander ---------- */
div[data-testid="stExpander"] {
    background: #FFFFFF !important;
    border: 2px solid #CE93D8 !important;
    border-radius: 14px !important;
}

div[data-testid="stExpander"] summary {
    color: #4A148C !important;
    font-weight: 700 !important;
}

/* ---------- Footer ---------- */
.footer {
    text-align: center;
    color: #37474F !important;
    padding: 22px 0;
    font-size: 13px;
}

.footer b {
    color: #4527A0 !important;
}

/* ---------- Mobile ---------- */
@media (max-width: 600px) {
    .hero h1 {
        font-size: 30px;
    }

    .hero {
        padding: 22px 12px;
    }

    .result-number {
        font-size: 34px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="hero">
    <h1>🥗 Joshna Calorie Calculator</h1>
    <p>✨ Calculate your estimated daily calorie requirement ✨</p>
</div>
""", unsafe_allow_html=True)

st.info(
    "ℹ️ This calculator provides an estimate for educational purposes only. "
    "It is not medical or professional nutritional advice."
)

# =========================================================
# INPUTS
# =========================================================
st.markdown('<div class="input-card">', unsafe_allow_html=True)

st.markdown("### 👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age (years)",
        min_value=1,
        max_value=120,
        value=20,
        step=1
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=165.0,
        step=0.5
    )

with col2:
    weight = st.number_input(
        "Weight (kg)",
        min_value=10.0,
        max_value=300.0,
        value=60.0,
        step=0.5
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

activity = st.selectbox(
    "🏃 Activity Level",
    [
        "Sedentary - little or no exercise",
        "Lightly active - exercise 1-3 days/week",
        "Moderately active - exercise 3-5 days/week",
        "Very active - exercise 6-7 days/week",
        "Extra active - very hard exercise/physical job"
    ]
)

st.markdown('</div>', unsafe_allow_html=True)

activity_factors = {
    "Sedentary - little or no exercise": 1.20,
    "Lightly active - exercise 1-3 days/week": 1.375,
    "Moderately active - exercise 3-5 days/week": 1.55,
    "Very active - exercise 6-7 days/week": 1.725,
    "Extra active - very hard exercise/physical job": 1.90
}

# =========================================================
# CALCULATE
# =========================================================
if st.button("🧮 CALCULATE MY CALORIES"):

    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    daily_calories = bmr * activity_factors[activity]

    st.balloons()

    st.success("🎉 Calculation completed successfully!")

    st.markdown(
        f"""
        <div class="result-card">
            <h2>🔥 Your Estimated Daily Calories</h2>
            <div class="result-number">{daily_calories:,.0f} kcal/day</div>
            <p>Based on your personal details and activity level.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Metrics
    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">🔥 Estimated BMR</div>
                <div class="metric-value">{bmr:,.0f}</div>
                <div>kcal/day</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">🏃 Activity Factor</div>
                <div class="metric-value">{activity_factors[activity]}</div>
                <div>multiplier</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Interpretation
    st.markdown("### 💡 Simple Interpretation")

    if daily_calories < 1800:
        message = (
            "Your estimated requirement is relatively low. "
            "Focus on balanced meals, protein, fruits, vegetables and hydration."
        )
    elif daily_calories < 2500:
        message = (
            "Your estimated requirement is in a moderate range. "
            "Aim for balanced meals with protein, vegetables, fruits, whole grains "
            "and healthy fats."
        )
    else:
        message = (
            "Your estimated requirement is relatively high. "
            "This can be associated with higher activity levels or body size. "
            "Choose nutrient-dense foods and stay hydrated."
        )

    st.markdown(
        f"""
        <div class="tip">
            🥗 <b>Your result:</b> {message}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Details
    with st.expander("📋 VIEW CALCULATION DETAILS"):
        st.write(f"**Age:** {age} years")
        st.write(f"**Height:** {height:.1f} cm")
        st.write(f"**Weight:** {weight:.1f} kg")
        st.write(f"**Gender:** {gender}")
        st.write(f"**Activity level:** {activity}")
        st.write(f"**BMR:** {bmr:,.0f} kcal/day")
        st.write(f"**Daily calorie estimate:** {daily_calories:,.0f} kcal/day")

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    💜 <b>Joshna Calorie Calculator</b><br>
    Python + Streamlit • Colorful UI • Animated Interface • No Database
</div>
""", unsafe_allow_html=True)
