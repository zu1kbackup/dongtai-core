# DongTai-models

[![django-project](https://img.shields.io/badge/django%20versions-3.0.3-blue)](https://www.djangoproject.com/)
[![DongTai-project](https://img.shields.io/badge/DongTai%20versions-beta-green)](https://hxsecurity.github.io/DongTaiDoc)
[![DongTai-models](https://img.shields.io/badge/DongTai--models-v1.0-lightgrey)](https://github.com/HXSecurity/dongtai-models)

## DongTai项目介绍
“火线～洞态IAST”是一款专为甲方安全人员、甲乙代码审计工程师和0 Day漏洞挖掘人员量身打造的辅助工具，可用于集成devops环境进行漏洞检测、作为代码审计的辅助工具和自动化挖掘0 Day。

“火线～洞态IAST”具有五大模块，分别是`DongTai-webapi`、`DongTai-openapi`、`DongTai-engine`、`DongTai-web`、`agent`，其中：
- `DongTai-webapi`用于与`DongTai-web`交互，负责用户相关的API请求；
- `DongTai-openapi`用于与`agent`交互，处理agent上报的数据，向agent下发策略，控制agent的运行等
- `DongTai-engine`用于对`DongTai-openapi`接收到的数据进行分析、处理，计算存在的漏洞和可用的污点调用链等
- `DongTai-web`为“火线～洞态IAST”的前端项目，负责页面展示
- `agent`为各语言的数据采集端，从安装探针的项目中采集相对应的数据，发送至`DongTai-openapi`服务
