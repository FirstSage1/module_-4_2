# ДЗ модуль 4_2 Пространство имен.
# ===================================
def test_function(txt_):
    def inner_function(txt_):
        #nonlocal txt_
        txt_ = "Я в области видимости функции test_function"
        print(txt_)
        return txt_

    result = inner_function("test")
    print(result)
#result = inner_function("test")
#print(result)
