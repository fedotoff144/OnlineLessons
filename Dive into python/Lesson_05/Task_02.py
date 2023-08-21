link = 'https://www.google.com/search?channel=fs&client=ubuntu&q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA'
prefix, *_, suffix = link.split('/')
print(f'{prefix=} {type(prefix)}\t{suffix=} {type(suffix)}')
# prefix='https:'	suffix='search?channel=fs&client=ubuntu&q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA'