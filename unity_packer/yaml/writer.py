"""
Writer will be used to parse and form new yaml items from defined templates using delimeters.

in this case the delimeters are ` $ item $ `

This can use reflection to look at the object supplied in order to fill in the missing items in the string.

"""

import re
from typing import List

from mesh import meshyaml

delim = r'\$(.*?)\$'

# takes in a unity object and based off class will derive yaml code to link
def GenerateYamlIdentifiers(UnityObject) -> List[str]:
    """ Generates named bindings for the yaml object

    Returns:
        List[str]: all of the bindings
    """
    iter = re.finditer(delim, meshyaml)
    mesh_identifiers = []
    for index in iter:
        # print("MeshYaml - \t" + meshyaml[index.start(0): index.end(0)])
        mesh_identifiers.append(meshyaml[index.start(0): index.end(0)])

    return mesh_identifiers
