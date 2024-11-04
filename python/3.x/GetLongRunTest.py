import testrail
import fileOperation
import datetime
import json
import dateTimeOperation

# Test Plans:
# Legacy - AdHoc - Release 183
# BaaS - AdHoc - Milestone 165
# GSS - AdHoc - Milestone 165

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
statusDic = {1: 'Passed', 2: 'Blocked', 3: 'Untested', 4: 'Retest', 5: 'Failed', 6: 'Automated Pass', 7: 'Automated Fail', 10: 'Not Ready', 12: 'Not Valid'}

def getLongRunningTest(projectId, planName, mileStone):
     
    reportDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_id = '1,2,4,5,6,7'
    longRunThreshold = 300 # max run time: 300 seconds 
    longRunTest = ["TestId,Title,Elapsed,Milestone,Plan,Run,Section,Status,Tested On"]

   # #Get PlanId    
    planId = testrail.get_planId(client, projectId, planName)
    print("PlanId: " + str(planId))

    
    # #Get Runs under given plan
    planResponse = client.send_get(f'get_plan/{planId}')
    entries = planResponse["entries"]
    # print(entries)

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
            elapsed = result["elapsed"]
            print(elapsed)
            if elapsed:  # elapsed is not None
                runDuration = dateTimeOperation.convertToSeconds(elapsed=elapsed)
                if  runDuration > longRunThreshold:
                    # print(result)
                    test_id = result["test_id"] 
                    test = testrail.get_test_by_testId(client, test_id)
                    test_name = test.get('title')          
                    section = ''
                    status = statusDic.get(result['status_id'])
                    testDate = datetime.datetime.fromtimestamp(result['created_on'])
                    # ["TestId,Title,Elapsed,Milestone,Plan,Run,Section,Status,Tested On"]
                    record = f"{test_id},{test_name},{elapsed},{mileStone},{planName},{runName},{section},{status},{testDate}"
                    print(record)
                    longRunTest.append(record)

    return longRunTest  



def main():
    # ProjectId: ACC: 96, TailFin: 108
    projectId = 108
    mileStone = 'Milestone 169'
    legacyMileStone = 'Release 184'
    outputFile = f'./python/3.x/output/longRunTest_AdHoc.csv'

    # 3.x\output\longRunTest_AdHoc.csv
    testPlans = [
        'BaaS - AdHoc - Milestone 169 - 10/17'
        # 'GSS - AdHoc - Milestone 167'      
        # 'BaaS - Adhoc - WMMC - Milestone 166 - 8/30',
        # 'GSS - Adhoc - WMMC - Milestone 166 - 8/30'
        # 'Legacy - Walmart - Release 183 - Regression - Adhoc'
        # f'BaaS - AdHoc - {mileStone}'
        # f'GSS - AdHoc - {mileStone}',
        # f'Legacy - AdHoc - {legacyMileStone}'
    ]    
    
    longRunTest = []
    for testplan in testPlans:
        if legacyMileStone in testplan: 
            longRunTest = getLongRunningTest(projectId, testplan, legacyMileStone)
        else:
            longRunTest = getLongRunningTest(projectId, testplan, mileStone)
        # print(longRunTest)

        # Write failures to file                
        fileOperation.append_to_file(outputFile, longRunTest)  



 
if __name__ == "__main__"    :
    main()

