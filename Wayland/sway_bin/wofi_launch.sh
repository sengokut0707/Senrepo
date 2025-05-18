#!/bin/bash

# 使用方法: ./wofi_bookmark.sh file1.txt file2.txt ...

# テキストファイルをすべて結合して、無効な行を除去
entries=()
while [[ $# -gt 0 ]]; do
    file="$1"
    while IFS= read -r line; do
        [[ -z "$line" || "$line" == \#* ]] && continue
        title=$(echo "$line" | cut -d',' -f1 | xargs)
        cmd=$(echo "$line" | cut -d',' -f2- | xargs)
        [[ "$cmd" == http* ]] && cmd="xdg-open $cmd"
        title_clean=$(echo "$title" | sed -e 's/[\\\"'\''\/:*?<>|[\] ]/_/g' -e 's/__\+/_/g')
        entries+=("$title_clean:::${cmd}")
    done < "$file"
    shift
done

# wofi 用にタイトルリスト作成
title_list=()
for entry in "${entries[@]}"; do
    title_list+=("${entry%%:::*}")
done

# ユーザーに選ばせる
selected=$(printf "%s\n" "${title_list[@]}" | wofi -dmenu -disable-history -s ~/.config/wofi/*.css)
[[ -z "$selected" ]] && echo "Null" && exit

# 選択肢に対応するコマンドを探して実行
for entry in "${entries[@]}"; do
    title="${entry%%:::*}"
    cmd="${entry##*:::}"
    if [[ "$selected" == "$title" || "$title" == *"$selected"* ]]; then
        eval "$cmd"
        exit
    fi
done
