import os


file_path = r"C:\Users\dxiang\GitHub\ReadyAPI\qa-readyapi-BE-ACC\BaaS\Requirement\BAT\BaaS_MoneySweepProcessor Service"

for root, dirs, files in os.walk(file_path):
    print(root)

    for name in files:
        print(name)
    #     print(os.path.join(root, name))

    # for dir in dirs:
    #     # print(os.path.join(root, dir))         
    #     print(dir)      



