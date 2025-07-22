import random
item_id = int(f'{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}')
print(item_id)


rawId = 100
rawId+=1
itemId = str('000000'[len(str(rawId)):] + str(rawId))
print(itemId)