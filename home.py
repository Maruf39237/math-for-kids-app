import streamlit as st 

c1, c2 = st.columns(2)
with st.container():
    with c1 :
        st.title("🧮Math 4 kids")
        st.markdown("### A helper website for kids to learn basic math that makes building foundational skills fun and easy, ensuring every child gains the confidence to master early arithmetic.")

    with c2 :
        st.divider()
        # url = 'https://images.unsplash.com/photo-1664854953181-b12e6dda8b7c?q=80&w=764&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/The_Ancient_Quipu_Plate_XXI.jpg/960px-The_Ancient_Quipu_Plate_XXI.jpg"
        st.image(url, caption="Math is Fun!", width= 340)

st.divider()

st.markdown("""
##### Welcome, Math Explorer!🚀

##### Did you know that math is like a secret superpower? It helps you count your favorite toys, share pizza with friends, and even understand how rockets fly to the moon! Every time you solve a problem, your brain gets a little bit stronger. Are you ready to level up your skills?????

##### Let’s start adding!🧠
""")

