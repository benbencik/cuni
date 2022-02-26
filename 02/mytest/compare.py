
out = open("02/out")
exp = open("02/expected")

o = out.readlines()
e = exp.readlines()

for i in range(len(o)):
    if o[i] == e[i]: print(True)
    else: print(False)

out.close()
exp.close()