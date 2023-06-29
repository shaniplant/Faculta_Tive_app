import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.markdown("<h1 style='text-align: center;'>פקולטה - טיב 👋</h1>", unsafe_allow_html=True)
#st.write("# פקולטה - טיב 👋")

st.sidebar.success("עזרו לנו להגיע לכמה שיותר סטודנטים")

htp = "https://raw.githubusercontent.com/shaniplant/Faculta_Tive_app/main/images/landing%20page.jpg"
#htp = "G:\My Drive\Faculta_tive\images\landing page.jpg"
image = Image.open(htp)
st.image(image, caption='image of vision')
st.markdown("<h3 style='text-align: center;'>פקולטה - טיב הוא אתר שנועד לעזור לנו הסטודנטים ולסטודנטים לעתיד לשפר את איכת ההוראה והיחס לסטודנטים בפקולטות השונות. תחרות יוצרת שיפור</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>👈 עזרו לנו במילוי הסקר</h2>", unsafe_allow_html=True)


want_to_contribute = st.button("אני רוצה להצביע!")
if want_to_contribute:
    switch_page("survey 😷 ")


st.markdown("<h1 style='text-align: center;'>אודותינו</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>סטודנטים לרפואה מתעבדים להתקבל ואז מתיחסים אליהם חרא</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>מה המצב? </h2>", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

# number of votes
votes = 2
plos_votes = 5
text_plos_votes = "הצבעות נוספות מאתמול: "+str(plos_votes)

col1.metric("הצביעו",votes , text_plos_votes)

#

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])
col2.bar_chart(chart_data)

#

data_df = pd.DataFrame({"faculty" : ["tel_aviv", "tec", "huji", "beer_sheva", "ariel"],
        "score": [200, 550, 1000, 80, 0] })


col3.data_editor(
    data_df,
    column_config={
        "score": st.column_config.ProgressColumn(
            "score1",
            help="help_what is score",
            format="$%f",
            min_value=0,
            max_value=1000,
        ),
    },
    hide_index=True,
)
#col3.metric("Humidity", "86%", "4%")


