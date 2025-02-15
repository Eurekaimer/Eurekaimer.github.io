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
    最近更新时间为 *{{git_revision_date_localized}}* .




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

+ 2020.09 - 2023.06 莆田第一中学
+ 2023.09 - present 南开大学统计与数据科学学院 


## 关于本站

### 建站纪念

- 2024-10-28 本站建成，作为一个个人学习的一个小记录.
- 2025-02-09 由于一些原因进行了一次迁移，原本的repo已经删除，现有的站点是按照原站点备份恢复的。
- 2025-02-13 由于站点不再纯粹由数学组成，思考后本站点更名为`Eurekaimer's Digital Garden`


### 建站流程

#### 框架选择

要想简单高效地解决问题就必须先抓住主要矛盾的主要方面，这是我一贯的方法论。

首先，我需要判断我出于什么目的需要一个个人博客，我本人是一个统计学学生而不是计算机系或是其他工科专业的学生，我没有很强烈的通过各种开源项目学习的需求，我的个人网站主要是为了记录我的学习过程和一些阅读笔记，所以它最好建立简单；其次，我的美学理念 并不喜欢华丽繁复的设计，我的网站也应该简洁大方；最后，它最好有一定的交互功能以达到和他人交流的目的所以拒绝了在其他网站上写作的选项(如知乎、博客园)。除了这些，还有一个契机是我浏览了比较多的博客也有相当一部分选择`mkdocs`框架，我可以有更多的样本用来借鉴。

基于上述需求和想法，我选择`mkdocs`框架创建了我的博客网站。

#### Plugins

+ [**mkdocs-git-revision-date-localized-plugin**](https://timvink.github.io/mkdocs-git-revision-date-localized-plugin/)：日期显示 css.color.rgb:[140,73,90] 小鞠发色！
+ [mkdocs-callouts](https://github.com/sondregronas/mkdocs-callouts)：一个能够将Obsidian的callouts块自动转换为mkdocs支持语法的插件.
+ [**Material-plugins**](https://squidfunk.github.io/mkdocs-material/plugins/)
  + [**Blog**](https://squidfunk.github.io/mkdocs-material/plugins/blog/)
  + [**Search**](https://squidfunk.github.io/mkdocs-material/plugins/search/)
  + [**Tags**](https://squidfunk.github.io/mkdocs-material/plugins/tags/)

+ [**statistics**](https://github.com/TonyCrane/mkdocs-statistics-plugin?tab=readme-ov-file)：一个用于文档统计的插件，并且可给出预计阅读时间，感谢[TonyCrane](https://github.com/TonyCrane)的开源.

#### Other extension


<div class="grid cards" markdown>

-   :material-notebook-edit-outline:{ .lg .middle } __参考资料__

    ---

    - 在构建本网站的过程中参考了[Wcowin同学的Mkdocs教程](https://wcowin.work/Mkdocs-Wcowin/)

</div>





!!! warning "公告栏"
    如有侵权，请联系我.



## 网页资源汇总


### Intoxicating and Useful

+ [Zlibrary](https://zh.z-lib.gs/)：很好用的电子书网站可以疯狂下PDF
+ [MKDOCS官方](https://github.com/mkdocs/mkdocs)：本站采用的静态框架来源于这里
+ [LaTeX在线编辑器](https://www.latexlive.com/)：一个简单好用且免费的在线网站
+ [MCM/ICM](https://www.contest.comap.com/undergraduate/contests/index.html)：美赛官网
+ [樱花动漫](https://www.295k.cc/dongmanplay/2340-1-1.html)：盗版的动漫网站，尽可能保证链接畅通
+ [Texlive Tshinghua University](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)：清华的镜像站，可以用来下载Texlive(如果网络不佳)
+ [fotor](https://www.fotor.com/cn/features/resize/)：免费在线图片尺寸修改
+ [EMOJI网站](https://www.unicode.org/emoji/charts/full-emoji-list.html)：官方的EMOJI网站
+ [tikzcd-editor](https://tikzcd.yichuanshen.de/)：可以帮助绘制tikz
+ [Overleaf](https://www.overleaf.com/project)：一个多人协作的LaTeX在线编译网站，好处是免去了本地配环境，坏处是编译速度和内存受限

### 数学学习

+ [*Terence Tao*](https://terrytao.wordpress.com/)：大名鼎鼎的特仑苏·陶的个人网页，纯英文，内涵很丰富
+ [Math Stackexchange(MSE)](https://math.stackexchange.com/tour)：几乎是世界上最大的数学讨论平台(不考虑MO的情况下)，优点是跨度大
+ [Math Overflow(MO)](https://mathoverflow.net/)：最权威的数学讨论平台，只接受发布研究生以上的问题讨论，否则会被警告
+ [ZWP学长](https://zhangwp.com/share/nku-sms-exams)：NKU数院学长的个人网页，存放有很多专业课试卷，截至2025仍在更新
+ [谢启鸿老师(torsor)的个人博客](https://www.cnblogs.com/torsor)：有很多高质量的复旦大学高等代数的资料(尤其是高等代数每周一题)
+ [清华丘班于品讲义](https://www.bananaspace.org/wiki/%E8%AE%B2%E4%B9%89:%E6%95%B0%E5%AD%A6%E5%88%86%E6%9E%90/%E6%95%B0%E5%AD%A6%E5%88%86%E6%9E%90%E4%B8%80%E7%AE%80%E4%BB%8B)：香蕉空间，一个国内新兴的数学平台，有一些高质量在线电子讲义
+ [丘赛官网](http://yau-contest.com/)：Yau的手笔，里面的参考资料值得一看，也有一些国外大学的网站链接
+ [MIT](https://ocw.mit.edu/)：内嵌许多优质课程的Lecure Notes和Problem Sets
+ [齐震宇](https://www.youtube.com/watch?v=3JBUUE1aLIk&list=PLil-R4o6jmGhUqtKbZf0LIFKd-xN__g_M)：搬运的Youtube上的分析一，难度比较高，老师是湾湾的(Yau的学生)
+ [AMM](http://libgen.rs/scimag/journals/1154)：美国数学月刊，适合和谢惠民一起使用

### CS学习

+ [CSDIY](https://github.com/pkuflyingpig/cs-self-learning/)：一位北大学长写的CS(Computer Science)自学指南，主要是国外的公开课资源

+ [CS自学社区](https://www.learncs.site/docs/curriculum-resource/cs61a/dis/sol-disc00)：一位前辈在CSDIY的基础上衍生出的帮助刷课的网站

+ [CS50x](https://cs50.harvard.edu/x/2025)：Harvard的一门计算机导论公开课，课程质量很高，老师口音也很正常

+ [博客园](https://www.cnblogs.com/)：有上古的好帖子，普遍文章质量较C\*S\*D\*N高许多

  

  

### Favourite Anime

排名不分先后：

+ 轻音少女
+ GBC
+ 冰菓
+ 紫罗兰永恒花园
+ 败犬女主太多了




