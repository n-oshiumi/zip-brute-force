# ブルートフォース攻撃用
from itertools import product

chars = "abcdefgjijklmnopqrstuvwxyz0123456789" # 探したい文字
repeat = 4 # 桁数
zipFilePath = './sample.zip' # zipファイルのパス


## ZIPファイル
from zipfile import ZipFile

with ZipFile(zipFilePath) as zip:
    success = False
    for i in range(repeat + 1):
        passwordList = product(chars, repeat=i)

        for password in passwordList:
            passwd = ''.join(password)
            print(passwd)
            try:
                zip.extractall(pwd=passwd.encode('utf-8'))
                print('----------------------------------------------')
                print('----------------------------------------------')
                print('！！！！パスワードの解析に成功しました！！！！')
                print('----------------------------------------------')
                print('----------------------------------------------')
                print('パスワード: ' + passwd)
                success = True
                break;
            except:
                continue

        # 成功したらループ抜ける
        if (success == True):
            break;
