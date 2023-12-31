#just a demo test file
from IYP import AS
asnDom=AS.top_dom_asn(2497) #Taking the example of AS2497
asnDomJson=asnDom.json()#accuring the Json data
print("Tabular Form :")
print(asnDomJson) #printing its value
print(asnDom.table()) #roughly printing the data into tabular form
asnDom.close()


