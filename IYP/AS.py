# Import required libraries
from neo4j import GraphDatabase
import pandas as pd
import json

# Connect to the Neo4j server
uri = "neo4j+s://iyp.iijlab.net:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", ""))  # No password required

class asn:
    def __init__(self, asn=2497):
        """
        - asn (str) : Autonomus System Number.
        - query (str): The Cypher query to be executed.
        """
        self.asn = asn
        self.query = f"MATCH (a:AS {{asn:{asn}}})--(n:Name) RETURN a,n"

    def execute_query(self):
        """
        Execute the query on the Neo4j server and fetch the results.

        Returns:
        - list: A list of records returned by the query.
        """
        with driver.session() as session:
            result = session.run(self.query)
            records = [record for record in result]
        return records

    def json(self)->(str):
        """
        Retrieve and print the query results in JSON format.
        """
        records = self.execute_query()
        json_data = [record.data() for record in records]
        return json.dumps(json_data, indent=4)

    def table(self):
        """
        Retrieve and print the query results in table format using pandas.
        """
        records = self.execute_query()
        table_data = pd.DataFrame([record.data() for record in records])
        print("Table Format:")
        print(table_data)

    def close(self):
        """
        Close the connection to the Neo4j database.
        """
        driver.close()

class as_country_code (asn): # Country code of AS in delegated files
    def __init__(self, asn=2497): #by default 2497
        """
        Here we search for a country node directly connected to asn's node and that comes from NRO's delegated stats.
        """
        self.asn = asn
        self.query = f"MATCH (iij:AS {{asn:{asn}}})-[{{reference_name:'nro.delegated_stats'}}]-(cc:Country) RETURN iij, cc"


class top_dom_asn (asn): #Top domain names hosted by AS
    def __init__(self, asn=2497): #by default 2497
        '''
        Select domain names in top 50k rankings that resolves to an IP originated by asn.
        '''
        self.asn = asn
        self.query=f"MATCH (:Ranking)-[r:RANK]-(dn:DomainName)--(ip:IP)--(pfx:Prefix)-[:ORIGINATE]-(iij:AS {{asn:{asn}}})WHERE r.rank < 50000 RETURN dn, ip, pfx, iij"

class ixps_for_as(asn):
    def __init__(self,asn=2497):#by default 2497
        '''
        Starting from the node corresponding to AS2497, find IXPs where AS2497 is member of, and then the country corresponding to each IXP.
        '''
        self.asn = asn
        self.query=f"MATCH (iij:AS {{asn:{asn}}})-[:MEMBER_OF]-(ix:IXP)--(cc:Country) RETURN iij, ix, cc"
