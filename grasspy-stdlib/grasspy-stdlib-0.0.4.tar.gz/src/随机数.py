"""随机数生成器

    整数
    --------
            一定范围内的均匀分布

    序列
    --------
            选择随机元素
            选择随机样本
            选择加权随机样本
            生成随机排列

    实数轴上的分布
    ------------------------------
            均匀分布
            三角分布
            正态分布 (高斯分布)
            对数正态分布
            负指数分布
            伽玛分布
            贝塔分布
            帕累托分布
            韦伯分布

    圆上分布 (角度在 0 到 2*pi 之间)
    ---------------------------------------------
            循环均匀分布
            冯·米塞斯分布
"""

导入 random

__all__ = ["〇随机数","种子","随机数","均匀分布","随机整数","单选","取样",
           "随机范围数","打乱","正态分布","对数正态分布",
           "指数分布","圆上正态分布","伽马分布","三角分布",
           "高斯分布","贝塔分布","帕累托分布","韦伯分布",
           "取状态","设状态", "k比特整数", "选k次",
           "〇系统随机数"]

类 〇随机数(random.Random):
    """绑定的模块函数使用的随机数发生器.
    """
    套路 种子(分身, a=空, 版本=2):
        """从可散列对象初始化内部状态.
        无参数或参数为空时, 种子为当前时间或操作系统特点的随机源.
        """
        分身.seed(a, 版本)
    
    套路 随机数(分身):
        """获取 [0, 1.0) 范围内的下一个随机数."""
        返回 分身.random()
    
    套路 取状态(分身):
        """返回内部状态; 稍后可传递给 <设状态()>."""
        返回 分身.getstate()

    套路 设状态(分身):
        """根据 <取状态()> 返回的对象恢复内部状态."""
        分身.setstate()

## -------------------- 整数方法  -------------------

    套路 随机范围数(分身, 起, 止=空, 步长=1, _整数=int):
        """从 <范围(起, 止[, 步长])> 中随机选择一个元素.
        注意: 不包括最后一个元素.
        """
        返回 分身.randrange(起, 止, 步长, _整数)

    套路 随机整数(分身, a, b):
        """返回 [a, b] 闭区间内的随机整数, 包括两个端点.
        """
        返回 分身.randint(a, b)
    
    套路 k比特整数(分身, k):
        """生成一个有 k 个随机比特的整数."""
        返回 分身.getrandbits(k)

## -------------------- 序列方法  -------------------

    套路 单选(分身, 序列):
        """从一个非空序列中随机选择一个元素."""
        返回 分身.choice(序列)

    套路 打乱(分身, x, 随机数=空):
        """原位打乱列表 x, 返回空."""
        分身.shuffle(x, 随机数)

    套路 取样(分身, 群组, k):
        """从一个序列或集合中随机选取 k 个唯一元素.
        返回一个新列表, 原群组不变.
        """
        返回 分身.sample(群组, k)
    
    套路 选k次(分身, 群组, 权重=空, *, 累计权重=空, k=1):
        """从一个群组中随机选 k 次 (每次从中选择的群组是相同的).
        返回一个含 k 个元素的列表, 元素可能有重复.
        """
        返回 分身.choices(群组, 权重, cum_weights=累计权重, k=k)   # * 号之后是关键字参数

## -------------------- 实值分布  -------------------

    套路 均匀分布(分身, a, b):
        """获取 [a, b) 或 [a, b] 范围内 (取决于舍入情况) 的一个随机数."""
        返回 分身.uniform(a, b)

    套路 三角分布(分身, 低=0.0, 高=1.0, 模式=空):
        """三角分布."""
        返回 分身.triangular(低, 高, 模式)

    套路 正态分布(分身, mu, sigma):
        """正态分布."""
        返回 分身.normalvariate(mu, sigma)

    套路 对数正态分布(分身, mu, sigma):
        """对数正态分布."""
        返回 分身.lognormvariate(mu, sigma)

    套路 指数分布(分身, lambd):
        """指数分布."""
        返回 分身.expovariate(lambd)

    套路 圆上正态分布(分身, mu, kappa):
        """冯·米塞斯分布."""
        返回 分身.vonmisesvariate(mu, kappa)

    套路 伽马分布(分身, alpha, beta):
        """伽马分布."""
        返回 分身.gammavariate(alpha, beta)

    套路 高斯分布(分身, mu, sigma):
        """高斯分布."""
        返回 分身.gauss(mu, sigma)

    套路 贝塔分布(分身, alpha, beta):
        """贝塔分布."""
        返回 分身.betavariate(alpha, beta)

    套路 帕累托分布(分身, alpha):
        """帕累托分布."""
        返回 分身.paretovariate(alpha)

    套路 韦伯分布(分身, alpha, beta):
        """韦伯分布."""
        返回 分身.weibullvariate(alpha, beta)

类 〇系统随机数(random.SystemRandom):
    """使用操作系统提供的随机源的备选随机数发生器."""
    
    套路 随机数(分身):
        """获取 [1.0, 1.0) 范围内的下一个随机数."""
        返回 分身.random()

    套路 k比特整数(分身, k):
        """生成一个有 k 个随机比特的整数."""
        返回 分身.getrandbits(k)

## 创建一个实例, 以当前时间为种子, 将其方法导出为模块级函数.

_实例 = 〇随机数()
种子 = _实例.种子
随机数 = _实例.随机数
均匀分布 = _实例.均匀分布
三角分布 = _实例.三角分布
随机整数 = _实例.随机整数
单选 = _实例.单选
随机范围数 = _实例.随机范围数
取样 = _实例.取样
打乱 = _实例.打乱
选k次 = _实例.选k次
正态分布 = _实例.正态分布
对数正态分布 = _实例.对数正态分布
指数分布 = _实例.指数分布
圆上正态分布 = _实例.圆上正态分布
伽马分布 = _实例.伽马分布
高斯分布 = _实例.高斯分布
贝塔分布 = _实例.贝塔分布
帕累托分布 = _实例.帕累托分布
韦伯分布 = _实例.韦伯分布
取状态 = _实例.取状态
设状态 = _实例.设状态
k比特整数 = _实例.k比特整数

