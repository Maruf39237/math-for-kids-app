import random
import streamlit as st


st.markdown("""### ➖ The Magic of Subtraction ➖
##### Subtraction is like sharing or savoring less! Imagine you have three glasses of rich red wine on the table. You pour one out for a friend to enjoy. Now, only two glasses remain for you.

##### Example : 🍷🍷🍷 − 🍷 = 🍷🍷

##### That’s subtraction: starting with a full set and gently taking some away. It’s the math of sharing, balance, and discovering what’s left behind. Every time you subtract, your problem-solving powers become more refined—like a fine wine!
""")

st.divider()

c1, c2 = st.columns(2)

with c2 :
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Subtraction01.svg/1280px-Subtraction01.svg.png"
    st.image(url, width = 345, caption = "minus is so fun!!")
    

with c1 : 
    @st.cache_data
    def get_math_data():
        num1, num2 = random.randint(1, 20), random.randint(1, 20)
        num_1, num_2 = random.randint(1, 20), random.randint(1, 20)
        num__1, num__2 = random.randint(1, 20), random.randint(1, 20)
        numm1, numm2 = random.randint(1, 20), random.randint(1, 20)
        return num1, num2, num_1, num_2, num__1, num__2, numm1, numm2


    num1, num2, num_1, num_2, num__1, num__2, numm1, numm2  = get_math_data()

    if num1 < num2 :
        tmp = num1
        num1 = num2
        num2 = tmp

    if num_1 < num_2 :
        tmp = num_1
        num_1 = num_2
        num_2 = tmp

    if num__1 < num__2 :
        tmp = num__1
        num__1 = num__2
        num__2 = tmp

    if numm1 < numm2 :
        tmp = numm1
        numm1 = numm2
        numm2 = tmp

    st.markdown(f"#### ➖Subtraction : {num1} - {num2} = ❓")
    
    # option - 1
    math = f'{num1} - {num2}'
    res = num1 - num2

    # option - 2
    math_1 = f'{num_1} - {num_2}'
    res_1 = num_1 - num_2

    # option - 3
    math__1 = f'{num__1} - {num__2}'
    res__1 = num__1 - num__2

    # option - 4
    mathh1 = f'{numm1} - {numm2}'
    ress1 = numm1 - numm2

    options = [num1-num2, num_1-num_2, num__1-num__2, numm1-numm2]

    if 'order' not in st.session_state:
        indices = [0, 1, 2, 3]
        random.shuffle(indices)
        st.session_state.order = indices

    shuffled_indices = st.session_state.order

    c1_c1, c1_c2 = st.columns(2)
    with c1_c1 :
        for i, label in enumerate(["Ⅰ", "Ⅱ"]):
            idx = shuffled_indices[i]
            val = options[idx]
            
            if st.button(f"{label}. {val}", use_container_width=True):
                if val == res:
                    st.success("Correct!✅")
                else:
                    st.error("Wrong!❌")
    
    with c1_c2 :
        for i, label in enumerate(["Ⅲ", "Ⅳ"], start=2):
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