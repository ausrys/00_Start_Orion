def next_num_gen(num_arr):
    for i in num_arr:
        yield (i * 3) // 2


nums = [1, 2, 3, 5]
generated_nums = next_num_gen(nums)
for num in generated_nums:
    print(num)
