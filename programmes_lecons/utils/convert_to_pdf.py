import subprocess

from .index import tous_les_programmes

for programme_name in tous_les_programmes:
    print(programme_name)
    _temp = __import__(programme_name, globals(), locals(), ['fig'], 0)
    _temp.fig.savefig('_pdf/{}.pdf'.format(programme_name))

file_list = ['_pdf/{}.pdf'.format(programme_name) for programme_name in tous_les_programmes]

subprocess.call(['pdfjoin', '--outfile', 'doc/programmes_lecons.pdf']+file_list)
