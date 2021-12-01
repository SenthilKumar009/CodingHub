heros=['spider man','thor','hulk','iron man','captain america']

print(f"Total Avengers is the list: {len(heros)}")

heros.insert(len(heros),'black panther')
print(f"Total Avengers after adding Black Panther the the list: {heros}")
#print(f"Total Avengers is the list: {len(heros)}")


#print(heros.index('black panther'))
heros.remove('black panther')
#heros.remove(heros.index('black panther'))
pos = heros.index('hulk')
heros.insert(pos+1,'black panther')
print(f"Total Avengers after updating the the list: {heros}")

heros[1:3]=['doctor strange']
print(heros)

heros.sort()
print(heros)
