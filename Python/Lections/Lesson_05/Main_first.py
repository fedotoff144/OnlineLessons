# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))




from progress.bar import Bar
import time

bar = Bar('Processing', max=10)
for i in range(20):
    time.sleep(1)
    bar.next()
bar.finish()


# from isOdd import isOdd

# print(isOdd(2))
# print(isOdd(1))