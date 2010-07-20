'''
--- model master

|input name=a| -> |s1:slave| -> |output name=b| 


s1.gain = 3

--- model slave

|input name=x| -> |gain k=${gain}| -> |output name=y|


default.gain = 1

'''

