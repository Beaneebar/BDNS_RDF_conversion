# Design Structure
The conversion kit has been designed to pull the latest version of BDNS from its Github repo and drive the generation of the RDF file from this. As part of the conversion process, a CSV is generated on the users local computer that is populated with the contents of the current version of BDNS.

From this CSV, rdflib is used to create a graph within which the RDF conversion is created. BDNS is written already with associated IFC tags; these tags are maintained through the use of an OWL:equivalentClass tag such that the ontology can be federated more easily with IFC. The IFC ontology that is used for reference is using IFC v4.

There is also debugging code written into the program whereby BDNS is broken down into the relevant sections and stored in a dictionary. This can be used or deleted depending on the user requirements.

Users are free to make changes and submit change requests to the code where useful additions or optimisations are made. 

## NOTE: 
The operation of this conversion kit is sensitive to changes in the file structure of the original BDNS database - if changes occur this conversion kit may no longer function correctly. 
