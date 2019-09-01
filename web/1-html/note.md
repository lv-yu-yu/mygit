# 创建HTML文件
- 文件名部分
    1. 使用英文数组下划线或者 - 等字符组成
    2. 请尽量有意义
    3. 不要随便使用空格和特殊字符
- 文件后缀部分
.html后缀
    win2000年后对文件的后缀长度不做限制，后缀就开始变得完整了
    比如：.doc->.docx  .txt->.text  .jpe->.jpeg  .htm->.html
.htm后缀
    在早期的win98操作系统中，只能够支持三位数的文件后缀，所以那个时候诞生的文件，都是三位数以内的后缀。
    比如：.doc word文档   .avi  视频文件  .txt  文本文件  .jpg/jpe 图片文件
- 注意：组织->文件和文件夹选项-> 查看选项卡->高级设置部分->去掉“隐藏已知文件类型的扩展名”的勾

# 第一个HTML代码
    <marquee>什么是图灵？图灵就是秃了就会灵光一现，顿悟！</marquee>
- 总结特征/基本结构：
                  <标签名>内容</标签名>
                  
        <marquee width="50%">什么是图灵？图灵就是秃了就会灵光一现，顿悟！</marquee>
- 总结特征/结构2：
                  <标签名 属性名="属性值">内容</标签名>

        <marquee width="50%" loop="2">什么是图灵？图灵就是秃了就会灵光一现，顿悟！</marquee>
- 总结特征/结构3：
                  <标签名 属性名="属性值" 属性名="属性值">内容</标签名>
- 注意：HTML标签属性没有顺序限制.

           <marquee loop="2" width="50%">
               <font color="pink">什么是图灵？图灵就是秃了就会灵光一现，顿悟！</font>
           </marquee>
- 总结特征/结构4：
                    <标签名1 属性名="属性值" 属性名="属性值">
                        <标签名2 属性名="属性值">内容</标签名2>
                    </标签名1>
- 注意事项：
   - 1.所有的单词字母符号，都必须在英文半角下输入
   - 2.标签非常多则么办？多写多练
   - 3.标签对应的属性非常多？多写多练
- 注释：注解和解释，说明文字，不会被浏览器识别，只是用于程序员或者开发人员之间沟通和说明
# HTML标签的学习
## 全局架构标签
        <!doctype html>
        <html>
            <head>
                <!--网页的思想 都是看不到信息-->
                <meta charset="utf-8">
            </head>
            <body>
                <!--网页的显示主题  都是看不到信息-->      
                为什么男人用符号♂，女人的符号用♀，我觉得很不妥！明显男人应该用%，女人用@符号，这才贴切！
            </body>
        </html>
        案例v1
 ## 标签详解
 #### body标签
    bgcolor属性       用于设置页面的背景颜色
    background属性    设置页面的背景图片
    案例v02
    注意：如果同时存在背景颜色和背景图片，优先显示背景图片
    了解属性：
    link属性        设置超链接的颜色（正常状态）
    alink属性       active link 设置鼠标点击超链接的颜色
    vlink属性       visited link 设置鼠标点击过后的颜色
    案例v03
    
    topmargin       设置网页内部内容距离预览器视窗顶部的距离
    leftmargin      设置网页内部内容距离预览器视窗左部的距离
    bottommargin    设置网页内部内容距离预览器视窗底部的距离
    rightmargin     设置网页内部内容距离预览器视窗右部的距离

### 文本标签
#### h1,h2,h3,h4,h5,h6
    作用：用于表示文章的标题
    特征：
        1.h1-h6字体大小逐渐变小
        2.所有的h系列标签都是粗体标签
        3.所用的h系列标签都会换行，独占一行
    注意：
        h1在一个页面中只允许使用一次，用于当前页面的主要内容标题
        在网站首页->logo位置  文章页->文章主标题
        
        h2标签没有数量要求，用于表示和当前h1标题并列关系的内容标题，次重点内容
        h3,h4没有数量要求，对搜索引擎的影响很弱，可以忽略不计
        h5,h6基本不用
        
### 样式标签
#### 1.单纯的样式标签
    b标签       粗体标签   bold粗
    i标签       斜体标签   italic斜体
    u标签       下划线标签    underline
#### 2.强调意义的样式标签
    strong标签  具有强调意义的粗体
    cite标签    具有强调意义的斜体字效果   床震
    em标签      具有强调意义的斜体字效果   车震 > 床震    
#### 3.自定义的样式标签
    font标签   自定义字体标签
        color属性  设置颜色
        size属性   设置字体大小  取值 1 - 7
        face属性   设置字体类型   取值字体名称（必须是操作系统中存在的字体）
     案例v05
        
### 格式标签
    p 标签    段落标签
            表示一个自然段落，在文章中比较常用，段落格式参照外国文字效果，
        首行不会缩进2个字符，如果需要缩进，必须使用css来解决
    br 标签    强制换行标签
        在制定的位置进行强制换行操作
    hr 标签    水平线标签
        width属性   设置水平线的宽度
        color属性   设置水平线的颜色
    center标签    水平居中标签
        注意：尽量不要使用
    案例v06
    div标签   无意义标签
        作用：在页面布局中进行页面画块和分割页面使用标签
    span标签   无意义标签
        作用：在页面布局中使用用于存放文本内容
    块标签和行内标签的特征
        div 标签是块标签的代表
        span 标签是行内标签的代表 行内标签也称为内标签
        
        行内标签和块标签的区别：
            1.块状元素可以设置宽高 行内元素不可以设置宽高
            2.块状元素不可以和其他元素在一行共存，内敛元素可以和内敛元素在一行共存
            3.块状元素可以包含内联元素，内联元素不可以包含块状元素
        元素和标签
            元素和标签标示的内容不太一样
            div元素   在js称呼
            div标签   在HTML中的称呼
        在绝大多数的书籍中，元素和标签的概念等效
        案例：v07
#### 列表标签
     ul 标签     unorder list   无序列表
        <ul>
            <li>内容</li>
            <li>内容</li>
            ......
        </ul>
     ol 标签  order list   有序列表
        <ol>
            <li>内容</li>
            <li>内容</li>
        </ol>
     type属性  设置表示类型
     start属性  设置表示开始值
     dl 标签  defined list   定义列表
        <dl>
            <dt>定义内容标题</dt>
            <dd>定义内容相关属性</dd>
            <dd>定义内容相关属性</dd>
            ...
        </dl>
     注意：一个dl标签内部只允许有1个dt标签，dd标签不受数量限制。

#### 超链接标签  
    超链接简单的说就是内容链接，通过点击操作可以跳转或者打开新的文件的一种方式
    a标签
        href属性 用于设置超链接跳转或者打开的文件地址
        target属性 设置超链接的打开方式
            _self 当前自己页面打开（默认值）
            _blank 在新的页面打开
            _top 在顶级页面打开（在框架集中使用）
            _parent 在父级页面打开（在框架集中使用）
            自定义打开方式（在框架集中使用）
    超链接的三种使用方式：
        1.普通超链接
            格式：<a href="地址">内容</a>
            案例v09
        2.锚点链接
            第一步：在需要跳转到的目的地，使用a 标签和name属性定义锚点位置和名称
                <a name="锚点名称"></a>
            第二步：在需要点击跳转的位置，使用正常的超链接设置跳转位置，必须以#开头
                <a href = "#锚点名称">内容</a>
            注意：锚点的设置可以使用id名称代替a标签和name 属性设定
        3.邮件链接（不推荐使用）
            格式：<a href = "mailto:邮件地址">内容</a>
        案例v11
    地址的分类
        相对链接
            ./img/girl.jpg
            ../img/body.jpg
            man.png
            没有协议的链接就是相对链接。
            . 表示在当前文件夹中查找
            .. 表示在上一层文件夹中查找
        绝对链接
            http://www.biadu.com/img/girl.jpg
            https://www.taobao.com/img/girl.jpg
            ftp://file.163.com/img/girl.jpg
            
            具有协议的链接就是绝对链接，地址固定不变，无论如何地  
        案例v10 
        
### 图片标签
    img标签 图像标签
        作用：用于在页面中引入图片使用
          src属性   用于设置引入的图片地址
          width属性   设置图片的宽度
          height属性   设置图片的高度
          
        注意：如果只设置宽高之一，则另一侧会等比例缩放，保证图片比例不变，但是如果同时设置宽度和高度，图片会
        被强制拉伸至指定的宽高
        
        alt属性  设置图片和加载失败时显示的文字内容，有描述图片的作用
        title属性  设置图片正常加载时鼠标悬停的提示文字，描述图片的作用
        
        要求alt和title属性必须同时书写而且内容必须一致
        
        border属性   设置图片的边框宽度属性，一般不用，偶尔用于取消低版本的IE浏览器图片带有链接时的蓝色默认边框
        
 ### 图像热点
    能够实现在一张图片上面添加多种不同超链接效果的技术
    需要使用到图片标签img，地图标签map，区域标签area
    map标签   图像热点标签
        name属性用于设置热点地图的名称
    area标签   图像热点区域标签
        shape属性  设置热点区域的形状
        circle圆形   rect 矩形  poly多边形
        coords属性  热点区域记录属性
        用于记录绘制指定形状需要的参数
        href属性   设置热点区域的链接地址
        target属性   设置热点区域链接的打开方式
    格式
        <img src="图片地址"  usemap="#地图名称" />
        
        <map name="地图名称">
            <area shape="形状" coords="形状的信息" href="链接地址" target="打开方式" />
            <area shape="形状" coords="形状的信息" href="链接地址" target="打开方式" />
            ...
        </map>
    
### 表格
- 早期时候表格由于页面布局和数据摆放
- 现在表格基本上用于数据摆放这一种形式
#### table标签 用于定义表格的范围
    border属性  设置表格的宽度 单位像素
    width属性   设置表格总宽度
    height属性  设置表格总高度
    align属性   设置表格相对于外层标签的对齐方式
    left 左对齐  center水平居中 right 右对齐
    cellspacing属性  设置单元格之间的间隙大小
    cellpadding属性  设置单元格中内容开始书写的位置
    bgcolor属性  设置表格的背景颜色
    案例v14
#### tr标签  table row用于定义表格的行
    bgcolor属性  设置单元格行的背景原色
    注意：如果存在表格颜色和行颜色，以行颜色为主
    
    align 属性  设置单元格行的水平对齐方式
    left左对齐 center水平居中 right右对齐
    valign属性 设置行内内容的垂直对齐方式
    top上对齐 middle垂直居中  bottom底部对齐
    height属性  设置当前行的行高
#### td标签  用于定义表格的单元格，存放表格中的数据
    bgcolor属性  设置单元格的背景颜色
    注意：如果存在表格颜色和行颜色和单元格颜色，以单元格颜色为主
    
    align属性  设置单元格内内容的水平对齐方式
    left左对齐  center水平居中  right右对齐
    
    valign属性  设置单元格内内容的垂直对齐方式
    top上对齐  middle垂直居中  bottom底部对齐
 
    width属性  设置单元格的宽度
    注意：设置单元格宽度会影响一列的宽度
    
    height属性  设置单元格的高度
    注意：设置单元格的高度会影响一行的高度
    
    colspan属性  单元格跨列设置
    值：整数  表示当前单元格占用水平方向的单元格个数
    rowspan属性  单元格跨行设置
    值：整数  表示当前单元格占用垂直方向的单元格个数
    案例：v15
    
#### caption标签  表格描述标签
#### th标签  表头标签
    注意：th标签和td标签具有相同的属性和用法
    th具有固定样式：粗体字，居中对齐
### 表单标签
#### 什么是表单
    表单是用于连接用户和后台服务器的窗口，负责接收用户的数据和操作，将数据提交到后台服务器页面的标签
    
    form标签  表单范围标签
    用于声明一个完整的可以提交数据的表单范围
        action属性  设置当前表单数据提交的地址
        method属性  设置当前表单提交数据的方式
        get提交（使用明信片发信）
            1.明文传输，所有信息会在浏览器的地址栏显示
            2.get方式提交的数据长度有限，受地址栏长度的限制
        post提交（使用信封发送信息）
            1.密文传输，所有信息都不会显示在地址栏中，在head头信息中发送
            2.post方式提交数据长度几乎没有限制，因为服务器可以无限设置
        enctype属性  设置当前表单提交数据的编码方式
            application/x-www-form-urlencoded值 URL编码（默认值）
            multipart/form-data值  上传文件必备值（必须记住）
            text/plain值  基本不编码
        target属性  设置提交页面的打开方式
        值和a标签href属性一致
#### 表单内容
    input标签  输入表单
        1.文本输入框
        <input type="text" name="自定义名称" value="" />
        type属性  text值  表示当前表单类型为文本输入框
        name属性  设置当前表单提交数据的名称
        value属性  设置当前表单的默认值或者提示信息（推荐作为默认值使用）
        
        2.密码输入框
        <input type="password" name="自定义名称" value="" />
        type属性  password值  表示当前表单为密码输入表单
        name属性  设置当前表单提交数据的名称
        value属性  设置当前表单的默认值（一般不设置）
        
        3.单选表单
        <input type="radio" name="自定义名称" value="默认值" />
        type属性  radio值  表示当前表单为单选表单
        name属性  设置当前表单提交数据的名称，所有name属性值相同才可以实现单选
        value属性  设置当前表单的默认值（必须填写，因为该表单无法输入内容）
        
        4.复选表单
        <input type="checkbox" name="自定义名称"  value="默认值" />
        type属性  checkbox值表示当前表单为复选表单
        name属性  设置当前表单提交数据的名称，如果需要实现多选name属性后面必须添加[]
        value属性  设置当前表单的默认值（必须填写，因为该表单无法输入内容）
        
        5.文件选取表单
        <input type="file" name="自定义名称" value="" />
        type属性  file表示当前表单为文件选取表单
        name属性  设置当前表单提交数据的名称
        value属性  设置表单的默认值（一般不写）
        
        6.提交按钮
        <input type="submit" name="可以不填写" value="按钮名称" />
        type属性  submit值  设置当前表单为提交按钮类型
        name属性  设置当前按钮提交的名称（一般不需要填写）
        value属性  设置当前按钮的名称
        
        7.重置按钮
        <input type="reset" name="可以不填写" value="按钮名称" />
        type属性  reset值  设置当前按钮为重置按钮
        name属性  设置当前按钮提交的名称（一般不填写）
        value属性  设置当前按钮的名称
        
        8.图片提交按钮
        <input type="image" src="引入图片地址" name="可以不填写" value="可以不填写" />
        type属性 image值 表示当前表单为图像提交按钮
        src属性 用于引入图片的地址
        name属性  用于设置 表单的名称（一般不填写）
        value属性  按钮值（一般不写，根本不会显示）
        
        9.隐藏表单
        <input type="hidden" name="自定义用户名" value="默认值" />
        type属性  hidden值表示当前表单为隐藏表单
        name属性  设置当前提交数据的名称（必须填写）
        value属性  设置当前表单的默认值（必须填写）
        
    select标签
        用于定义一个可以选择内容提交内容的下拉列表
        下拉格式：
            <select name="自定义名称">
                <option value="提交值">显示内容</option>
                <option value="提交值">显示内容</option>
                ...
            </select>
        注意：如果option标签中不使用value属性，那么提交的时候会将option标签中的内容提交上去（不推荐）
        
        multiple属性  单属性没有值，设置当前列表为多选列表 
        多选列表：
            <select name="自定义名称" multiple>
                <option value="提交值">显示内容</option>
                <option value="提交值">显示内容</option>
                ...
            </select>
        注意：多选列表如果要使用请在name后面添加[],和checkbox表单一样
            如果想选取多个选项，需要按住Ctrl进行选取
            
        textarea标签  多行文本标签/文本域标签
            
            主要用于用户输入多行文本使用，input type=“text” 标签只可以输入单行不可以回车。
            格式：
                <textarea name="自定义名称" cols="列数（宽度）" rows="行数（高度）">
                    默认值或者提醒值
                </textarea>
            注意：textarea标签没有value属性，值需要在开始和结束标签之间进行设置。
        
        button标签  多功能按钮标签
            type属性
                type="submit"  提交按钮（默认）
                type="reset"  重置按钮
                type="button"  普通按钮
- 案例17                
                
#### 表单标签相关属性
    尺寸相关的属性
        size属性  设置input标签的长度
            主要用于 input中的文本输入框和密码输入框，还可以用于多选列表
        cols属性  设置文本域的宽度
        rows属性  设置文本域的高度
            主要用于textarea标签
    内容长度限制属性
        maxlength属性  设置表单允许输入的最大字符数
            主要用于input类型的文本输入框和密码输入框即文本域标签
    只读属性
        readonly属性  设置表单内容只可以查看不可以修改
            适用于input类型中的文本输入框，密码输入框及文本域标签
    不可见属性
        disabled属性  设置当前表单内容不会提交给服务器（服务器不可见）
        注意：设置disabled表单不会被提交，当前表单内容不可以修改，并且背景变为灰色，
    选中属性
        checked属性  设置表单中默认选中的选项
            适用于input标签的单选和复选表单。
        selected属性  设置表单中的默认选中选项
            适用于select下拉列表或者多选列表标签
#### 表单中的其他内容
    lable标签  为input表单添加标注，可以绑定文字和选项
        格式1：
        <label for="id名称">标注内容</label>
        <input type="radio" name="sex" id="id名称" value="" />
        
        格式2：
        <label for="id名称">
            <input type="radio" name="sex" id="id名称" value=""/>标注内容
        </label>
    案例v19
    
    fieldset标签  为表单定义可见范围边框，同时可以配合legend添加标题
        格式：
            <form>
                <fieldset>
                    <legend>表单名称</legend>
                    
                    表单内容部分
                </fieldset>
            </form>
        案例v18
        
### 框架和框架集
    框架和框架集合
    在当前页面中插入其他页面
    框架：在当前页面中引入一部分其它页面的内容来使用
    
    iframe标签  框架标签
        在用户的页面中引入部分其他页面
        
        src属性  用于设置引入的地址
        scrolling属性  设置是否允许出现滚动条
            auto自动  no没有 yes有
            
        width属性  设置引入页面的宽度
        height属性  设置引入页面的高度
        
        frameborder属性  设置是否有边框
            0 没有  1 有 
    案例v21
    
    单纯由其他页面组成的页面
    框架集：当前页面完全由其他页面组成，当前页面没有自己的内容
    frameset标签  框架集合标签
     
        在一个页面中包含多个页面从而组成一个框架集合页面
        cols属性  纵向切割页面属性，值为多个数值组成，使用逗号分隔
            cols="40%,60%"  纵向切割  左侧40%  右侧60%
        rows属性  横向切割页面属性，值为多个数值组成，使用逗号分隔
            rows="20%,80%:  横向切割  顶部20%  右侧80%
        frameborder属性  设置框架集合是否使用边框 (开关)
            1  使用边框   （默认值）
            0  不使用边框
            
        border属性  设置框架集合边框的粗细
            值为像素长度值，不需要单位
            注意：在frameborder=1的情况下才会设置border属性
            
    frame标签  引入框架页面标签
      在框架集合页面用于引入其他页面使用
      src属性  设置引入页面的地址
      noresize属性  禁止拖动页面属性
      
      scrolling属性  设置是否允许出现滚动条
        auto值  自动检测  如果内容超出高度就出现滚动条，如果不高就不出现
        no值  一直都没有滚动条
        yes值  一直都有滚动条，但是不一定有滑块（低版本浏览器中有效）
      注意：在框架集合党中，不允许出现任何body标签或者body标签中的内容
- 案例v20，bottom.html, top.html, left.html, right.html

#### head头中的主要标签
    title标签
        用于定义当前页面的标题，会在浏览器的标签栏中显示
        注意：title对网站的SEO优化有一定的影响
        首页：一般设置为网站名称即可
            
            <title>网易</title>
            <title>京东-你值得拥有</title>
            
        内容页：当前页面的主要标题 视频名称 网站名称
            
            <title>习近平访美 国内新闻 网易新闻 网易</title>
            
        屏道列表页：当前频道名称 网站名称
            
            <title>网易酒香 网易</title>
            
        注意：title中可以出现当前网站的关键字，但是不要太多不要重复，尽量精简
        
    meta标签
        浏览器信息设置标签，用于设置浏览器行为或者为搜索引擎设置信息
        
        为浏览器进行设置：
        1.设置浏览器的声明字符集
        
        <meta http-equiv="content-type" content="text/html;charset=utf-8" />
        
        2.设置浏览器的刷新和跳转方式
        
        <meta http-equiv="refresh" content="时间";url="地址" />
        
        为搜索引擎进行的信息设置
        
        1.设置关键字
        <meta name="keywords" content="关键字。。。" />
        
        注意：关键字之间必须使用英文逗号分隔，关键字总字数尽量保持在60-80个字之间
        
        2.设置网站描述信息
        <meta name="description" content="当前网站的描述，要使用通顺的语言！" />
        注意：描述内容写人话，字数尽量保证在140个以内，80个左右比较好。
        
        其他的设置：（相对来说不那么重要的）
        3.设置网站作者
        <meta name="author" content="作者名称" />
        4.设置开发工具
        <meta name="generator" content="作者，时间" />
        
    base标签
        基本链接标签
        href属性  设置基准链接属性
        注意：为页面中所有的相对链接添加href属性，组成一个新的绝对路径，对绝对路径无效
        target属性  设置链接的基本的打开方式
        注意：为页面中所有没有设置打开方式的链接，添加打开方式，主要设置了打开方式，就不会受到该属性的影响
        
    link标签
        用于在页面中引入css文件标签
        href属性  设置引入的css文件地址
        type属性  设置引入文件的MIME类型，MIME是浏览器区分文件的标示，类似于文件后缀
        rel属性  设置引入文件和当前页面之间的关系，stylesheet 样式表单
        注意：rel属性和src属性天生冲突不可以共存，所以link采用href来引入文件地址
        
        其他作用：
        设置网站标示
        <link rel="icon" href="./favicon.ico" type="image/x-icon" />
    案例v22，link.css
#### 实体字符
    什么是实体字符？
    为了将html中预先使用保留的字符在页面中显示，只能使用特殊的字符组和来进行操作，这些特殊的字符组和就是实体字符
    
    必须记忆的实体字符：
    
    空格：   &nbsp;
    <  :     &lt;
    >  :     &gt;
    ©  :     &copy;
    &  :     &amp;
- 案例v23
### XHTML规范
    1.所有标签名属性名必须使用小写字母
    2.所有标签必须闭合，单标签自封闭
    3.所有属性必须有值，单属性值为属性名，disabled="disabled"
    4.所有属性值必须使用双引号
    5.所有标签必须合理嵌套
    6.所有特殊字符必须使用实体字符表示
    7.所有img标签必须添加alt属性
    8.所有注释内容中不允许出现-等信息，如果需要使用-，可以使用=代替
    
### 关于颜色的表示方式
    1.使用颜色英文单词
        red  红色， green  绿色， blue  蓝色， orange 橙色， cyan 青色， purple 紫色。。。
    2.RGB颜色表示模式（RGB仅IE支持）
        格式：RGB（红色值，绿色值，蓝色值）
        所有颜色的取值都是从0-255,0表示没有当前颜色  255表示全色
    3.HEX模式/16进制模式
        格式：#红色值绿色值蓝色值
        所有颜色的取值必须从00-ff
        
### 进制的转换规则
    总数=位数*进制的N次方累加而得
    N次方  从右向左数  0次方  1次方  2次方  3次方。。。

### SEO概念
    SEO  Search Engine Optimization   搜索引擎优化
    针对于搜索引擎的喜好和自己网站的特征进行代码或者环境的调整 
        
    SEM Search Engine Marketing  搜索引擎营销
    使用付费的方式使得自己的网站在搜索引擎中排名靠前
    
### 关于长度单位
    px像素   相对单位
    设备具有物理像素：组成屏幕的每一个颜色点。（液晶屏幕的每一个小格子）
    设备像素：有系统的设置决定
    
    相对单位：具体长度由设备或者设置决定的长度，可以随设置或者设备的改变大小
    绝对单位：具体长度是固定设置不会改变
    
### 关于字符集设置
    gb2312  国标2312标准字符集
        能够表示5000个常用汉字
    gbk    国标扩展字符集
        能够表示15000个汉字，所有汉子都可以表示
    utf-8  国标字节字符集
        能够表示绝大多数语言，包括亚洲的多字节语言，日语，韩语，汉语，俄语。。。
    utf-8和gb2312及gbk的区别：
        gb2312和gbk中存储一个汉字需要2个字节
        utf-8存储一个汉字需要三个字节大小
    为了保证页面代码文字正确显示，需要设置页面字符集和声明字符集一致
        

        
        
       
       
        
          
        
        
    
 
 
 
 
 
 
 
 
 
                
               
            
          
          
































                 