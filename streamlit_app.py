# negotion.py
# ---------------------------------------------------------------------------
import streamlit as st

st.set_page_config(page_title="Negotion", page_icon="💰", layout="centered")
st.title("💰 Negotiation App")

# 1️⃣  Base amount ------------------------------------------------------------
base_price = st.number_input(
    "Base amount",
    min_value=0.00,
    value=100.00,
    step=1.00,
    format="%.2f",
)

# 2️⃣  Quick-Add buttons (10 / 20 / 30 % markup) -----------------------------
if "price_factor" not in st.session_state:
    st.session_state.price_factor = 1.00

st.write("### Quick-Add")
btn10, btn20, btn30 = st.columns(3)
if btn10.button("+10 %"):
    st.session_state.price_factor = 1.10
if btn20.button("+20 %"):
    st.session_state.price_factor = 1.20
if btn30.button("+30 %"):
    st.session_state.price_factor = 1.30

active_price = base_price * st.session_state.price_factor

# 3️⃣  Price tables & green goal figures -------------------------------------
discount_percents = [65, 85, 95, 100]
upsell_percents   = [165, 145, 135, 100]

goal_discount_price = active_price * min(discount_percents) / 100  # 65 % of active

left_col, right_col = st.columns(2, gap="large")

with left_col:
    st.markdown(
        f"### Goal Price Discount: "
        f"<span style='color:green'>${goal_discount_price:,.2f}</span>",
        unsafe_allow_html=True,
    )
    st.subheader("Discounts")
    for pct in discount_percents:
        st.write(f"{pct}% → **${active_price * pct / 100:,.2f}**")

with right_col:
    st.markdown(
        f"### Goal Price Increase: "
        f"<span style='color:green'>${active_price:,.2f}</span>",
        unsafe_allow_html=True,
    )
    st.subheader("Upsells")
    for pct in upsell_percents:
        st.write(f"{pct}% → **${active_price * pct / 100:,.2f}**")

st.caption(
    "Learn how to negotiate by using this strategy.\n" \
    "1. Find the market price\n" \
    "2. Find the realistic discount or price increase. Most people don't blink an eye at 10% percent\n" \
    "3. Use the discount or price increase from top to bottom. The first offer is a low ball or out of the park offer to prime the negotiation conversation. THEY WILL LIKEY SAY NO \n" \
    "4. Happy Negotiating! If you have any app ideas send me a message and I can create them for free!"
)

if __name__ == "__main__":
    pass
