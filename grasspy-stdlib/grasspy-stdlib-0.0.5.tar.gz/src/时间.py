"""
本模块提供各种操纵时间值的函数。

时间有两种标准表示法。一是时间戳表示，可能是一个整数或浮点数（表示秒的分数）。
“纪元”由系统定义；在 Unix 中，它一般指 1970 年 1 月 1 日。
实际开始时间可以通过调用 世界时元组(0) 或 本地时元组(0) 来获得。
另一种方法是用包含 9 个整数的元组来表示当地时间。元组各项如下：
  年 (例如 1998)
  月 (1-12)
  日 (1-31)
  时 (0-23)
  分 (0-59)
  秒 (0-59)
  周之日（一周中的第几天，0-6，星期一为 0，以此类推）
  年之日（一年中的第几天，1-366）
  是夏令时（-1、0 或 -1）
夏令时标志为 0 时，表示时间是在正常时区给出的；
夏令时标志为 1 时，表示时间是在夏令时时区给出的；
夏令时标志为-1 时，元组转秒() 应根据时间与日期来猜测。
"""

从 time 导入 *
从 time 导入 __doc__
从 collections 导入 namedtuple

时间元组 = namedtuple('时间元组', '年 月 日 时 分 秒 周之日 年之日 是夏令时')
# 时间元组.__new__.__defaults__ = (False, False, False, False, False, False, False, False, False, 0, 0)
套路 时间元组汉化(st) -> 时间元组:
    '''
    将 struct_time(tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                          tm_sec,tm_wday,tm_yday,tm_isdst)
    汉化为 时间元组(年, 月, 日, 时, 分, 秒, 周之日, 年之日, 是夏令时)\n
    周之日 即一周中的第几天, 周一为 0 \n
    年之日 即一年中的第几天
    '''
    年 = st.tm_year
    月 = st.tm_mon
    日 = st.tm_mday
    时 = st.tm_hour
    分 = st.tm_min
    秒 = st.tm_sec
    周之日 = st.tm_wday
    年之日 = st.tm_yday
    是夏令时 = st.tm_isdst
    返回 时间元组(年, 月, 日, 时, 分, 秒, 周之日, 年之日, 是夏令时)

