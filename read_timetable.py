import csv, os
files = os.scandir()
for file in files:
	file_name = file.name
	lst = file_name.split("-")
	print(file_name, lst)
	
	if lst[0] != 'Section':
		continue
	
	with open(file_name, 'r') as file:
	    reader = csv.reader(file)

	    headers = next(reader)

	    data = list(reader)
	wrd = 'Timetable-'+lst[1]
	with open('Timetable-'+lst[1].split('.csv')[0]+'.html', 'w') as file:
	    file.write('<table border=2px>\n')

	    file.write('  <tr>\n')
	    for header in headers:
	        file.write(f"   <th>{header}</th>\n")
	    file.write('  </tr>\n')

	    for row in data:
	        file.write('    <tr>\n')
	        for item in row:
	            file.write(f'   <td>{item}</td>\n')
	        file.write('</tr>\n')

	    file.write('</table>\n')


