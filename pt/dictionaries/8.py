a = {}
for i in range(int(input())):
    eng, lat = input().split(" - ", 1)
    lat = lat.split(", ")
    for elem in lat:
        a[elem] = a.get(elem, '') + eng + ", "
print(len(a))
for key in sorted(a.keys()):
    print(key + " - " + a[key][:-2])