import streamlit as st 

# reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
# signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
# home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
td_page = st.Page("./pgs/chat.py", title="Self service", icon=":material/language:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")



pg = st.navigation([td_page, chatbot_page])

st.set_page_config(
    page_title="EcoVerse",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': "Your digital sustainability companion—helping you act green, earn rewards, and visualize your eco impact. Turning Organic Waste into Energy and Eco-Tokens for a Greener Tomorrow!"
    }
)

pg.run()

