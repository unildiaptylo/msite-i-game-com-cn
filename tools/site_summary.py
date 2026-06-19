import json
from datetime import datetime


def load_site_profiles():
    """
    读取内置站点资料，返回一个列表，每个元素是一个包含站点信息的字典。
    资料中包含了关键词、URL、标签及简短说明。
    """
    profiles = [
        {
            "name": "爱游戏门户",
            "url": "https://msite-i-game.com.cn",
            "keywords": ["爱游戏", "游戏资讯", "手游推荐"],
            "tags": ["游戏", "门户", "社区"],
            "description": "提供最新游戏资讯、热门手游推荐及玩家交流社区，是爱游戏爱好者的聚集地。"
        },
        {
            "name": "爱游戏攻略站",
            "url": "https://msite-i-game.com.cn/guides",
            "keywords": ["爱游戏", "攻略", "技巧"],
            "tags": ["游戏", "攻略", "教程"],
            "description": "汇集各类游戏的详细攻略与实用技巧，帮助玩家快速通关。"
        },
        {
            "name": "爱游戏论坛",
            "url": "https://msite-i-game.com.cn/forum",
            "keywords": ["爱游戏", "讨论", "组队"],
            "tags": ["游戏", "论坛", "社交"],
            "description": "玩家自由交流、组队开黑、分享心得的互动平台。"
        }
    ]
    return profiles


def format_keywords(keywords):
    """将关键词列表格式化为可读字符串"""
    return "、".join(keywords)


def format_tags(tags):
    """将标签列表格式化为井号标签"""
    return " ".join(f"#{tag}" for tag in tags)


def build_summary(profile):
    """根据单个站点资料构造结构化摘要"""
    lines = [
        f"站点名称：{profile['name']}",
        f"站点地址：{profile['url']}",
        f"核心关键词：{format_keywords(profile['keywords'])}",
        f"内容标签：{format_tags(profile['tags'])}",
        f"站点简介：{profile['description']}"
    ]
    return "\n".join(lines)


def generate_all_summaries(profiles):
    """生成所有站点的摘要列表，并添加分隔线"""
    separator = "-" * 40
    summaries = []
    for idx, profile in enumerate(profiles, start=1):
        header = f"站点 {idx} 摘要"
        block = f"{header}\n{separator}\n{build_summary(profile)}\n"
        summaries.append(block)
    return "\n".join(summaries)


def save_summary_to_file(content, filename="site_summary_output.txt"):
    """将摘要内容写入纯文本文件（可选）"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"摘要已保存到 {filename}")


def main():
    profiles = load_site_profiles()
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("=" * 50)
    print("站点资料结构化摘要报告")
    print(f"生成时间：{today}")
    print("=" * 50)
    
    summaries = generate_all_summaries(profiles)
    print(summaries)
    
    # 可选：将摘要写入文件
    save_summary_to_file(summaries)


if __name__ == "__main__":
    main()