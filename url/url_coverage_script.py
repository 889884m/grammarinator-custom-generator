from maliciousURLChecker import urlChecker
import os

def testsToList(direc):
    result = []
    # Iterate through all files in the folder
    for file_name in os.listdir(direc):
        file_path = os.path.join(direc, file_name)
        with open(file_path, 'r') as file:
            content = file.read().strip()  # Read and strip leading/trailing whitespace
            result.append(content)
    
    return result


#for mine:
custom_tests = testsToList("/Users/brooke_s/grammarinator-custom-generator/url/custom_url_files/tests")
#for grammarinator:
#custom_tests = testsToList("/Users/brooke_s/grammarinator-custom-generator/url/url_grammarinator_files/tests")

for i in custom_tests:
    urlChecker(i)
