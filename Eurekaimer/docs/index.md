---
title:  
statistics: True
comments: true
hide:
    - toc
    - navigation
---

<style>
.md-grid {
  max-width: 1440px;  /* 增加最大宽度，适合大屏幕 */
  padding: 0 20px;    /* 添加左右内边距 */
}

/* 响应式设计 - 不同屏幕尺寸的适配 */
@media (max-width: 1920px) {
  .md-grid {
    max-width: 90%;  /* 2K屏幕使用90%宽度 */
  }
}

@media (max-width: 1366px) {
  .md-grid {
    max-width: 95%;  /* 普通屏幕使用95%宽度 */
  }
}

@media (max-width: 1024px) {
  .md-grid {
    max-width: 100%;  /* 小屏幕使用全宽 */
  }
}
</style>

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


<style>
/* 优化卡片布局 */
.grid.cards {
  gap: 1.5rem;  /* 增加卡片间距 */
}

.grid.cards > ul {
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));  /* 增加最小宽度 */
}

/* 大屏幕优化 */
@media (min-width: 1600px) {
  .grid.cards > ul {
    grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));  /* 大屏幕更大卡片 */
  }
}
</style>

<div class="grid cards" markdown>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
-   :simple-homepage:{ .lg .middle } 公告栏:目前正在研究高维统计和信息论(欢迎交流)
=======
-   :simple-homepage:{ .lg .middle } __公告栏:目前沉迷泛函分析
>>>>>>> parent of 06ce14d5 (Revert "Add mkdocs-codeforces-plugin")
=======
-   :simple-homepage:{ .lg .middle } __公告栏:上线了不背单词进度(欢迎push__
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
-   :simple-homepage:{ .lg .middle } __公告栏:上线了不背单词进度(欢迎push__
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
-   :simple-homepage:{ .lg .middle } __公告栏:上线了不背单词进度(欢迎push__
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)

    ---
    ![image](https://cdn.jsdelivr.net/gh/Eurekaimer/MyIMGs@main/img/profile.jpg){ class="responsive-image" align=right width="480" height="320" style="border-radius: 25px;" }

    可以听听歌啊！(播放曲目随站长品味而改变)

     <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=2089023383&auto=1&height=66"></iframe>

    - [x] 这里是 `Eurekaimer` 的数字花园，本站由 `mkdocs` 生成，持续更新中.
    - [x] 本站共有 {{ pages }} 个页面，{{ words }} 个字，{{ codes }} 行代码，{{ images }} 张图片.
    - [x] 最近更新时间为 *{{git_site_revision_date_localized}}* .
    
    === "推荐"

        - [x] [学术主页](https://www.eurekaimer.xyz/Academic/) 

    === "Quote"

         All models are wrong, but some are useful.
            
         —— [George Box](http://en.wikipedia.org/wiki/George_Box)

    === "移动端"

        请点击左上角图标选择分类和文章

    === "PC端/Mac"

        请点击上方导航栏选择你感兴趣的部分

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    
=======
>>>>>>> parent of 06ce14d5 (Revert "Add mkdocs-codeforces-plugin")
=======
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
    === "不背单词"

        [![leftover's bbdc stats](https://stat.leftover.cn/bbdc?userId=988693129&nickname=Eurekaimer)](https://github.com/left0ver/github-bbdc-stat) -->

    
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)

</div>
<style>
    /* 响应式图片优化 */
    .responsive-image {
        max-width: 100%;
        height: auto;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    @media only screen and (max-width: 768px) {
        .responsive-image {
            display: none;
        }
    }
    
    /* 大屏幕优化 */
    @media (min-width: 1600px) {
        .responsive-image {
            margin-left: 2rem;
        }
    }
</style>





<div class="grid cards" markdown>

-   :material-checkbox-multiple-marked-outline:{ .lg .middle } __ABOUT ME__

    ---

    - From: Nankai University
    - Major: Statistics
    - MBTI: INTJ
    - Love: 小鞠知花/数学/Logical and Elegant Things

    页脚处是联系我的一些方式：

-   :simple-sparkfun:{ .lg .middle } __Personal Interest__

    ---

    + :simple-wolframmathematica::Analysis and Probability Theory
    + :simple-simpleanalytics::Mathematical Statistic
    + :simple-datastax::Data Science
    + :simple-greatlearning::Machine Learning
    + :simple-myanimelist::Anime
    + :fontawesome-solid-chess-queen::Chess

    
-   :material-book-education:{ .lg .middle } __Education__

    ---

    - [x] 2020.09 - 2023.06 莆田第一中学
    - [x] 2023.09 - 2024.09 南开大学生命科学学院 

    ---

    - [ ] 2024.09 - present 南开大学统计与数据科学学院 

-   :material-scale-balance:{ .lg .middle } __Open Source, [CC BY-SA 4.0 license](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License)__

    ---

    - [x] 请在搬运或是引用本站内容前查询相关开源协议
    - [x] Reference: 移步[这里](blog/posts/建站纪念贴.md)
    - [x] 欢迎给一个 Star :material-star: 或者 Fork :fontawesome-solid-code-fork: 这个仓库

    [请我喝下午茶 :material-coffee:](https://raw.githubusercontent.com/Eurekaimer/MyIMGs/refs/heads/main/img/buy_me_a_coffee.png){.md-button}

-   :yum:{ .lg .middle } __Yuri__

    ---

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    - [x] 一周一次[399]
    - [x] 终将成为你
    - [x] 安达与岛村
    
-   :octicons-goal-16:{ .lg .middle } __Goal__
=======
{% codeforces username="Eurekaimer" width="100%" theme="light" %}



>>>>>>> parent of 06ce14d5 (Revert "Add mkdocs-codeforces-plugin")
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)
=======
>>>>>>> parent of 40ab7323 (Add mkdocs-codeforces-plugin)

    ---

    - [ ] GBC_Shanghai
    - [ ] One paper before 2026.6

</div>