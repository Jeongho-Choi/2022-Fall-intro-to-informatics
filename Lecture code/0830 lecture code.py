x = "this is a sentence with {} and {} placeholders"
x
'this is a sentence with {} and {} placeholders'
a = 'apple'
b = 'bagel'
print('this is a sentence with', a, 'and', b)
      
print('this is a sentence with', a, 'and', b, 'placeholders')
print('this is a sentence with' + a+ 'and'+b+'placeholders')
print('this is a sentence with ' + a+ ' and '+b+' placeholders')
x.format('apple', 'bagel')

'here is what we want: {2}, {1}, {2}!'.format('a', 'b', 'c')
'here is what we want: c, b, c!'
'here is what we want: {2}, {1}, {2}!'.format('a', 'b', 99)
'here is what we want: 99, b, 99!'
'here is what we want: {2}, {1}, {2}!'.format('a', 'b', 99-3)
'here is what we want: 96, b, 96!'
'{:<19.2f}', format(1.3)
('{:<19.2f}', '1.3')
'{:<19.2f}'.format(1.3)
'1.30               '
letter = '''
Dear {0} {1}.
How are you? \
Are you free to meet on {2}
Thanks
'''
type(letter)
letter.format('Mary','Jones','Oct 6')

l = letter.format('Mary','Jones','Oct 6')

l = letter.format('Mary','Jones','Oct 6')
print(l)

for i in range(1,11):
	print(i,"\t", i**2, "\t", i**3)

for i in range(2,22):
	print(i,"\t", i**2, "\t", i**3)
