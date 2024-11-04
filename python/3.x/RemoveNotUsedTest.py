import lxml.etree as ET
import os


projectPath = "C:\\Users\\dxiang\\GitHub\\ReadyAPI\\qa-readyapi-BE-ACC\\BaaS\Requirement\\BAT\BaaS_MoneySweepProcessor Service"

testCasePath = "C:\\Users\\dxiang\\GitHub\\ReadyAPI\\qa-readyapi-BE-ACC\\BaaS\Requirement\\BAT\BaaS_MoneySweepProcessor Service\\Script_Accounts\\Get-Accounts-By-AccountIdentifier.xml"

def getTestCaseId(testCasePath):
    tree = ET.parse(testCasePath)
    root = tree.getroot()
    # print(root)
    # print(root.tag)
    print(root.attrib)
    testAttributes = root.attrib
    testId = testAttributes['id']
    print(testAttributes['id'])
    return testId

    # testCase = root.iter('con:testCase')
    # print(testCase)


def isTestInvoked(testCasePath, targetTestId):
    with open(testCasePath, 'r', encoding='UTF8') as f:
        content = f.read()
        print(content)
        return True if targetTestId in content else False

def traveralProject(projectPath):
    for root, dirs, files in os.walk(projectPath):
        print(root)








if __name__ == "__main__":
    testId = getTestCaseId(testCasePath)
    isInvoked = isTestInvoked(testCasePath, testId)
    # traveralProject(projectPath)
    print(isInvoked)