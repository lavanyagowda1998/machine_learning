
import os
import sys
import commands

def main(dir):
	print "display the list of directory"
	f=os.listdir(dir)
	print f
	
	for filename in f:
		path=os.path.join(dir,filename)
		print path
		print os.path.abspath(path)
		
	print os.path.exists('/home/cit')
	
	cmd = 'ls -l ' + dir
	(status,output) = commands.getstatusoutput(cmd)
	if status:
		print sys.stderr 'there was an error',output
		sys.exit(1)
	print output


	try:
	
	
	

if __name__ == '__main__':
	main(sys.argv[1])
