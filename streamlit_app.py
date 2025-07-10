# negotion.py
# ---------------------------------------------------------------------------
import streamlit as st

st.set_page_config(page_title="Negotion", page_icon="💰", layout="centered")
st.title("💰 Negotiation App")

# 1️⃣  Base amount ------------------------------------------------------------
base_price = st.number_input(
    "The Going Rate",
    min_value=0.00,
    value=100.00,
    step=1.00,
    format="%.2f",
)

# 2️⃣  Quick-Add buttons (10 / 20 / 30 %) ------------------------------------
if "price_factor" not in st.session_state:
    st.session_state.price_factor = 1.00
if "discount_pct" not in st.session_state:
    st.session_state.discount_pct = 0

st.write("### Quick Math")
btn10, btn20, btn30 = st.columns(3)
if btn10.button("10 %"):
    st.session_state.price_factor = 1.10
    st.session_state.discount_pct = 10
if btn20.button("20 %"):
    st.session_state.price_factor = 1.20
    st.session_state.discount_pct = 20
if btn30.button("30 %"):
    st.session_state.price_factor = 1.30
    st.session_state.discount_pct = 30

# 3️⃣  Derived goal prices ----------------------------------------------------
goal_discount_price = base_price * (1 - st.session_state.discount_pct / 100)
goal_increase_price = base_price * st.session_state.price_factor

# 4️⃣  Lookup percentages & labels -------------------------------------------
discount_percents = [65, 85, 95, 100]      # % of *discounted* price
upsell_percents   = [165, 145, 135, 100]   # % of *goal-increase* price
offer_labels      = ["1st offer", "2nd offer", "3rd offer", "final offer"]

# 5️⃣  Layout -----------------------------------------------------------------
left_col, right_col = st.columns(2, gap="large")

# 👉 LEFT: Goal Price Discount & further discounts
with left_col:
    st.markdown(
        f"### Goal Price Discount "
        f"<span style='color:green'>${goal_discount_price:,.2f}</span>",
        unsafe_allow_html=True,
    )
    st.subheader("Discount")
    for pct, label in zip(discount_percents, offer_labels):
        st.write(
            f"**{label}** — {pct}% → **${goal_discount_price * pct / 100:,.2f}**"
        )

# 👉 RIGHT: Goal Price Increase & upsells
with right_col:
    st.markdown(
        f"### Goal Price Increase "
        f"<span style='color:green'>${goal_increase_price:,.2f}</span>",
        unsafe_allow_html=True,
    )
    st.subheader("Upsell")
    for pct, label in zip(upsell_percents, offer_labels):
        st.write(
            f"**{label}** — {pct}% → **${goal_increase_price * pct / 100:,.2f}**"
        )

# 6️⃣  Footer -----------------------------------------------------------------
st.caption(
    "Negotiate smarter:\n"
    "1. Find the market price.\n"
    "2. Decide on a realistic discount or markup.\n"
    "3. Lead with an anchor, then work toward your goal.\n"
    "4. Happy negotiating! MESSAGE ME TO CREATE FREE APP IDEAS"
)

# 7️⃣  Bottom image (optional) ------------------------------------------------
# st.image("logo.png", use_column_width=True, caption="Powered by Negotiation Science")

if __name__ == "__main__":
    pass
