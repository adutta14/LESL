import re
import sys

def expression(exp):
	object = []
	exp = exp.strip()
	i=0
	while(i<exp.__len__()):
		if exp[i] != ' ':
			if 'true' in exp or 'false' in exp or '==' in exp or '!=' in exp or '>=' in exp or '<=' in exp:
				if exp[-1] == '.':
					exp = exp.strip('.')
					exp1 = exp.split()
					exp1.append('.')
				else:
					exp1 = exp.split()
				for e in exp1:
					if e == 'true':
						object.append('true')
					elif e == 'false':
						object.append('false')
					elif e == '==':
						object.append('==')
					elif e == '!=':
						object.append('!=')
					elif e == '>=':
						object.append('>=')
					elif e == '<=':
						object.append('<=')
					else:
						for n in e:
							object.append(n)
				break
			else:
				object.append(exp[i])
		i+=1

	return object

def main():
	filename = sys.argv[1]
	try:
		file = open(filename, "r")
	except IOError as e:
		print 'File could not be found'
		return
	except Exception as e:
		print 'Error in opening the file'
		return

	#reading form the file.
	rows = file.readlines()
	Object = []
	
	i = 0
	while(i<rows.__len__()):
		row = rows[i].strip()

		#if row is not a blank line.
		if(row != ''):
			if row.startswith('while'):
				Object.append('while')
				elementExpression = expression(row[5:])
				for elem in elementExpression:
					 Object.append(elem)

			elif row.startswith('if'):
				Object.append('if')
				elementExpression = expression(row[2:])
				for elem in elementExpression:
					Object.append(elem)

			elif row.startswith('elseif'):
				Object.append('elseif')
				elementExpression = expression(row[6:])
				for elem in elementExpression:
					Object.append(elem)

			elif row.startswith('#show'):
				Object.append('#show')
				elementExpression = expression(row[5:])
				for elem in elementExpression:
					Object.append(elem)

			elif row.startswith('begin'):
				Object.append('begin')
				if row.__len__() != 5:
					Object.append(row[5:])

			elif row.startswith('end'):
				Object.append('end')
				if row.__len__() != 3:
					Object.append(row[3:])

			elif row.startswith('else'):
				Object.append('else')
				if row.__len__() != 4:
					Object.append(row[4:])

			elif row.startswith('@'):
				Object.append('@')
				Object.append(row[1:])

			else:
				for elem in (expression(row)):
					Object.append(elem)

		i+=1
	
	try:
		file1 = open("tokens.lbsl", "w+")
	except IOError as e:
		print 'File could not be created'
		return
	except Exception as e:
		print 'Error in opening the file'
		return
		
	file1.write("%s" %Object)
	file1.write(".")
	
	
	#Closing the file in the end
	file1.close()
	file.close()




if __name__ == '__main__':
	main()