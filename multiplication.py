import random
import streamlit as st


st.markdown("""### ✖️ The Magic of Multiplication ✖️
##### Multiplication is like serving up more joy! Imagine you have two cheesy pizzas, and each of your three friends gets the same amount. Suddenly, you need six pizzas in total!

##### Example : 🍕🍕 × 3 friends = 🍕🍕🍕🍕🍕🍕

##### That’s multiplication: instead of adding again and again, you grow groups faster with one powerful step. It’s the math of building bigger feasts with fewer moves—your shortcut to super speed in numbers!
""")

st.divider()

c1, c2 = st.columns(2)

with c2 :
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Multiply_4_bags_3_marbles.svg/960px-Multiply_4_bags_3_marbles.svg.png"
    st.image(url, width = 290, caption = "total 12 balloons")

with c1 : 
    @st.cache_data
    def get_math_data():
        num1, num2 = random.randint(1, 20), random.randint(1, 20)
        num_1, num_2 = random.randint(1, 20), random.randint(1, 20)
        num__1, num__2 = random.randint(1, 20), random.randint(1, 20)
        numm1, numm2 = random.randint(1, 20), random.randint(1, 20)
        return num1, num2, num_1, num_2, num__1, num__2, numm1, numm2


    num1, num2, num_1, num_2, num__1, num__2, numm1, numm2  = get_math_data()
    
    st.markdown(f"#### ✖️ Multiplication : {num1} * {num2} = ❓")
    
    # option - 1
    math = f'{num1} x {num2}'
    res = num1 * num2

    # option - 2
    math_1 = f'{num_1} x {num_2}'
    res_1 = num_1 * num_2

    # option - 3
    math__1 = f'{num__1} x {num__2}'
    res__1 = num__1 * num__2

    # option - 4
    mathh1 = f'{numm1} x {numm2}'
    ress1 = numm1 * numm2


    options = [num1*num2, num_1*num_2, num__1*num__2, numm1*numm2]


    if 'order' not in st.session_state:
        indices = [0, 1, 2, 3]
        random.shuffle(indices)
        st.session_state.order = indices

    shuffled_indices = st.session_state.order


    for i, label in enumerate(["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ"]):
        idx = shuffled_indices[i]
        val = options[idx]
        
        if st.button(f"{label}. {val}", use_container_width=True):
            if val == res:
                st.success("Correct!✅")
            else:
                st.error("Wrong!❌")

    if st.button("Next Question ➡️"):
        st.cache_data.clear()
        st.session_state.clear()
        st.rerun()

    st.divider()