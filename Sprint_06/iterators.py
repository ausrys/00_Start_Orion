nums = [1, 2, 3]

it = iter(nums)  # Get an iterator from the list

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3


nums = [10, 20, 30]
it = iter(nums)

for val in it:
    print(val)


class CountUpTo:
    def __init__(self, max_val):
        self.max = max_val
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


# Usage
counter = CountUpTo(3)
for num in counter:
    print(num)
