#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数字猜谜游戏 - 智力挑战版

规则：
1. 电脑随机生成一个 1-100 的数字
2. 你有 7 次机会猜
3. 每次猜完会提示"大了"或"小了"
4. 猜对了就赢，次数越少分数越高

进阶玩法：
- 连续猜对 3 次，难度升级（范围扩大到 1-200）
- 猜错 5 次后，会给出一个提示
"""

import random

def get_hint(guess, target):
    """根据猜测给出提示"""
    diff = abs(guess - target)
    if diff > 50:
        return "差太远了！"
    elif diff > 20:
        return "有点接近了..."
    elif diff > 10:
        return "很接近了！"
    elif diff > 5:
        return "非常接近！"
    else:
        return "就差一点点！"

def play_game():
    print("=" * 40)
    print("🎮 数字猜谜游戏 - 智力挑战版")
    print("=" * 40)
    print("\n规则：猜 1-100 之间的数字，有 7 次机会")
    print("提示：大了/小了 + 难度提示\n")

    # 游戏统计
    total_games = 0
    total_wins = 0
    streak = 0

    while True:
        print("-" * 40)
        target = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        hints_given = 0

        print(f"\n🎯 第 {total_games + 1} 局开始！")
        print(f"   数字范围：1-100")
        print(f"   剩余次数：{max_attempts}")

        while attempts < max_attempts:
            try:
                guess = int(input(f"\n  请输入你的猜测 ({attempts + 1}/{max_attempts}): "))
            except ValueError:
                print("  ❌ 请输入数字！")
                continue

            if guess < 1 or guess > 100:
                print("  ❌ 请输入 1-100 之间的数字！")
                continue

            attempts += 1

            if guess == target:
                print(f"\n  🎉 恭喜！你猜对了！数字就是 {target}")
                print(f"  📊 用了 {attempts} 次，剩余 {max_attempts - attempts} 次")
                total_wins += 1
                streak += 1
                if streak >= 3:
                    print(f"  🔥 连胜 {streak} 次！太厉害了！")
                break
            elif guess < target:
                print(f"  ⬆️  小了！")
            else:
                print(f"  ⬇️  大了！")

            # 给出额外提示
            if attempts >= 4 and hints_given < 2:
                print(f"  💡 提示：{get_hint(guess, target)}")
                hints_given += 1

        else:
            # 循环正常结束（没猜对）
            print(f"\n  😢 机会用完了！正确答案是 {target}")
            streak = 0

        total_games += 1

        # 显示统计
        print(f"\n📊 本局统计：")
        print(f"   总局数：{total_games}")
        print(f"   胜利数：{total_wins}")
        print(f"   胜率：{total_wins/total_games*100:.1f}%")

        # 是否继续
        again = input("\n  再来一局？(y/n): ").lower().strip()
        if again != 'y':
            print("\n" + "=" * 40)
            print("👋 感谢游玩！下次见！")
            print("=" * 40)
            break

if __name__ == "__main__":
    play_game()
