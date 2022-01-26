# Main file for BDNS RDF converstion kit.

# See original BDNS: https://github.com/theodi/BDNS
# TODO: need to refactor this code.

from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import RDF, RDFS, OWL
from re import sub
import csv
import requests

# Defining namespaces.
namespace =  "https://raw.githubusercontent.com/Beaneebar/BDNS_RDF_conversion/main/BDNS/namespace" # defining the namespace for BDNS as out of the GitHub Repo
IFC = Namespace("http://ifcowl.openbimstandards.org/IFC4#") # Github page: https://github.com/buildingSMART/ifcOWL - Using IFC4 - may require update. - NOT A PERMALINK

# URI generator function
def urigen(uri, className):
    # writing the className in camelCase
    className = sub(r"(_|-)+", " ", className).title().replace(" ", "")
    uriAppend = ''.join([className[0].lower(), className[1:]])
    return uri + "#" + uriAppend

# Importing latest version of BDNS
url = 'https://raw.githubusercontent.com/theodi/BDNS/master/BDNS_Abbreviations_Register.csv' # Getting the most uptodate version of BDNS
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
rdfClass = dict([("No Parent",[])])  # defining an empty dict - not needed but here for debugging.

# Starting RDF graph construction
g_BDNS = Graph()

# for loop
for x in BDNS[1:]:
    # Breaking the array down - only needed for pythong dictionary.
    name = x[0]
    abbr = x[1]
    ifcTag = x[2]
    ifcType = x[3]
    print(ifcTag)

    findParent = name.find("-") # searching for the character that marks the presence of a parent
    if name.find("-") != -1:
        parentClass = name[:findParent - 1]
        childClass = name[findParent + 1:]

        # generating the URI in correct format, in type String
        uriParent = urigen(namespace, parentClass)
        uriChild = urigen(namespace, childClass)

        # converting URI string to URIRef
        parentClass_URI = URIRef(uriParent)
        childClass_URI = URIRef(uriChild)

        # adding parent and child classes to graph
        g_BDNS.add((parentClass_URI, RDF.type, RDFS.Class)) # adding parentClass triple
            # Note: parentClasses exist for navigation purposes only, they do not have any instances
        g_BDNS.add((childClass_URI, RDFS.subClassOf, parentClass_URI)) # adding childClass triple
        g_BDNS.add((childClass_URI, RDFS.comment, Literal(abbr)))  # adding abbreviation as label
        g_BDNS.add((childClass_URI, OWL.equivalentClass, IFC[ifcTag])) # adding IFC class equivalence

        # exception handling to add to dict
        try: # case where parentClass already exists
            rdfClass[parentClass].append([childClass, abbr, ifcTag, ifcType])
        except: # case where no parentClass
            rdfClass[parentClass] = [childClass, abbr, ifcTag, ifcType]
    else:
        uriName = urigen(namespace, name) # generating correctly formatted URI string.
        name_URI = URIRef(uriName) # conversting URI string to URIRef
        g_BDNS.add((name_URI, RDF.type, RDFS.Class)) # generating the triple
        g_BDNS.add((name_URI, RDFS.comment, Literal(abbr)))  # adding abbreviation as isDefinedBy
        g_BDNS.add((name_URI, OWL.equivalentClass, IFC[ifcTag]))

        # adding element to special array in dict - only for debugging.
        rdfClass["No Parent"].append([name, abbr, ifcTag, ifcType])

g_BDNS.serialize(destination="BDNS.ttl") #saving file

# TODO: write meta data for the namespace