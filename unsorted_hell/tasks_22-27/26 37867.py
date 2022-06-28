f = open('26-44.txt')
n = int(f.readline())
a = [int(x) for x in f]
a = sorted(a)
k = [[]*2 for i in range(20)]
border = 501
c = 0
#сортируем все числа в свою категорию
for i in range(len(a)):
    if a[i] < border:
        k[c].append(a[i])
    else:
        border += 500
        c+=1
        k[c].append(a[i])

#НАйти: сумму скидки для всего чека и конечную стоимость самого дорогого проданного по акции товара
#сортировка
for i in range(20):
    k[i] = sorted(k[i])
    if len(k[i]) > 0:
        print(min(k[i]), max(k[i]), len(k[i]))

sales_bag = []
for i in range(20):
    #print((len(k[i]))//2, len(k[i]))
    for j in range(0, (len(k[i]))//2):
        sales_bag.append(k[i][j]/2)

print(sales_bag, sum(sales_bag), max(sales_bag))
