def get_ch_value(num):
    if len(num.split('.')) > 2:
        return '请输入正确的阿拉伯数字'
    num = int(num)
    _MAPPING = (u'零', u'壹', u'贰', u'叁', u'肆', u'伍', u'陆', u'柒', u'捌', u'玖',)
    _P0 = (u'', u'拾', u'佰', u'仟', u'万')
    _S4 = 999999999999
    if num < 0 or num >= _S4:
        return '最大%d' % _S4
    if num < 10:
        raw = _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num // 10
        lst.append(num)
        c = len(lst)  # 位数
        result = u''
        for idx, val in enumerate(lst):
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
            if idx < c - 1 and lst[idx + 1] == 0:
                result += u'零'
        result = result[::-1]
        if result[:2] == u"壹拾":
            result = result[1:]
        if result[-1:] == u"零":
            result = result[:-1]
        raw = result
    return raw + u'圆整'
