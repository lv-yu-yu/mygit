import  xml.etree.ElementTree as et

stu = et.Element("Student")

name = et.SubElement(stu, "Name")
name.attrib = {'lang','en'}
name.text = 'maozedong'


age = et.SubElement(stu,'Age')
age.text = 18

et.dump()