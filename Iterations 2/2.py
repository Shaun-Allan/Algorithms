def sumSeries(n):
    sum = 0
    for i in range(n):
        sum += (i*(i+1))/2
    return sum

n = int(input("Enter n: "))
print("Sum of series: ", sumSeries(n))