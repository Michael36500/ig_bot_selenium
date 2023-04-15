def get_hashtags():
    import random as rn

    freq = open("hst_freq.txt", "r")
    mine = open("hst_mine.txt", "r")
    rare = open("hst_rare.txt", "r")
    avg = open("hst_avg.txt", "r")

    freq = freq.readlines()
    mine = mine.readlines()
    rare = rare.readlines()
    avg = avg.readlines()

    def listing (inp):

        temp = []
        for a in inp:
            l = len(a)
            short = a[:l - 2]
            temp.append(short)
        return temp

    freq = listing(freq)
    mine = listing(mine)
    rare = listing(rare)
    avg = listing(avg)
    # txt.close()


    def ap_hst(inp, kolik):
        hst = []
        for b in range (kolik):
            hst.append(inp[rn.randint(0,len(inp) - 1)])
        return hst
    
    freq = ap_hst(freq, 4)
    mine = ap_hst(mine, 8)
    rare = ap_hst(rare, 12)
    avg = ap_hst(avg, 6)

    hst = str(freq) + str(mine) + str(rare) + str(avg)
    # print(hst)

    hst = str(hst)
    hst = hst.replace("[", "")
    hst = hst.replace("]", "")
    hst = hst.replace("'", "")
    hst = hst.replace(",", "")

    return hst

print(get_hashtags())