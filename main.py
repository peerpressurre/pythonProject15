import random

size = int(input('size->'))
start = int(input('start->'))
end = int(input('end->'))
nums = list()

for i in range(size):
    nums.append(random.randint(start, end))
print(f'Cписок: {nums}')

max_from_list = lambda nums: max(nums)
min_from_list = lambda nums: min(nums)
reverseList = lambda nums: nums[::-1]
nums = reverseList(nums)


res = {'max': max_from_list(nums), 'min': min_from_list(nums), 'reversed': nums}
#пишу так бо з print(res['max]) не виходить добавити стрінг(max =) в прінт
fmax = res.get('max')
fmin = res.get('min')
print(f'max = {fmax}')
print(f'min = {fmin}')
print(f'reversed list: {nums}')