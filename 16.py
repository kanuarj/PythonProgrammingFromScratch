import sys
'''\
sys.stdout.write("Hey\n")
sys.stderr.write("Hi")
'''
'''\
data = sys.stdin.readlines()
print("This is the length of lines you have entered",len(data))
'''
print(int(sys.argv[1]) + 5)
