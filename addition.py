import random
import streamlit as st


st.markdown("""### ✨ The Magic of Addition ✨
##### Addition is like bringing friends together! Imagine holding one shiny, yummy apple in your hand. Then—surprise!—your friend gives you two more. When you gather them all in a big hug, you now have three delicious apples to crunch on.

##### Example : 🍎 + 🍎🍎 = 🍎🍎🍎

##### That’s the magic of addition: small groups join to make one big, happy family of numbers. Every time you add, you unlock new math superpowers—turning simple steps into exciting discoveries!
""")

st.divider()

c1, c2 = st.columns(2)

with c2 :
    # url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Binary_addition_with_carry.svg/1280px-Binary_addition_with_carry.svg.png"
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Complex_Number_Addition_Visualization_svg.svg/960px-Complex_Number_Addition_Visualization_svg.svg.png"
    st.image(url, width = 240, caption = "A + B = OX")

with c1 : 
    @st.cache_data
    def get_math_data():
        num1_1, num2_1 = random.randint(1, 20), random.randint(1, 20)
        num1_2, num2_2 = random.randint(1, 20), random.randint(1, 20)
        num1_3, num2_3 = random.randint(1, 20), random.randint(1, 20)
        num1_4, num2_4 = random.randint(1, 20), random.randint(1, 20)
        return num1_1, num2_1, num1_2, num2_2, num1_3, num2_3, num1_4, num2_4


    num1_1, num2_1, num1_2, num2_2, num1_3, num2_3, num1_4, num2_4  = get_math_data()
    st.markdown(f"#### ➕Addition : {num1_1} + {num2_1} = ❓")

    # option - 1
    math = f'{num1_1} + {num2_1}'
    res = num1_1 + num2_1

    # option - 2
    math_1 = f'{num1_2} + {num2_2}'
    res_1 = num1_2 + num2_2

    # option - 3
    math__1 = f'{num1_3} + {num2_3}'
    res__1 = num1_3 + num2_3

    # option - 4
    mathh1 = f'{num1_4} + {num2_4}'
    ress1 = num1_4 + num2_4


    options = [num1_1+num2_1, num1_2+num2_2, num1_3+num2_3, num1_4+num2_4]

    if 'order' not in st.session_state:
        indices = [0, 1, 2, 3]
        random.shuffle(indices)
        st.session_state.order = indices

    shuffled_indices = st.session_state.order

    c1_c1, c1_c2 = st.columns(2)

    with c1_c1:
        idx = shuffled_indices[0]
        val = options[idx]
        if st.button(f"Ⅰ. {val}", use_container_width=True):
            if val == res: 
                st.success("Correct!✅")
            else:
                st.error("Wrong!❌")
        
        idx1 = shuffled_indices[1]
        val1 = options[idx1]
        if st.button(f"Ⅱ. {val1}", use_container_width=True):
            if val1 == res: 
                st.success("Correct!✅")
            else:
                st.error("Wrong!❌")

    with c1_c2:
        idx = shuffled_indices[2]
        val = options[idx]
        if st.button(f"Ⅲ. {val}", use_container_width=True):
            if val == res: 
                st.success("Correct!✅")
            else:
                st.error("Wrong!❌")
        
        idx1 = shuffled_indices[3]
        val1 = options[idx1]
        if st.button(f"Ⅳ. {val1}", use_container_width=True):
            if val1 == res: 
                st.success("Correct!✅")
            else:
                st.error("Wrong!❌")

    if st.button("Next Question ➡️"):
        st.cache_data.clear()
        st.session_state.clear()
        st.rerun()

    st.divider()