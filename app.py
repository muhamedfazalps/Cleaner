from flask import Flask, jsonify, render_template
import pyautogui
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clean_files', methods=['GET'])
def clean_files():
    try:
        clean_temp_and_prefetch()
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/empty_recycle_bin', methods=['GET'])
def empty_recycle_bin():
    try:
        open_recycle_bin()
        empty_recycle_bin()
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

@app.route('/clean_all', methods=['GET'])
def clean_all():
    try:
        clean_temp_and_prefetch()
        open_recycle_bin()
        empty_recycle_bin()
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

def open_folder(folder_path):
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)
    pyautogui.typewrite(folder_path)
    pyautogui.press('enter')
    time.sleep(1)

def delete_all_files():
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'delete')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)

def clean_temp_and_prefetch():
    # Open and clean Temp folder
    open_folder('%temp%')
    time.sleep(1)
    delete_all_files()
    
    # Open and clean Prefetch folder
    open_folder('C:\\Windows\\Prefetch')
    time.sleep(1)
    delete_all_files()

def open_recycle_bin():
    os.startfile('shell:RecycleBinFolder')
    time.sleep(2)

def empty_recycle_bin():
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.press('enter')

if __name__ == '__main__':
    app.run(debug=True)
