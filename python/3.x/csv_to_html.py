import pandas as pd

def make_link(url, link):
    return f'<a href="{url}">{link}</a><br>'

def csv_to_html(inFile, outFile):

    # Read CSV file
    df = pd.read_csv(inFile)
    # df.info()
    df.fillna('', inplace=True)

    #Define HTML String
    html_string = '''
    <html>
    <head>
        <title>HTML Pandas Dataframe with CSS</title>
        <link rel="stylesheet" type="text/css" href="../CSS/table.css"/>
    </head>
    <body>
        {table}
    </body>
    </html>
    '''
    # Write to file
    with open(outFile, 'w') as f:
        f.write(html_string.format(table=df.to_html(escape=False)))


####################### Sample ##################################################
    # df = pd.read_csv("python/3.x/output/UnstableCases_BaaS - Regression - WMMC - Milestone 162.csv")

    # Define html file
    # html_string1 = '''
    # <html>
    # <head>
    #     <title>HTML Pandas Dataframe with CSS</title>
    #     <style>
    #         table, th, td {{
    #             border: 1px solid black;
    #             border-collapse: collapse;
    #         }}
    #         th, td {{padding: 5px;}}
    #         th {{text-align: left;}}
    #     </style>
    # </head>
    # <body>
    #     {table}
    # </body>
    # </html>
    # '''

    # OUTPUT AN HTML FILE
    # with open('python/3.x/output/myhtml_test1.html', 'w') as f:
    #     # table = df.to_html(escape=False)
    #     # html_string1.format(table=table)
    #     # print(html_string1.format(table=table))
    #     f.write(html_string1.format(table=df.to_html(escape=False)))

####################### Sample ##################################################



#Export as HTML file
# df.style.set_table_styles([{'selector':'table,th,td','props': 'border: 1px solid black;border-collapse: collapse;'}]).to_html("python/3.x/output/myhtml_test.html", escape=False, render_links=True)

# df.style.set_table_attributes('class="mystyle"').to_html("python/3.x/output/myhtml_test.html", escape=False, render_links=True)

# df.to_html("python/3.x/output/unstableCase.html", escape=False, render_links=True)

# link = '<a href="{0}">{0}</a>'
# stackOverflowLink = link.format("http://stackoverflow.com")


# import pandas as pd

# class DocumentTable:
#     def __init__(self, file_names, path):
#         d = {
#             "File_Code": [
#                 f"[P{i+1:03}](<{path}/{f}>)" for i, f in enumerate(file_names)
#             ],
#             "File_Name": file_names,
#         }
#         self._df = pd.DataFrame(d)

#     def to_markdown(self):
#         return self._df.to_markdown()

# example_data = DocumentTable(
#     ["tech1.doc", "tech2.doc", "tech3.doc"],
#     "//ishare.xl.company.com/sites/NTC_Intranet/Shared\ Documents/Review",
# )
# print(example_data.to_markdown())


# import pandas as pd
# import html

# urls = {
#     'P001': 'https://example.com/tech1.doc',
#     'P002': 'https://example.com/tech2.doc',
#     'P003': 'https://example.com/tech3.doc'
# }


# def make_link(url, link):
#     return f'<a href="{url}">{link}</a><br>'

# links = []

# for item in urls:
#     links.append(make_link(urls[item], item))

# df = pd.DataFrame([link for link in links], columns=['urls'])
# df = df.set_index('urls')
# print(html.unescape(df.to_html(render_links=True)))