import os
from streamlit.connections import ExperimentalBaseConnection
from pymongo import MongoClient
from streamlit.runtime.caching import cache_data
import ssl

class MongoConnection(ExperimentalBaseConnection[MongoClient]):

    def _connect(self, **kwargs):
        url = self._secrets['url'] if 'url' in self._secrets else kwargs['url']
        self.db = self._secrets['database'] if 'database' in self._secrets else kwargs['database']
        self.collection = self._secrets['collection'] if 'url' in self._secrets else kwargs['collection']
        self.connection = MongoClient(url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        return self.connection
    

    def cursor(self):
        return self.connection[self.db][self.collection]
    


    def query(self, query, request = None,ttl = 3600, *args , **kwargs):

        curr = self.cursor()
        @cache_data(ttl=ttl)
        def find(request):
            data = curr.find(request)
            return [x for x in data]
        

        @cache_data(ttl=ttl)
        def findOne(request):
            data = curr.find_one(request)
            return [x for x in data]


        @cache_data(ttl=ttl)
        def insertOne(request):
            return curr.insert_one(request)



        @cache_data(ttl=ttl)
        def insertMany(request):
            return curr.insert_many(request)

        
        @cache_data(ttl=ttl)
        def deleteOne(request):
            return curr.delete_one(request)


        @cache_data(ttl=ttl)
        def deleteMany(request):
            return curr.delete_many(request)




        function_mapper = {"find": find, 
                  "findOne": findOne, 
                  "insertOne": insertOne, 
                  "insertMany": insertMany, 
                  "deleteOne": deleteOne, 
                  "deleteMany": deleteMany}
        
        action = function_mapper.get(query, None)
        response = action(request) if action != None else None
        return response
