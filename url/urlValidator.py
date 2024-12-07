import validators
import os
import django.core.validators as dj
from django.core.exceptions import ValidationError
import json


def urlValidator():
    #for mine:
    with open("custom_url_files/scheme_list.json") as f:
        schemes = json.load(f)

    tests_mine = testsToList("/Users/brooke_s/grammarinator-custom-generator/url/custom_url_files/tests")
    #for grammarinator:
    tests_grammarinator = testsToList("/Users/brooke_s/grammarinator-custom-generator/url/url_grammarinator_files/tests")
    
    myValidator = dj.URLValidator(schemes)

    for i in tests_mine:
        try:
            valid = myValidator(i)
        except ValidationError as e:
            print(f"The url {i} is not valid from CUSTOM generator")

    for j in tests_grammarinator:
            try:
                valid = myValidator(j)
            except ValidationError as e:
                print(f"The url {j} is not valid from GRAMMARINATOR generator")



def testsToList(direc):
    result = []
    # Iterate through all files in the folder
    for file_name in os.listdir(direc):
        file_path = os.path.join(direc, file_name)
        with open(file_path, 'r') as file:
            content = file.read().strip()  # Read and strip leading/trailing whitespace
            result.append(content)
    
    return result

urlValidator()