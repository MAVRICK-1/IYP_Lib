#just a demo test file

from IYP import AS
asnDom=AS.ixps_for_as(2497) #Taking the example of AS2497
asnDomJson=asnDom.json()#accuring the Json data
print(asnDomJson) #printing its value
asnDom.table() #roughly printing the data into tabular form
asnDom.close() #Close the connection to the Neo4j database.


