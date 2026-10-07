import random
import streamlit as st

st.markdown("""### ➗ The Magic of Division ➗
##### Division is like fair sharing! Imagine you have six yummy cupcakes and three friends. You want everyone to enjoy equally, so you split them up. Each friend gets two cupcakes.

##### Example : 🧁🧁🧁🧁🧁🧁 ÷ 3 friends = 🧁🧁 each

##### That’s division: breaking a big group into smaller, equal parts. It’s the math of fairness, balance, and making sure everyone gets their share.""")

st.divider()

c1, c2 = st.columns(2)

with c2:
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Divide20by4.svg/960px-Divide20by4.svg.png"
    st.image(url, width=325)

with c1: 
    @st.cache_data
    def get_math_data():
        set_a = (random.randint(2, 20), random.randint(2, 20))
        set_b = (random.randint(2, 20), random.randint(2, 20))
        set_c = (random.randint(2, 20), random.randint(2, 20))
        set_d = (random.randint(2, 20), random.randint(2, 20))
        return set_a, set_b, set_c, set_d

    data_a, data_b, data_c, data_d = get_math_data()
    
    # Option 1 (The actual Question)
    divisor_1, answer_1 = data_a
    dividend_1 = divisor_1 * answer_1 

    # Option 2
    divisor_2, answer_2 = data_b
    dividend_2 = divisor_2 * answer_2

    # Option 3
    divisor_3, answer_3 = data_c
    dividend_3 = divisor_3 * answer_3

    # Option 4
    divisor_4, answer_4 = data_d
    dividend_4 = divisor_4 * answer_4

    st.markdown(f"#### ➗ Division  : {dividend_1} ÷ {divisor_1} = ❓")

    dct = {
        f"{dividend_1}/{divisor_1}": dividend_1 // divisor_1,
        f"{dividend_2}/{divisor_2}": dividend_2 // divisor_2,
        f"{dividend_3}/{divisor_3}": dividend_3 // divisor_3,
        f"{dividend_4}/{divisor_4}": dividend_4 // divisor_4
    }
    
    for key in dct:
        if key not in st.session_state:
            st.session_state[key] = dct[key]

    options = [dividend_1 // divisor_1, dividend_2 // divisor_2, dividend_3 // divisor_3, dividend_4 // divisor_4]

    if 'order' not in st.session_state:
        indices = [0, 1, 2, 3]
        random.shuffle(indices)
        st.session_state.order = indices

    shuffled_indices = st.session_state.order

    for i, label in enumerate(["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ"]):
        idx = shuffled_indices[i]
        val = options[idx]
        
        if st.button(f"{label}. {val}", use_container_width=True):
            if val == answer_1:
                st.success("Correct! ✅")
            else:
                st.error("Wrong! ❌")

    if st.button("Next Question ➡️"):
        st.cache_data.clear()
        st.session_state.clear()
        st.rerun()
    st.divider()