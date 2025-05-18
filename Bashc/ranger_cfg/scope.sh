#!/bin/bash

# パスと表示エリアサイズ
FILE="$1"
WIDTH="$2"
HEIGHT="$3"

# MIME タイプ確認
MIMETYPE=$(file --mime-type -Lb "$FILE")

# 画像ファイルなら viu で表示
if [[ "$MIMETYPE" == image/* ]]; then
    viu -w "$WIDTH" -h "$HEIGHT" "$FILE"
    exit 0
fi

# テキストファイルなど他のタイプは ranger のデフォルト表示へ
exit 1
