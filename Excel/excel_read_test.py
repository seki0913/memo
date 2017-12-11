#coding:utf-8
import openpyxl, sys

def main():
# 引数で指定したエクセルファイルを読み込む
    book = openpyxl.load_workbook(excel_path)

# アクティブなシートオブジェクトを取得する
    sheet = book.active

# 各種パラメータの取得
    Compuer_Name = sheet.cell("B5").value
# コンピュータ名の変更
    Computer_Name_Change = "Rename-Computer -NewName " + Compuer_Name + " -Force -Restart" + "\r\n" 


# PowerShell の生成
    f = open("./Windows_Server_Setting.ps1", "w") 
# コンピュータマシンの変更
    f.write(Computer_Name_Change)
    f.close() 

# 作業報告書の作成



# メイン関数
if __name__ == '__main__':
    args = sys.argv
    
    if len(args) == 2:
        excel_path = args[1]
        main()
    else:
        print("引数にエクセルファイルを指定して再実行してください")
        quit()