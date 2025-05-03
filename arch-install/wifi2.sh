#!/bin/bash
set -e

SSID="tplink_sen_E27A"
PASSWORD="chikako1109"
WLAN_INTERFACE="wlan0"

echo "[+] インターフェース: $WLAN_INTERFACE を使用します。"

# WPA設定ファイルの生成
wpa_passphrase "$SSID" "$PASSWORD" > /tmp/wpa_supplicant.conf

# wpa_supplicant をバックグラウンドで起動
echo "[+] wpa_supplicant を起動..."
wpa_supplicant -B -i "$WLAN_INTERFACE" -c /tmp/wpa_supplicant.conf

# DHCP で IP アドレス取得
echo "[+] DHCP により IP を取得..."
sleep 3
dhclient "$WLAN_INTERFACE" || dhcpcd "$WLAN_INTERFACE"

# 接続確認
echo "[+] 接続確認:"
ip a show "$WLAN_INTERFACE"
ping -c 3 archlinux.org
