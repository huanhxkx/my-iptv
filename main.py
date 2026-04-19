import requests
import re

def fetch_music_channels():
    # 我们从几个高质量的开源维护源中抓取音乐频道
    sources = [
        "https://githubusercontent.com", # 范明明源
        "https://githubusercontent.com"        # Gather-tv源
    ]
    
    music_list = []
    
    for url in sources:
        try:
            print(f"正在从 {url} 抓取...")
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    # 匹配包含“音乐”、“MTV”、“演唱会”或“Music”的行
                    if "#EXTINF" in lines[i] and any(keyword in lines[i] for keyword in ["音乐", "MTV", "Music", "演唱会", "经典歌"]):
                        channel_info = lines[i]
                        channel_url = lines[i+1]
                        if channel_url.startswith("http"):
                            music_list.append((channel_info, channel_url))
        except Exception as e:
            print(f"抓取失败: {e}")

    # 去重处理
    unique_channels = list(set(music_list))
    return unique_channels

def save_to_m3u(channels):
    # 注意：这里我们统一使用英文名 playlist.m3u 确保 APTV 订阅成功
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for info, url in channels:
            f.write(f"{info}\n{url}\n")
    print(f"成功！已抓取 {len(channels)} 个音乐频道。")

if __name__ == "__main__":
    channels = fetch_music_channels()
    save_to_m3u(channels)
