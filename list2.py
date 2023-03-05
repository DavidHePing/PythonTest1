print(list())
lt1 = [1,2,3]
lt2 = [4,5,6]
lt1.append(3.5)
print(lt1)
del lt1[3]
print(lt1)
lt1.extend(lt2)
print(lt1)
lt1 = lt1[0:3]
print(lt1)
lt1.insert(1, 1.5)
print(lt1)
lt1.remove(1.5)
print(lt1)
print(1.5 in lt1, 1 in lt1)
lt1 = [2,3,1]
lt3 = sorted(lt1)
print(lt3, lt1)
lt1.sort()
print(lt1)
lt1.sort(reverse=True)
print(lt1)
lt4 = lt1.copy()
print(lt4)
lt5 = sorted(lt1)
lt5.extend(lt2)
print(lt5)
print(lt5[-2:])