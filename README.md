

# poetryを試す


新規プロジェクト作成

```
poetry new <project-name>
```

必要な依存関係をインストールする

```bash
poetry install
```

仮想環境を起動する。

```bash
poetry shell
```

仮想環境を終了

```bash
exit
```


依存関係を追加。

```bash
poetry add <dependency>
```



スクリプト実行

仮想環境起動して実行(`python <script.py>`) or`poetry run`を使用して実行( `poetry run python <script.py>`)