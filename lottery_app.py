code = """
import numpy as np
import pandas as pd
import streamlit as st

def generate_lottery_numbers(first_zone_probs, second_zone_probs, num_tickets=5):
    first_zone_numbers = first_zone_probs['號碼'].values
    first_zone_weights = first_zone_probs['機率'].values
    first_zone_weights /= first_zone_weights.sum()

    second_zone_numbers = second_zone_probs['號碼'].values
    second_zone_weights = second_zone_probs['機率'].values
    second_zone_weights /= second_zone_weights.sum()

    tickets = []
    for _ in range(num_tickets):
        first_zone_selection = np.random.choice(first_zone_numbers, size=6, replace=False, p=first_zone_weights)
        first_zone_selection.sort()
        second_zone_selection = np.random.choice(second_zone_numbers, size=1, replace=False, p=second_zone_weights)
        tickets.append(list(first_zone_selection) + list(second_zone_selection))

    return pd.DataFrame(tickets, columns=[\"號碼1\", \"號碼2\", \"號碼3\", \"號碼4\", \"號碼5\", \"號碼6\", \"第二區\"])

first_zone_probs = pd.DataFrame({
    '號碼': list(range(1, 39)),
    '機率': [0.026, 0.028, 0.025, 0.030, 0.027, 0.029, 0.024, 0.031, 0.022, 0.021, 0.023, 0.026, 0.028, 0.029, 0.027, 0.025, 0.030, 0.022, 0.031, 0.020, 0.019, 0.024, 0.026, 0.029, 0.030, 0.027, 0.025, 0.028, 0.023, 0.022, 0.026, 0.029, 0.030, 0.027, 0.025, 0.028, 0.022, 0.031]
})
first_zone_probs['機率'] /= first_zone_probs['機率'].sum()

second_zone_probs = pd.DataFrame({
    '號碼': list(range(1, 9)),
    '機率': [0.14, 0.12, 0.13, 0.11, 0.10, 0.09, 0.16, 0.15]
})
second_zone_probs['機率'] /= second_zone_probs['機率'].sum()

st.title(\"威力彩號碼產生器\")
st.write(\"根據歷史機率隨機生成號碼組合\")

num_tickets = st.number_input(\"請選擇要產生的組數\", min_value=1, max_value=20, value=5, step=1)
if st.button(\"產生號碼\"):
    lottery_tickets = generate_lottery_numbers(first_zone_probs, second_zone_probs, num_tickets=num_tickets)
    st.write(lottery_tickets)
"""

with open("lottery_app.py", "w") as f:
    f.write(code)

print("✅ lottery_app.py 已建立成功！")
