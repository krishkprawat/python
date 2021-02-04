#Question 3: Given a string, display only those characters which are present at an even index number.
#For example str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

def evenprint(str):
    for i in range(0, len(str),2):  #range(start, end, step)
        print(str[i])

evenprint("python")

