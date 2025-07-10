# negotion.py
# Streamlit app: Negotion
# ------------------------
import streamlit as st

# ---- Page setup -------------------------------------------------------------
st.set_page_config(page_title="Negotion", page_icon="💰", layout="centered")

st.title("💰 Negotiation App")

# ---- User input -------------------------------------------------------------
st.write("Enter a base amount and instantly see discounted and upsell prices.")

base_price = st.number_input(
    "Base amount",
    min_value=0.00,
    value=100.00,
    step=1.00,
    format="%.2f",
    key="base_price",
)

# ---- Percentage tables ------------------------------------------------------
discount_percents = [65, 85, 85, 100]   # ⬅️ Edit here if needed
upsell_percents   = [165, 145, 135, 100]

left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.subheader("Discounts")
    for pct in discount_percents:
        price = base_price * pct / 100
        st.write(f"**{pct}%** → ${price:,.2f}")

with right_col:
    st.subheader("Upsells")
    for pct in upsell_percents:
        price = base_price * pct / 100
        st.write(f"**{pct}%** → ${price:,.2f}")

# ---- Footer hint ------------------------------------------------------------
st.caption(
    "Built with Streamlit • Change the numbers or percentages as you like —"
    " the table updates instantly."
)

if __name__ == "__main__":
    # Streamlit handles execution; nothing needed here.
    pass
