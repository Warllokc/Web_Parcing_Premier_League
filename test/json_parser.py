import json

# read file
my_file = open('players.json')
data=json.load(my_file)
for i in data:
    print(i)
    # print(data)

# with open('players.json', 'r') as fd:
#     d_old_str = fd.read().replace('\n', '') # remove all \n
#     old_d = json.loads(d_old_str)
#     print(old_d)
# parse file
# obj = json.loads(data)
# # # show values
# print(str(obj))
# print("eur: " + str(obj['eur']))
# print("gbp: " + str(obj['gbp']))
#
# for distro in distros_dict:
#     print(distro['name'])