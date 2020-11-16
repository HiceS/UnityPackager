"""
Writer will be used to parse and form new yaml items from defined templates using delimeters.

in this case the delimeters are ` $ item $ `

This can use reflection to look at the object supplied in order to fill in the missing items in the string.

"""

import re
from typing import List

from unity_packer.yaml.format import meshyaml, assetmeta

delim = r'\$(.*?)\$'

# takes in a unity object and based off class will derive yaml code to link
def GenerateYamlIdentifiers(UnityObject = None) -> List[str]:
    """ Generates named bindings for the yaml object

    Returns:
        List[str]: all of the bindings
    """
    iter = re.finditer(delim, meshyaml)
    mesh_identifiers = []
    for index in iter:
        print(f'\'{meshyaml[index.start(0)+1: index.end(0)-1]}\': val,')
        mesh_identifiers.append(meshyaml[index.start(0)+1: index.end(0)-1])

    return mesh_identifiers

def GenerateYamlData(bindings: dict, yamlFormat: str) -> str:
    mesh_identifiers = []
    ret = ''
    prev = 0

    for index in re.finditer(delim, yamlFormat):
        # add the first protion if empty
        start = index.start(0)-1
        end = index.end(0)-1

        key = yamlFormat[start + 2: end]
        # print("Key: " + key)
        val = bindings[key]

        if val is not None:
            # construct previous data + value of binding
            ret = f'{ret}{yamlFormat[prev : start+1]}{val}'
        else:
            print("Cannot find value for key: " + key)

        # include the $ and skip over it
        prev = end + 1

    ret = f'{ret}{yamlFormat[prev : ]}'

    print(ret)
    return ret