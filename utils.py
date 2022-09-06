from deep_translator import GoogleTranslator
import io
import re

def translate(to_translate,source,target):
    # to_translate = 'I want to translate this text'
    # translated = GoogleTranslator(source='auto', target='de').translate(to_translate)
    translated = GoogleTranslator(source=source, target=target).translate(to_translate)
    # print('translated',translated)
    return translated
    

def write_file(file_name,ndung):
    f = io.open(file_name, "w", encoding="utf-8")
    f.write(ndung)
    f.close()


def read_file(file_name):
    f = io.open(file_name, "r", encoding="utf-8")
    ndung = f.read()
    f.close()
    return ndung

def regex_one_value(pattern, input_str):
    regex1 = re.compile(pattern)
    kq = regex1.search(input_str)
    if kq:
        kq = kq.group(1)
    else:
        kq = ""
    return kq

def regex_many_value(pattern, input_str):
    regex1 = re.compile(pattern)
    kq = regex1.findall(input_str)
    return kq