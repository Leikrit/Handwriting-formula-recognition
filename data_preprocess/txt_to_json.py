import os
from pandas.io import json
from tqdm import tqdm

def txtToJson(path):
    filename = path + "cn_vocab.txt" #获取path路径下的所有文件的名字(eg:123.txt)
    # filename=filename[:2]
    # print(len(filename),filename)
    filejson=dict()
    # for fn in tqdm(filename):
    #     p=os.path.join(path,fn)
    try:
        # 大多数文件都是utf-8格式的，少数文件是gbk格式，默认使用utf-8格式读取，为了防止gbk文件使程序中断,使用try catch处理特殊情况
        f=open(filename,mode="r",encoding="utf-8")
        data=f.read().replace(" ","").replace("\n","")
        # filejson[fn.rstrip(".txt")] = data
        f.close()
    except Exception:
        f = open(filename, mode="r", encoding="gbk")
        data=f.read().replace(" ","").replace("\n","")
        # filejson[fn]=data
        f.close()
    return data#, filejson,len(filejson)

def saveInJsonFile(dd,path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(dd, ensure_ascii=False))

# 要读取的文件夹路径
readpath=r"C:\Users\65344\Desktop\dataset1_after_fmm/"
d=txtToJson(readpath)
# print(filejson)
# print(type(filejson))
j = dict()
index = 0
for i in range(len(d)):
    j[d[i]] = i + 413

print(type(j))
# 保存的文件路径 1.json可以更换成其他的名字
save_path = r"C:\Users\65344\PycharmProjects\image-to-latex-main\dataset1\cn_vocab.json"
saveInJsonFile(j,save_path)

# if __name__ == "__main__":
#     txtToJson("C:/Users/65344/PycharmProjects/image-to-latex-main/image_to_latex/data/cun")
