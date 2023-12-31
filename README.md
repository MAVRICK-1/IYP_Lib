# IYP (Internet Yellow Pages) Python Library

## Overview

The IYP Python library is a lightweight query tool designed to simplify interactions with Neo4j DBMS. By encapsulating common query operations and providing a user-friendly interface, the library streamlines the process of retrieving and analyzing data from Neo4j databases.

## Features

### 1. Simplified Querying
- Execute Cypher queries with minimal code and configuration.
- Retrieve and Returns Pandas DataFrame Object .
which can use for Data Exploring, Data Selection and Indexing , Data Manipulation,
Data Cleaning,Data Visualization, Data Transformation,Time Series Analysis,Advance Operation
and Integration with Other Libraries
- Fetch nodes, relationships, and properties effortlessly.

### 2. Flexible Output Options
- Retrieve query results in both JSON .
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

### It hasn't been published yet, you'll need to build it locally,Here's how you can create it

#### Run the following commands in your terminal
```cmd
cd IYP_Lib
```
### To install the required packages
```cmd
pip install -r requirements.txt
```
### The wheel package is a build-package format for python

```cmd
pip install wheel
````
### To create a wheel distribution using setup.py file
```cmd
python setup.py bdist_wheel
```
### Names for ASn
Find 'Name' nodes directly connected to the node corresponding to any given ASn(Autonomous System Number).
```python
from IYP import AS #importing Library

asnData=AS.asn(2497) #Taking the example of AS2497
asnjson=asnData.json()#accuring the Json data
print(asnjson) #printing its value
print("Tabular Form :")
print(asnData.table()) #printing the data into tabular form
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

   Autonomus System Number                                name
0                     2497  IIJ Internet Initiative Japan Inc.
1                     2497                                 IIJ
2                     2497           Internet Initiative Japan
3                     2497      Internet Initiative Japan Inc.
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

   Autonomus System Number Country Code   Name Alpha3
0                     2497           JP  Japan    JPN

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
           Domain Name  AF               IP            Prefix  Autonomus System Number
0           crea-tv.jp   4  202.221.140.170    202.221.0.0/16                     2497
1            ndl.go.jp   4   133.159.67.120    133.159.0.0/16                     2497
2           konami.com   4   210.149.81.150    210.149.0.0/16                     2497
3      yugioh-card.com   4   210.149.81.150    210.149.0.0/16                     2497
6               pia.jp   4    202.214.74.78    202.214.0.0/16                     2497
7            pia.co.jp   4    202.214.74.78    202.214.0.0/16                     2497
8           deqwas.net   4    202.214.162.7    202.214.0.0/16                     2497
10      gamecity.ne.jp   4   202.214.51.232    202.214.0.0/16                     2497
11              iij.jp   4   203.180.140.77    203.180.0.0/16                     2497
13        tetrabit.net   4    203.180.251.7    203.180.0.0/16                     2497
14         hi-ho.ne.jp   4   58.138.168.104   58.138.128.0/18                     2497
16         timescar.jp   4    58.138.176.23   58.138.128.0/18                     2497
18        madamlive.tv   4   202.32.201.193     202.32.0.0/16                     2497
19         goo-net.com   4      163.49.4.15     163.49.0.0/16                     2497
21         goobike.com   4      163.49.4.56     163.49.0.0/16                     2497
22        pinzuba.news   4    163.49.35.165     163.49.0.0/16                     2497
23        gendai.media   4    163.49.35.159     163.49.0.0/16                     2497
24    chugoku-np.co.jp   4    163.49.35.121     163.49.0.0/16                     2497
25            tower.jp   4   202.238.233.84  202.238.192.0/18                     2497
26             tdk.com   4  202.238.239.243  202.238.192.0/18                     2497
28   hankyu-travel.com   4  202.238.233.175  202.238.192.0/18                     2497
29          webike.net   4  202.238.231.218  202.238.192.0/18                     2497
31            tower.jp   4   202.238.233.87  202.238.192.0/18                     2497
32   hankyu-travel.com   4  202.238.233.174  202.238.192.0/18                     2497
33        athome.co.jp   4   220.156.137.21  220.156.128.0/19                     2497
34           jprime.jp   4   202.238.151.94  202.238.128.0/18                     2497
35      forzastyle.com   4   202.238.151.45  202.238.128.0/18                     2497
36      toyokeizai.net   4   202.238.151.52  202.238.128.0/18                     2497
38     gentosha-go.com   4  202.238.151.111  202.238.128.0/18                     2497
39  okinawatimes.co.jp   4  202.238.151.129  202.238.128.0/18                     2497
40          bunshun.jp   4  202.238.151.148  202.238.128.0/18                     2497
41           afpbb.com   4   202.238.151.70  202.238.128.0/18                     2497
42          limo.media   4   202.238.151.83  202.238.128.0/18                     2497
43        president.jp   4   202.238.151.28  202.238.128.0/18                     2497
44       mi-mollet.com   4   202.238.151.96  202.238.128.0/18                     2497
45   skyperfectv.co.jp   4   210.148.90.150    210.148.0.0/16                     2497
46        1024tera.com   4    210.148.85.59    210.148.0.0/16                     2497
48         terabox.com   4    210.148.85.50    210.148.0.0/16                     2497
52          diamond.jp   4  210.148.177.240    210.148.0.0/16                     2497
54         4funbox.com   4     210.148.85.9    210.148.0.0/16                     2497
55      teraboxapp.com   4    210.148.85.41    210.148.0.0/16                     2497
57        nephobox.com   4    210.148.85.13    210.148.0.0/16                     2497
59     tttturbonet.com   4    210.148.85.53    210.148.0.0/16                     2497
61          ismedia.jp   4  210.148.177.150    210.148.0.0/16                     2497
62         terabox.app   4    210.148.85.14    210.148.0.0/16                     2497
64         kenwood.com   4   150.31.252.150     150.31.0.0/16                     2497
66          tamiya.com   4     150.31.244.4     150.31.0.0/16                     2497
67        2ndstreet.jp   4    150.31.179.81     150.31.0.0/16                     2497
68             jvc.com   4   150.31.252.139     150.31.0.0/16                     2497
69       japanet.co.jp   4   202.232.74.201    202.232.0.0/16                     2497
70        family.co.jp   4    202.232.114.4    202.232.0.0/16                     2497
71           iij.ad.jp   4    202.232.2.191    202.232.0.0/16                     2497
73            suumo.jp   4      160.17.3.13     160.17.0.0/16                     2497
75            zexy.net   4     160.17.1.144     160.17.0.0/16                     2497
76       carsensor.net   4      160.17.8.24     160.17.0.0/16                     2497
77        townwork.net   4       160.17.2.8     160.17.0.0/16                     2497
78           jalan.net   4      160.17.5.13     160.17.0.0/16                     2497
80        hotpepper.jp   4    160.17.98.198     160.17.0.0/16                     2497

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
<<<<<<< HEAD
     ASn    Internet Exchange  Country Code                                       Country Name
0   2497          JPNAP Tokyo            JP                                              Japan
1   2497          SIX Seattle            US                           United States of America
2   2497     Equinix San Jose            US                           United States of America
3   2497      Equinix Ashburn            US                           United States of America
4   2497    Equinix Hong Kong            HK                                          Hong Kong
5   2497     Equinix New York            US                           United States of America
6   2497                 HKIX            HK                                          Hong Kong
7   2497    Equinix Singapore            SG                                          Singapore
8   2497     DE-CIX Frankfurt            DE                                            Germany
9   2497                 SGIX            SG                                          Singapore
10  2497            LINX LON1            GB  United Kingdom of Great Britain and Northern I...
11  2497    Equinix Palo Alto            US                           United States of America
12  2497               DIX-IE            JP                                              Japan
13  2497  Equinix Los Angeles            US                           United States of America
14  2497       NYIIX New York            US                           United States of America
15  2497          JPNAP Osaka            JP                                              Japan
```
=======
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
>>>>>>> 2139cbb247e5edcfb6d188b1d81d2965423d86f7
