# 调试版：自动统计白给次数（带详细日志）
import re
import os

# 定义日期文件所在路径
diary_path = "白给记录/"
print(f"🔍 开始统计，目标路径：{diary_path}")

# 检查路径是否存在
if not os.path.exists(diary_path):
    print(f"❌ 错误：路径 {diary_path} 不存在！")
else:
    print(f"✅ 路径存在，开始遍历文件...")

# 初始化总次数
total_fail = 0
# 记录找到的文件和次数
found_files = []
found_counts = []

# 遍历目标路径下的文件
if os.path.exists(diary_path):
    for filename in os.listdir(diary_path):
        # 只匹配 YYYY-MM-DD.md 格式的文件
        if re.match(r"\d{4}-\d{2}-\d{2}\.md", filename):
            found_files.append(filename)
            file_full_path = os.path.join(diary_path, filename)
            print(f"📄 找到日期文件：{file_full_path}")
            
            # 读取文件内容
            try:
                with open(file_full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                print(f"✅ 成功读取 {filename}（utf-8 编码）")
            except:
                with open(file_full_path, "r", encoding="gbk") as f:
                    content = f.read()
                print(f"✅ 成功读取 {filename}（gbk 编码）")
            
            # 匹配「白给次数：X次」标记
            fail_counts = re.findall(r"白给次数[:：]\s*(\d+)", content)
            print(f"🔢 {filename} 中找到的次数标记：{fail_counts}")
            
            if fail_counts:
                file_total = sum(int(num) for num in fail_counts)
                found_counts.append(file_total)
                total_fail += file_total

# 打印核心统计结果（关键！看这里）
print(f"\n📊 统计汇总：")
print(f"- 找到的日期文件：{found_files}")
print(f"- 各文件次数：{found_counts}")
print(f"- 总白给次数：{total_fail}")

# 替换 README 里的徽章
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
    print(f"✅ 成功读取 README.md")
except:
    with open("README.md", "r", encoding="gbk") as f:
        readme_content = f.read()
    print(f"✅ 成功读取 README.md（gbk 编码）")

# 替换徽章数字
badge_pattern = r"https://img.shields.io/badge/总白给次数-\d+次-red.svg"
new_badge = f"https://img.shields.io/badge/总白给次数-{total_fail}次-red.svg"
new_readme = re.sub(badge_pattern, new_badge, readme_content)

# 保存 README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)
print(f"✅ 已替换 README 徽章，新徽章链接：{new_badge}")
