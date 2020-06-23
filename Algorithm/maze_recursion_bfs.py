import sys

sys.setrecursionlimit(10 ** 7)  # 再帰関数の呼び出し制限
h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
print(c)


def dfs(x, y):
    if not (0 <= x < h) or not (0 <= y < w) or c[x][y] == "#":  # 壁に当たったり、探索範囲外になった場合はreturn
        return
    if c[x][y] == "g":  # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()

    c[x][y] = "#"  # 探索済みを示すためのマーキング
    for i in range(h):  # スタート位置
        for j in range(w):
            print(c[i][j], end='')
        print()
    print()

    dfs(x, y + 1)  # これだとxが下方向、yが右方向
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x - 1, y)


sx, sy = 0, 0
for i in range(h):  # スタート位置
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j
            break

dfs(sx, sy)
print("No")
