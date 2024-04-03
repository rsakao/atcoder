# シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 a と b の積が偶数か奇数か判定してください。

# 入力
# 3 4

# 出力
# Even

a, b = map(int, input().split())
if a % 2 == 0 or b % 2 == 0:
    print("Even")
else:
    print("Odd")