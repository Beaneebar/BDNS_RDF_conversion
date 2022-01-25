# Main file for BDNS RDF converstion kit.

# See original BDNS: https://github.com/theodi/BDNS

import rdflib as rdf
import csv
import requests

# Getting the most uptodate version of BDNS
url = 'https://raw.githubusercontent.com/theodi/BDNS/master/BDNS_Abbreviations_Register.csv'
req = requests.get(url)
url_content = req.content

# Save file (in binary) to csv file.
file_name = "BDNS.csv"
with open(file_name, 'wb') as BDNS_csv:
    BDNS_csv.write(url_content)

# Re-opening the file in read mode to pull data out.
with open(file_name, newline='') as BDNS_csv:
    BDNS = list(csv.reader(BDNS_csv))

# Sort data and pull out classes and subclasses
rdfClass = dict([("No Parent",[])])  # defining an empty dict

# for loop
for x in BDNS[1:]:
    # Breaking the array down
    name = x[0]
    abbr = x[1]
    ifcTag = x[2]
    ifcType = x[3]

    findParent = name.find("-") # searching for the character that marks the presence of a parent
    if name.find("-") != -1:
        parentClass = name[:findParent - 1]
        childClass = name[findParent + 1:]

        # exception handling to add to dict
        try:
            rdfClass[parentClass].append([childClass, abbr, ifcTag, ifcType])
        except:
            rdfClass[parentClass] = [childClass, abbr, ifcTag, ifcType]
    else:
        rdfClass["No Parent"].append([name, abbr, ifcTag, ifcType]) # if no parent - write to No Parent class.

print(rdfClass["No Parent"])
# TODO: Write classes to RDF with instance

# TODO: use Label for the name, and use properties to attach the abreviation and IFC.
# TODO: need to also add the instances
