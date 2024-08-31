# 專案指引

## 安裝 poetry

[Python Poetry Installer](https://github.com/python-poetry/install.python-poetry.org/blob/main/README.md)

### Install

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

### Uninstall

```sh
curl -sSL https://install.python-poetry.org | python3 - --uninstall
curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
```

### V&V

```sh
poetry --version
```


## 安裝及設定專案執行環境

### 下載原始碼

```sh
git clone git@github.com:AlanJui/Django_Project_Template_for_python-language-server.Git
cd git@github.com:AlanJui/Django_Project_Template_for_python-language-server
```

### 設定專案使用之 Python 直譯器

```sh
pyenv versions
pyenv local <Python_Version>
```

### 建置及啟用專案使用之Python虛擬環境

```sh
python -m venv .venv
poetry shell
```

### 安裝專案引用之套件

```sh
poetry install
```

### 驗證專案作業環境設定結果

```sh
(.venv) [alanjui@NucBoxM6 Django_Project_Template_for_python-language-server (main ✗)]$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 31, 2024 - 09:27:04
Django version 4.2.9, using settings 'web_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

[31/Aug/2024 09:27:20] "GET / HTTP/1.1" 200 14
Not Found: /favicon.ico
[31/Aug/2024 09:27:21] "GET /favicon.ico HTTP/1.1" 404 2456
^C%                                                                                                                                                                                 (.venv) [alanjui@NucBoxM6 Django_Project_Template_for_python-language-server (main ✗)]$
```

## poetry 安裝指引

以下說明如何透過 poetry 安裝 Python 套件。

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

## 參考

### 建置 Django 專案作業

1. 建置專案目錄及 poetry 設定檔

```sh
cd ~/workspace/python/
poetry new <ProjectName>
cd <ProjectName>
```

2. 建置專案使用 Git Repo

```sh
git branch main
git init
```

3. 建置及啟用專案用 Python 虛擬環境

```sh
pyenv local <Python_Version>
python -m venv .venv
poetry shell
```

4. 依專案需求修改 poetry 設定檔

```sh
nvim pyproject.toml
```

pyproject.toml 設定檔內容

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

