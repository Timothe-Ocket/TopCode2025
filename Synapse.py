# NE PAS TOUCHER
timestamps = [1742770800, 1742770828, 1742770856, 1742770884, 1742770912, 1742770940, 1742770977, 1742771005, 1742771033, 1742771061, 1742771094, 1742771122, 1742771150, 1742771178, 1742771206, 1742771234, 1742771269, 1742771297, 1742771325, 1742771353, 1742771381, 1742771409]
# NE PAS TOUCHER

result = ''
count = 0

verify = timestamps[0] - timestamps[1]

for i in range(1, len(timestamps)):
    
    if timestamps[i-1] - timestamps[i] != verify :
        result = result + str(timestamps[i])
        count += 1
        if count == 1 :
            result = result + '_'
        else:
            break

print(result)
