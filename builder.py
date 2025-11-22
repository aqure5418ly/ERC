import os

# 定义新的目录结构 (扁平化设计)
structure = {
    "Items": ["Bases", "Containers", "Gear", "Machines"],
    "Texts": [],
    "Images": ["Containers", "Icons"],  # 存放贴图
    "Sounds": []
}

def create_structure():
    base_path = os.getcwd()
    print(f"正在构建 ERC Mod 项目结构于: {base_path}")

    # 1. 创建文件夹
    for root, subs in structure.items():
        root_path = os.path.join(base_path, root)
        os.makedirs(root_path, exist_ok=True)
        print(f"+ 创建目录: {root}/")
        for sub in subs:
            os.makedirs(os.path.join(root_path, sub), exist_ok=True)
            print(f"  + 创建子目录: {root}/{sub}/")

    # 2. 创建说明文件
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("# Barotrauma ERC Logistics Mod\n\n欧罗巴捷运物流模组 - 开发库")

    print("\n✅ 项目骨架搭建完成！请将 XML 文件放入对应的文件夹中。")
    print("⚠️ 注意：请确保将 filelist.xml 放在根目录下。")

if __name__ == "__main__":
    create_structure()