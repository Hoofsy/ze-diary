# 自动统计 ze-diary/白给记录/ 下的白给次数
import re
import os

# 定义日期文件所在的路径（关键！匹配你的文件夹结构）
diary_path = "白给记录/"

# 定义要匹配的日期文件格式（比如 2026-01-04.md）
date_file_pattern = r"\d{4}-\d{2}-\d{2}\.md"

# 初始化总白给次数
total_fail = 0

# 检查路径是否存在，避免报错
if os.path.exists(diary_path):
    # 遍历 ze-diary/白给记录/ 下的所有文件
    for filename in os.listdir(diary_path):
        # 只处理 YYYY-MM-DD.md 格式的文件
        if re.match(date_file_pattern, filename):
            # 拼接完整文件路径（比如 ze-diary/白给记录/2026-01-19.md）
            file_full_path = os.path.join(diary_path, filename)
            
            # 读取文件内容（兼容中文编码）
            try:
                with open(file_full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except:
                with open(file_full_path, "r", encoding="gbk") as f:
                    content = f.read()
            
            # 匹配文件里的「白给次数：X次」格式（可自定义）
            # 只要你的 md 文件里写了「白给次数：3次」，就会被识别
            fail_counts = re.findall(r"白给次数[:：]\s*(\d+)", content)
            if fail_counts:
                total_fail += sum(int(num) for num in fail_counts)

# 读取 README.md 并更新总次数徽章
try:
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()
except:
    with open("README.md", "r", encoding="gbk") as f:
        readme_content = f.read()

# 替换徽章里的数字（匹配「总白给次数-X次」格式）
text_pattern = r"\*\*总白给次数\*\*：\d+次"
new_text = f"**总白给次数**：{total_fail}次"
new_readme = re.sub(text_pattern, new_text, readme_content)

# 保存更新后的 README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_readme)

# 打印结果，方便查看日志
print(f"✅ 统计完成！ze-diary/白给记录/ 下总白给次数：{total_fail}")
