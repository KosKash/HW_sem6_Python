# (1+1/i)**i последовательнось

# Old code

# num = int(input('Input N '))
# num_list = []
# for i in range(1,num):
#     num_list.append((1+1/i)**i)
# res = sum(num_list)
# print('{}: {}'.format(num,round(res,3)))

num = int(input('>>> '))
res_num = round(sum(list(map(float,([((1+1/i)**i) for i in range(1,num)])))),3)

print(f'{num}:{res_num}')