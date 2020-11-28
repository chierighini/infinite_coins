input_value = 12
coins=[25,10,5,0]
comb= []
possibility=[0,0,0,0]
rest = 0


def makeChange(val,size,coins,poss,rest):

  '''making the conditions for each coin type for the recursive step of this 
  function. It could be done without so many if's, but I think it's easier to 
  see things clearly like this'''
  if size == 25:
    next =10
  elif size==10:
    next=5
  elif size == 5:
    next = 1
  elif size==1:
    return

  '''in python the range function takes the arguments of start, stop and step
  that means that the following call takes 0 as a start, val+1 as a stop
  (not included) and the size as a step'''
  for i in range(0,val+1,size):
    rest = rest-i
    poss[coins.index(size)]=poss[coins.index(size)]+1
    makeChange(val-i,next,coins,poss,rest)

    '''a condition for saving the possibility into the set 
    (which is an array, since the set data structure in python is immutable)
    and then reseting it'''
    if rest==0:
      comb.append(poss)
      poss=[0,0,0,0]

  return comb