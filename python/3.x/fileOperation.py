# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
import os
import pandas as pd

def write_to_file(outputFile,list):
        with open(outputFile,'w') as output_file:
                for row in list:
                    output_file.writelines(row + '\n')

def append_to_file(outputFile,list):
        if len(list) > 0:        
            with open(outputFile, 'a', encoding="UTF-8") as output_file:
                    for row in list:
                        output_file.writelines(row + '\n')                    

def read_file(file):
       with open(file, 'r') as f:
              return f.read()
        

def delete_file(file):
       if os.path.exists(file):
              os.remove(file)
       else:
              print("The file does not exist")


def csv_to_html(csvFile, htmlFile):
    # Read CSV file
    df = pd.read_csv(csvFile)
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
    with open(htmlFile, 'w') as f:
        f.write(html_string.format(table=df.to_html(escape=False)))              