import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
_, center, _ = st.columns(3)
with center:
    st.write("# פקולטה - טיב 👋")

    st.sidebar.success("Select")

    htp = https://github.com/shaniplant/Faculta_Tive_app/images/landing page.jpg
    image = Image.open(htp+'/landing_page.jpg')
    st.image(image, caption='image of vision')

    st.markdown(
        """
        פקולטה - טיב הוא אתר שנועד לעזור לנו הסטודנטים ולסטודנטים לעתיד לשפר את איכת ההוראה והיחס לסטודנטים בפקולטות השונות. תחרות יוצרת שיפור
        **👈 עזרו לנו במילוי הסקר**
        ### אודותינו
        אני דביר
        ### כבר השפיעו

    """
    )

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


