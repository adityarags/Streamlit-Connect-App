# Streamlit - MongoDB Connection


<p align="center"> <img src="https://global.discourse-cdn.com/business7/uploads/streamlit/optimized/3X/d/6/d6e06e08c5eae258e58f8e71e9bb0db8c77a9db1_2_750x750.jpeg"> <br>This repository is my submission for the "Streamlit Connections Hackathon"</p>




# Functionalities⚙️
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

# Connection Setup 🖊
### `secrets.toml` Setup
Set up the `secrets.toml` file for your project as such:
 ```
                [connections.mongodb]
                url="mongodb+srv://<username>:<password>@<cluster-name>.<cluster-id>.mongodb.net"
                database="<Your DB Name>"
                collection="<Your Collection Name>"
```


# Sample Application🔥
The example application is a simple comments app that has been deployed using Streamlit and uses MongoDB for storing/accessing the data.
![image](https://github.com/adityarags/Streamlit-Connect-App/assets/59119736/f347c8f2-8035-4010-afc6-0b7e2db3824c)


# Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_red.svg)](https://ad-mdb-connect.streamlit.app/)


