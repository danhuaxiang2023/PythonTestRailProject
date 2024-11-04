import sys
from urllib import request

# import lxml.etree as ET


from testrail import *
import json

from pytimeparse.timeparse import timeparse

from json2xml import json2xml

from json2xml.utils import readfromurl, readfromstring, readfromjson

import datetime
from datetime import datetime
from datetime import timedelta
import time
import testrail



import getpass

#testids = [167379465,167379278,167379277,167379276,167379275,167379274,167379273,167379650,167379649,167379583,167379283,167379302,167379295,167379294,167379291,167379290,167379289,167379505,167379504,167379280,167379567,167379565,167379564,167379562,167379561,167379759,167379502,167379501,167379500,167379499,167379498,167379497,167379496,167379316,167379460,167379459,167379458,167379457,167379456,167379455,167379451,167379449,167379448,167379446,167379445,167379444,167379443,167379442,167379441,167379440,167379439,167379438,167379437,167379436,167379435,167379434,167379433,167379432,167379431,167379430,167379429,167379428,167379427,167379426,167379425,167379424,167379423,167379422,167379421,167379420,167379419,167379418,167379417,167379416,167379415,167379414,167379413,167379645,167379742,167379246,167379757,167379272,167379271,167379270,167379269,167379268,167379267,167379266,167379265,167379264,167379263,167379262,167379261,167379260,167379259,167379258,167379257,167379254,167379253,167379577,167379507,167379236,167379235,167379731,167379730,167379728,167379726,167379725,167379724,167379722,167379710,167379708,167379386,167379379,167379749,167379748,167379746,167379745,167379744,167379588,167379585,167379621,167379622,167379623,167379627,167379628,167379629,167379630,167379632,167379619,167379620,167379624,167379625,167379626,167379631,167379671,167379670,167379669,167379538,167379537,167379530,167379525]
testids = [167379302,167379301,167379295,167379294,167379291,167379290,167379289,167379505,167379504,167379280,167379567,167379563,167379255,167379727]

# baseUrl = 'http://gdcqatestrail01/testrail'
client = testrail.APIClient('http://gdcqatestrail01/testrail/')


# client.user = 'dli@greendotcorp.com'
# client.password = 'avX8eFkpPXmpKo3LMXm0-HT5Ib.6LGVzYUeATevjE'

# client.user = 'qa_test_automation@greendotcorp.com'
# # client.password = 'qa_test_automation'
# client.password = 'cWFfdGVzdF9hdXRvbWF0aW9uQGdyZWVuZG90Y29ycC5jb206cWFfdGVzdF9hdXRvbWF0aW9u'


def getconfigs():
    configsofbaas = client.send_get('get_configs/85')

    for group in configsofbaas:
        print(group['name'])


    #result = client.send_post('add_config_group/96', {"name": groupname})
    #result  = client.send_post('delete_config_group/' + str(group['id']),{})
    #print(result)

        if True:
            for config in group['configs']:
                print(config['name'])
            #client.send_post('add_config/' + str(result['id']), {"name": config['name']})

#def getCasesForProject(projectid, suite_id):
def getCasesForProject(projectid, suite_id):
    casesuitemap = {}
    allsections =  client.send_get('get_sections/%i&suite_id=%i' % (projectid, suite_id))
    for section in allsections:
        allcases = client.send_get('get_cases/%i&suite_id=%i&section_id=%i' % (projectid, suite_id, section['id']))
        for case in allcases:
            casesuitemap[case['id']] = [case['title'], section['name']]

    return casesuitemap





#def getCasesForProject(projectid, suite_id):
def getProject(projectid):
    #client.send_get('get_sections/%i&suite_id=%i' % (projectid, suite_id))
    #client.send_get('get_project/%i' %  projectid)
    client.send_get('get_projects' )


def getresults(case_id):
    return client.send_get('get_history_for_case/%i' % case_id)

#print(getCasesForProject(85, 248713))

def getplan(case_id):
    plan =  client.send_get('get_plan/%i' % case_id)
    for entry in plan['entries']:
        print(str(entry['name']) + ',' + str(entry['runs'][0]['custom_status2_count']))

def getusers():
    plan =  client.send_get('get_users')
    print(plan)




def get_baas_opened_milestones():
    return client.send_get('get_milestones/96&is_completed=0')

def get_result():
    totaltime = 0
    for r in client.send_get('get_results/172236832'):
        if r['elapsed'] is not None:
            totaltime = totaltime + timeparse(r['elapsed'])
            print(timeparse(r['elapsed']))
    print(str(timedelta(seconds=totaltime)))

    return client.send_get('get_results/172236832')


def addresult():
    #    #   self.testRailClient.send_post(f'add_result/{c["id"]}', {"assignedto_id": sCurrentuser})
    #client.send_post(f'add_result/167379537', {"status_id": 12})
    for t in testids:
        client.send_post(f'add_result/{t}', {"status_id": 12})


def get_milestone():
    return client.send_get('get_milestones/96&is_completed=0')



def close_plans(project_id, date_before):
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


def checkplans(project_id):
    testplans =  client.send_get(f'get_plans/{project_id}&is_completed=0')
    #print(testplans[0])
    for p in testplans:
        print(p)

#print(get_result())
#checkplans(96)
#auth = str(            base64.b64encode(                 bytes('%s:%s' % ('dli@greendotcorp.com', 'avX8eFkpPXmpKo3LMXm0-HT5Ib.6LGVzYUeATevjE'), 'utf-8')            ),            'ascii'        ).strip()
#print(auth)


def checktestinfiles(mileStone):
    testrunobjects = []

    testplans = get_regression_test_runs(mileStone)
    for testplan in testplans:
        testruns = get_test_runs(testplan['plan_id'])
        for testsuite in testruns["entries"]:
            testrunobjects.append(testsuite['runs'][0])

    testcases = {}
    casemaptosuite = {}
    fp = open("allcases.txt", "r", encoding='utf-8')
    for x in fp:
        if "https://gdcqatestrail01/testrail/index.php?/tests/view/" in x:
            testid = x[len("https://gdcqatestrail01/testrail/index.php?/tests/view/"): len(
                "https://gdcqatestrail01/testrail/index.php?/tests/view/") + 9]
            
            print("testId:" + testid)
            testObject = client.send_get(f'get_test/{testid}')

            caseid = testObject['case_id']

            caseobject = client.send_get(f'get_case/{caseid}')

            testcases[testObject['case_id']] = testObject['title']

            casemaptosuite[testObject['case_id']] = caseobject['suite_id']




    #print(len(testcases))
    #print(testcases)

    caseMaptoprogram = {}

    for key, value in testcases.items():
        testRunsofcase = ""
        for testrunobject in testrunobjects:
            testrunid = testrunobject['id']

            if casemaptosuite[key] == testrunobject['suite_id']:
                try:
                    testRunobjectofCase = client.send_get(f'get_results_for_case/{testrunid}/{key}')
                    if testRunsofcase.find(testrunobject['config'].split(',')[2]) < 0:
                        testRunsofcase = testRunsofcase + testrunobject['config'].split(',')[2]
                except APIError as e:
                    print("No (active) test found for the run/case combination.")

        if len(testRunsofcase) > 0:
            caseMaptoprogram[value] = testRunsofcase

    return caseMaptoprogram









def get_plans_by_milestone_id(milestone_id):
    test_plans = client.send_get('get_plans/96&milestone_id=' + str(milestone_id))
    return test_plans


def get_results_for_case():
    test_plans = client.send_get('get_results_for_case/1321518/173197572' )
    return test_plans

def get_baas_all_plans():
    test_plans = client.send_get('get_plans/96')
    return test_plans

def __filter_by_milestone(_milestone, _planName):
    def filter_closure(run):
        return str(_milestone) in run['name'] and _planName in run['name'] and run['name'].endswith(str(_milestone))
    return filter_closure
def get_qa_regression_info(_milestone):
    test_plans = get_baas_all_plans()
    runs_with_project = filter(__filter_by_milestone(_milestone, 'BaaS - Regression'), test_plans)
    return runs_with_project
def get_test_runs(plan_id):
    test_runs = client.send_get('/get_plan/' + str(plan_id))
    return test_runs
def get_test_run_list_by_plan_id(plan_id, project_name='BaaS_Partner Service'):
    test_runs = get_test_runs(plan_id)
    test_run_list = []
    for r in test_runs['entries']:
        test_run = {}
        if project_name in r['name']:
            test_run_id = r['runs'][0]['id']
            test_run['id'] = test_run_id
            test_run_partner = r['runs'][0]['config']
            test_run['partner'] = test_run_partner
            test_run['plan_id'] = plan_id
            test_run_list.append(test_run)
    return test_run_list

def get_regression_test_runs(_milestone, _projectName='BaaS_Partner Service'):
    all_test_runs = []
    if _projectName == 'BaaS_Partner Service':
        plans = get_qa_regression_info(_milestone)

    for plan in plans:
        test_runs = get_test_run_list_by_plan_id(plan['id'], _projectName)
        all_test_runs = all_test_runs + test_runs

    return all_test_runs



def sort_words_after_comma(filename):
    """Sorts the words after the comma in each row of a file,
    preserving line breaks, and writes the modified rows to a new file.
    """

    with open(filename, 'r') as file:
        rows = file.readlines()

    with open('casemaptoprogram_sorted_output.txt', 'w') as output_file:
        for row in rows:
            parts = row.split(',')
            if len(parts) > 1:
                words_after_comma = parts[1].strip().split()
                words_after_comma.sort()
                parts[1] = ' '.join(words_after_comma)
            # Preserve line breaks by using writelines()
            output_file.writelines((','.join(parts) + '\n'))

            

# print(get_regression_test_runs('Milestone 149'))

#print(get_plans_by_milestone_id(6476))


#testruns = get_test_runs(1317302)
#print(testruns['entries'][1]['runs'][0])

#print(client.send_get(f'get_run/1298994'))

#print(client.send_get(f'get_case/106353742'))

#print(client.send_get(f'get_test/172199757'))

#print("AWS_QA, 50600, intuitqb".split(',')[2])

# mileStone = 'Milestone 149'
# fpformap = open("RegressionCoverage_BaaS - QA - {mileStone}.csv", "w", encoding='utf-8')
# list = checktestinfiles(mileStone)

# for key, value in list.items():
#     print(value)
#     fpformap.write(key + ',' + value + '\r')


#print(get_results_for_case())
statusList = get_statuses

print(statusList)
    



# if __name__ == '__main__':
#    filename = 'casemaptoprogram.csv'  # Replace with the actual filename
#    sort_words_after_comma(filename)    
