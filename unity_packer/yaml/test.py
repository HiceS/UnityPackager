""" Tests the usage of the YAML generation module
"""

from writer import GenerateYamlIdentifiers

def main():
    bindings = GenerateYamlIdentifiers()
    if (len(bindings) > 0):
        print(bindings)
        print("YAML - \tPASSED ASSERT")
        return True
    else:
        print("Failed to generate YAML Bindings")
        return False
    
if __name__ == "__main__":
    main()