"""
logging模块将日志打印到屏幕上(stdout)，
日志级别为WARNING(即只有日志级别高于WARNING的日志信息才会输出)
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
    1.DEBUG:详细信息，典型地调试问题时会感兴趣。
    2.INFO:证明事情按预期工作。
    3.WARNING:表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。
    4.ERROR:由于更严重的问题，软件已不能执行一些功能了。
    5.CRITICAL:严重错误，表明软件已不能继续运行了。
"""

"""
2、部分名词解释
Logging.Formatter：这个类配置了日志的格式，在里面自定义设置日期和时间，输出日志的时候将会按照设置的格式显示内容。
Logging.Logger：Logger是Logging模块的主体，进行以下三项工作：
1. 为程序提供记录日志的接口
2. 判断日志所处级别，并判断是否要过滤
3. 根据其日志级别将该条日志分发给不同handler
常用函数有：
Logger.setLevel() 设置日志级别
Logger.addHandler() 和 Logger.removeHandler() 添加和删除一个Handler
Logger.addFilter() 添加一个Filter,过滤作用
Logging.Handler：Handler基于日志级别对日志进行分发，如设置为WARNING级别的Handler只会处理WARNING及以上级别的日志。
常用函数有：
setLevel() 设置级别
setFormatter() 设置Formatter
"""
import logging
s1 = str(10)

# 通过下面的方式进行简单配置输出方式与日志级别
# basicConfig来设置日志级别
logging.basicConfig(filename="log.log", filemode="a")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info("info....")
logging.debug("debug....")
logging.error("error....")
logging.warning("warning.....")
