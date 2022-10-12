#호랭이 술집
price = [
    73500,  #호랭이 술집 1차
    161500, #호랭이 술집 2차
    38000   #오거리술집 (테이블당 따로) 
]

firstppl  = ["하영", "세진", "은진", "경아", "시윤", "성주", "인서", "가영", "지윤"]
secondppl = ["하영", "세진", "은진", "경아", "시윤", "성주", "남석", "지원", "병우"]
thirdppl  = ["자헌", "정원", "하영", "시윤"]

total = firstppl + secondppl + thirdppl

total = {i : 0 for i in total}

firstPrice  = price[0]//len(firstppl)
secondPrice = price[1]//len(secondppl)
thirdPrice  = price[2]//len(thirdppl)

for i in firstppl:
    total[i]+= firstPrice
for i in secondppl:
    total[i] += secondPrice
for i in thirdppl:
    total[i] += thirdPrice
    
# for i in total.items():
#     print(i)


paidppl = ["하영", "정원", "자헌", "성주", "인서", "은진", "세진", "경아", "지윤", "시윤", "남석"]

for i in paidppl:
    total[i] = 0

for i in total.items():
    print(i)