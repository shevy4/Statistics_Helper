import tableprint as tp
from tqdm import trange
import time
import numpy as np
from math import sqrt

tp.banner("Statistics Data Analyzer   ")


def Men():
    tp.banner(
        '1.) Simple Average   |   2.) Grouped Average  |   3.) Weighted Average   |   4.) Probability Contingency Table')
    b = int(input("Select An Option # : "))
    if b == 1:
        simple_mean()
    if b == 2:
        grouped_average()
    if b == 3:
        weighted_avg()
    if b == 4:
        cont_table()


def find_mode(a):
    maxx = 0
    for _ in a:
        b = a.count(_)
        if b > maxx:
            maxx = b
            mode = _
        if b == maxx:
            mode2 = _
    if mode == mode2:
        return mode
    else:
        mode = str(mode) + ' & ' + str(mode2)
    if len(set(a)) == len(a):
        return "No Mode"
    else:
        return mode


def find_median(a):
    if len(a) % 2 != 0:
        median = a[int(len(a) / 2)]
    else:
        median = (a[int(((len(a) + 1) / 2))] + a[int((len(a) - 1) / 2)]) / 2
    return median


def find_dev(b, a):
    c = 0
    for _ in a:
        c = c + ((_ - b) ** 2)
    vari = (c / (len(a) - 1)).__round__(3)
    devi = sqrt(vari).__round__(3)
    return vari, devi


def find_freq(a):
    freq_total = 0
    temp = []
    arr = np.array(a)
    arr = np.bincount(arr)
    arrr = np.nonzero(arr)[0]
    arrr = list(zip(arrr, arr[arrr]))
    cu_freq, cu_freq_total = cumulative_fre(arrr)
    for __, _ in enumerate(arrr):
        freq_total = arrr[__][1] + freq_total
        _ = list(_)
        _.extend([cu_freq[__]])
        temp.append(_)
    return temp, freq_total, cu_freq, cu_freq_total


def cumulative_fre(a):
    freq = []
    cu_freq_total = 0
    for __, _ in enumerate(a):
        _ = list(_)
        freq.append(a[__][1])
    cu_freq = [a[0][1]]
    for x in range(len(freq)):
        try:
            cu_freq.append(cu_freq[x] + freq[x + 1])
            cu_freq_total += cu_freq[x]
        except:
            pass
    return cu_freq, cu_freq_total


def cumulative_fre_2(a):
    freq = []
    cu_freq = []
    cu_freq_total = int(a[0])
    for __, _ in enumerate(a):
        freq.append(int(_))
    cu_freq.append(freq[0])
    for x in range(len(freq)):
        try:
            cu_freq.append(cu_freq[x] + freq[x + 1])
            cu_freq_total += cu_freq[x + 1]
        except:
            pass
    return cu_freq, cu_freq_total


def table(a, b, c, d, e, f, g, h, i, j):
    # a.append(['', '', ''])
    a.append(['x̄ :' + str(h), 'Variance :' + str(i), 'Std_Deviation :' + str(j)])
    a.append(['Median :' + str(d), 'Range :' + str(c), 'Mean :' + str(b)])
    a.append(['Mode :' + str(e), 'Total Freq :' + str(f), 'Total Cumulative Freq :' + str(g)])
    a.append(['Coefficient :' + str((j / b).__round__(3)), 'Skewness :' + str(((3 * (b - d)) / j).__round__(3)), ''])
    data = np.array(a)
    headers = ['Arguments ', 'Frequency', 'Cumulative Frequency']
    return data, headers


def simple_mean():
    freq = []
    _ = input("Enter All Numbers With Spaces Then Enter\n")
    _ = _.split()
    for x in _:
        x = float(x)
        freq.append(int(x))
    freq.sort()
    summ = np.array(freq)
    summ = summ.sum()
    median = find_median(freq)
    modee = find_mode(freq)
    ran = freq[len(freq) - 1] - freq[0]
    mean = (sum(freq) / len(freq)).__round__(2)
    vari, devi = find_dev(mean, freq)
    temp, freq_total, cu_freq, cu_freq_total = find_freq(freq)
    data, headers = table(temp, mean, ran, median, modee, freq_total, cu_freq_total, summ, vari, devi)
    for _ in trange(len(freq)):
        time.sleep(.2)
    tp.table(data, headers)
    time.sleep(1.2)


def find_dev_grouped(a, b, d, e):
    c = 0
    for x, y in enumerate(a):
        c = c + ((y - b) ** 2) * int(d[x])
    vari = c / (e - 1)
    c = sqrt((c / (e - 1)))
    return c.__round__(3), vari.__round__(3)


def table2(a, b, c, e):
    temp2 = []
    sum_fxm = 0
    for _, __ in enumerate(a):
        temp2.append([__, b[_], e[_], e[_] * int(b[_]), c[_]])
        sum_fxm = sum_fxm + e[_] * int(b[_])
    # temp2.append(['', '', '', '', ''])
    tot_freq = []
    for x in range(len(b)):
        tot_freq.append(int(b[x]))
    tot_freq = np.array(tot_freq)
    mode = grouped_find_mode(b, a)
    devi, vari = find_dev_grouped(e, round(sum_fxm / tot_freq.sum(), 2), b, int(tot_freq.sum()))
    # temp2.append(['Mean : ' + str(round(sum_fxm / tot_freq.sum(), 2)), 'Total Freq : ' + str(tot_freq.sum()),
    # 'Median :' + str(tot_freq.sum() / 2), 'ΣfreqXMid : ' + str(sum_fxm), 'Total Cumul_Freq :' + str(d)])
    temp2.append(['Mode:' + str(mode) + '|Mean :' + str(round(sum_fxm / tot_freq.sum(), 2)), 'Variance :' + str(vari),
                  'Median :' + str(tot_freq.sum() / 2), 'ΣfreqXMid : ' + str(sum_fxm), 'Std_Deviation :' + str(devi)])
    data = np.array(temp2)
    headers = ['Ranges ', 'Frequencies', 'Mid Point ', ' Freq X Mid', 'Cumulative Frequency']
    print("data = ", data)
    print("header = ", headers)
    return data, headers


def grouped_find_mode(a, b):
    for _, __ in enumerate(a):
        a[_] = int(__)
    for _, __ in enumerate(a):
        if __ == max(a):
            index = _
    x = (int((b[index].split('-')[0])) - 0.5)

    try:
        return (((max(a) - a[(index - 1)]) / ((max(a) - a[(index - 1)]) + (max(a) - a[index + 1]))) * (
                int(b[1].split('-')[1]) - int(b[0].split('-')[1]))).__round__(1) + x
    except:
        pass

    # return (((max(a) - a[(index - 1)]) / ((max(a) - a[(index - 1)]) + (max(a) - a[index + 1]))) * (
    # int(b[1].split('-')[1]) - int(b[0].split('-')[1]))).__round__(1) + x


def grouped_average():
    ranges = []
    temp = []
    midpoint = []
    _ = input("Enter Ranges Eg (1-10) Separated by Spaces\n")
    _ = _.split()
    ___ = []
    for x in _:
        ___.append(x.split('-'))
    _ = []
    for x in ___:
        _.append([int(x[0]), int(x[1])])
    _.sort()
    for x in _:
        midpoint.append((x[0] + x[1]) / 2)
    __ = []
    for x in _:
        __.append(str(x[0]) + '-' + str(x[1]))
    for _ in __:
        ranges.append(_)
        temp.append([_, 'xxx'])
    print("1temp = ", temp)
    temp = np.array(temp)
    print("2temp = ", temp)
    headers = [' Ranges ', ' Frequencies ']
    data = np.array(temp)
    tp.table(data, headers)
    __ = input("Input Frequencies Separated By Spaces\n")
    __ = __.split()

    cu_freq, cu_freq_total = cumulative_fre_2(__)
    data, headers = table2(ranges, __, cu_freq, midpoint)
    tp.table(data, headers)
    time.sleep(1.2)


def weighted_avg():
    freq = []
    _ = input("Enter Frequencies Separated By Spaces\n")
    _ = _.split()
    for x in _:
        freq.append(int(x))
    freq.sort()
    summ = np.array(freq)
    mean = summ.mean()
    summ = summ.sum()
    data = []
    headers = ['Frequencies', ' Weighted Values']
    for x in freq:
        data.append([str(x), 'xxx'])
    data.append(['Sum : ' + str(summ), ''])
    print(data)
    tp.table(data, headers)
    while True:
        _ = input("Enter Weighted Values\n")
        _ = _.split()
        if len(_) < len(freq):
            print("List Index Short, Enter", len(freq), ' Or More\n')
        else:
            break
    weighted_table(freq, _, mean)


def weighted_table(a, b, c):
    data = []
    total_weighted_freq = total_weighted_amount = 0
    headers = ['Frequencies', ' Weighted Amount', 'Weighted Frequency']
    for x, y in enumerate(a):
        data.append([str(y), b[x], y * int(b[x])])
        total_weighted_freq = total_weighted_freq + y * int(b[x])
        total_weighted_amount = total_weighted_amount + int(b[x])
    data.append(
        ["Mean : " + str(c), 'Weighted_Mean :' + str((total_weighted_freq / total_weighted_amount).__round__(5)), ''])
    data = np.array(data)
    tp.table(data, headers)


def find_var(a):
    temp, b = [], 0
    for x, y in enumerate(a, start=1):
        try:
            temp.append(float(a[x]))
            b += float(a[x])
        except ValueError:
            pass
        if x == len(a) - 1:
            break
    b = b.__round__(3)
    temp.append(b)
    # for _ in temp:
    # x += _ *
    return (1 - b).__round__(1)


def cont_table():
    data, headers = [], []
    headers = input("Enter Headers\n").split()
    data.append(input("Enter Data Values\n").split())
    for x, y in enumerate(data[0]):
        try:
            a = float(data[0][x + 1])
        except ValueError:
            a = data[0][x + 1]
            break
        except IndexError:
            continue
        # except IndexError:
    a = 0
    tp.table(data, headers)
    mess = "1.) Find  |  2.) Input Parameter"
    tp.banner(mess)
    b = input()
    if b == '1':
        print(find_var(data[0]))


while True:
    Men()
