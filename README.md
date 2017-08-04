# Data-Structures
This is a practice for Data Structures

## Sort

## String 

### Transform.py
     变形词判断            
                 对于两个字符串A和B,如果A和B中出现的字符种类相同且
                 每种字符出现的次数相同,则A和B互为变形词       

     方法:
          用字典统计个字符的个数
          A字典中的key B字典中没有 则false,有值但不等 也是false

### Rotation.py
    旋转词判断
                字符串A,将A的前面任意部分移动到后边形成的字符串为A的旋转词
                如A="1234",旋转词有 "1234","4321","3412","2341"

    方法:
         将A字符串相加组成大字符串C,此时C中拥有A所有旋转词的集合
         判断B是否未c中子串即可

## 
