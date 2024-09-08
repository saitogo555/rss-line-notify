# RSS LINE Notify

[LINE Notify](https://notify-bot.line.me/ja/)を利用して、RSSから取得した情報を定期的にLINEに通知するプログラムです。

定期実行はGithubActionsでCRONを使って行います。

## 環境変数

このプロジェクトでは以下の環境変数を使用します。

- `LINE_NOTIFY_TOKEN`: LINENotifyAPIにアクセスするためのトークン
