from List import ArrayList


sample = ArrayList(2)

sample.append(1)
sample.prepend(3)
sample.append(2)
sample.insert(1, 5)
sample.print()
print("index 1: ",sample.access(1))
sample.set_head(2)
sample.print()