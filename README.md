# wechat-bot
微信公众号
基于werobot库的菜鸟练习项目
菜单栏json:
```json
{
    "button":[
        {
            "type":"click",
            "name":"今日新闻",
            "key":"V1001_TODAY_NEWS"
        },
        {
            "type":"click",
            "name":"每日英语",
            "key":"V1001_TODAY_ENGLISH"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"view",
                    "name":"搜索",
                    "url":"http://www.soso.com/"
                },
                {
                    "type":"view",
                    "name":"视频",
                    "url":"http://v.qq.com/"
                },
                {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                }
            ]
        }
    ]
}
```
