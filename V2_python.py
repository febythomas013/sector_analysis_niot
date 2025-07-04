import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("📊 Sectoral Impact Analysis for India (based on NIOT 2022)")

# === Load real Leontief matrix ===
leontief_df = pd.read_excel(r"NIOT_2022.xlsx", sheet_name="Leontief_Val", index_col=0)
L_matrix = leontief_df.values
sector_names = leontief_df.index.tolist()
n = len(sector_names)

# === Sidebar: User input shocks ===
st.sidebar.header("⚙️ Apply Sectoral Demand Shocks")

shock_dict = {}
selected_sectors = st.sidebar.multiselect("Select sectors to apply demand shocks:", sector_names)

for sector in selected_sectors:
    shock_dict[sector] = st.sidebar.slider(f"{sector} Shock (%)", -100, 100, 5)

# === Shock vector ===
shock_vector = np.zeros(n)
for idx, name in enumerate(sector_names):
    if name in shock_dict:
        shock_vector[idx] = shock_dict[name] / 100.0

# === Output vector: Leontief simulation ===
impact_vector = L_matrix @ shock_vector
impact_percent = impact_vector * 100

# === Output DataFrame ===
impact_df = pd.DataFrame({
    "Sector": sector_names,
    "Change in Output (%)": np.round(impact_percent, 2)
}).sort_values("Change in Output (%)", ascending=False)

# === Show results ===
st.subheader("📉 Output Change by Sector")
st.dataframe(impact_df, use_container_width=True)

st.subheader("📈 Visualize Sectoral Impact")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(y="Sector", x="Change in Output (%)", data=impact_df, palette="crest", ax=ax)
ax.axvline(0, color='gray', linestyle='--')
st.pyplot(fig)
