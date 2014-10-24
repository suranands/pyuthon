from sys import argv

script,name = argv
print 'Hi %r, welcome to the program %r!' %(name,script)
prompt = '>'
fname = raw_input('What is your full name?')
age = raw_input('How old are you?')
sex = raw_input('And your gender as well please!')
print 'Thanks %r. I can see that you are %r old %r. That brings you here!' %(fname,age,sex)
