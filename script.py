import os
             
f=open('README.md','w+')
f.write('# Notes')
f.write('\n\n\n')
startpath = './notes'

for root, dirs, files in os.walk(startpath):
    if root is not startpath:
	    level = root.replace(startpath, '').count(os.sep) -1
	    indent = ' ' * 2 * (level)
	    f.write('{}- {}'.format(indent, os.path.basename(root)))
	    f.write('\n')
	    subindent = ' ' * 2 * (level + 1)
	    for file in files:
		    path = os.path.join(root,file)
		    #f.write('{}- {}/'.format(indent, os.path.basename(root)))
		    f.write("{}- [{}]({})".format(subindent,file[:-3],path))
		    f.write('\n')
