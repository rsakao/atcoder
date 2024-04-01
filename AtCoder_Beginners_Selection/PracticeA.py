# 整数 a,b,cと、文字列 s が与えられます。 a+b+c の計算結果と、文字列 s を並べて表示しなさい。

# input
# 1
# 2 3
# test

# output
# 6 test

a = int(input())
b, c =  map(int, input().split())
s = input()
print(f"{a+b+c} {s}")
