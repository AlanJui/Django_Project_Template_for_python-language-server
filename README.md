# 專案指引

## 啟動專案

```sh
cd ~/workspace/python/
poetry new <ProjectName>
cd <ProjectName>

git branch main
git init

python -m venv .venv
poetry shell
```

```sh
nvim pyproject.toml
```

pyproject.toml

```sh
...
[tool.poetry.dependencies]
python = "^3.11"
django = ">=4.0,<5.0"


[tool.poetry.group.dev.dependencies]
pydocstyle = "^6.3.0"
django-stubs = { version = "^4.2.7", extras = ["compatible-mypy"] }
mypy = ">=1.7.0,<1.8.0"
...
```

```sh
poetry install
```

```sh

```

```sh

```

```sh

```

```sh

```

## poetry 安裝指引

### 指定安裝某一版本之 Python 套件

```sh
poetry add django@4.2.3
```

### 要求安裝 4.x 版

不想升級到最新版 5.1 ，只要 4.x 最後一版即可。

```sh
poetry add django "django>=4.0,<5.0"
```

### pip install 指令轉成 poetry add

遇以下 pip install 安裝指令：

```sh
pip install django-stubs[compatible-mypy]
```

想改用 poetry add 安裝 Pyhon 套件：

```sh
poetry add django-stubs --extras "compatible-mypy" --group dev
```
