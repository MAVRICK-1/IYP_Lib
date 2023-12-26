# IYP (Internet Yellow Pages) Python Library

## Overview

The IYP Python library is a lightweight query tool designed to simplify interactions with Neo4j DBMS. By encapsulating common query operations and providing a user-friendly interface, the library streamlines the process of retrieving and analyzing data from Neo4j databases.

## Features

### 1. Simplified Querying
- Execute Cypher queries with minimal code and configuration.
- Fetch nodes, relationships, and properties effortlessly.

### 2. Flexible Output Options
- Retrieve query results in both JSON and table formats.
- Integrate seamlessly with other Python data manipulation libraries.

### 3. User-friendly Interface
- Designed for ease of use and rapid development.
- Includes comprehensive documentation and examples for quick onboarding.

### From source files
Get the latest source files:
```
git clone git@github.com:MAVRICK-1/IYP_Lib.git

```

## Installation

It's not been publised yet , so  have build it locally.
```cmd
cd IYP_Lib
pip install -r requirements.txt
pip install wheel
python setup.py bdist_wheel
```
### Names for ASN
Find 'Name' nodes directly connected to the node corresponding to any given ASn(Autonomous System Number).
```python
from IYP import AS

asnData=AS.asn(2497) #Taking the example of AS2497

asnjson=asnData.json()#accuring the Json data

print(asnjson) #printing its value

asnData.table() #roughly printing the data into tabular form

asnData.close() #Close the connection to the Neo4j database.
```
<h3> Output </h3>

```cmd
[
    {
        "a": {
            "asn": 2497
        },
        "n": {
            "name": "IIJ Internet Initiative Japan Inc."
        }
    },
    {
        "a": {
            "asn": 2497
        },
        "n": {
            "name": "IIJ"
        }
    },
    {
        "a": {
            "asn": 2497
        },
        "n": {
            "name": "Internet Initiative Japan"
        }
    },
    {
        "a": {
            "asn": 2497
        },
        "n": {
            "name": "Internet Initiative Japan Inc."
        }
    },
    {
        "a": {
            "asn": 2497
        },
        "n": {
            "name": "IIJ"
        }
    },
    {
        "a": {
            "asn": 2497
        },
        "n": {
            "name": "IIJ"
        }
    }
]
Table Format:
               a                                               n
0  {'asn': 2497}  {'name': 'IIJ Internet Initiative Japan Inc.'}
1  {'asn': 2497}                                 {'name': 'IIJ'}
2  {'asn': 2497}           {'name': 'Internet Initiative Japan'}
3  {'asn': 2497}      {'name': 'Internet Initiative Japan Inc.'}
4  {'asn': 2497}                                 {'name': 'IIJ'}
5  {'asn': 2497}                                 {'name': 'IIJ'}
```
<br>

### Country code of AS2497 in delegated files
Here we search for a country node directly connected to AS2497's node and that
comes from NRO's delegated stats.
```python
from IYP import AS
countryCode=AS.as_country_code(2497) #Taking the example of AS2497
countryCodeJson=countryCode.json()#accuring the Json data
print(countryCodeJson) #printing its value
countryCode.table() #roughly printing the data into tabular form
countryCode.close() #Close the connection to the Neo4j database.
```
<h3>Output</h3>

```cmd
[
    {
        "iij": {
            "asn": 2497
        },
        "cc": {
            "country_code": "JP",
            "name": "Japan",
            "alpha3": "JPN"
        }
    }
]
Table Format:
             iij                                                 cc
0  {'asn': 2497}  {'country_code': 'JP', 'name': 'Japan', 'alpha...

```

<br>

### Top domain names hosted by AS2497
Select domain names in top 50k rankings that resolves to an IP originated by
AS2497.
```python
from IYP import AS
asnDom=AS.top_dom_asn(2497) #Taking the example of AS2497
asnDomJson=asnDom.json()#accuring the Json data
print(asnDomJson) #printing its value
asnDom.table() #roughly printing the data into tabular form
asnDom.close() #Close the connection to the Neo4j database.
```
<h3>Output</h3>

```cmd
[
    {
        "dn": {
            "name": "crea-tv.jp"
        },
        "ip": {
            "af": 4,
            "ip": "202.221.140.170"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.221.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "ndl.go.jp"
        },
        "ip": {
            "af": 4,
            "ip": "133.159.67.120"
        },
        "pfx": {
            "af": 4,
            "prefix": "133.159.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "konami.com"
        },
        "ip": {
            "af": 4,
            "ip": "210.149.81.150"
        },
        "pfx": {
            "af": 4,
            "prefix": "210.149.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "yugioh-card.com"
        },
        "ip": {
            "af": 4,
            "ip": "210.149.81.150"
        },
        "pfx": {
            "af": 4,
            "prefix": "210.149.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "konami.com"
        },
        "ip": {
            "af": 4,
            "ip": "210.149.81.150"
        },
        "pfx": {
            "af": 4,
            "prefix": "210.149.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "yugioh-card.com"
        },
        "ip": {
            "af": 4,
            "ip": "210.149.81.150"
        },
        "pfx": {
            "af": 4,
            "prefix": "210.149.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "pia.jp"
        },
        "ip": {
            "af": 4,
            "ip": "202.214.74.78"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.214.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "pia.co.jp"
        },
        "ip": {
            "af": 4,
            "ip": "202.214.74.78"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.214.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "deqwas.net"
        },
        "ip": {
            "af": 4,
            "ip": "202.214.162.7"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.214.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "deqwas.net"
        },
        "ip": {
            "af": 4,
            "ip": "202.214.162.7"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.214.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "gamecity.ne.jp"
        },
        "ip": {
            "af": 4,
            "ip": "202.214.51.232"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.214.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "iij.jp"
        },
        "ip": {
            "af": 4,
            "ip": "203.180.140.77"
        },
        "pfx": {
            "af": 4,
            "prefix": "203.180.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "iij.jp"
        },
        "ip": {
            "af": 4,
            "ip": "203.180.140.77"
        },
        "pfx": {
            "af": 4,
            "prefix": "203.180.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "tetrabit.net"
        },
        "ip": {
            "af": 4,
            "ip": "203.180.251.7"
        },
        "pfx": {
            "af": 4,
            "prefix": "203.180.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "hi-ho.ne.jp"
        },
        "ip": {
            "af": 4,
            "ip": "58.138.168.104"
        },
        "pfx": {
            "af": 4,
            "prefix": "58.138.128.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "hi-ho.ne.jp"
        },
        "ip": {
            "af": 4,
            "ip": "58.138.168.104"
        },
        "pfx": {
            "af": 4,
            "prefix": "58.138.128.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "timescar.jp"
        },
        "ip": {
            "af": 4,
            "ip": "58.138.176.23"
        },
        "pfx": {
            "af": 4,
            "prefix": "58.138.128.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "timescar.jp"
        },
        "ip": {
            "af": 4,
            "ip": "58.138.176.23"
        },
        "pfx": {
            "af": 4,
            "prefix": "58.138.128.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "madamlive.tv"
        },
        "ip": {
            "af": 4,
            "ip": "202.32.201.193"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.32.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "goo-net.com"
        },
        "ip": {
            "af": 4,
            "ip": "163.49.4.15"
        },
        "pfx": {
            "af": 4,
            "prefix": "163.49.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "goo-net.com"
        },
        "ip": {
            "af": 4,
            "ip": "163.49.4.15"
        },
        "pfx": {
            "af": 4,
            "prefix": "163.49.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "goobike.com"
        },
        "ip": {
            "af": 4,
            "ip": "163.49.4.56"
        },
        "pfx": {
            "af": 4,
            "prefix": "163.49.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "pinzuba.news"
        },
        "ip": {
            "af": 4,
            "ip": "163.49.35.165"
        },
        "pfx": {
            "af": 4,
            "prefix": "163.49.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "gendai.media"
        },
        "ip": {
            "af": 4,
            "ip": "163.49.35.159"
        },
        "pfx": {
            "af": 4,
            "prefix": "163.49.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "chugoku-np.co.jp"
        },
        "ip": {
            "af": 4,
            "ip": "163.49.35.121"
        },
        "pfx": {
            "af": 4,
            "prefix": "163.49.0.0/16"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "tower.jp"
        },
        "ip": {
            "af": 4,
            "ip": "202.238.233.84"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.238.192.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "tdk.com"
        },
        "ip": {
            "af": 4,
            "ip": "202.238.239.243"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.238.192.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "tdk.com"
        },
        "ip": {
            "af": 4,
            "ip": "202.238.239.243"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.238.192.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "hankyu-travel.com"
        },
        "ip": {
            "af": 4,
            "ip": "202.238.233.175"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.238.192.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "webike.net"
        },
        "ip": {
            "af": 4,
            "ip": "202.238.231.218"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.238.192.0/18"
        },
        "iij": {
            "asn": 2497
        }
    },
    {
        "dn": {
            "name": "webike.net"
        },
        "ip": {
            "af": 4,
            "ip": "202.238.231.218"
        },
        "pfx": {
            "af": 4,
            "prefix": "202.238.192.0/18"

Table Format:
                              dn  ...            iij
0         {'name': 'crea-tv.jp'}  ...  {'asn': 2497}
1          {'name': 'ndl.go.jp'}  ...  {'asn': 2497}
2         {'name': 'konami.com'}  ...  {'asn': 2497}
3    {'name': 'yugioh-card.com'}  ...  {'asn': 2497}
4         {'name': 'konami.com'}  ...  {'asn': 2497}
..                           ...  ...            ...
241        {'name': 'ndl.go.jp'}  ...  {'asn': 2497}
242           {'name': 'iij.jp'}  ...  {'asn': 2497}
243           {'name': 'iij.jp'}  ...  {'asn': 2497}
244     {'name': 'tetrabit.net'}  ...  {'asn': 2497}
245       {'name': 'crea-tv.jp'}  ...  {'asn': 2497}

[246 rows x 4 columns]
```

<br>

### Countries of IXPs where AS2497 is present
Starting from the node corresponding to AS2497, find IXPs where AS2497 is member
of, and then the country corresponding to each IXP.

```python
from IYP import AS
asnDom=AS.ixps_for_as(2497) #Taking the example of AS2497
asnDomJson=asnDom.json()#accuring the Json data
print(asnDomJson) #printing its value
asnDom.table() #roughly printing the data into tabular form
asnDom.close() #Close the connection to the Neo4j database.
```
<h3>Output</h3>

```cmd
[
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "JPNAP Tokyo"
        },
        "cc": {
            "country_code": "JP",
            "name": "Japan",
            "alpha3": "JPN"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "SIX Seattle"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix San Jose"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix Ashburn"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix Hong Kong"
        },
        "cc": {
            "country_code": "HK",
            "name": "Hong Kong",
            "alpha3": "HKG"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix New York"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "HKIX"
        },
        "cc": {
            "country_code": "HK",
            "name": "Hong Kong",
            "alpha3": "HKG"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix Singapore"
        },
        "cc": {
            "country_code": "SG",
            "name": "Singapore",
            "alpha3": "SGP"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "DE-CIX Frankfurt"
        },
        "cc": {
            "country_code": "DE",
            "name": "Germany",
            "alpha3": "DEU"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "SGIX"
        },
        "cc": {
            "country_code": "SG",
            "name": "Singapore",
            "alpha3": "SGP"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "LINX LON1"
        },
        "cc": {
            "country_code": "GB",
            "name": "United Kingdom of Great Britain and Northern Ireland",
            "alpha3": "GBR"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix Palo Alto"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "DIX-IE"
        },
        "cc": {
            "country_code": "JP",
            "name": "Japan",
            "alpha3": "JPN"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "Equinix Los Angeles"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "NYIIX New York"
        },
        "cc": {
            "country_code": "US",
            "name": "United States of America",
            "alpha3": "USA"
        }
    },
    {
        "iij": {
            "asn": 2497
        },
        "ix": {
            "name": "JPNAP Osaka"
        },
        "cc": {
            "country_code": "JP",
            "name": "Japan",
            "alpha3": "JPN"
        }
    }
]
Table Format:
              iij                               ix                                                 cc
0   {'asn': 2497}          {'name': 'JPNAP Tokyo'}  {'country_code': 'JP', 'name': 'Japan', 'alpha...
1   {'asn': 2497}          {'name': 'SIX Seattle'}  {'country_code': 'US', 'name': 'United States ...
2   {'asn': 2497}     {'name': 'Equinix San Jose'}  {'country_code': 'US', 'name': 'United States ...
3   {'asn': 2497}      {'name': 'Equinix Ashburn'}  {'country_code': 'US', 'name': 'United States ...
4   {'asn': 2497}    {'name': 'Equinix Hong Kong'}  {'country_code': 'HK', 'name': 'Hong Kong', 'a...
5   {'asn': 2497}     {'name': 'Equinix New York'}  {'country_code': 'US', 'name': 'United States ...
6   {'asn': 2497}                 {'name': 'HKIX'}  {'country_code': 'HK', 'name': 'Hong Kong', 'a...
7   {'asn': 2497}    {'name': 'Equinix Singapore'}  {'country_code': 'SG', 'name': 'Singapore', 'a...
8   {'asn': 2497}     {'name': 'DE-CIX Frankfurt'}  {'country_code': 'DE', 'name': 'Germany', 'alp...
9   {'asn': 2497}                 {'name': 'SGIX'}  {'country_code': 'SG', 'name': 'Singapore', 'a...
10  {'asn': 2497}            {'name': 'LINX LON1'}  {'country_code': 'GB', 'name': 'United Kingdom...
11  {'asn': 2497}    {'name': 'Equinix Palo Alto'}  {'country_code': 'US', 'name': 'United States ...
12  {'asn': 2497}               {'name': 'DIX-IE'}  {'country_code': 'JP', 'name': 'Japan', 'alpha...
13  {'asn': 2497}  {'name': 'Equinix Los Angeles'}  {'country_code': 'US', 'name': 'United States ...
14  {'asn': 2497}       {'name': 'NYIIX New York'}  {'country_code': 'US', 'name': 'United States ...
15  {'asn': 2497}          {'name': 'JPNAP Osaka'}  {'country_code': 'JP', 'name': 'Japan', 'alpha...
```

