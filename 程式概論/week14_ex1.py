#Programming 101
#week14
#ex 1

#可以幫忙檢查傳入的參數num是否可成功轉換成浮點數資料型態的自訂函數
#回傳值：True 代表可以成功轉成浮點數
#回傳值：False 代表無法成功轉成浮點數
#請注意：在此函數中會使用到一個區域變數的名稱為result
def check_float(num):
    try:
        float(num)
    except:   
                           #有發生例外時，將變數result的內容設為False
    else:
                           #沒有發生例外時，將變數result的內容設為True
    finally:
                           #不管有沒有發生例外，最後都將result的內容回傳


while True:
    a=input('輸入一個可以成功轉為浮點數的資料:')
    if (not check_float(a)):
        print('輸入資料有錯誤，請重新', end='')
        continue
    else:
        print('輸入的資料可以成功轉為浮點數', float(a))
        break
