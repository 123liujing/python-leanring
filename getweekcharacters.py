#input 1234567 gerback sunday tuesday wenesday blahblah
weekstr="星期一星期二星期三星期四星期五星期六星期天"
getday=eval(input("请输入数字"))
pos=(getday-1)*3
print(weekstr[pos:pos+3])