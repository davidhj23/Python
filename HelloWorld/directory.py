from pathlib import Path

path = Path("ecommerce")
print(path.exists())

path1 = Path()
print(path1.glob('*'))

print('')
print('files: ---------------')
print('')

path2 = Path()
for file in path2.glob('*.py'):
    print(file)