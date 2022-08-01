
def snake_to_camel(fname):
    '''将字段名转换为驼峰命名法，但是首字母要小写'''
    if '_' in fname:
        fname = ''.join(part[0].upper() + part[1:] for part in fname.split('_'))
        fname = fname[0].lower() + fname[1:]
    return fname

def title_first(st):
    '''首字母大写'''
    return st[0].upper() + st[1:]

def isEmpty(st):
    if st is None or len(st) == 0:
        return True
    return False

def isNotEmpty(st):
    if st and len(st) > 0:
        return True
    return False

# 是否为http(s)://开头
def ishttp(link:str):
    return link.startswith('http://') or link.startswith('https://')
