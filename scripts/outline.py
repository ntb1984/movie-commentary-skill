import argparse
import sys

RATIOS = {"hook": 0.033, "setup": 0.27, "turn": 0.537, "close": 0.16}
CPS = 5.4  # 汉字/秒

SKELETONS = {
    "A": "反差神作型：当年扑街 / 现在封神",
    "B": "意难平型：一个遗憾，一个人",
    "C": "冷门遗珠型：你知道它，但你没看过",
    "D": "人物弧光型：一个人怎么变成这样",
    "E": "一句话反转型：全片为最后一句服务",
}


def main():
    ap = argparse.ArgumentParser(description="影视解说脚本骨架生成器")
    ap.add_argument("title", help="片名")
    ap.add_argument("--seconds", type=int, default=90, help="目标时长，默认 90")
    ap.add_argument("--type", dest="sk", default="B", choices=list(SKELETONS), help="骨架类型 A-E")
    ap.add_argument("--cps", type=float, default=CPS, help="语速，字/秒，默认 5.4")
    a = ap.parse_args()

    total_chars = int(a.seconds * a.cps)
    lines = []
    lines.append(f"# 《{a.title}》解说骨架")
    lines.append("")
    lines.append(f"- 目标时长：{a.seconds} 秒")
    lines.append(f"- 语速：{a.cps} 字/秒 → 总字数约 {total_chars} 字")
    lines.append(f"- 骨架：{a.sk} {SKELETONS[a.sk]}")
    lines.append("")
    lines.append("| 段 | 秒数 | 字数 | 任务 |")
    lines.append("|---|---|---|---|")

    t = 0
    for key, name, task in (
        ("hook", "钩子", "一句反常识或一个结果，不讲背景"),
        ("setup", "铺垫", "只交代后面用得上的信息"),
        ("turn", "反转", "一个意外、一层含义、或一次视角翻转"),
        ("close", "落点", "一句让人接话的话，不总结"),
    ):
        sec = round(a.seconds * RATIOS[key])
        chars = round(total_chars * RATIOS[key])
        lines.append(f"| {name} | {t}–{t + sec} | {chars} | {task} |")
        t += sec

    lines.append("")
    lines.append("## 填写区")
    lines.append("")
    lines.append("### 钩子（3 秒）")
    lines.append("1. ")
    lines.append("2. ")
    lines.append("3. ")
    lines.append("")
    for key, title in (("setup", "铺垫"), ("turn", "反转"), ("close", "落点")):
        lines.append(f"### {title}")
        lines.append("")
        lines.append("")
    lines.append("## 自检")
    lines.append("")
    for item in (
        "前 3 秒有没有背景交代",
        "是不是只讲了一个观点",
        "每 10 秒有新信息吗",
        "结尾是选择题不是总结",
        "正片截帧占比不超过 50%",
        "封面文案含数字或对比",
    ):
        lines.append(f"- [ ] {item}")

    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
