def idenpotend(strok):
    mas = strok.split("+")
    for i in mas:
        while(mas.count(i) != 1):
            mas.remove(i)
    mas.sort()
    return "+".join(mas)

def rezolution(strok1, strok2):
    mas1 = strok1.split("+")
    mas2 = strok2.split("+")
    for i in mas1:
        if len(i) == 2 and i[0] == "-" and i[1] in mas2:
            mas1.remove(i)
            mas2.remove(i[1])
            mas1 = mas1 + mas2
            if (len(mas1) > 0):
                return ("+".join(mas1))
            else:
                return "▯"
        elif len(i) == 1 and i[0] != "-" and "-"+i in mas2:
            mas1.remove(i)
            mas2.remove("-"+i)
            mas1 = mas1 + mas2
            if(len(mas1) > 0):
                return ("+".join(mas1))
            else:
                return "▯"
    return 0

def rezol1(strok):
    mas = strok.split("+")
    for i in mas:
        if len(i) == 2 and i[1] in mas:
            mas.remove(i)
            mas.remove(i[1])
        elif len(i) == 1 and "-"+i in mas:
            mas.remove(i)
            mas.remove("-"+i)
    if len(mas) > 0:
        return ("+".join(mas))
    else:
        print(strok, "преобразовалось в ▯")
        return 0


print("Формат ввода дизъюнктов {A; B; ...} ИЛИ A; B; ... Z; ")
strok =input("Введите множество дизъюнктов K = ").upper()
masdiz = []
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-+"
alfwithdiz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
dopst = ""
for j in strok:
    if j in alf:
        dopst = dopst + j
    elif j == ";" or j == "}":
        masdiz.append(idenpotend(dopst))
        dopst = ""

set(masdiz)

i = 0
while i < len(masdiz):
    mas = masdiz[i].split("+")
    for k in masdiz:
        if masdiz[i] != k:
            dopmas = k.split("+")
            for d in mas:
                if d in dopmas:
                    masdiz.remove(k)
                    print("{} и {} преобразовали в {}".format(masdiz[i], k, idenpotend("+".join(mas + dopmas))))
                    masdiz.remove(masdiz[i])
                    masdiz.append(idenpotend("+".join(mas + dopmas)))
                    i = 0
                    break
    i += 1

i = 0
while i < len(masdiz):
    dop1 = masdiz[i]
    dop1 = rezol1(dop1)
    if dop1 != 0:
        j = i+1
        while j < len(masdiz):
            dop2 = masdiz[j]
            dop3 = rezolution(dop1, dop2)
            if dop3 != 0:
                print(dop1, "и", dop2, "переобразовалось в", dop3)
                masdiz[i] = ""
                masdiz[j] = ""
                dop4 = idenpotend(dop3)
                if dop4 == dop3:
                    masdiz.append(dop3)
                else:
                    print(dop3, "преобразовалось в", dop4)
                    masdiz.append(dop4)
                i = 0
                break
            else:
                j += 1
    else:
        masdiz[i] = ""
        i = 0
    i += 1

while "" in masdiz:
    masdiz.remove("")

if masdiz.count("▯") > 0 or len(masdiz) == 0:
    print("Из", strok, "выводится пустая резольвента!🥳🥳🥳")
else:
    print("Из", strok, " НЕ выводится пустая резольвента!⚰️ ⚰️ ⚰️ ")
