import json
import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--name')
    parser.add_argument ('--surname')
    parser.add_argument ('--middle_name', default = None)
    parser.add_argument ('--age')
    parser.add_argument ('--sex')
    parser.add_argument ('--married', action='store_const', const=True, default = False)
    parser.add_argument ('--hobbies', nargs='+', default = None)
    
    return parser


if __name__ == "__main__":


    parser = createParser()
    namespace = parser.parse_args()

    print(namespace)
    
    data = {
           "name": "{}".format (namespace.name), 
           "surname": "{}".format (namespace.surname),
           "middle_name": "{}".format (namespace.middle_name),
           "age": "{}".format (namespace.age),
           "sex": "{}".format (namespace.sex),
           "married": "{}".format (namespace.married),
           "hobbies": "{}".format (namespace.hobbies)
          }
    
    with open("journal.txt", "a") as journal:
        json.dump(data, journal, ensure_ascii=False)
        journal.write('\n')
