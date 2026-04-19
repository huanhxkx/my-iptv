import requests
import re

# 定义需要抓取的 MTV 相关频道列表（示例使用一些公开已知的源或占位符）
channels = [
    {"name": "MTV China", "url": "http://121.18.168.149/cache.ott.ystenlive.itv.cmvideo.cn:80/000000001000/5000000010000030951/index.m3u8"},
    {"name": "MTV Live", "url": "https://githubusercontent.com"} # 引用聚合源
]

def generate_m3u():
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for ch in channels:
            f.write(f'#EXTINF:-1 tvg-name="{ch["name"]}" group-title="Music",{ch["name"]}\n')
            f.write(f'{ch["url"]}\n')
    print("M3U 订阅文件已生成")

if __name__ == "__main__":
    generate_m3u()
