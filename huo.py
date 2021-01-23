dicts = {4: 1, 3: 0, 2: 0, 1: 1}
for k, v in sorted(dicts.items(), key=lambda x: x[1], reverse=True):
    print("%s: %s" % (k, dicts[k]))