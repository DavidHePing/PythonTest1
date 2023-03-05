def sum(a=100, b=100):
    return a+b

print(sum(2,3))
print(sum())

fak = 'global' # First-Aid Kit

def home1():
	print(fak) # 直接取得全域的變數，不做修改

def home2():
	fak = 'h2' # 定義一個local的變數，所以修改到的變數跟全域的fak無關
	print(fak)
	
def home3():
	global fak # 告訴Python現在要用的就是全域的那個fak
	fak = 'h3'
	print(fak)

home1()
home2()
home3()