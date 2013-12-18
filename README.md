# OMyList

## Tools
* [user]()

	User Center!
    用户中心!

* [bill]()

	Bill Manager!

## Requirements
* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy]()
* [MongoEngine]()

## How to start the application?

At first you should rename env.sample.py to env.py.

首先需要把样例文件重命名为 env.py.


```
cp env.sample.py env.py
```

Then you should change the env.py configurations depending on your applicaiton environment:

然后, 需要根据应用环境修改 env.py 的配置：

```
# environment (production, testing, development)
ENV = ''

# Application directory
APP_DIR = '/your/application/directory'
```

Run the application server:

运行服务：

```
python runserver.py
```

open `http://0.0.0.0:5000` in the browser.

