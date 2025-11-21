# 🎬 中国电影数据采集与可视化分析系统

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Web-Flask-green)
![ECharts](https://img.shields.io/badge/Visual-ECharts-red)

## 📖 项目简介
本项目是一个集 **网络爬虫、数据存储、数据分析、Web 可视化** 于一体的综合实战案例。

系统后端采用 **Python Flask** 框架，前端结合 **ECharts** 与 **WordCloud** 实现数据的直观展示。针对豆瓣电影网站的反爬虫机制，实现了高效的数据采集策略（成功率 >90%），并将数据持久化存储于 **SQLite** 数据库中。

## 📸 运行效果展示 (Demo)

### 1. 数据可视化大屏 (Dashboard)
通过 ECharts 展示电影评分分布、地区分布等关键指标。
![Dashboard](此处链接稍后替换)

### 2. 电影词云分析 (WordCloud)
直观展示电影标题与简介的高频热点词汇。
![WordCloud](此处链接稍后替换)

## 🛠️ 技术架构
* **数据采集 (Spider)**: 
    * 使用 `Requests` + `BeautifulSoup` / `Re` 进行数据抓取与解析。
    * 实现 **User-Agent 伪装** 与 **代理 IP 轮询**，有效突破反爬限制。
* **数据存储 (Data)**: SQLite3 关系型数据库。
* **Web 后端 (Server)**: Flask 轻量级框架。
* **前端展示 (View)**: HTML5 + CSS + JavaScript (ECharts, WordCloud)。

## 📂 项目结构
```text
movie-data-visualization/
├── spider/                # 🕸️ 爬虫模块
│   ├── spider.py          # 爬虫主程序
│   └── ...
├── web/                   # 🖥️ Web可视化模块
│   ├── app.py             # Flask 启动入口
│   ├── static/            # 静态资源 (CSS, JS, Images)
│   └── templates/         # HTML 模板
├── README.md              # 项目说明文档
└── requirements.txt       # 项目依赖文件
