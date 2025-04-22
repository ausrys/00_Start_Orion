def next_num_gen(n):
    for i in range(1, n):
        yield (i * 3) // 2


generated_nums = next_num_gen(10)
for num in generated_nums:
    print(num)
