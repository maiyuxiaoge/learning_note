# 什么是jquery
javascript + query

# jquery demo
```js
$(function(){
    var $btnobj = $("#btnId");
    $btnobj.click(function(){
        alert(1);
    });
})

```

# jquery函数核心
- 传入参数为函数，在文档加载完成后执行这个函数
- 传入参数为html字符串，根据这个字符串创建元素节点对象
- 传入参数为选择器字符串，根据这个字符串查找元素节点对象
- 传入参数为dom对象，将dom对象包装为jquery对象返回

# jquery对象与dom对象

## Dom 对象
1. 通过 getElementById()查询出来的标签对象是 Dom 对象
2. 通过 getElementsByName()查询出来的标签对象是 Dom 对象
3. 通过 getElementsByTagName()查询出来的标签对象是 Dom 对象
4. 通过 createElement() 方法创建的对象，是 Dom 对象
DOM 对象 Alert 出来的效果是：[object HTML 标签名 Element]
## jQuery 对象
5. 通过 JQuery 提供的 API 创建的对象，是 JQuery 对象
6. 通过 JQuery 包装的 Dom 对象，也是 JQuery 对象
7. 通过 JQuery 提供的 API 查询到的对象，是 JQuery 对象
jQuery 对象 Alert 出来的效果是：[object Object]

# jquery对象本质
jQuery 对象是 dom 对象的数组 + jQuery 提供的一系列功能函数。

# jquery和dom互转
![$[dom对象]    1](images/ca136d722aa4fea230b73aeb90ba5b9428666fb7b508e6652d932b5d2a336969.png)  

# 基础选择器
- $(#id)
- $(element)
- $("*")
- $(".class")
- $(div,span,p.myClass)

# 层级选择器
- $(ancestor descendant) 给定祖先元素的下匹配所有的后代元素
- $(parent > child) 给定父元素的所有子元素
- $(prev + next) 在prev后的一个next元素
- $(prev ~ siblings) 在prev后的所有sibling元素

# 基本过滤选择器
- ：first 第一个元素
- : last 最后一个元素 
- : not(selector)  去除匹配的
- : even  索引为偶数
- ：odd
- : eq(index)  索引等于index
- ：gt(index)
- :lt(index)
- :header
- :animated

# 内容过滤器
- ：contains（）  包含给定文本的元素
- : empty
- : has()  含有选择器所匹配的元素的个数
- ：parent 含有子元素或文本的元素

# 属性过滤器
- [attribute=value] 属性为特定值
- [attribute!=value] 不含有指定属性或者属性不等于特定值
- [attribute^=value] 属性以某些值开头
- [attribute$=value] 以某些值结尾
- [attribute*=value] 包含某些值
- [][][] 同时满足多个条件


# 表单过滤器
- :text
- :password
- :checkbox
- :submit
- :image
- :reset
- :button
- :file
- :hidden
- ：enabled
- :disabled
- :checked
- :selected 表单中选中的option

# 元素筛选
- eq() 获取给定索引的元素                                       功能跟 :eq() 一样
- first() 获取第一个元素                                        功能跟 :first 一样
- last() 获取最后一个元素                                       功能跟 :last 一样
- filter(exp) 留下匹配的元素
- is(exp) 判断是否匹配给定的选择器，只要有一个匹配就返回，true
- has(exp) 返回包含有匹配选择器的元素的元素                      功能跟 :has 一样
- not(exp) 删除匹配选择器的元素                                 功能跟 :not 一样
- children(exp) 返回匹配给定选择器的子元素                      功能跟 parent>child 一样
- find(exp) 返回匹配给定选择器的后代元素                        功能跟 ancestor descendant 一样
- next() 返回当前元素的下一个兄弟元素                           功能跟 prev + next 功能一样
- extAll() 返回当前元素后面所有的兄弟元素                       功能跟 prev ~ siblings 功能一样
- nextUntil() 返回当前元素到指定匹配的元素为止的后面元素
- parent() 返回父元素
- rev(exp) 返回当前元素的上一个兄弟元素
- revAll() 返回当前元素前面所有的兄弟元素
- prevUnit(exp) 返回当前元素到指定匹配的元素为止的前面元素
- siblings(exp) 返回所有兄弟元素
- add() 把 add 匹配的选择器的元素添加到当前 jquery 对象中

# 属性操作
- html() 它可以设置和获取起始标签和结束标签中的内容。 跟 dom 属性 innerHTML 一样。
- text() 它可以设置和获取起始标签和结束标签中的文本。 跟 dom 属性 innerText 一样。
- val() 它可以设置和获取表单项的 value 属性值。 跟 dom 属性 value 一样
- attr() 可以设置和获取属性的值，不推荐操作 checked、readOnly、selected、disabled 等等。attr 方法还可以操作非标准的属性。比如自定义属性：abc,bbj
- prop() 可以设置和获取属性的值,只推荐操作 checked、readOnly、selected、disabled 等等

# dom的增删改
内部插入：
- appendTo() a.appendTo(b) 把 a 插入到 b 子元素末尾，成为最后一个子元素
- prependTo() a.prependTo(b) 把 a 插到 b 所有子元素前面，成为第一个子元素
外部插入：
- insertAfter() a.insertAfter(b) 得到 ba
- insertBefore() a.insertBefore(b) 得到 ab
替换:
- replaceWith() a.replaceWith(b) 用 b 替换掉 a
- replaceAll() a.replaceAll(b) 用 a 替换掉所有 b
删除：
- remove() a.remove(); 删除 a 标签
- empty() a.empty(); 清空 a 标签里的内容

# CSS样式
- addClass() 添加样式
- removeClass() 删除样式
- toggleClass() 有就删除，没有就添加样式。
- offset() 获取和设置元素的坐标。

# jquery 动画

## 基本动画
- show() 将隐藏的元素显示
- hide() 将可见的元素隐藏。
- toggle() 可见就隐藏，不可见就显示。
- 以上动画方法都可以添加参数。
1. 第一个参数是动画 执行的时长，以毫秒为单位
2. 第二个参数是动画的回调函数 (动画完成后自动调用的函数)
## 淡入淡出动画
- fadeIn() 淡入（慢慢可见）
- fadeOut() 淡出（慢慢消失）
- fadeTo() 在指定时长内慢慢的将透明度修改到指定的值。0 透明，1 完成可见，0.5 半透明
 -fadeToggle() 淡入/淡出 切换