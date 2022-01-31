bonus = [[95,95], [96,90], [92,98], [85,88], [87,86], [92,80], [75,85], [75,80], [88, 65], [82, 85]]
nobonus = [[20,30], [35,40], [50,45], [20,75], [45,55], [60,60], [70,50], [50,70], [30,75], [55,45]]
#일한시간 = x(점수)   일한 성과 = y(점수)

mytime = float(input("올해 일한 시간을 입력하세요: "))
mywork = float(input("올해 일한 성과를 입력하세요: "))
b = 0
k = 3
result = [float('inf'), float('inf'), float('inf')]
which = [True, True, True]

for i in bonus:
    x = i[0]
    y = i[1]
    distance1 = ((mytime - x)**2 + (mywork - y)**2)
    distance = distance1**0.5
    for b, j in enumerate(result):
        if distance < j:
            result.insert(b, distance)
            del result[-1]
            break
for i in nobonus:
    x = i[0]
    y = i[1]
    distance = ((mytime - x)**2 + (mywork - y)**2)**0.5
    for b, j in enumerate(result):
        if distance < j:
            result.insert(b, distance)
            del result[-1]
            which.insert(b, False)
            del which[-1]
            break

if which.count(True)>1:
    print("보너스를 획득할 수 있을것 같습니다!")
else:
    print("아쉽게도 보너스를 획득하지 못할것 같습니다")