import json

with open('C:\python2\week4\lab\json\data.json', 'r') as file:
    json_data = json.load(file)

print("""Interface Status
================================================================================
DN                                              Description           MTU    Speed 
---------------------------------------------- --------------------  ------  ------""")

for i in range(3):
    for key, value in json_data["imdata"][i]['l1PhysIf']["attributes"].items():
        if key == 'dn':
            print(value, end = "                            ")
        if key == 'speed':
            print(value, end = "")
        if key == 'mtu':
            print(value, end = "   ")
    print()

    