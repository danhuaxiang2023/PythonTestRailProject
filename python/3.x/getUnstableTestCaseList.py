import testrail
import fileOperation
import datetime
import json

# Test Plans:
# BaaS - Regression - GBR - Milestone 149
# BaaS - Regression - Intuitqb - Milestone 149
# BaaS - Regression - Wealthfront - Milestone 149

# Status List
# 1 Passed
# 2 Blocked
# 3 Untested
# 4 Retest
# 5 Failed
# 6 Automated Pass
# 7 Automated Fail
# 10 Not Ready
# 12 Not Valid

# ************************************************************************
# Update mileStone and reportDate for each release before execution
# ************************************************************************
#TestRail URL 
baseUrl = 'http://gdcqatestrail01/testrail'
client = testrail.APIClient(baseUrl)

# Get Status List
def getStatus():    
    statusList = client.send_get('/get_statuses')
    # print(statusList)

    statusDic = {}
    for status in statusList:
        # statusItem = json.loads(status)
        # print(status['id'], status['label'])
        statusDic[status['id']] = status['label']

    return statusDic

# Get QA employee Id and Name
def getEmployees():
    with open('python/3.x/files/employeeEmail.txt', 'r') as f:
        emails = f.readlines()

    employees = {}
    for email in emails:
        # print(email)
        employee = testrail.get_user_by_email(client, email.strip('\n'))
        # print(employee)
        employees[employee['id']] = employee['name']

    return employees

def make_link(url, text):
    return f'<a href="{url}">{text}</a>'

def main():
    # ProjectId: ACC: 96, TailFin: 108
    accProject_id = 108
    mileStone = 'Milestone 167'
    planName = f'BaaS - Regression - WMMC - {mileStone}'
    reportDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_id = '1,2,5,12' #unstable case Status
    # failureList = ["No,Title,Link,Run,Case Status,Defect,Assignee,Root Cause"]
    failureList = ["Title,Run,Case Status,Assignee,Bug/Root Cause"]
    outputFile = f'./python/3.x/output/unstableCase/UnstableCases_{planName}.csv'
    
    # Get Status List
    # statusDic = getStatus()
    # print(statusDic)
    statusDic = {1: 'Passed', 2: 'Blocked', 3: 'Untested', 4: 'Retest', 5: 'Failed', 6: 'Automated Pass', 7: 'Automated Fail', 10: 'Not Ready', 12: 'Not Valid'}

    # Get employee list
    # employeeDic = getEmployees()
    # print(employeeDic)
    employeeDic = {816: 'Nick Xiong', 577: 'Harry Song', 1745: 'Kejing Zuo', 1539: 'Lisa Liu', 927: 'Merry Zhong', 1146: 'Ping Hu', 973: 'Sparta Zhang', 1124: 'Zhe Yang', 1517: 'Cindy Song', 1390: 'Donna Xiang', 28: 'David Li', 1899: 'Chris He', 1902: 'Eric Gu'}


    # #Get PlanId    
    planId = testrail.get_planId(client, accProject_id, planName)
    print("PlanId: " + str(planId))

    
    # #Get Runs under given plan
    planResponse = client.send_get(f'get_plan/{planId}')
    entries = planResponse["entries"]
    # print(entries)


    # count = 0
    # Get manually passed test cases
    for entry in entries:
        runName = entry["name"]
        runId = entry["runs"][0]["id"]
        print(f"RunName: {runName} ; RunId: {str(runId)}" )

        # testDic = testrail.get_tests_by_run(client, runId)
        # print(testDic)

        results = testrail.get_results_by_run(client, runId, status_id, reportDate)
        # print(results)
        for result in results:
            # print(result)
            # count = count + 1
            test_id = result["test_id"]            
            test_view = f"https://gdcqatestrail01/testrail/index.php?/tests/view/{test_id}"
            test = testrail.get_test_by_testId(client, test_id)
            test_name = test.get('title')
            test_link = make_link(test_view, test_name)
            assignee = employeeDic.get(test.get('assignedto_id'))
            # test_name = testrail.get_caseName_by_testId(client, test_id)
            # assignee = result["assignedto_id"] if result["assignedto_id"] != None else ''
            status = statusDic.get(result['status_id'])
            defect = result['defects'] if result["defects"] != None else ''
            # rootCause = ''
            # record = f"{count},{test_name},{test_view},{runName},{status},{defect},{assignee}"
            record = f"{test_link},{runName},{status},{assignee},{defect}"
            # print(record)
            failureList.append(record)

    # Write failures to file
    fileOperation.write_to_file(outputFile, failureList)

    #Export as HTML file
    fileOperation.csv_to_html(csvFile=outputFile, htmlFile=f"python/3.x/output/unstableCase/unstableCase_{mileStone}.html")



if __name__ == "__main__"    :
    main()

