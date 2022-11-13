

# poetryを試す


新規プロジェクト作成

```
poetry new <project-name>
```

プロジェクトフォルダー内に`.venv`を作成するように変更  
`poetry.toml`が作られ、`in-project = true`が追加されるはず。  
```bash
poetry config virtualenvs.in-project true --local
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