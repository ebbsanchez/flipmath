# -*- coding:utf-8 -*-

configured = False

def config():
	ordered = None
	payed = None
	test = None
	with open("ordered.txt", 'r') as f:
		exec("ordered =" +f.read())
	with open('payed.txt', 'r') as f:
		exec('payed = ' + f.read())
	with open('test.txt', 'r') as f:
		exec('test = ' + f.read())
	return ordered, payed, test

def update(varname):
	with open(varname + ".txt", 'w') as f:
		exec("content =" + varname)
		f.write(str(content))
		print("update success")

def adding(varname, name):
	exec("global " + varname)
	exec(varname + ".append(name)")
	exec("update('" + varname + "')")


ordered, payed, test = config()
not_payed = []

for o in ordered:
	if o not in payed:
		not_payed.append(o)

def printing():
	print "order: %d" %len(ordered)
	print "payed: %d" %len(payed)
	print "not_payed: %d "  %(len(not_payed))
	for n in not_payed:
		print n,
def respond():
	global ordered, payed, not_payed
	return ordered, payed, not_payed

if __name__ == '__main__':
	printing()

