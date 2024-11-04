import os
from lxml import etree as ET

ET.register_namespace('con', "http://eviware.com/soapui/config")


def get_all_valid_tags(folder_path):

    project_setting_file = folder_path + r"\settings.xml"
    try:
        tree = ET.parse(project_setting_file, parser=ET.XMLParser(strip_cdata=False))
    except Exception as e:
        raise e
    root = tree.getroot()

    print(root.tag)
    print(root.attrib)

    for child in root:
        print(child.tag, child.attrib)

    # tag_ids = []
    # for tag in root.findall('.//{*}tag'):
    #     print(f"tag: {tag}")
    #     for id in tag.findall('.//{*}id'):
    #         tag_ids.append(id.text)
    # return tag_ids


def remove_invalid_tags_in_project(folder_path, valid_tags):

    for rootd, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(rootd, file_name)
            if os.path.isfile(file_path):
                try:
                    tree = ET.parse(file_path, parser=ET.XMLParser(strip_cdata=False))
                except Exception as e:
                    continue
                root = tree.getroot()
                for tag_id in root.findall('.//{*}tagId'):
                    if tag_id.text not in valid_tags:
                        print(file_path)
                        print(tag_id.text)
                        root.remove(tag_id)
                        tree.write(file_path, encoding='utf-8', xml_declaration=True)

        for sub_dir in dirs:
            remove_invalid_tags_in_project(os.path.join(rootd, sub_dir), valid_tags)


if __name__ == "__main__":
    folder_path = r"C:\Users\dxiang\GitHub\ReadyAPI\qa-readyapi-BE-ACC\BaaS\Requirement\Com\EGift Service"
    get_all_valid_tags(folder_path)
    # valid_tags = get_all_valid_tags(folder_path)
    # remove_invalid_tags_in_project(folder_path,valid_tags)