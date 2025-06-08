#!/usr/bin/env python3
from flask import Flask, request, render_template_string
import subprocess
import argparse
import os

app = Flask(__name__)
MENU_DICT = {}

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Command Launcher</title>
</head>
<body>
    <h1>コマンド選択</h1>
    <form method="POST">
        <select name="selection">
            {% for title in titles %}
                <option value="{{ title }}">{{ title }}</option>
            {% endfor %}
        </select>
        <button type="submit">実行</button>
    </form>
    {% if output %}
    <h2>実行結果:</h2>
    <pre>{{ output }}</pre>
    {% endif %}
</body>
</html>
"""

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text_files', default=[], nargs='*')
    return parser.parse_args()

def get_text_list(text_file):
    with open(text_file) as f:
        text_list = [s.strip() for s in f.readlines()]
        text_list = [s for s in text_list if s and not s.startswith('#')]
    return text_list

def get_command_dict(text_lists):
    wofi_dict = {}
    for text in text_lists:
        try:
            title, cmd = text.split(',', 1)
            title, cmd = title.strip(), cmd.strip()
            title = name_repair(title)
            if cmd.startswith('http'):
                cmd = 'xdg-open ' + cmd
            wofi_dict[title] = cmd
        except ValueError:
            continue
    return wofi_dict

def name_repair(name):
    for ch in ['\\', '\"', '\'', '/', ':', '*', '?', '<', '>', '|', '[', ']', ' ']:
        name = name.replace(ch, '_')
    while '__' in name:
        name = name.replace('__', '_')
    return name

@app.route("/", methods=["GET", "POST"])
def index():
    titles = list(MENU_DICT.keys())
    output = ""
    if request.method == "POST":
        selected_title = request.form.get("selection", "")
        command = MENU_DICT.get(selected_title, "")
        if command:
            try:
                result = subprocess.run(command, shell=True, check=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output = result.stdout or "(No output)"
            except subprocess.CalledProcessError as e:
                output = f"エラー:\n{e.stderr or str(e)}"
        else:
            output = "選択されたコマンドが見つかりません。"
    return render_template_string(HTML_TEMPLATE, titles=titles, output=output)

def load_menu(text_files):
    combined_list = []
    for file in text_files:
        if os.path.exists(file):
            combined_list.extend(get_text_list(file))
    return get_command_dict(combined_list)

if __name__ == "__main__":
    args = get_args()
    MENU_DICT = load_menu(args.text_files)
    app.run(debug=True)
