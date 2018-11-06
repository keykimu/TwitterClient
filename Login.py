#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Twitterライブラリ
import tweepy

# 使用ライブラリ
import os

# 使用クラスファイル
import Setting

def oauth_login():
    # ログイン情報を格納してるクラスをsetに格納
    set = Setting.LoginSetting

    # KEY等設定
    CK = set.CONSUMER_KEY
    CS = set.CONSUMER_SECRET
    AT = set.ACCESS_TOKEN
    ATS = set.ACCESS_TOKEN_SECRET

    # ログイン情報設定
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)

    # ログイン情報を返り値に
    return auth

