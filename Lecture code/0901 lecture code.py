s = 'sample string'

# 1. Create a new string that has the first 2 characters
# followed by sang for above

a = s[0:2]+s[-2:]

# 2. Get a single string from two given strings, 
# separated by a space and swap the first two characters
# of each string
a = 'apple'
b = 'bear'

b[0]+a[1:]+' '+a[0]+b[1:]

# 3. Create a new string from s where the last 2 chars are added to the ned 3 times
s+s[-2:]+s[-2:]+s[-2:]
s+s[-2:]*3

# 4. Find the first sppearance of the substring 'not' in x
x='from nottingham we do not go'
x.find('not')

# 5. Split s at the sequence le
s.split('le')

# 6. revese s
s[::-1]

# 7. See if X is contained in s
s.find('X')

'X' in s

# 8. See if a string '123.5' contains only numbers
'123.5'.isalnum()

# 9. Remove all the white space to the left of x

x = '\tpic     '
print(x)

x.lstrip()

## Loops

integer = 60
if integer % 3 ==0:
    print('{} is divisible by 3'.format(integer))
else:
    print('{} is not divisible by 3'.format(integer))

integer = 60
if integer % 3 ==0 or integer %  4==0:
    print('{} is divisible by either 3 or 4'.format(integer))
else:
    print('{} is not divisible by either 3 or 4'.format(integer))

# if:
# elif: check the next condition if the first condition is wrong
# else: if none of previous condition is true

if integer %3 ==0:
    print('{} is divisible by 3'.format(integer))
elif integer%4 == 0:
    print('{} is not divisible by 3 but it is \
        divisible by 4'.format(integer))
else:
    print(f'{integer} is not divisible by either 3 or 4')

# iterable is a given str

for char in 'what is the point in this?':
    print('charater is: ', char)

x = 'some strange phrase %-#'
for char in x:
    if char not in 'a%-':
         print('charater is: ', char)

chars_to_ignore = 'a%-'
for char in x:
    if char not in chars_to_ignore:
        print('char is: ', char)

for item in [1,5,6, 'ab']:
    print('item is: ', item)

for item in [1,5,6,20]:
    if item %2==0:
        print('{} is divisible by 2'.format(item))

for item in [1,5,6,20]:
    if item %2==0:
        print(item)
    else:
        print('item', item, ' is not divisible by 2')

x={1,5,3,7}
for item in x:
    if item%2==0 and item>3:
        print(item, " is even")
    else:
        print(item, " is odd")  # But we should keep in mind that this is logically wrong because 2 is not an odd

count = 0
for x in ['aa', 'bb', 'ccc', 'd']:
    #count +=1
    count=count+1
    if x == 'bb':
        print('found')

count = 0
for x in ['aa', 'bb', 'ccc', 'd']:
    #count +=1
    count=count+1
    if x == 'bb':
        print('found')
        break

print(count)

count = 0
for x in ['aa', 'bb', 'ccc', 'd']:
    #count +=1
    count=count+1
    if x == 'bb':
        print('found')
        break
    else:
        print('not found')

print(count)

count = 0
for x in ['aa', 'bb', 'ccc', 'd']:
    #count +=1
    count=count+1
    if x == 'xx':
        print('found')
        break
    elif count==4:
        print('not found')

count = 0
inlist = ['aa', 'bb', 'ccc', 'd']
for x in inlist:
    #count +=1
    count=count+1
    if x == 'xx':
        print('found')
        break
    elif count==len(inlist):
        print('not found')

#What happen you use else?
# Test commit