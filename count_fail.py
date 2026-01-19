import re
import os

# 只改这一行！确认你的文件夹名是「白给记录」，不是的话改这里
diary_path = "白给记录/"
total_fail = 0

# 统计所有日期文件里的白给次数
if os.path.exists(diary_path):
    for filename in os.listdir(diary_path):
        if re.match(r"\d{4}-\d{2}-\d{2}\.md", filename):
            file_path = os.path.join(diary_path, filename)
            # 兼容各种编码
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except:
                with open(file_path, "r", encoding="gbk") as f:
                    content = f.read()
            # 匹配「白给次数：X次」
            counts = re.findall(r"白给次数[:：]\s*(\d+)", content)
            total_fail += sum(int(num) for num in counts)

# 修改README里的徽章
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
except:
    with open("README.md", "r", encoding="gbk") as f:
        readme = f.read()

# 替换数字
new_readme = re.sub(
    r"https://img.shields.io/badge/总白给次数-\d+次-red.svg",
    f"https://img.shields.io/badge/总白给次数-{total_fail}次-red.svg",
    readme
)

# 保存README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

print(f"✅ 统计完成！总白给次数：{total_fail}")
