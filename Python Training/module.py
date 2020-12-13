# # 載入內建的 sys 模組並取得資訊
# import sys as s # 僅別名方便
# print(s.platform)
# print(s.maxsize)
# # 建立 geometry 模組，載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# print(geometry.slope(1,2,5,6))
# # 調整搜尋模組的路徑
# # 印出模組的搜尋路徑
# print(s.path)

import sys

sys.path.append("modules")
print(sys.path)
import geometry
print(geometry.distance(1,1,5,5))