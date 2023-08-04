
import streamlit as st
from st_on_hover_tabs import on_hover_tabs


from connection.connection import MongoConnection



conn = st.experimental_connection("mongodb", type=MongoConnection)





    
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Sample App', 'Functionalities', 'Set Up'], 
                         iconName=['favorite', 'settings', 'mode heat'], default_choice=0)
    

if tabs == "Sample App":
    st.title("Example Application for Streamlit:  MongoDB Connection")
    
    name = st.text_input("Your Name")
    comment = st.text_input("Your Comment")
    

    if st.button("Submit"):
        conn.query("insertOne", request = {"name": name, "comment": comment}, ttl = 0)


    posts = conn.query("find", request = {}, ttl = 0)


    if posts:
        for post in posts:
            with st.chat_message("user"):
                st.write(post["name"] + " says " + post["comment"])

elif tabs == "Functionalities":
    st.title("Functionalities")
    st.write("The following functionalities are available for MongoDB connection")
    st.markdown("""
                #### Creating the connection:  

                Use the following code to create the connection object    
                 `conn = st.experimental_connection("mongodb", type=MongoConnection)`
                
                #### Creating a cursor object:  

                A cursor object can be created to retrieve the underlying connection object.   
                ` cur = conn.cursor() `  

                #### Query Tool:  

                There are three kinds of query implemented in MongoConnection Module which are:    
                1. find / findOne
                2. insertOne/ insertMany
                3. deleteOne/ deleteMany

                Use these queries with the query() function of the connection object with a specific request. Example:   
                `q = conn.query("find", request = {})`  
                The return value is the response by the MongoDB server.
                """)

elif tabs == "Set Up":
    st.title("How to set up the connection⚙️")
    st.markdown("""
                ### `secrets.toml` Setup
                Set up the `secrets.toml` file for your project as such:
                ```
                [connections.mongodb]
                url="mongodb+srv://<username>:<password>@<cluster-name>.<cluster-id>.mongodb.net"
                database="<Your DB Name>"
                collection="<Your Collection Name>"
                ```
                """)

    
