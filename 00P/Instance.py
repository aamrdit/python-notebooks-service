from Bird import *

print('\nClass Instances Of:\n', Bird.__doc__)

polly = Bird('Squawk,squawk!')

print('\nNmber of Birds:', polly.count)
print('Polly Says:', polly.talk())

harry = Bird('Tweet,Tweet')

print('\nNumber of Birds', harry.count)
print('\nHarry Says:', harry.talk())
