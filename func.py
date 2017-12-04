def dict_kv(keys,vals):
    res={}.fromkeys(keys)# функция fromkeys(keys) создает словарь с ключами keys и заполняет их значения None
    i=0 #индекс keys
    for key in keys:
        if i<len(vals):
            res[key]=vals[i]# присваивает ключу key в словаре res значение vals, соответсвующее индексу ключа
            i+=1    
    return res
