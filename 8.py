
score = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.5, 'D': 1.3, 'D-': 1.0,
         'F': 0.0}
gpaSum, creditSum = 0, 0
while True:
    s = input()
    if s == '-1':
        break
    elif s in score.keys():
        credit = float(input())
        gpaSum = gpaSum + score[s] * credit
    else:
        print('data error')
    creditSum = creditSum + credit
gpaAve = gpaSum / creditSum
print('{:.2f}'.format(gpaAve))