red, blue, other = range(0, 3, 1)   #assign a positional assignment to candidates
candidate = [0,0,0]                 #initialize all votes to 0
vote = ''
while vote != 4:
    vote = input ("Vote for your color. Red<0>, Blue<1>, Other<2> or Done<4>") #ask voter for vote
    candidate[vote==other] += 1     #if vote = other, increment other
    candidate[vote==blue] += 1      #if vote = blue, increment blue
    candidate[vote==red] += 1       #if vote = red, increment red
print {'other': candidate[other],'blue' : candidate[blue],'red'  : candidate[red]} #display results
