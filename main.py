import requests

def fetch_channels():
    # 增加更多源，并添加 User-Agent 伪装成浏览器
    sources = [
        "https://githubusercontent.com",
        "https://githubusercontent.com",
        "https://live.fanmingming.com/tv/m3u/ipv6.m3u"
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # 关键词放宽，涵盖更多音乐和国际频道
    keywords = ["音乐", "MTV", "Music", "演唱会", "经典歌", "唱片", "Vevo", "Migu"]
    music_list = []
    
    for url in sources:
        try:
            print(f"尝试抓取源: {url}")
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code == 200:
                lines = r.text.split('\n')
                for i in range(len(lines)):
                    if "#EXTINF" in lines[i]:
                        # 只要包含任一关键词就记录
                        if any(k.lower() in lines[i].lower() for k in keywords):
                            if i + 1 < len(lines) and lines[i+1].startswith("http"):
                                music_list.append((lines[i], lines[i+1]))
        except Exception as e:
            print(f"连接源失败: {e}")

    # --- 保底方案：如果上面都抓不到，手动加入几个长期稳定的源 ---
    if not music_list:
        print("在线抓取未发现结果，启用保底列表")
        backup = [
            ('#EXTINF:-1 tvg-name="MTV China" group-title="Music",MTV China', 'http://121.18.168'),
            ('#EXTINF:-1 tvg-name="咪咕音乐" group-title="Music",咪咕音乐', 'http://miguvideo.com')
        ]
        music_list.extend(backup)

    return list(set(music_list))

def save_to_m3u(channels):
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for info, url in channels:
            f.write(f"{info}\n{url}\n")
    print(f"写入完成，共 {len(channels)} 个频道")

if __name__ == "__main__":
    ch = fetch_channels()
    save_to_m3u(ch)
