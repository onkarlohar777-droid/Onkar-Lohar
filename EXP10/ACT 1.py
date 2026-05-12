# grocery_bill_calculator.py

import streamlit as st

st.set_page_config(page_title="Grocery Bill Calculator", page_icon="🛒")

st.title("🛒 Grocery Bill Calculator")

st.write("Enter grocery item details below:")

# List to store items
items = []

# Number of items
num_items = st.number_input("How many items?", min_value=1, step=1)

total_bill = 0

for i in range(num_items):
    st.subheader(f"Item {i+1}")

    item_name = st.text_input(f"Enter item name {i+1}", key=f"name{i}")

    price = st.number_input(
        f"Enter price of item {i+1}",
        min_value=0.0,
        format="%.2f",
        key=f"price{i}"
    )

    quantity = st.number_input(
        f"Enter quantity of item {i+1}",
        min_value=1,
        step=1,
        key=f"qty{i}"
    )

    item_total = price * quantity
    total_bill += item_total

    items.append([item_name, price, quantity, item_total])

# Display bill
if st.button("Generate Bill"):
    st.header("🧾 Final Bill")

    for item in items:
        st.write(
            f"**{item[0]}** → ₹{item[1]} × {item[2]} = ₹{item[3]:.2f}"
        )

    st.success(f"Total Grocery Bill: ₹{total_bill:.2f}")
