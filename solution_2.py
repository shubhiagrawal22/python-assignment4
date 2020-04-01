def nested(nestedDict,Dic,currentKey):
    for key in nestedDict.keys():
        if type(nestedDict[key])==int:
            Dic[(currentKey+"."+key).strip(".")]=nestedDict[Key]
        else:
            Dic = nested(nestedDic[key],Dic,(currentkey+"."+key).strip('.'))
    return Dic
def fun_dic(nestedDic):
    return nested(nestedDic,dict(),"")
def main():
    nestedDictionary = {
     "key":3
     "foo":{
     "a":5
     "bar":{
     "baz":8
         }
         }
        }
    dicten = func_dic(nestedDictionary)
    print(dicten)

if __name__=="__main__":
    main()
