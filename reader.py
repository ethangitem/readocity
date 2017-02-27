import openpyx1
import csv
import string

file = open('BookUploadtemplate.xlsx.xlsx', 'r+') #opens file
fileto = open('BookUploadtemplate.xlsx.xlsx','r+')


for line in file:
	new = line.replace('"','')
	fileto.write(new)

csv_data = csv.reader(open('BookUploadtemplate.xlsx.xlsx', 'rU'))   #reads the file with each variable seperated by commas
for row in csv_data:
	sql = 'INSERT INTO bookobjects(Age, Title, Author, ISBN, Illustrated_By, Catagory, Keywords, Booklist source, Release Date, Amazon link, Age Range Max) VALUES("%s", "%s", "%s", "%s");' % (col[a], col[b], col[c], col[d], col[e], col[f])
	print(sql)

def column_to_number(c):
    """Return number corresponding to excel-style column."""
    number=-25
    for l in c:
        if not l in string.ascii_letters:
            return False
        number+=ord(l.upper())-64+25
    return number

def stop():
	if no Title then stop
	elif Age then continue
	else continue

class book:
	def Btitle():
