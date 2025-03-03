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

## Preface

!!! quote "[George Box](http://en.wikipedia.org/wiki/George_Box)"
    *All models are wrong, but some are useful.* 


这里是 `Eurekaimer` 的数字花园，本站由 `mkdocs` 生成，持续更新中.


本站共有 {{ pages }} 个页面，{{ words }} 个字，{{ codes }} 行代码，{{ images }} 张图片.


!!! info "更新时间"
    最近更新时间为 *{{git_site_revision_date_localized}}* .




## About ME

![profile](imgs/profile.jpg){ align=left width="200" }

### Who is me?

我是来自Nankai University的一名**统计学类**大类学生（分流意向是统计学），MBTI：INTJ，喜欢数学与一切logical and elegant的事物，目前最喜欢的动漫角色是小鞠知花，欢迎一起学习为宇宙写下注脚，以下是联系我的一些方式：

- :octicons-mail-16: QQ邮箱(Email) ： `2507983039@qq.com`
- :octicons-mail-16: 163邮箱(Email)： `Eurekaimer@163.com`
  

这里的笔记内容主要是NKU统计学类课程的课程笔记和自我学习的成果输出，也有参考外文经典教材时的读书笔记。

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


## 关于本站

### 建站纪念

- 2024-10-28 本站建成，作为一个个人学习的一个小记录.
- 2025-02-10 由于一些原因进行了一次迁移，原本的repo已经删除，现有的站点是按照原站点备份恢复的。
- 2025-02-13 由于站点不再纯粹由数学组成，思考后本站点更名为`Eurekaimer's Digital Garden`


### 建站流程

#### 框架选择

要想简单高效地解决问题就必须先抓住主要矛盾的主要方面，这是我一贯的方法论。

首先，我需要判断我出于什么目的需要一个个人博客，我本人是一个统计学学生而不是计算机系或是其他工科专业的学生，我没有很强烈的通过各种开源项目学习的需求，我的个人网站主要是为了记录我的学习过程和一些阅读笔记，所以它最好建立简单；其次，我的美学理念并不喜欢华丽繁复的设计，我的网站也应该简洁大方；最后，它最好有一定的交互功能以达到和他人交流的目的所以拒绝了在其他网站上写作的选项(如知乎、博客园)。最初是在一位知乎看到了本校的一位学长使用了这个框架，后来在浏览了比较多的博客之后中发现其中有相当一部分选择`mkdocs`框架，这也使我可以有更多的样本用来借鉴。

基于上述需求和想法，我选择`mkdocs`框架创建了我的第一个个人博客网站。

#### Plugins

+ [**mkdocs-git-revision-date-localized-plugin**](https://timvink.github.io/mkdocs-git-revision-date-localized-plugin/)：日期显示 css.color.rgb:[140,73,90] 小鞠发色！
+ [mkdocs-callouts](https://github.com/sondregronas/mkdocs-callouts)：一个能够将Obsidian的callouts块自动转换为mkdocs支持语法的插件.
+ [**Material-plugins**](https://squidfunk.github.io/mkdocs-material/plugins/)
      + [**Blog**](https://squidfunk.github.io/mkdocs-material/plugins/blog/)：一个方便写博客的内置插件
      + [**Search**](https://squidfunk.github.io/mkdocs-material/plugins/search/)：内置的搜索插件
      + [**Tags**](https://squidfunk.github.io/mkdocs-material/plugins/tags/)：一个给文件加标签的插件，方便管理
+ [**statistics**](https://github.com/TonyCrane/mkdocs-statistics-plugin?tab=readme-ov-file)：一个用于文档统计的插件，并且可给出预计阅读时间，感谢[TonyCrane](https://github.com/TonyCrane)的开源.

#### Other extension


<div class="grid cards" markdown>

-   :material-notebook-edit-outline:{ .lg .middle } __参考资料__

    ---

    - 在构建本网站的过程中参考了[Wcowin同学的Mkdocs教程](https://wcowin.work/Mkdocs-Wcowin/)

</div>


!!! warning "公告栏"
    如有侵权，请联系我.



[蓝以中](https://pan.baidu.com/s/17YuBy-p8AmS95Y7nDOYRJw?pwd=9kdi)
