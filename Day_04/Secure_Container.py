
def passwords(number_range):
    low, high = (int(x) for x in number_range.split('-'))
    ans = []
    while low <= high:
        temp = str(low)
        increasing = True
        doubles = False
        prev = temp[0]
        rest = temp[1:]
        for i in rest:
            if prev == i:
                doubles = True
            if prev > i:
                increasing = False
                break
            prev = i
        if doubles and increasing:
            ans.append(low)
        low += 1
    return len(ans)


print(passwords("130254-678275"))
