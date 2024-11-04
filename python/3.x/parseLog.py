
filePath = 'python\\3.x\\files\\log.txt'

outPath = 'python\\3.x\\files\\Parsedlog.txt'

log = []
stepList = [
    'MMF - ACI Live Mode',
    'Run TestCase - Process MMF',
    'Check MonthlyFeeEvaluation',
    'Run TestCase - Trigger IXGOFileForAcctHistoryJob',
    'Update ProcessorMessage Records',
    'Validate ProcessorMessage Records',
    'Validate PostInternalTransaction',
    'GetACIBalance-After',
    'Check PurseBalance'
]
with open(filePath, 'r', encoding='UTF-8') as f:
    lines = f.readlines()

    for line in lines:
        for step in stepList: 
            if step in line:
                log.append(line)

print(log)   

with open(outPath, 'w', encoding='UTF-8') as f:
    for line in log:
        f.writelines(line)