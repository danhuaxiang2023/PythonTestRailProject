import lxml.etree as ET
import os
import json



tree = ET.parse(r"3.x\files\movies.xml")
root = tree.getroot()

# print(tree)
# print(root)
# print(root.tag)
# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# Get a specific attribute
for movie in root.iter('movie'):
    #Print element movie
    print(movie)    
    #Get a specific attribute
    print(movie.get('title'))  
    #Print XML
    print(ET.tostring(movie,encoding='utf-8',xml_declaration=True,pretty_print=True))


# for description in root.iter('description'):
#     print(description.text)    

# # find node with XPath
# for movie in root.findall("./genre/decade/movie/[year='1981']"):
#     print(movie.attrib)


# for format in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
#     print(format.attrib)

# find movies in 1980s
# for movie in root.findall("./genre/decade[@years='1980s']/movie"):
#     print(movie.attrib)


# b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
# print(b2tf)

# # Write out the tree to the file again
# # tree.write("movies.xml")

# #Append and Remove
# xmen = root.find("./genre/decade/movie[@title='X-Men']")
# print(xmen)

# dec1980s = root.findall("./genre[@category='Action']/decade[@years='1980s']")
# dec1980s.append(xmen)
# print(dec1980s)
# print(ET.tostring(dec1980s, encoding='utf8').decode('utf8'))

# dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
# dec1990s.remove(xmen)
# print(dec1990s)



# action = root.find("./genre[@category='Action']")
# print(ET.tostring(action, encoding='utf8').decode('utf8'))

#Remove invalid tag
# def remove_invalid_tags(projectPath, tags):
#     for rootd, dirs, files in os.walk(projectPath):
#         # print(rootd)
#         # print(files)
        
#         for fileName in files:
#             filePath = os.path.join(rootd, fileName)
#             if(os.path.isfile(filePath)):
#                 try:
#                     tree = ET.parse(filePath, parser=ET.XMLParser(strip_cdata=False))
#                 except Exception as e:
#                     continue
#                 root = tree.getroot()
#                 for tag_id in root.findall(".//{*}tagId"):
#                     if tag_id.text not in tags:
#                         print(f"Remove tagId {tag_id.text} from file {fileName}")
#                         root.remove(tag_id)
#                 tree.write(filePath, encoding='utf-8',xml_declaration=True)

#         for dir in dirs:
#             # print(os.path.join(rootd,dir))
#             remove_invalid_tags(os.path.join(rootd,dir), tags)

# ET.register_namespace('con',"http://eviware.com/soapui/config")
# projectPath = r"C:\Users\dxiang\GitHub\ReadyAPI\qa-readyapi-BE-ACC\BaaS\Requirement\Partner\BaaS_Partner Service_SCC_ACI"
# tree = ET.parse( projectPath + r"\settings.xml")
# root = tree.getroot()
# # print(root)

# #Find all tag ids
# tags = []
# for tag in root.findall(".//{*}tag"):
#     # print(tag.tag)
#     for id in tag.findall(".//{*}id"):
#         # print(id.text)
#         tags.append(id.text)
# print(tags)


# validCardPath = r"C:\Users\dxiang\GitHub\ReadyAPI\qa-readyapi-BE-ACC\BaaS\Requirement\Partner\BaaS_Partner Service_SCC_ACI\ValidateCard-Negative-Suite"
# remove_invalid_tags(validCardPath, tags)


