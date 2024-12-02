def groupby(iterable):
    if not iterable:
        return

    stack = []
    current_key = iterable[0]
    
    for item in iterable:        
        if item == current_key:
            stack.append(item)
        else:
            yield (current_key, stack)
            current_key = item
            stack = [item]

    yield (current_key, stack)

def destroy_balls(balls, res=0):
    c = 0
    for _, group in groupby(balls):
        lg = len(list(group)) 
        c += lg
        if lg >= 3: 
            return destroy_balls(balls[:c-lg] + balls[c:], res + lg)  
    return res


n, *balls = map(int, input().split())

print(destroy_balls(balls)) 