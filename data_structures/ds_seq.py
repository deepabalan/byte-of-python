

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0]) # apple
print('Item 1 is', shoplist[1]) # mango
print('Item 2 is', shoplist[2]) # carrot
print('Item 3 is', shoplist[3]) # banana
print('Item -1 is', shoplist[-1]) # banana
print('Item -2 is', shoplist[-2]) # carrot
print('Character 0 is', name[0]) # s

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3]) # [mango, carrot]
print('Item 2 to end is', shoplist[2:]) # [carrot, banana]
print('Item 1 to -1 is', shoplist[1:-1]) # [mango, carrot]
print('Item start to end is', shoplist[:]) # [apple, mango, carrot, banana]

# Slicing on a string
print('charcaters 1 to 3 is', name[1:3]) # wa
print('characters 2 to end is', name[2:]) # aroop
print('charcaters 1 to -1 is', name[1:-1]) # waroo
print('characters start to end is', name[:]) # swaroop
