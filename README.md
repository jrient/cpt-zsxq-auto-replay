# cpt-zsxq-auto-replay
一个简单的chatgpt知识星球自动回复提问

## 部署

设置环境变量

| 参数 | 说明|
| -- | -- | 
| ZSXQ_GROUP_ID | 知识星球频道id|
| ZSXQ_COOKIE | 知识星球cookie，从知识星球网页端获取 |
| OPENAI_API_KEY | open ai key [点击获取](https://platform.openai.com/account/api-keys) |

安装依赖

```sh
$ pip install requests
$ pip install openai
```

配置定时任务

```crontab
* * * * * your_python your_path/cpt-zsxq-auto-replay/zsxq.py
```

## 通过github action部署

1. fork本项目
2. 在 `github.com/[your name]/[your project name]/settings/secrets/actions` 下 `New repository secret` 添加 `ZSXQ_GROUP_ID` `ZSXQ_COOKIE` `OPENAI_API_KEY` 三个环境变量
3. 通过 `github.com/[your name]/[your project name]/actions` 查看运行状态


## 加入我们

有问题或者想法可以联系我们，我们欢迎你的加入！

![IMG](./%E5%8A%A0%E5%85%A5%E6%98%9F%E7%90%83.jpg)

![IMG](./%E6%98%9F%E7%90%83%E4%BC%98%E6%83%A0%E5%88%B8.png)