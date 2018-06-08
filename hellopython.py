def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    else:
        if 2*key in d.keys():
            d[2*key].append(value)
        else:
            d[2*key] = [value]

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)


