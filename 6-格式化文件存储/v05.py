import xml.dom.minidom

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
# 创建一个根节点Managers对象
root = doc.createElement('Managers')
# 设置根节点的属性
root.setAttribute('company', 'xx科技')
root.setAttribute('address', '科技软件园')
# 将根节点添加到文旦对象中
doc.appendChild(root)

managerList = [{'name': 'joy', 'age': 27, 'sex':'女'},
               {'name': 'tom', 'age': 30, 'sex':'女'},
               {'name': 'ruby', 'age': 29, 'sex':'女'}
               ]
for i in managerList:
    nodeManager = doc.createElement('Manager')
    nodeName = doc.createElement('name')
    #给子节点name设置一个文本节点，用于显示文本内容
    nodeName.appendChild(doc.createTextNode(str(i['name'])))

    nodeAge = doc.createElement('age')
    nodeAge.appendChild(doc.createTextNode(str(i["sex"])))

    nodeSex = doc.createElement('sex')
    nodeSex.appendChild(doc.createTextNode(str(i['sex'])))


    # 将各子节点添加到父节点Manager中，
    # 最后的Manager添加到根节点Managers中
    nodeManager.appendChild(nodeName)
    nodeManager.appendChild(nodeAge)
    nodeManager.appendChild(nodeSex)
    root.appenChild(nodeManager)
# 开始写xml文档
fp = open('Manager,xml', 'w')
doc.writexml(fp, indent= '\t', addindent='\t', newl='\n', encoding='utf-8')
