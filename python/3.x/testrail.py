"""TestRail API binding for Python 3.x.

(API v2, available since TestRail 3.0)

Compatible with TestRail 3.0 and later.

Learn more:

http://docs.gurock.com/testrail-api2/start
http://docs.gurock.com/testrail-api2/accessing

Copyright Gurock Software GmbH. See license.md for details.
"""

import base64
import json

import requests
import datetime
import time
import dateTimeOperation



class APIClient:
    def __init__(self, base_url):
        self.user = 'qa_test_automation@greendotcorp.com'
        self.password = 'qa_test_automation'
        # self.encryptedPwd = 'uMzck3FGBixjW76GuB/5Px5hp1axQhJv'
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

    def send_get(self, uri, filepath=None):
        """Issue a GET request (read) against the API.

        Args:
            uri: The API method to call including parameters, e.g. get_case/1.
            filepath: The path and file name for attachment download; used only
                for 'get_attachment/:attachment_id'.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('GET', uri, filepath)

    def send_post(self, uri, data):
        """Issue a POST request (write) against the API.

        Args:
            uri: The API method to call, including parameters, e.g. add_case/1.
            data: The data to submit as part of the request as a dict; strings
                must be UTF-8 encoded. If adding an attachment, must be the
                path to the file.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('POST', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri

        auth = str(
            base64.b64encode(
                bytes('%s:%s' % (self.user, self.password), 'utf-8')
            ),
            'ascii'
        ).strip()
        # auth = 'cWFfdGVzdF9hdXRvbWF0aW9uQGdyZWVuZG90Y29ycC5jb206cWFfdGVzdF9hdXRvbWF0aW9u'
        # print(auth)
        headers = {'Authorization': 'Basic ' + auth}

        if method == 'POST':
            if uri[:14] == 'add_attachment':    # add_attachment API method
                files = {'attachment': (open(data, 'rb'))}
                response = requests.post(url, headers=headers, files=files)
                files['attachment'].close()
            else:
                headers['Content-Type'] = 'application/json'
                payload = bytes(json.dumps(data), 'utf-8')
                response = requests.post(url, headers=headers, data=payload)
        else:
            headers['Content-Type'] = 'application/json'
            response = requests.get(url, headers=headers)

        if response.status_code > 201:
            try:
                error = response.json()
            except:     # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('TestRail API returned HTTP %s (%s)' % (response.status_code, error))
        else:
            if uri[:15] == 'get_attachment/':   # Expecting file, not JSON
                try:
                    open(data, 'wb').write(response.content)
                    return (data)
                except:
                    return ("Error saving attachment.")
            else:
                try:
                    return response.json()
                except: # Nothing to return
                    return {}



class APIError(Exception):
    pass




def close_plans(project_id, date_before):

    client = APIClient('http://gdcqatestrail01/testrail')
    # client.user = ''
    # client.password = ''

    datetime_object = datetime.strptime(date_before, '%Y-%m-%d')
    print("date_time =>", datetime_object)

    # displaying unix timestamp after conversion
    print("unix_timestamp => ",
          (time.mktime(datetime_object.timetuple())))
    unixtime = int(time.mktime(datetime_object.timetuple()))



    testplans =  client.send_get(f'get_plans/{project_id}&is_completed=0&created_before={unixtime}')
    #print(testplans[0])
    for p in testplans:
        if p['id'] not in [1174170, 1230820, 1205964]:
            id = p['id']

            client.send_post(f'close_plan/{id}', {})
            print(p)

#Close Plans
#close_plans(96, '2023-07-01')


def get_milestoneId(client, project_id, mileStone):
    #client = client('http://gdcqatestrail01/testrail')
    mileStones = client.send_get(f'get_milestones/{project_id}&is_completed=0')
    mileStoneId = 0

    for i in mileStones:
        if i["name"] == mileStone:
            mileStoneId = i["id"]
    return mileStoneId

def get_planId(client, project_id, planName):
    #client = client('http://gdcqatestrail01/testrail')
    plans = client.send_get(f'get_plans/{project_id}&is_completed=0')
    planId = 0

    for i in plans:
        if i["name"] == planName:
            planId = i["id"]
    return planId

def get_userId_by_email(client, email):
    user = client.send_get(f'get_user_by_email&email={email}')  #{'id': 1390, 'name': 'Donna Xiang', 'email': 'dxiang@greendotcorp.com', 'is_active': True}
    userId = user['id']
    print(userId)
    return userId

def get_user_by_email(client, email):
    user = client.send_get(f'get_user_by_email&email={email}')  #{'id': 1390, 'name': 'Donna Xiang', 'email': 'dxiang@greendotcorp.com', 'is_active': True}
    return user


def get_failures_by_run(client, runId):
    #Get Failed Results for Run with RunId and StatusIds
    failedResults = client.send_get(f'get_results_for_run/{runId}&status_id=7,8')
    passedResults = client.send_get(f'get_results_for_run/{runId}&status_id=1,2,6')
    failedTestIds = []
    passedTestIds = []

    for result in failedResults:
        testId = result["test_id"]
        failedTestIds.append(testId)
        
    for result in passedResults:
        testId = result["test_id"]
        passedTestIds.append(testId) 

    #print("The original failed Test Ids: " + str(failedTestIds))

    # using set() to remove duplicated item from list
    failedTestIds = list(set(failedTestIds))
    passedTestIds = list(set(passedTestIds))
 
    # printing list after removal
    # distorted ordering
    # print ("The failed test id list : " + str(failedTestIds))
    # print ("The success test id list : " + str(passedTestIds))
 
    #Exclude passed testIds from failed list
    if failedTestIds:
        failedTestIds = [testId for testId in failedTestIds if testId not in passedTestIds]

    print("Failed TestId List after remove passed: " + str(failedTestIds))

    return failedTestIds

def get_results_by_run(client, runId, status_id, created_beofore):
    #Get Results for Run with RunId and StatusIds
    unixTime = dateTimeOperation.convertToUnixTime(created_beofore)
    results = client.send_get(f'get_results_for_run/{runId}&status_id={status_id}&created_before={unixTime}')

    return results

    # failedTestIds = []


    # for result in failedResults:
    #     testId = result["test_id"]
    #     failedTestIds.append(testId)

#Returns a list of test results for a test
def get_results_by_test(client, test_id, limit):
    results = client.send_get(f'get_results/{test_id}&limit={limit}')

    return results

# Returns test list
def get_tests_by_run(client, run_id):
    tests = client.send_get(f'get_tests/{run_id}')  

    # testDic = {}
    # for test in tests:
    #     print(test)
    #     testDic[test.get('id')] = test['title']

    # return testDic
    return tests

# Returns test_id/case_name dictionary for a given run and status list
def get_tests_by_run_status(client, run_id, status_id):
    tests = client.send_get(f'get_tests/{run_id}&status_id={status_id}')  

    testDic = {}
    for test in tests:
        print(test)
        testDic[test.get('id')] = test['title']

    return testDic
    # return tests    

def get_test_by_testId(client, test_id):
    test = client.send_get(f'get_test/{test_id}')  
    return test

def get_caseName_by_testId(client, test_id):
    test = client.send_get(f'get_test/{test_id}') 
    return test.get('title')

def get_caseName_by_caseId(client, case_id):
    case = client.send_get(f'get_case/{case_id}')
    print(case)
    return case.title

def get_statuses(client):
    statuses = client.send_get('/get_statuses')
    return statuses

def assign_failures_by_projectName(client, runId, runName):
    failedTestIds = get_failures_by_run(client, runId)

    if failedTestIds:
        with open(".\\3.x\\files\\BaaSProjectAssignee.json", "r") as json_file:
            data = json_file.read()
        projectAssigneeMapping = json.loads(data)        
        assigneeEmail = projectAssigneeMapping[runName]
        assigneeId = get_userId_by_email(client,assigneeEmail)
        print(f"Assign failures to {assigneeEmail}, assigneeId = {assigneeId}")

        # Assign Failurs to QA
        for testId in failedTestIds:
            url = f'add_result/{testId}'        
            data = {'assignedto_id':assigneeId}
            client.send_post(url, data )
        print("***"*10)

def assign_failures_by_testSuiteName(client, runId):
    print("Not Implement")
    print("***"*10)