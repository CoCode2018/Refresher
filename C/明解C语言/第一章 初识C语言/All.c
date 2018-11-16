/*
    第一章　初识C语言

    1-1 显示
        1.正确的训练方式 + 大量的训练
        2.通过字符序列创建出的程序称为源程序(source program)
        　用来保存源程序的文件称为源文件(soucre file)
        3.源程序需要转化为计算机能读懂的二进制位序列才能够执行，
        　这里的转化可以称为翻译(translation phase)也就是预处理、编译、链接、运行等步骤(理论上有8个阶段)
        4.源程序在翻译过程中如果遇到错误会停止并显示诊断信息(dignostic message)
        5.C语言的注释(comment)有两种
            块注释
            行注释   
        6.格式化输出函数printf()
            函数调用(function call)
            实参(argument):多个实参之间用‘，’隔开
                格式化字符串(format string):
                    使用    转换说明(conversion specification)和转义字符(escape sequence)，规定了一些格式。
            形参()
        7.C语言使用；表示一条语句
        8.字符串常量(string literal)
            使用双引号括起来的一连串连续排列的文字

    1-2 变量
        1.为了记录计算过程中的结果以及最终结果需要使用变量(variable)，是根据类型生成的实体
        2.常量(constant)
        3.C语言中变量需要先声明(通过声明明确类型和名称)再使用
            声明方式:   类型　变量名1, 变量名2;
        4.变量的特点
            存放固定类型的数据
            任何时候都可以通过变量名取值或存值
            尽量在声明变量时进行初始化(initialize)存入初始值(initializer)
            声明时如果没有初始化会被存入垃圾值，静态存储期的变量会被存入0
            初始化和先声明再赋值的区别在与存入数据的时间不同
                初始化:　在变量生成的时候放入数值
                赋值　:　在已生成的变量中放入数值
    1-3 输入和显示
        格式化输入函数scanf(): 从键盘读取指定类型的数值存入指定的变量中
            函数调用(function call)
                实参(argument):
                    转换说明: 
        输出函数puts("xxx"): == printf("xxx\n")

    总结：


implicit
    adj.不言明[含蓄]的;无疑问的，绝对的;成为一部份的;内含的
conversion
    n.变换，转变;改装物;财产转换，兑换;[逻] 换位（法）
generated
    adj.发电的
    v.生成;引起;生（儿、女）( generate的过去式和过去分词 );（通过物理或化学过程）发生
specifies
    v.指定( specify的第三人称单数 );详述;提出…的条件;使具有特性
specifier
    区分符，分类符，说明符
declaration
    n.宣言，布告，公告，声明;（纳税品在海关的）申报;[法]（原告的）申诉，（证人的）陈述，口供;[牌]摊牌，叫牌
*/
