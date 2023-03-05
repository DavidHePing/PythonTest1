import traceback

try:
    raise Exception('Exception is happen!!!')
except Exception as ex:
    print(ex)

try:
    dic = {1:10}
    print(dic[10])
except Exception as ex:
    print(traceback.format_exc())