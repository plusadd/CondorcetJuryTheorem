
def jury_value(mem):

    pt = int(pow(2 , len(mem)))

    v = 0.0
    for n in range(pt):
        js  = []
        for b in range(len(mem)):
            o = int(pow(2, b))
            a = o & n
            j = a >> b

            js.append(j)

        if sum(js) > (len(mem)/2):

            sv = 1
            for b in range(len(mem)):
                j = js[b]
                if j:
                    sv = sv * mem[b]
                else:
                    sv = sv * (1-mem[b])
            v = v + sv

            #print(str(js) + " -> " + str(sv))

    return v

v = jury_value([0.7, 0.7, 0.7]) # 0.7839999999999998
print(v)

# c = 0.1
# #c = 0.7
# for m1 in range(100):
#     mv1 = m1*0.01
#     for m2 in range(100):
#         mv2 = m2*0.01
#         v = jury_value([c, mv1, mv2])
#         if v >= c:
#             print(str(mv1) + "\t" + str(mv2) + "\t" + str(v))
