# 1
```sh
yukinishii@NM0020noAir10(14:40:05) ~/Numerical_analysis/11
% python3 prob.py
forward diff
    df/dx :4.200000000000004
    diff  :0.20000000000000373
backward diff
    df/dx :3.799999999999999
    diff  :0.20000000000000107
central diff
    df/dx :4.000000000000001
    diff  :8.881784197001252e-16
```
# 2
## Deriving the formula
![formula](equation2.svg)
## Output
```sh
yukinishii@NM0020noAir10(15:34:53) ~/Numerical_analysis/11
% python3 prob2.py
ddf/ddx :1.999999999999957
diff    :4.3076653355456074e-14
```
# 3
## Deriving the formula
![formula](equation3-1.svg)

よって講義内で説明された2次精度の微分公式をまとめると以下のようになる.

![formula](equation3-2.svg)
## Output
```sh
yukinishii@NM0020noAir10(17:37:51) ~/Numerical_analysis/11
% python3 prob3.py
   x   |   y   |   dy/dx   
---------------------------
  1.0  |  1.0  |0.24149999999999983
---------------------------
  2.0  | 2.718 |  3.1945   
---------------------------
  3.0  | 7.389 |   8.681   
---------------------------
  4.0  | 20.08 |  23.6005  
---------------------------
  5.0  | 54.59 |45.419500000000006
---------------------------
```