length = int(input())
width = int(input())
height = int(input())
percent_acc = float(input())
 
volume = length * width * height
 
total_lt = volume / 1000
 
acc_volume = total_lt * (percent_acc / 100)
result = total_lt - acc_volume
 
print(result)