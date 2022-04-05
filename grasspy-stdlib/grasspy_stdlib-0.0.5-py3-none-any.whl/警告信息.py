"""警告子系统的 Python 部分."""

从 warnings 导入 *


__all__ = ["警告", "警告_明确", "显示警告",
           "格式化警告", "过滤警告", "简易过滤器",
           "重置警告", "捕捉警告"]

套路 警告(消息, 类别=空, 栈级别=1, 来源=空):
    '''发出警告，可以忽略它或抛出异常。'''
    warn(消息, category=类别, stacklevel=栈级别, source=来源)

套路 警告_明确(消息, 类别, 文件名, 行号,
                  模块=空, 注册表=空, 模块全局字典=空,
                  来源=空):
    warn_explicit(消息, 类别, 文件名, 行号,
                  module=模块, registry=注册表, module_globals=模块全局字典,
                  source=来源)

套路 显示警告(消息, 类别, 文件名, 行号, 文件=空, 行=空):
    '''将警告写入文件的钩子; 如需要可替换.'''
    showwarning(消息, 类别, 文件名, 行号, file=文件, line=行)

套路 格式化警告(消息, 类别, 文件名, 行号, 行=空):
    '''以标准方式格式化警告的函数.'''
    返回 formatwarning(消息, 类别, 文件名, 行号, line=行)

_操作字典 = {
    '错误': 'error',
    '忽略': 'ignore',
    '始终': 'always',
    '默认': 'default',
    '模块': 'module',
    '一次': 'once'
}

套路 过滤警告(操作, 消息='', 类别=爻警告, 模块='', 行号=0, 追加=假):
    """在警告过滤器列表前方插入一条.

    '操作' -- '错误'、'忽略'、'始终'、'默认'、'模块' 或 '一次

    '消息' -- 警告消息必须匹配的正则表达式

    '类别' -- 警告所属的类

    '模块' -- 模块名称必须匹配的正则表达式

    '行号' -- 整数行号, 0 匹配全部警告

    '追加' -- 如果为真, 则追加到过滤器列表
    """
    action = _操作字典.获取(操作, 操作)
    断言 action 在 ("error", "ignore", "always", "default", "module",
                    "once"), "无效操作: %r" % (操作,)
    filterwarnings(action, message=消息, category=类别, module=模块, 
            lineno=行号, append=追加)

套路 简易过滤器(操作, 类别=爻警告, 行号=0, 追加=假):
    """在警告过滤器列表前方插入一个简易条目. 简易过滤器匹配所有模块和消息.

    '操作' -- '错误'、'忽略'、'始终'、'默认'、'模块' 或 '一次

    '类别' -- 警告所属的类

    '行号' -- 整数行号, 0 匹配全部警告

    '追加' -- 如果为真, 则追加到过滤器列表
    """
    action = _操作字典.获取(操作, 操作)
    断言 action 在 ("error", "ignore", "always", "default", "module",
                    "once"), "无效操作: %r" % (操作,)
    simplefilter(action, category=类别, lineno=行号, append=追加)

套路 重置警告():
    """清除警告过滤器列表, 使得没有活动过滤器."""
    resetwarnings()

类 捕捉警告(catch_warnings):
    """一个上下文管理器, 退出上下文时复制并恢复警告过滤器.

    '记录' 参数...
    """
    无操作 # 待完善