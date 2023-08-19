# Создайте вручную список с повторяющимися элементами
# Удалите из него все элементы, которые встречаются
# любое четное количествто раз


nums = [1,2,1,3,2,1,3,3]

for num in nums:
    # counter = nums.count(num)
    # if counter > 1 and counter % 2 == 0:
    #     for _ in range(counter):
    #         nums.remove(num)

    while nums.count(num) % 2 == 0 and num in nums:
        nums.remove(num)
        nums.remove(num)
print(nums)
