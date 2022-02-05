# BDNS_RDF_conversion
_Conversion kit for the Building Device Naming Standard into RDF._

## Overview
The Building Device Naming Standard (BDNS) is an industry effort to establish a standardised catelogy of names for devices used within buildings, along with a standardised abreviation. As part of BDNS, effort has been put into defining the standard with reference to IFC classes, and the schema is more generally cognizant of other industry projects such as Project Haystack, Brick Schema and the Digital Buildings Ontology. Further information on BDNS can be found here: https://github.com/theodi/BDNS

BDNS currently exits in the form of a CSV file that is maintained on Github through the Issues. While the CSV format lends BDNS to being easily accessed by industry experts, it is an compatible format for use in federating BDNS with other Semantic Web-based Ontologies such as those named above. While BDNS is explicit in existing as a _directory of terms_ and not an ontology, as part of increasing the extensibility of BDNS, defining the schema in a federatable format (e.g. RDF) could be useful for some use-cases. 

In response to this need, this repo has been created to chart and manage the development of a conversion tool that enables BDNS to be easily converted into RDF.

The design structure and methodology of this kit will be developed alongside the code. For future reference, please see [Design Structure](https://github.com/Beaneebar/BDNS_RDF_conversion/blob/main/Design_Structure.md). 
