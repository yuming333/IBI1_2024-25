# 步行到公交站的时间，单位为分钟
a = 15
# 坐公交的时间，1小时15分钟换算为分钟是75分钟
b = 75
# 计算坐公交通勤的总时间
c = a + b
# 开车的时间，1小时30分钟换算为分钟是90分钟
d = 90
# 从停车场步行的时间
e = 5
# 计算开车通勤的总时间
f = d + e
# 比较两种通勤方式的总时间
if c < f:
    print("bus is faster")
    result = "bus is faster"
elif c > f:
    print("driving is faster")
    result = "driving is faster"
else:
    print("the same")
    result = "the same"

# 以注释的形式记录结果
# 答案：{}
# 这里将结果字符串插入到注释中，方便查看
print(f"answer：{result}")