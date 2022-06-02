import xml.etree.ElementTree as xet
from glob import glob

path = glob('*.xml')

for filename in path:
    et = xet.parse(filename)
    root = et.getroot()
    tree = xet.ElementTree(root)
    xet.indent(tree, '  ')
    
    for folder in root.findall('folder'):
        root.remove(folder)
        f = xet.Element('folder')
        f.text = 'images'
        root.append(f)

    for fn in root.findall('filename'):
        root.remove(fn)
        file = str(filename[:3]) + '.jpg'
        fi = xet.Element('filename')
        fi.text = file
        root.append(fi)

    for pa in root.findall('path'):
        root.remove(pa)
        file = str(filename[:3]) + '.jpg'
        p = xet.Element('path')
        p.text = 'C:\\folder\\where\\the\\files\\are\\' + file
        root.append(p)

    tree.write(filename, encoding="utf-8")

