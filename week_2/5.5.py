users = [
{
    'name': 'Jill',
    'age': 40
},
{
    'name': 'Jack',
    'age': 45
},
{
    'name': 'Jenny',
    'age': 50
},{
    'name': 'John',
    'age': 25
},
{
    'name': 'Jane',
    'age': 30
}]

print(users)

sort_by = lambda x, y: x[y]

users.sort(key=lambda x: sort_by(x, 'age'))

print(users)

users.sort(key=lambda x: sort_by(x, 'name'))

print(users)