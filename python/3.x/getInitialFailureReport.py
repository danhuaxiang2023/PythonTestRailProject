import testrail
import fileOperation

# Test Plans:
# BaaS - Regression - Credibly_Milestone 149
# BaaS - Regression - Dayforce_DDA - Milestone 149
# BaaS - Regression - Dayforce_GPR- Milestone 149

# BaaS - Regression - flex - Milestone 149
# BaaS - Regression - GBR - Milestone 149
# BaaS - Regression - Intuitqb - Milestone 149
# BaaS - Regression - Wealthfront - Milestone 149

# BaaS - Regression - PLS - Milestone 149
# BaaS - Regression - StockPile_Parent - Milestone 149

# ************************************************************************
# Update mileStone and reportDate for each release before execution
# ************************************************************************
def make_link(url, text):
    return f'<a href="{url}">{text}</a>'

def main():
    
    # ProjectId: ACC: 96, TailFin: 108
    accProject_id = 108
    mileStone = 'Milestone 162'
    planName = f'BaaS - Regression - WMMC - {mileStone}'
    # planName = "BaaS - Regression - PLS - {mileStone}"
    reportDate = '2024-07-14 21:35:20'  #Find from Email, the first report from Jenkins with subject 'BaaS - Regression - GBR - {mileStone}'
    status_id = '7,8' #Failure Status
    failureList = ["test_name,runName,runId,custom_teststepname,request,response"]
    csvFile = f'./python/3.x/output/InitialFailures_{planName}.csv'
    htmlFile = f'./python/3.x/output/InitialFailures_{planName}.html'

    #TestRail URL 
    baseUrl = 'http://gdcqatestrail01/testrail'
    client = testrail.APIClient(baseUrl)


    #Get MileStoneId   
    mileStoneId = testrail.get_milestoneId(client, accProject_id, mileStone)
    #response = client.send_get(f'get_milestones/{project_id}&is_completed=0')
    print("MileStoneId: " + str(mileStoneId))

    #Get PlanId   
    # planId = 1343404  
    planId = testrail.get_planId(client, accProject_id, planName)
    print("PlanId: " + str(planId))

    
    #Get Runs under given plan
    planResponse = client.send_get(f'get_plan/{planId}')
    entries = planResponse["entries"]

    print(entries)


# Get The Failures on First Exectuion Time
    for entry in entries:
        runName = entry["name"]
        runId = entry["runs"][0]["id"]
        print(f"RunName: {runName}, RunId: {str(runId)}" )        

        results = testrail.get_results_by_run(client, runId, status_id, reportDate)
        print(results)

        for result in results:
            test_id = result["test_id"]
            test_view = f"https://gdcqatestrail01/testrail/index.php?/tests/view/{test_id}"
            test_name = testrail.get_caseName_by_testId(client, test_id)
            test = make_link(url=test_view, text=test_name)
            custom_teststepname = result["custom_teststepname"]
            custom_request_xml = result["custom_request_xml"]
            custom_response_xml = result["custom_response_xml"]            
            request = make_link(url=custom_request_xml, text='request') if custom_request_xml != None else ''
            response = make_link(url=custom_response_xml, text='response') if custom_response_xml != None else ''
            record = f"{test},{runName},{runId},{custom_teststepname},{request},{response}"
            print(record)
            failureList.append(record)

    #Write failures to csv file
    fileOperation.write_to_file(csvFile, failureList)
        
    #Export as HTML file
    fileOperation.csv_to_html(csvFile=csvFile, htmlFile=htmlFile)

if __name__ == "__main__"    :
    main()

