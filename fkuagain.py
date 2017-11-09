
import csv

# line is a list of String
def validation(line):
    countryPostalCode = line[0]
    codes = countryPostalCode.split("-")
    if len(codes) == 1: return True
    countryCode, postalCode = codes[0], codes[1]
    validateCountryCodes = {"US","DE","ES","FR","GB","IT","CZ","BE","AT","CH","DK","EE","FI","IE","LT","LU","LV","NL",
                            "NO","PL","PT","SE","GR","HR","HU","RO","RU","SK","TR","BG","SI"}
    isCountryCodeValid = countryCode in validateCountryCodes
    isEveryCharAlphanumeric = True
    for c in postalCode:
        if not c.isalnum():
            isEveryCharAlphanumeric = False
            break
    return isCountryCodeValid and isEveryCharAlphanumeric

filecontent = []
with open('/Users/how/downloads/CPT_test_Invalid_US_Postal.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
        if i == 0 or (i > 0 and validation(row)):
            filecontent.append(row)
        i += 1

with open('/Users/how/downloads/test.csv', 'w') as csvfile:
    fieldnames = filecontent[0]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for rowContent in filecontent[1:]:
        writer.writerow({fieldnames[0]: rowContent[0], fieldnames[1]: rowContent[1],
                         fieldnames[2]: rowContent[2], fieldnames[3]: rowContent[3]})





























































