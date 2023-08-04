import os
import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import pymongo



class MongoDBConnection(ExperimentalBaseConnection[pymongo.mongo_client.MongoClient]):

    def _connect(self, **kwargs):
        url = self._secrets['url']
        self.connection = pymongo.MongoClient(url)
    
    def query(self, query: str, ttl:int = 3600, **kwargs):
        db = self.cursor()
        pass
    

    
conn = st.experimental_connection("mongodb", type=MongoDBConnection)

print(type(conn.cursor()))