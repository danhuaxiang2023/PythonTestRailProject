import testrail
import json

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


def main():

    baseUrl = 'http://gdcqatestrail01/testrail'
    client = testrail.APIClient(baseUrl)
    accProject_id = 96
    mileStone = 'Milestone 149'
    planName = 'BaaS - Regression - GBR - Milestone 149'


    #Get MileStoneId   
    mileStoneId = testrail.get_milestoneId(client, accProject_id, mileStone)
    #response = client.send_get(f'get_milestones/{project_id}&is_completed=0')
    print("MileStoneId: " + str(mileStoneId))

    #Get PlanId   
    planId = testrail.get_planId(client, accProject_id, planName)
    print("PlanId: " + str(planId))

    
    #Get Runs under given plan
    planResponse = client.send_get(f'get_plan/{planId}')
    entries = planResponse["entries"]

    # print(entries)

    # # with open(".\\3.x\\files\\BaaSProjectAssignee.json", "r") as json_file:
    # #     data = json_file.read()
    # #     projectAssigneeMapping = json.loads(data)

    # #Assign Failures to QA
    # runId = 0
    # runName = ""
    # for entry in entries:
    #     runName = entry["name"]
    #     runId = entry["runs"][0]["id"]
    #     print("RunName: " + runName)
    #     print("RunId: " + str(runId))
    #     if runName != "BaaS_Partner Service":
    #         testrail.assign_failures_by_testSuiteName(client, runId)
    #     # else:
    #         testrail.assign_failures_by_projectName(client, runId, runName)
        
    #         # assigneeEmail = projectAssigneeMapping[runName]
    #         # assigneeId = testrail.get_userId_by_email(client,assigneeEmail)
    #         # print(assigneeId)

# Get The Failures on First Exectuion Time
    for entry in entries:
        runName = entry["name"]
        runId = entry["runs"][0]["id"]
        print(f"RunName: {runName}" )
        print(f"RunId: {str(runId)}")



if __name__ == "__main__"    :
    main()

