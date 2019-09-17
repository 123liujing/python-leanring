height,weight =eval(input("请输入身高(米)体重（kg）并且用逗号隔开"))
bmi=weight /pow(height,2)
print("BMI 数值:{:.2f}".format(bmi))
who=""
if bmi<18.5
    who="偏瘦"
elif 18.5 <= bmi <25
    who="正常"
elif 25 <= bmi <30
    who="偏胖"
else:
    who="肥胖"
print("指标为:'{0}'".format(who))
