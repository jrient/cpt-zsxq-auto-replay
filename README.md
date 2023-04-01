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

> pip install requests
> pip install openai

配置定时任务

> 0/30 * * * * your_python your_path/cpt-zsxq-auto-replay/zsxq.py
