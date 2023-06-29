import streamlit as st
import re
import pymongo
import matplotlib.pyplot as plt
import streamlit_survey as ss

## Connect to MongoDB 

def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()
db = client["faculta-tive"]
collection = db["studens"]


# Medical schools in Israel
MED_SCHOOLS = {
    "האוניברסיטה העברית": "mail.huji.ac.il",
    "תל-אביב": "tau.ac.il",
    "טכניון": "technion.ac.il",
    "בן גוריון": "bgu.ac.il",
    "בר אילן": "biu.ac.il",
    "אריאל" : "arieal.ac.il"
}

# Streamlit app
def main():
    st.title("פקולטה - טיב ")
    st.title("סקר הפקולטות לרפואה בישראל")
    st.markdown(" שלום! אנו מבצעים סקר זה כחלק ממאמץ לשדרג את חווית התלמידים בבתי הספר הרפואיים.")

    
    # Survey

    survey = ss.StreamlitSurvey("survey")
    #pages = survey.pages(3, on_submit=lambda: st.success("תגובתך נרשמה בהצלחה- תודה!!"))
    #with pages:
        # Collect student information
        #if pages.current == 0:
            
    st.header("מידע אישי")
    st.write("שם")
    name = survey.text_input("name", id = "name",label_visibility="collapsed")

    st.write("אימייל")
    email = survey.text_input("email", id = "email",label_visibility="collapsed")

    st.write("בית הספר לרפואה שלך")
    school = survey.selectbox("school", id ="school", options=list(MED_SCHOOLS.keys()),label_visibility="collapsed")

    st.write("באיזה מסלול אתה לומד/למדת?")
    med_track = survey.selectbox("med_track", id = "med_track", options=["שש שנתי", "ארבע שנתי"],label_visibility="collapsed")

    st.write("האם אתה בוגר או עדיין סטודנט?")
    student_status = survey.selectbox("student_status" , id = "student_status", options=["בוגר", "סטודנט"], label_visibility="collapsed")
    
#elif pages.current == 1:
    

    q1 = survey.radio("Q1", options=["NA", "גרוע😞", "🙁לא טוב", "😐סביר", "🙂טוב", "מצויין😀"], key="q1")

    st.write("שאלה")
    q2 = survey.radio("Q2", options=["NA", "גרוע😞", "🙁לא טוב", "😐סביר", "🙂טוב", "מצויין😀"], key="q2")
    q3 = survey.radio("Q3", options=["NA", "גרוע😞", "🙁לא טוב", "😐סביר", "🙂טוב", "מצויין😀"], key="q3")

    st.write("האם הפקולטה הכינה אותך היטב למקצוע?")
    q4 = survey.radio("Q4", options= ["NA", "כן", "לא"], key="q4")
    
    st.write("רמת שביעות רצון כללית")
    overall = survey.select_slider(
        "overall",
        options=["Every Day", "Every week", "Every Month", "Once a year", "Rarely"],
        label_visibility="collapsed",
    )

    if student_status == "big":
        overall = survey.radio("האם הפקולטה הכינה אותך היטב למקצוע?", ["NA", "כן", "לא"], index=0, key="q4")
    
        
 

#elif pages.current == 2:
    survey.checkbox("Check box")
    
    # Check email validity
    if st.button("שליחה"):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("אימייל לא תקין. נא להזין אימייל תקין.")
            return

          # Extract email domain and check against the chosen medical school
        email_domain = email.split("@")[1]
        if email_domain != MED_SCHOOLS[school]:
            st.error("אימייל לא מתאים לבית הספר שנבחר. נא לבחור ספר אחר.")
            return

        # Store student information in MongoDB
        student_data = {
                    "name": name,
                    "email": email,
                    "school": school,
                    "med_track": med_track,
                    "student_status": student_status,
                    "Q1": q1,
                    "Q2": q2,
                    "Q3": q3,
                    "Q4": q4,
                    "overall" : overall
                }
        #student_data_json = survey.to_json()
        collection.insert_one(student_data)
        st.success("תודה על המשוב!")
      



if __name__ == "__main__":
    main()
