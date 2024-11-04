import pyodbc


server = 'gdcqaautosql201'
database = 'extend_views'
username = 'dxiang'
password = 'ASDFqwer12345^'
driver = '{ODBC Driver 17 for SQL Server}'
# driver = '{SQL Server 2012 Native Client}' 

# To Resolve #[SQL Server]Login failed for user 'dxiang'. (18456) error, need add Trusted_Connection=YES to connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=YES'

backend_passRate_query = '''
Select Platform, TestCount
from TRPlanPassRate 
where 
Project='TailFin' 
--and Platform = 'GSS'
and Milestone in ( 'Milestone 166', 'Release 183')
order by CreateDate desc
'''

backend_longRunning_Query = '''
SELECT [Platform], Count(*) as 'Long Running Count'
FROM [extend_views].[dbo].[TRTestExecutionHistory]
where Domain = 'TailFin'
and Milestone in ( 'Milestone 166', 'Release 183')
and Duration >= 300 
Group by Platform
'''

# connect = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
# "Server=gdcqaautosql201;"
# "Database=extend_views;"
# "Trusted_Connection=yes;")  #[SQL Server]Login failed for user 'dxiang'. (18456)

# with open('data.csv', 'r') as f:
#    reader = csv.reader(f)
#    customer_list = list(reader)

# insert_multiple_data_query = '''
# INSERT INTO customers (id, first_name, last_name, email, UID, sign_up_date)
# VALUES (?, ?, ?, ?, ?, ?)
# '''

# cursor.executemany(insert_multiple_data_query, customer_list)
# conn.commit()
# connect.close()

# Connection is automatically closed when leaving the 'with' block
with pyodbc.connect(connection_string, autocommit=True) as conn:
    cursor = conn.cursor()
    cursor.execute(backend_passRate_query)
    passRates = dict(cursor.fetchall())
    print(passRates)   

    cursor.execute(backend_longRunning_Query)
    longRunnings = dict(cursor.fetchall())
    print(longRunnings)

    totalLongRunCount = 0
    totalTestCount = 0
    list = []
    for platform, testCount in passRates.items():
        totalTestCount += testCount
        longRunCount = longRunnings.get(platform)
        totalLongRunCount += longRunCount
        rate = longRunCount/testCount*100
        list.append(f'{platform},{longRunCount},{testCount},{rate:.2f}')
    
    totalRate = totalLongRunCount/totalTestCount*100    
    list.append(f'BackendTotal,%d,%d,%.2f' % (totalLongRunCount,totalTestCount,totalRate))
    print(list)
