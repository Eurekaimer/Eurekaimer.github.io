//var CURSOR;
//
//Math.lerp = (a, b, n) => (1 - n) * a + n * b;
//
//const getStyle = (el, attr) => {
//    try {
//        return window.getComputedStyle
//            ? window.getComputedStyle(el)[attr]
//            : el.currentStyle[attr];
//    } catch (e) {}
//    return "";
//};
//
//class Cursor {
//    constructor() {
//        this.pos = {curr: null, prev: null};
//        this.pt = [];
//        this.create();
//        this.init();
//        this.render();
//    }
//
//    move(left, top) {
//        this.cursor.style["left"] = `${left}px`;
//        this.cursor.style["top"] = `${top}px`;
//    }
//
//    create() {
//        if (!this.cursor) {
//            this.cursor = document.createElement("div");
//            this.cursor.id = "cursor";
//            this.cursor.classList.add("hidden");
//            document.body.append(this.cursor);
//        }
//
//        var el = document.getElementsByTagName('*');
//        for (let i = 0; i < el.length; i++)
//            if (getStyle(el[i], "cursor") == "pointer")
//                this.pt.push(el[i].outerHTML);
//
//        document.body.appendChild((this.scr = document.createElement("style")));
//        // 这里改变鼠标指针的颜色 由svg生成
//        this.scr.innerHTML = `* {cursor: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8' width='8px' height='8px'><circle cx='4' cy='4' r='4' opacity='.5'/></svg>") 4 4, auto}`;
//    }
//
//    refresh() {
//        this.scr.remove();
//        this.cursor.classList.remove("hover");
//        this.cursor.classList.remove("active");
//        this.pos = {curr: null, prev: null};
//        this.pt = [];
//
//        this.create();
//        this.init();
//        this.render();
//    }
//
//    init() {
//        document.onmouseover  = e => this.pt.includes(e.target.outerHTML) && this.cursor.classList.add("hover");
//        document.onmouseout   = e => this.pt.includes(e.target.outerHTML) && this.cursor.classList.remove("hover");
//        document.onmousemove  = e => {(this.pos.curr == null) && this.move(e.clientX - 8, e.clientY - 8); this.pos.curr = {x: e.clientX - 8, y: e.clientY - 8}; this.cursor.classList.remove("hidden");};
//        document.onmouseenter = e => this.cursor.classList.remove("hidden");
//        document.onmouseleave = e => this.cursor.classList.add("hidden");
//        document.onmousedown  = e => this.cursor.classList.add("active");
//        document.onmouseup    = e => this.cursor.classList.remove("active");
//    }
//
//    render() {
//        if (this.pos.prev) {
//            this.pos.prev.x = Math.lerp(this.pos.prev.x, this.pos.curr.x, 0.15);
//            this.pos.prev.y = Math.lerp(this.pos.prev.y, this.pos.curr.y, 0.15);
//            this.move(this.pos.prev.x, this.pos.prev.y);
//        } else {
//            this.pos.prev = this.pos.curr;
//        }
//        requestAnimationFrame(() => this.render());
//    }
//}
//
//(() => {
//    CURSOR = new Cursor();
//    // 需要重新获取列表时，使用 CURSOR.refresh()
//})();


// 立即执行函数表达式（IIFE），用于创建一个独立的作用域，避免全局变量污染
!function() {
    // 定义一个函数 o，用于获取元素的属性值
    // 参数 w 是元素对象，v 是要获取的属性名，i 是默认值
    function o(w, v, i) {
        // 如果元素有指定属性，则返回该属性值，否则返回默认值
        return w.getAttribute(v) || i
    }

    // 定义一个函数 j，用于获取指定标签名的所有元素
    // 参数 i 是标签名
    function j(i) {
        return document.getElementsByTagName(i)
    }

    // 定义一个函数 l，用于获取 script 标签的相关属性
    function l() {
        // 获取所有 script 标签
        var i = j("script"),
            // 获取 script 标签的数量
            w = i.length,
            // 获取最后一个 script 标签
            v = i[w - 1];
        return {
            // script 标签的数量
            l: w,
            // zIndex 属性值，默认为 -1
            z: o(v, "zIndex", -1),
            // opacity 属性值，默认为 0.5
            o: o(v, "opacity", 0.5),
            // color 属性值，默认为 "0,0,0"
            c: o(v, "color", "0,0,0"),
            // count 属性值，默认为 99
            n: o(v, "count", 75)
        }
    }

    // 定义一个函数 k，用于获取窗口的宽度和高度，并赋值给画布的宽度和高度
    function k() {
        // 获取窗口的宽度，兼容不同浏览器
        r = u.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        // 获取窗口的高度，兼容不同浏览器
        n = u.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    }

    // 定义一个函数 b，用于绘制画布内容并实现动画效果
    function b() {
        // 清除画布上的所有内容
        e.clearRect(0, 0, r, n);
        // 将 f 对象和 t 数组合并成一个新数组
        var w = [f].concat(t);
        var x, v, A, B, z, y;
        // 遍历 t 数组中的每个点
        t.forEach(function(i) {
            // 更新点的 x 坐标
            i.x += i.xa;
            // 更新点的 y 坐标
            i.y += i.ya;
            // 如果点超出了画布的左右边界，则反转 x 方向的速度
            i.xa *= i.x > r || i.x < 0 ? -1 : 1;
            // 如果点超出了画布的上下边界，则反转 y 方向的速度
            i.ya *= i.y > n || i.y < 0 ? -1 : 1;
            // 在画布上绘制一个 1x1 的矩形表示点
            e.fillRect(i.x - 0.5, i.y - 0.5, 1, 1);
            // 遍历 w 数组中的每个点
            for (v = 0; v < w.length; v++) {
                x = w[v];
                // 如果当前点和遍历到的点不是同一个点，并且它们都有有效的坐标
                if (i !== x && null !== x.x && null !== x.y) {
                    // 计算两点之间的 x 坐标差值
                    B = i.x - x.x;
                    // 计算两点之间的 y 坐标差值
                    z = i.y - x.y;
                    // 计算两点之间的距离的平方
                    y = B * B + z * z;
                    // 如果两点之间的距离小于当前点的最大距离
                    if (y < x.max) {
                        // 如果遍历到的点是 f 对象，并且距离大于等于最大距离的一半
                        if (x === f && y >= x.max / 2) {
                            // 调整当前点的位置
                            i.x -= 0.03 * B;
                            i.y -= 0.03 * z;
                        }
                        // 计算透明度
                        A = (x.max - y) / x.max;
                        // 开始绘制路径
                        e.beginPath();
                        // 设置线条宽度
                        e.lineWidth = A / 2;
                        // 设置线条颜色和透明度
                        e.strokeStyle = "rgba(" + s.c + "," + (A + 0.2) + ")";
                        // 移动到当前点的位置
                        e.moveTo(i.x, i.y);
                        // 绘制一条线到遍历到的点的位置
                        e.lineTo(x.x, x.y);
                        // 绘制线条
                        e.stroke();
                    }
                }
            }
            // 从 w 数组中移除当前点
            w.splice(w.indexOf(i), 1);
        });
        // 请求下一帧动画
        m(b);
    }

    // 创建一个 canvas 元素
    var u = document.createElement("canvas"),
        // 获取 script 标签的相关属性
        s = l(),
        // 生成一个唯一的 id
        c = "c_n" + s.l,
        // 获取 canvas 的 2D 上下文
        e = u.getContext("2d"),
        r,
        n,
        // 获取浏览器的动画帧请求函数，如果不支持则使用 setTimeout 模拟
        m = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
        function(i) {
            window.setTimeout(i, 1000 / 45);
        },
        // 随机数生成函数
        a = Math.random,
        // 定义一个对象 f，用于存储鼠标位置
        f = {
            x: null,
            y: null,
            max: 20000
        };
    // 设置 canvas 的 id
    u.id = c;
    // 设置 canvas 的样式
    u.style.cssText = "position:fixed;top:0;left:0;z-index:" + s.z + ";opacity:" + s.o;
    // 将 canvas 元素添加到 body 元素中
    j("body")[0].appendChild(u);
    // 初始化画布的宽度和高度
    k();
    // 当窗口大小改变时，重新设置画布的宽度和高度
    window.onresize = k;
    // 当鼠标移动时，更新 f 对象的 x 和 y 坐标
    window.onmousemove = function(i) {
        i = i || window.event;
        f.x = i.clientX;
        f.y = i.clientY;
    };
    // 当鼠标移出窗口时，将 f 对象的 x 和 y 坐标设置为 null
    window.onmouseout = function() {
        f.x = null;
        f.y = null;
    };
    // 创建一个空数组 t，用于存储点
    var t = [];
    // 根据 s.n 的值创建指定数量的点
    for (var p = 0; s.n > p; p++) {
        // 随机生成点的 x 坐标
        var h = a() * r;
        // 随机生成点的 y 坐标
        var g = a() * n;
        // 随机生成点的 x 方向速度
        var q = 2 * a() - 1;
        // 随机生成点的 y 方向速度
        var d = 2 * a() - 1;
        // 将点的信息添加到 t 数组中
        t.push({
            x: h,
            y: g,
            xa: q,
            ya: d,
            max: 6000
        });
    }
    // 延迟 100 毫秒后开始绘制动画
    setTimeout(function() {
        b();
    }, 100);
}();

//!function() {
//    function o(w, v, i) {
//        return w.getAttribute(v) || i
//    }
//    function j(i) {
//        return document.getElementsByTagName(i)
//    }
//    function l() {
//        var i = j("script"),
//        w = i.length,
//        v = i[w - 1];
//        return {
//            l: w,
//            z: o(v, "zIndex", -1),
//            o: o(v, "opacity", 0.5),
//            c: o(v, "color", "0,0,0"),
//            n: o(v, "count", 99)
//        }
//    }
//    function k() {
//        r = u.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
//        n = u.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight
//    }
//    function b() {
//        e.clearRect(0, 0, r, n);
//        var w = [f].concat(t);
//        var x, v, A, B, z, y;
//        t.forEach(function(i) {
//            i.x += i.xa,
//            i.y += i.ya,
//            i.xa *= i.x > r || i.x < 0 ? -1 : 1,
//            i.ya *= i.y > n || i.y < 0 ? -1 : 1,
//            e.fillRect(i.x - 0.5, i.y - 0.5, 1, 1);
//            for (v = 0; v < w.length; v++) {
//                x = w[v];
//                if (i !== x && null !== x.x && null !== x.y) {
//                    B = i.x - x.x,
//                    z = i.y - x.y,
//                    y = B * B + z * z;
//                    y < x.max && (x === f && y >= x.max / 2 && (i.x -= 0.03 * B, i.y -= 0.03 * z), A = (x.max - y) / x.max, e.beginPath(), e.lineWidth = A / 2, e.strokeStyle = "rgba(" + s.c + "," + (A + 0.2) + ")", e.moveTo(i.x, i.y), e.lineTo(x.x, x.y), e.stroke())
//                }
//            }
//            w.splice(w.indexOf(i), 1)
//        }),
//        m(b)
//    }
//    var u = document.createElement("canvas"),
//    s = l(),
//    c = "c_n" + s.l,
//    e = u.getContext("2d"),
//    r,
//    n,
//    m = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || window.oRequestAnimationFrame || window.msRequestAnimationFrame ||
//    function(i) {
//        window.setTimeout(i, 1000 / 45)
//    },
//    a = Math.random,
//    f = {
//        x: null,
//        y: null,
//        max: 20000
//    };
//    u.id = c;
//    u.style.cssText = "position:fixed;top:0;left:0;z-index:" + s.z + ";opacity:" + s.o;
//    j("body")[0].appendChild(u);
//    k(),
//    window.onresize = k;
//    window.onmousemove = function(i) {
//        i = i || window.event,
//        f.x = i.clientX,
//        f.y = i.clientY
//    },
//    window.onmouseout = function() {
//        f.x = null,
//        f.y = null
//    };
//    for (var t = [], p = 0; s.n > p; p++) {
//        var h = a() * r,
//        g = a() * n,
//        q = 2 * a() - 1,
//        d = 2 * a() - 1;
//        t.push({
//            x: h,
//            y: g,
//            xa: q,
//            ya: d,
//            max: 6000
//        })
//    }
//    setTimeout(function() {
//        b()
//    },
//    100)
//} ();