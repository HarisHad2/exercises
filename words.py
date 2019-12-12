def to_upper(names):
    res = []
    for x in names:
        res.append(x.upper())
    return res

names = ["Haris", "Miralem", "Edin"]
yyy = to_upper(names)
print(yyy)