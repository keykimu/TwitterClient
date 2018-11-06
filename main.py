#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Twitterライブラリ
import tweepy

# 使用クラスファイル
import Setting
import Login

# メイン関数
def main():
    # Setting設定
    setting = Setting

    # ログイン
    auth = Login.oauth_login()
    # クライアント
    client = tweepy.API(auth)

    # tweet
    client.update_status("test")

#メイン関数実行
main()