# Import required libraries
from neo4j import GraphDatabase
import pandas as pd
import json

# Connect to the Neo4j server
uri = "neo4j+s://iyp.iijlab.net:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", ""))  # No password required

class asn: #Names for AS2497
    '''
    Find 'Name' nodes directly connected to the node corresponding to AS2497.
    '''
    def __init__(self, asn=2497):
        """
        - asn (str) : Autonomus System Number.
        - query (str): The Cypher query to be executed.
        - parameters(dict): The Cypher qurey parameters
        - try and except for error Handeling
        """
        try:
            self.driver = driver
            self.query = '''MATCH (a:AS {asn:$asn})--(n:Name) RETURN a,n'''
            self.parameters={"asn":asn} #parameters
            
        except Exception as e:
            print("Failed to create the driver:", e)
            
    def execute_query(self,db=None):
        """
        Execute the query on the Neo4j server and fetch the results.
        records : A list of record returned by the query.
        Returns:
        A List comprehesion that iterates over each  record fetched
        """
        assert self.driver is not None, "Driver not initialized!"
        session = None
        try:
            session = self.driver.session(database=db) if db is not None else self.driver.session()
            with driver.session() as session:
                result = session.run(self.query,self.parameters)
                records = [record for record in result]
            return [record.data() for record in records]
        except Exception as e:
            print("Query failed:", e)
            
    def json(self)->(str):
        """
        Retrieve and print the query results in JSON format.
        """
        json_data = self.execute_query()
        return json.dumps(json_data, indent=4)


    def table(self):
        """
        Retrieve and Returns Pandas DataFrame Object .
        which can use for Data Exploring, Data Selection and Indexing , Data Manipulation,
        Data Cleaning,Data Visualization, Data Transformation,Time Series Analysis,Advance Operation
        and Integration with Other Libraries
        """
        data=self.execute_query()
        table_data = pd.DataFrame([{
            'Autonomus System Number': d['a']['asn'], 
            'name': d['n']['name']}
            for d in data])
        table_data.drop_duplicates(inplace=True) #Eliminating duplicate rows
        return table_data
        

    def close(self):
        """
        Close the connection to the Neo4j database.
        """
        driver.close()



'''Country code of AS2497 in delegated files'''
class as_country_code(asn):
    '''Here we search for a country node directly connected to AS2497's
    node and that comes from NRO's delegated stats.'''

    def __init__(self, asn=2497): #by default 2497
        """
        - asn (str) : Autonomus System Number.
        - query (str): The Cypher query to be executed.
        - parameters(dict): The Cypher qurey parameters
        - try and except for error Handeling
        """
        try:
            self.driver = driver
            self.query = '''MATCH (iij:AS {asn:$asn})-[{reference_name:'nro.delegated_stats'}]-(cc:Country) RETURN iij, cc'''
            self.parameters={"asn":asn}
        except Exception as e:
            print("Failed to create the driver:", e)
    
    def table(self):
        """
        Retrieve and Returns Pandas DataFrame Object ..
        """
        data=self.execute_query()
        table_data = pd.DataFrame([{
            'Autonomus System Number': d['iij']['asn'],
            'Country Code': d['cc']['country_code'],
            'Name': d['cc']['name'],
            'Alpha3': d['cc']['alpha3']}
            for d in data])
        table_data.drop_duplicates(inplace=True) #Eliminating duplicate rows
        return table_data



class top_dom_asn (asn): #Top domain names hosted by ASn
    '''
    Select domain names in top 50k rankings that resolves to an IP originated by ASn.
    '''
    def __init__(self, asn=2497):
        """
        - asn (str) : Autonomus System Number.
        - query (str): The Cypher query to be executed.
        - parameters(dict): The Cypher qurey parameters
        - try and except for error Handeling
        """
        try:
            self.driver = driver
            self.query = '''MATCH (:Ranking)-[r:RANK]-(dn:DomainName)--(ip:IP)--(pfx:Prefix)-[:ORIGINATE]-(iij:AS {asn:$asn})
            WHERE r.rank < 50000
            RETURN dn, ip, pfx, iij'''
            self.parameters={"asn":asn} #parameters
            
        except Exception as e:
            print("Failed to create the driver:", e)
            
    def table(self):
        """
        Retrieve and Returns Pandas DataFrame Object .
        """
        data=self.execute_query()
        table_data = pd.DataFrame([{
        'Domain Name': d['dn']['name'],
        'AF': d['ip']['af'],
        'IP': d['ip']['ip'],
        'Prefix': d['pfx']['prefix'],
        'Autonomus System Number': d['iij']['asn']
        }
        for d in data
        ])
        table_data.drop_duplicates(inplace=True) #Eliminating duplicate rows
        return table_data

class ixps_for_as(asn): #Countries of IXPs where required ASn is present
    '''tarting from the node corresponding to ASn, find IXPs where ASn is member of, and then the country corresponding to each IXP.'''
    def __init__(self, asn=2497): #by default 2497
        """
        - asn (str) : Autonomus System Number.
        - query (str): The Cypher query to be executed.
        - parameters(dict): The Cypher qurey parameters
        - try and except for error Handeling
        """
        try:
            self.driver = driver
            self.query = '''MATCH (iij:AS {asn:$asn})-[:MEMBER_OF]-(ix:IXP)--(cc:Country) RETURN iij, ix, cc'''
            self.parameters={"asn":asn}
        except Exception as e:
            print("Failed to create the driver:", e)
    
    def table(self):
        """
        Retrieve and Returns Pandas DataFrame Object .
        """
        data=self.execute_query()
        table_data = pd.DataFrame([
        {
        'ASn': d['iij']['asn'], #Asn Autonomus System Number
        'Internet Exchange': d['ix']['name'],
        ' Country Code': d['cc']['country_code'],
        'Country Name': d['cc']['name']
        }
        for d in data])
        
        table_data.drop_duplicates(inplace=True) #Eliminating duplicate rows
        return table_data