import sys

def hello():
	print "Good Moring"
	print sys.argv
	good(sys.argv[1])
	
def good(name):
	if name=='Girish' or name=='praveen':
		print 'Alert:Girish Mode'
		name=name+'????'
	else:
		DoesNotExist(name)
		#print 'Else'
	name=name+'!!!!!!!'
	print 'helllo',name
	print 'helllo'+ name
	
	print 'Hi %s I have %d books' % ('Girish',25)
	print 'we, %s and %s, have %d books' % ('Girish','praveen',25)
	
	a ='Hello'
	print len(a)
	print a[1:3]
	print a[1:]
	print a[:]
	# counting from last
	print a[-4:-2]
	print a[:-3]
	print a[-3:]
	print "From here LIST Execrises.............................................."
	list1()
	
#list excerices
def list1():
	print 'concating the list value.......... '
	print [1,2,1]
	print [1,2,'giri'] + ['sh']
	print [1,2,'giri'] + [3,4]
	a=[1,2,3]
	
	print 'printing the list value of position 1.........'
	print a[1]
	b=a
	#It does not change the value of a and b
	print a
	print b
	
	#slice syntax to copy the content
	b=a[:]
	a[0]=8
	print b
		
	#b=':'.join(a)
	#print b
	
	
	a= [6,8,9]
	for num in a: print num
	
	#check the value in list it gives true and false
	#print 8 in a
	
	
	#append the value to list
	print 'append the value to list.............'
	print a
	a.append(16)
	print a
	
	#to pop (delete) the list value
	print 'pop (delete) the list value of position 0..........'
 	a.pop(0)
	print a
	
	# delete the variable or string
	#del a
	#del a[1]
	
	
	#sorting 
	print 'hey do sorting here............'
	a=[1,26,3,66,7]
	print a
	print sorted(a)
	
	#sort me in reverse order  by specifying revrse=True
	print 'sort me in reverse order.............'
	print sorted(a,reverse=True)
	
	#a.insert(1,'gggggg')
	

	print "Custom sorting ................"
	a=['zz','aa','bb','kk']
	print a
	
	def Last(s): 
		return s[-1]
	print sorted(a,key=Last)
	
	
	
	print 'From here splitting excersies ..................................................'
	a=['a','b','dd','jj']
	a= ':'.join(a)
	print 'splt the values of a using :....'
	print a
		
	print 'join the value using : ......'
	b=':'.join(a)
	print b
	
	print 'split the value using : .....'
	#print ':'.split(b)
	#print '\n'.split(b)
	
	print b.split(':')
	
	c='172.16.9.4'
	c.split('.')
	print c
	
	e='02/08/2017'
	e.split('/')[2]
	print e
	
	print "can print the values in given range...."
	print range(20)
	dictionary()
	
def	dictionary():
	print "From here dictionary Exercises ................................................."
	print "create the dictionary and print It...."
	d={}
	d['a']='apple'
	d['b']='mango'
	d['c']='orange'
	d['d']='kiwi'
	d['e']='grapes'
	print d
	
	print 'disply the specific value in  dictionary...'
	print d['a']
	
	print 'disply the specific value in  dictionary using get...'
	print d.get('a')
	print d.get('x')
	
	print 'disply the specific value using IN....'
	if 'b' in d:
		print d['b']
	
	print 'disply only the keys....'	
	print d.keys()
	
	print 'disply only the values....'	
	print d.values()
	
	print 'display both key and value....'	
	for c in d.keys(): 
			print 'key:' '->', d[c]
			
	for a,b in d.items(): 
			print a,b
	#cat(filename)
			
			



	
	
	
if __name__ == '__main__':
	print "hey"
	hello()
	#cat(sys.argv[1])
