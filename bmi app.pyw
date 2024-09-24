import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.T("身長と体重を入力してください。", pad=((10, 10), (10, 10)))],
          [sg.T("身長cm", size=(10, 1), pad=((10, 10), (5, 5))), sg.I("160", k="in1", size=(10, 1))],
          [sg.T("体重kg", size=(10, 1), pad=((10, 10), (5, 5))), sg.I("60", k="in2", size=(10, 1))],
          [sg.B("実行", k="btn", size=(10, 1), pad=((10, 10), (10, 10))), sg.T(k="txt", size=(30, 1))]]
          
win = sg.Window("BMI値計算アプリ", layout, font=(None, 14), size=(600,300))  # ウィンドウサイズを広げる

def execute():
    in1 = float(v["in1"]) / 100.0  # 身長をcmからメートルに変換
    in2 = float(v["in2"])  # 体重（kg）
    bmi = in2 / (in1 * in1)  # BMI計算式

    # BMIに基づく結果を判断
    if bmi < 18.5:
        category = "痩せすぎ"
    elif bmi <= 24.9:
        category = "標準体型"
    elif bmi <= 29.9:
        category = "前肥満"
    elif bmi <= 34.9:
        category = "肥満1度"
    elif bmi <= 39.9:
        category = "肥満2度"
    else:
        category = "肥満3度"

    txt = f"BMI値は、{bmi:.2f}です。({category})"  # BMI値とカテゴリを出力
    win["txt"].update(txt)  # 結果をウィンドウ内のテキスト要素に表示

while True:
    e, v = win.read()
    if e == sg.WIN_CLOSED:  # ウィンドウの閉じるイベントを処理
        break
    if e == "btn":
        execute()

win.close()
