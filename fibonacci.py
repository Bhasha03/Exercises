def fibonacci(x,y):
    first_two=[x,y]
    pattern=first_two
    def recur(count):
        if count<10:
            pattern.append(pattern[-1]+pattern[-2])
            count+=1
            return recur(count)
        else:
            return pattern
    return recur(0)
fibonacci(0,1)