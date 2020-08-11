from matplotlibTest.die import Die
import pygal

# 创建一个D6
die_1 = Die(20)
die_2 = Die(3)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(2, die_1.num_sides + die_2.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8+D8', frequencies)
hist.render_to_file('die_visual.svg')
