# 参照 Python 官网中文文档, pickling 和 unpickling 分别译作 封存 和 解封
"""创建 Python 对象的可移植序列化表示.

类:
    〇封存器
    〇解封器

函数:
    转储(对象, 文件)
    转储串(对象) -> 字符串
    加载(文件) -> 对象
    加载串(字符串) -> 对象
"""

从 pickle 导入 *

最高协议版本 = HIGHEST_PROTOCOL
默认协议版本 = DEFAULT_PROTOCOL

爻封存库错误 = PickleError
爻封存错误 = PicklingError
爻解封错误 = UnpicklingError

套路 转储(对象, 文件, 协议=空, *, 修复导入=真, 缓冲回调=空):
    """将 ``对象`` 封存以后的对象写入已打开的 文件 对象.
    等同于 ``〇封存器(文件, 协议).转储(对象)``.
    参数含义参见 ``〇封存器`` 的构造函数.
    """
    dump(对象, 文件, protocol=协议, fix_imports=修复导入, buffer_callback=缓冲回调)

套路 转储串(对象, 协议=空, *, 修复导入=真, 缓冲回调=空):
    """将 ``对象`` 封存以后的对象作为字节类型直接返回.
    参数含义参见 ``〇封存器`` 的构造函数.
    """
    返回 dumps(对象, protocol=协议, fix_imports=修复导入, buffer_callback=缓冲回调)

套路 加载(文件, *, 修复导入=真, 编码方式="ASCII", 错误处理="严格", 缓冲=空):
    """从打开的 文件 对象读取封存的对象并返回重构的对象.
    相当于 ``〇解封器(文件).加载()``.
    参数含义参见 ``〇解封器`` 的构造函数.
    """
    返回 load(文件, fix_imports=修复导入, encoding=编码方式,
         errors=错误处理, buffers=缓冲)

套路 加载串(字节对象, *, 修复导入=真, 编码方式="ASCII", 错误处理="严格", 缓冲=空):
    """基于对象的封存表示形式返回重构的对象.
    参数含义参见 ``〇解封器`` 的构造函数.
    """
    返回 loads(字节对象, fix_imports=修复导入, encoding=编码方式,
         errors=错误处理, buffers=缓冲)


类 〇封存器(Pickler):

    套路 __init__(分身, 文件, 协议=空, *, 修复导入=真, 缓冲回调=空):
        """接受一个二进制文件对象, 用于写入封存数据流.

        可选参数 *协议* 是一个整数, 告知 〇封存器 使用指定的协议. 可选范围从 0 到
        *最高协议版本*. 如果没有指定, 则使用 *默认协议版本*. 指定负数选择最高
        支持的协议版本.

        *文件* 参数须有 写入() 方法, 该方法接收字节作为其唯一参数. 因此, 它可以是
        一个以二进制写入方式打开的文件对象，或是一个 io.字节IO 实例, 或是满足此接口
        的任何其他自定义对象.

        如果 *修复导入* 为 真 且 协议 小于 3, 封存器将尝试将 Python 3 中的新名称
        映射到 Python 2 中的旧模块名称, 使得 Python 2 也可以读取封存的数据流.

        如果 *缓冲回调* 为 空(默认值), 缓冲区视图将会作为封存流的一部分被序列化到 文件 中.

        如果 *缓冲回调* 不为 空, 那它可以用缓冲区视图调用任意次. 如果某次调用返回了 假 值
        (例如 空), 则给定缓冲区是带外的, 否则缓冲区是带内的 (即位于封存流里面).

        如果 *缓冲回调* 不是 空 且 协议 是 空 或小于 5, 就会出错.
        """
        super().__init__(文件, 协议, fix_imports=修复导入, buffer_callback=缓冲回调)

    套路 清除备忘(分身):
        """清除封存器的'备忘录'.
        """
        分身.clear_memo()
    
    套路 转储(分身, 对象):
        "将 对象 封存以后的对象写入构造函数中指定的已打开 文件 对象."
        返回 分身.dump(对象)

    套路 持久id(分身, 对象):
        返回 分身.persistent_id(对象)

    @property
    套路 分派表(分身):
        返回 分身.dispatch_table

    套路 归并器重载(分身, 对象):
        返回 分身.reducer_override(对象)

    
类 〇解封器(Unpickler):

    套路 __init__(分身, 文件, *, 修复导入=真, 编码方式="ASCII", 错误处理="严格", 缓冲=空):
        """接受一个二进制文件对象, 用于读取封存的数据流.

        封存库协议版本是自动检测出来的, 所以不需要参数来指定协议.

        参数 *文件* 须有三个方法: 读取() 方法接受一个整数参数, 读入() 方法接受一个
        缓冲区作为参数, 读一行() 方法不需要参数. 这与 io.BufferedIOBase 里定义的
        接口是相同的, 因此 文件 可以是以二进制读取方式打开的文件对象, 或是一个
        io.字节IO 实例, 或是满足此接口的任何其他自定义对象.

        可选关键词参数是 *修复导入*, *编码方式* 和 *错误处理*, 用于控制由 Python 2 生成的
        封存流的兼容性. 如果 修复导入 为 真，解封器将尝试将旧的 Python 2 名称映射到
        Python 3 中对应的新名称.
        编码方式 和 错误处理 参数告诉解封器如何解码 Python 2 存储的 8 位字符串实例; 这两个
        参数的默认值分别为 'ASCII' 和 '严格'. 编码方式 参数可置为 'bytes' 来将这些 8 位
        字符串实例作为字节对象读取. 读取 NumPy array 和 Python 2 存储的 datetime,
        date 和 time 实例时，请使用 编码方式='latin1'.

        如果 *缓冲* 为 空(默认值), 则解封所需的所有数据都必须包含在封存流中. 这意味着
        在实例化封存器时 (或调用 转储() 或 转储串() 时), 参数 缓冲回调 为 空.

        如果 *缓冲* 不为 空, 则每次封存流引用带外缓冲区视图时, 消耗的对象都应该是可迭代
        地启用缓冲区的对象. 这样的缓冲区应该按顺序地提供给封存器对象的 缓冲回调 方法.
        """
        super().__init__(文件, fix_imports=修复导入, encoding=编码方式,
                         errors=错误处理, buffers=缓冲)

    套路 加载(分身):
        "从构造函数中指定的已打开 文件 对象读取封存的对象并返回重构的对象."
        返回 分身.load()

    套路 持久加载(分身, 持久id):
        返回 分身.persistent_load(持久id)

    套路 查找类或函数(分身, 模块, 名称):
        返回 分身.find_class(模块, 名称)



