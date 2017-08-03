import sys	

def cat(filename):
	print "From here file operation...................................................."
	print "Display the file content ...."
	f = open(filename, 'rU')
	#for line in f:
	#	print line
	
	#lines = f.readlines()
	#print lines
	
	print "read the file content and store it in variable...."
	text=f.read()
	print text
	

	
def write(filename):

	with open(filename,'a') as the_file:
		the_file.write("Hello\n")
	the_file.close()
	
def create_file(filename):
	with open(filename,'a') as this_file:
		this_file.write("Hello\n")
		
def wordcount(filename):
	f=open(filename,'rU')
	line =f.read()
	print len(line.split())
	
		
	
	

if __name__ == '__main__':
	print "hey"
	#hello()
	#cat(sys.argv[1])
	#write(sys.argv[1])
	wordcount(sys.argv[1])
