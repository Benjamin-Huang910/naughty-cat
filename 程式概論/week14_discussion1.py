#Programming 101
#week14
#discussion 1

data_dict={'Mary':200, 'John':'Hello World','Gary':'Farewell'}

while True:
    try:
        message=''
        key1=input("請輸入一個名字的key值:")
        value1=data_dict[key1]
        message+=value1
    except KeyError:
        message = 'How are you today?'
    except TypeError:
        message = '200'
    else:
        message=message+"  "+"Finished!"
    finally:
        if message.isdigit():
            message=int(message) + 100


    print (message)
