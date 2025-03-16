---
statistics: True
comments: true
hide:
  - navigation
---


<center><font  color= #757575 size=6 class="ml3">“Welcome to Eurekaimer's Digital Garden”</font></center>
<script src="https://cdn.statically.io/libs/animejs/2.0.2/anime.min.js"></script>   

<body>
        <font color="#8C495A">
        <p style="text-align: center; ">
                <span>本站已经运行</span>
                <span id='box1'></span>
    </p>
      <div id="box1"></div>
      <script>
        function timingTime(){
          let start = '2024-10-28 00:00:00'
          let startTime = new Date(start).getTime()
          let currentTime = new Date().getTime()
          let difference = currentTime - startTime
          let m =  Math.floor(difference / (1000))
          let mm = m % 60  // 秒
          let f = Math.floor(m / 60)
          let ff = f % 60 // 分钟
          let s = Math.floor(f/ 60) // 小时
          let ss = s % 24
          let day = Math.floor(s  / 24 ) // 天数
          return day + "天" + ss + "时" + ff + "分" + mm +'秒'
        }
        setInterval(()=>{
          document.getElementById('box1').innerHTML = timingTime()
        },1000)
      </script>
      </font>
    </body>



# Home

可以听听歌啊！(播放曲目随站长品味而改变)

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=2112531307&auto=0&height=66"></iframe>

## Preface

!!! quote "[George Box](http://en.wikipedia.org/wiki/George_Box)"
    *All models are wrong, but some are useful.* 


这里是 `Eurekaimer` 的数字花园，本站由 `mkdocs` 生成，持续更新中.


本站共有 {{ pages }} 个页面，{{ words }} 个字，{{ codes }} 行代码，{{ images }} 张图片.


!!! info "更新时间"
    最近更新时间为 *{{git_site_revision_date_localized}}* .




## About ME

![profile](https://cdn.jsdelivr.net/gh/Eurekaimer/MyIMGs@main/img/profile.jpg){ align=left width="200" }

### Who is me?

我是来自Nankai University的一名**统计学类**大类学生（分流意向是统计学），MBTI：INTJ，喜欢数学与一切logical and elegant的事物，目前最喜欢的动漫角色是小鞠知花，欢迎一起学习为宇宙写下注脚，以下是联系我的一些方式：

- :octicons-mail-16: QQ邮箱(Email) ： `2507983039@qq.com`
- :octicons-mail-16: 163邮箱(Email)： `Eurekaimer@163.com`
  

这里的笔记内容主要是NKU统计学类课程的课程笔记和自我学习的成果输出，也有参考外文经典教材时的读书笔记。

!!! warning "公告栏"
    本网站的所有内容均遵循 [CC BY-SA 4.0 license](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License).
    Reference: 移步[这里](blog/posts/建站纪念贴.md)

如果喜欢这个小站，欢迎给一个 Star :material-star: 或者 Fork :fontawesome-solid-code-fork: 这个仓库。

### Personal Interest

+ :simple-wolframmathematica::Analysis and Probability Theory
+ :simple-simpleanalytics::Mathematical Statistic
+ :simple-datastax::Data Science
+ :simple-greatlearning::Machine Learning
+ :simple-myanimelist::Anime
+ :fontawesome-solid-chess-queen::Chess

### Timeline


<div class="grid cards" markdown>

-   :material-notebook-edit-outline:{ .lg .middle } __Education__

    ---

    - 2020.09 - 2023.06 莆田第一中学

    ---

    - 2023.09 - present 南开大学统计与数据科学学院 

</div>




[请我喝下午茶 :material-coffee:](https://raw.githubusercontent.com/Eurekaimer/MyIMGs/refs/heads/main/img/buy_me_a_coffee.png){.md-button}
