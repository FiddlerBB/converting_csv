import re
import numpy as np

TCVN3TAB = "µ¸¶·¹¨»¾¼½Æ©ÇÊÈÉË®ÌÐÎÏÑªÒÕÓÔÖ×ÝØÜÞßãáâä«åèæçé¬êíëìîïóñòô-õøö÷ùúýûüþ¡¢§£¤¥¦"  # NOQA
TCVN3TAB = [ch for ch in TCVN3TAB]

UNICODETAB = "àáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵĂÂĐÊÔƠƯ"   # NOQA
UNICODETAB = [ch for ch in UNICODETAB]

r = re.compile("|".join(TCVN3TAB))

replaces_dict = dict(zip(TCVN3TAB, UNICODETAB))


def TCVN3_to_unicode(tcvn3str):
    return r.sub(lambda m: replaces_dict[m.group(0)], tcvn3str)


def unicode_to_TCVN3(unicodestr):
    return r.sub(lambda m: replaces_dict[m.group(0)], unicodestr)

def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'a', s)
    s = re.sub(r'[èéẹẻẽêềếệểễÈÉẸẺẼÊỀẾỆỂỄ]', 'e', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'o', s)
    s = re.sub(r'[ìíịỉĩÌÍỊỈĨ]', 'i', s)
    s = re.sub(r'[ùúụủũưừứựửữƯỪỨỰỬỮÙÚỤỦŨ]', 'u', s)
    s = re.sub(r'[ỳýỵỷỹỲÝỴỶỸ]', 'y', s)
    s = re.sub(r'[đĐ]', 'd', s)
    return s

def return_keyword(column, key_words):
    for i in key_words:
        if i in column:
            return i
    return ''