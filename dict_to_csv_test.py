import csv

sample_dict1 = {'header1': 1, 'header2': 2}
sample_dict2 = {'header1': 3, 'header2': 4}
headernames = ['header1', 'header2']
output_file = open('test_file.csv', 'w')
datawriter = csv.DictWriter(output_file, fieldnames = headernames)

datawriter.writeheader()
datawriter.writerow(sample_dict1)
datawriter.writerow(sample_dict2)
output_file.close()