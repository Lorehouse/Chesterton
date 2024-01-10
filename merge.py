''' import xml.etree.ElementTree as ET

# List of input XML file names
#input_files = ['./1.1.xml', './1.2.xml', 'file3.xml']

input_files = ["../Chesterton/^([1-3]\.[1-9]\.xml$)"]

# Create a new ElementTree object
root = ET.ElementTree()

# Read each input file and append its content to the root element
for input_file in input_files:
	tree = ET.parse(input_file)
	root.append(tree.getroot())

# Write the combined XML content to a new file
output_file = 'all.xml'
root.write(output_file) '''


import glob
# Get a list of files matching the pattern
files = glob.glob("../Chesterton/*.*.xml")
print(files)

# Concatenate the files' contents into a single string
contents = '\n'.join(open(file).read() for file in files)

# Write the combined contents to a new file
with open('all.xml', 'w') as outfile:
	outfile.write(contents)

