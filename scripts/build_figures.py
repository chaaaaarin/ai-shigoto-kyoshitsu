# -*- coding: utf-8 -*-
"""レッスンのたとえ話イラストと、図解ボックスのアイコンを生成する。

スタイルv2（~/.claude/skills/research/references/illust-style-guide.md）の部品だけで組み、
data/figures.js を書き出す。生成済みの SVG は手で直さず、このスクリプトを直して再実行する。

    python3 scripts/build_figures.py            # data/figures.js と figures-preview.html を作る
"""
import json
import pathlib
import sys

sys.path.insert(0, "/Users/karin/.claude/skills/research/references")
from svg_parts_v2 import (  # noqa: E402
    person_v2, bot_v2, desk_v2, paper_v2, laptop_v2, envelope_v2, calendar_v2, clock_v2,
    book_v2, padlock_v2, stop_mark_v2, monitor_v2, board_v2, corkboard_v2, shelf_v2,
    ribbon_badge_v2, schoolgate_v2, desk_row_v2, server_v2, bars_v2, usage_log_v2,
    card_box_v2, blueprint_v2, alarm_clock_v2, wifi_v2, flag_star_v2, loop_icon_v2,
    crate_v2, tab_v2, recipe_card_v2, gate_v2, key_v2, speech_bubble_v2, sparkle, cloud,
    alert_bubble, ground_v2, dashed_arc, wrap, magnifier_v2,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent


def scene(*parts):
    return wrap(ground_v2(14, 286, 172) + "".join(parts), vb="8 26 284 156")


# id: (svg, チップ, 見出し, キャプション)。コースごとに同じ具体例の場面で描く（figure-patterns A1）
SCENES = {
    # コース1: お詫びメール
    "1-1": (scene(desk_v2(196, 172, w=78), laptop_v2(192, 144, w=40), calendar_v2(262, 64, marks=2),
                  bot_v2(140, 172), alert_bubble(164, 100), person_v2(64, 172, face="smile")),
            "たとえるなら", "筆がとても速い、新人の相棒", "文章は速くて上手。でも、昨日決まった納品日は知らない"),
    "1-2": (scene(person_v2(80, 172, face="smile", wave=True), recipe_card_v2(150, 118, rot=-6, dense=False),
                  bot_v2(218, 172), sparkle(244, 110)),
            "たとえるなら", "頼み方で、出来上がりが変わる", "ゴール・読み手・形式・条件の4つをそろえて渡す"),
    "1-3": (scene(person_v2(62, 172, face="smile"), desk_v2(166, 172, w=70), card_box_v2(150, 150, w=34, h=20),
                  paper_v2(186, 144, rot=5), bot_v2(248, 172), sparkle(222, 104)),
            "たとえるなら", "材料を箱に分けて渡す", "事実・参考・状況を、指示とは分けて渡す"),
    "1-4": (scene(bot_v2(62, 172), envelope_v2(150, 160, s=1.2, sealed=False), magnifier_v2(188, 112, s=1.1),
                  person_v2(236, 172, face="smile")),
            "たとえるなら", "送る前に、虫眼鏡で見直す", "事実・目的・責任の3つを確かめてから送る"),
    # コース2: 営業週報
    "2-1": (scene(calendar_v2(66, 62, marks=4), desk_v2(168, 172, w=82), paper_v2(150, 144), paper_v2(188, 144, rot=4),
                  loop_icon_v2(244, 62, r=16), person_v2(252, 172, face="trouble")),
            "この場面", "毎週やってくる、同じ仕事", "回数が多く、形の決まった作業から選ぶ"),
    "2-2": (scene(person_v2(38, 172, face="smile"), crate_v2(96, 172, w=26, h=20), dashed_arc(112, 146, 140, 146),
                  crate_v2(152, 172, w=26, h=20), dashed_arc(168, 146, 196, 146), crate_v2(208, 172, w=26, h=20),
                  bot_v2(262, 172)),
            "たとえるなら", "レシピのように、1手順ずつ", "材料 → 作業 → 出来上がり、を小さく分ける"),
    "2-3": (scene(bot_v2(46, 172), gate_v2(118, 172, 1, w=48, h=56), person_v2(178, 172, face="smile"),
                  gate_v2(242, 172, 2, w=48, h=56)),
            "たとえるなら", "要所に、チェックポイント", "全部ではなく、2〜3か所で人が確かめる"),
    "2-4": (scene(corkboard_v2(150, 68, w=62, h=42), person_v2(88, 172, face="smile", wave=True),
                  bot_v2(212, 172), sparkle(196, 44)),
            "たとえるなら", "うまくいった型を、掲示板に", "変わる所だけ空けたテンプレートを育てる"),
    # コース3: 競合3社の調査
    "3-1": (scene(person_v2(64, 172, face="smile"), speech_bubble_v2(64, 104, s=0.9), bot_v2(196, 172),
                  tab_v2(236, 84, w=30, h=22), tab_v2(258, 112, w=30, h=22, tint=True)),
            "たとえるなら", "1往復か、用事を丸ごとか", "エージェントは、自分で調べて・まとめて・作る"),
    "3-2": (scene(person_v2(66, 172, face="smile", wave=True), blueprint_v2(150, 172, w=58, h=42),
                  bot_v2(226, 172), stop_mark_v2(264, 82, r=11)),
            "たとえるなら", "出発前の、打ち合わせ", "完了の条件・材料・禁止・途中の確認を渡す"),
    "3-3": (scene(person_v2(58, 172, face="smile"), speech_bubble_v2(58, 104, s=0.85), bot_v2(176, 172),
                  alert_bubble(200, 104), stop_mark_v2(252, 132, r=15)),
            "たとえるなら", "途中で、声をかける", "ずれたら直し、危ない操作の前では止める"),
    "3-4": (scene(bot_v2(60, 172), paper_v2(112, 172, rot=-4), magnifier_v2(190, 116, s=1.1),
                  person_v2(236, 172, face="smile"), sparkle(262, 96)),
            "たとえるなら", "持ち帰った成果を、点検する", "形・出どころ・操作の3つを確かめてから使う"),
    # コース4: 総務の社内問い合わせ
    "4-1": (scene(person_v2(64, 172, face="smile", wave=True), desk_v2(156, 172, w=72), envelope_v2(142, 146, s=0.8),
                  envelope_v2(172, 146, s=0.8, rot=8), flag_star_v2(246, 172)),
            "たとえるなら", "小さく始める、最初の一歩", "効果が大きく、進めやすい業務を1つ選ぶ"),
    "4-2": (scene(corkboard_v2(150, 62, w=62, h=42), padlock_v2(198, 54, s=0.8), person_v2(92, 172, face="smile"),
                  person_v2(146, 172, face="smile"), bot_v2(206, 172)),
            "たとえるなら", "みんなで守る、1枚のルール", "入れてよい情報・確かめる人・相談先を決める"),
    "4-3": (scene(person_v2(40, 172, face="smile"), gate_v2(110, 172, 1, w=42, h=50, level=0),
                  gate_v2(184, 172, 2, w=46, h=58, level=1), gate_v2(256, 172, 3, w=50, h=66, level=3)),
            "たとえるなら", "試す → 広げる → 定着させる", "段階ごとに、期間と見る数字を決める"),
    "4-4": (scene(person_v2(66, 172, face="wow", wave=True), person_v2(116, 172, face="smile"),
                  person_v2(164, 172, face="smile"), bot_v2(214, 172), ribbon_badge_v2(260, 92, s=0.9), sparkle(246, 58)),
            "たとえるなら", "うまくいったことを、分け合う", "推進役・実務での研修・定期的な振り返り"),
    # コース5: 中2理科「電流と電圧」
    "5-1": (scene(board_v2(150, 116, w=112, h=58), person_v2(70, 172, face="smile"), bot_v2(226, 172),
                  paper_v2(258, 172, rot=6)),
            "たとえるなら", "下ごしらえはAI、味見は先生", "例題やプリントの下書きはAI、ねらいと正確さは先生"),
    "5-2": (scene(person_v2(36, 172, face="smile"), desk_row_v2(172, 172, n=3, gap=56), sparkle(262, 70)),
            "たとえるなら", "同じねらいを、3つの段で", "基本・標準・発展と、やさしい日本語の版"),
    "5-3": (scene(usage_log_v2(150, 86, w=66, h=48), person_v2(76, 172, face="smile"), bot_v2(224, 172),
                  padlock_v2(258, 66, s=0.7)),
            "たとえるなら", "ものさしを、先にそろえる", "基準表の下書きはAI、成績を決めるのは先生"),
    "5-4": (scene(schoolgate_v2(206, 172, w=66, h=74), person_v2(70, 172, face="smile"),
                  person_v2(120, 172, face="smile", scale=0.85), cloud(52, 44, 0.8)),
            "たとえるなら", "校門をくぐる前に、ルールを", "学校の方針と、年齢の条件を先に確かめる"),
    # コース6: 大学2年のレポート
    "6-1": (scene(person_v2(56, 172, face="smile"), desk_v2(118, 172, w=60), book_v2(118, 144, w=34),
                  bot_v2(206, 172), speech_bubble_v2(206, 106, s=0.8), stop_mark_v2(260, 138, r=11)),
            "たとえるなら", "先生役・壁打ち相手・添削役", "代わりに書かせて、そのまま出すのはNG"),
    "6-2": (scene(person_v2(88, 172, face="wow"), speech_bubble_v2(88, 104, s=0.9), bot_v2(196, 172),
                  book_v2(246, 172, w=34), sparkle(120, 50)),
            "たとえるなら", "自分の理解から、話しはじめる", "たとえ話や確認問題で、一歩ずつ教わる"),
    "6-3": (scene(bot_v2(56, 172), alert_bubble(80, 104), person_v2(140, 172, face="smile"),
                  magnifier_v2(172, 112, s=1.0), shelf_v2(236, 172, w=62, h=44)),
            "たとえるなら", "本棚で、出典を確かめる", "AIが挙げた本が、本当にあるとは限らない"),
    "6-4": (scene(calendar_v2(76, 64, marks=3), person_v2(150, 172, face="wow", wave=True),
                  alarm_clock_v2(236, 172), ribbon_badge_v2(248, 70, s=0.8)),
            "たとえるなら", "毎日の、小さな練習", "練習問題と計画で、自分で判断する力を育てる"),
    # コース7: 備品貸し出しアプリに検索機能
    "7-1": (scene(person_v2(66, 172, face="smile", wave=True), desk_v2(176, 172, w=84), monitor_v2(162, 144, w=40, h=28),
                  laptop_v2(202, 144, w=30), bot_v2(254, 172)),
            "たとえるなら", "コードを読める、新しい仲間", "読む・書く・直す・テストするを、続けて進める"),
    "7-2": (scene(person_v2(70, 172, face="smile"), recipe_card_v2(124, 120, rot=-6, dense=True),
                  bot_v2(186, 172), corkboard_v2(248, 70, w=56, h=40)),
            "たとえるなら", "依頼メモと、共通ルールの掲示板", "4つを入れた依頼と、約束事は AGENTS.md に"),
    "7-3": (scene(person_v2(64, 172, face="smile"), key_v2(94, 116, rot=-25, s=1.25), bot_v2(168, 172),
                  server_v2(244, 172, w=40, h=56), padlock_v2(244, 94, s=0.9)),
            "たとえるなら", "鍵を渡す範囲を、決めておく", "確認のタイミング・作業範囲・ネットワークは狭く始める"),
    "7-4": (scene(bot_v2(56, 172), tab_v2(124, 82, w=34, h=26), tab_v2(170, 100, w=34, h=26, tint=True),
                  magnifier_v2(196, 128, s=1.0), person_v2(248, 172, face="smile")),
            "たとえるなら", "差分を見てから、取り込む", "差分・テスト・説明を確かめ、小さく取り込む"),
    # コース8: 社内規程に答えるAIチャット
    "8-1": (scene(person_v2(72, 172, face="trouble"), desk_v2(160, 172, w=72), envelope_v2(144, 146, s=0.8),
                  envelope_v2(174, 146, s=0.8, rot=8), bot_v2(246, 172)),
            "この場面", "毎月200件の、同じような質問", "誰の・どんな困りごとか、AIに向くかを先に決める"),
    "8-2": (scene(shelf_v2(66, 172, w=62, h=44), book_v2(132, 172, w=36), bot_v2(186, 172),
                  speech_bubble_v2(234, 104, s=0.8), person_v2(258, 172, face="smile")),
            "たとえるなら", "本棚から該当ページを探して答える", "探す → 渡す → 答える → 出典を示す"),
    "8-3": (scene(board_v2(150, 122, w=110, h=62), bars_v2(114, 114, vals=(12, 22, 17, 30), bw=9, gap=6),
                  person_v2(56, 172, face="smile"), bot_v2(244, 172)),
            "たとえるなら", "毎回、同じテストで測る", "テスト質問集と合格の条件を、先に作る"),
    "8-4": (scene(bot_v2(80, 172), loop_icon_v2(150, 70, r=18), clock_v2(226, 70, r=16, hh=10, mm=10),
                  person_v2(204, 172, face="smile")),
            "たとえるなら", "1つずつ変えて、そのたび測る", "指示 → 検索 → モデルの順に、変えるたびテスト"),
}


def icon(inner, vb="0 0 70 70"):
    return f'<svg viewBox="{vb}" width="100%" height="100%" aria-hidden="true">{inner}</svg>'


def centered(part, dx=0, dy=0, s=1.0):
    return f'<g transform="translate({dx},{dy}) scale({s})">{part}</g>'


# 図解ボックスの見出し語 → アイコン（figure-patterns A5: 同じ絵は全ページで同じ意味）
ICONS = {
    "stop": icon(stop_mark_v2(35, 35, r=20)),
    "key": icon(key_v2(35, 18, rot=-30, s=1.25)),
    "lock": icon(padlock_v2(35, 38, s=1.5)),
    "check": icon(magnifier_v2(31, 29, s=1.25)),
    "wifi": icon(wifi_v2(35, 52, s=1.6)),
    "ai": icon(bot_v2(35, 62)),
    "person": icon(person_v2(35, 68), vb="0 0 70 74"),
    "paper": icon(centered(paper_v2(35, 50, rot=-4), -18, -22, 1.5)),
    "calendar": icon(calendar_v2(35, 36, w=42, h=38, marks=3)),
    "clock": icon(clock_v2(35, 36, r=22, hh=10, mm=10)),
    "bars": icon(bars_v2(14, 58, vals=(14, 26, 20, 38), bw=9, gap=4)),
    "book": icon(book_v2(35, 52, w=52)),
    "flag": icon(centered(flag_star_v2(35, 60), -30, -34, 1.9)),
    "bubble": icon(speech_bubble_v2(35, 54, s=1.1)),
    "loop": icon(loop_icon_v2(35, 35, r=20)),
}

# 上から順に最初に当たったものを使う（否定・注意を先に判定する）
ICON_RULES = [
    ["してはいけない|NG|禁止|向かない|入れない|任せない|慎重", "stop"],
    ["権限|作業できる範囲|鍵", "key"],
    ["個人情報|秘密|機密", "lock"],
    ["ネットワーク|インターネット", "wifi"],
    ["確認|確かめ|チェック|見直|レビュー|点検|差分", "check"],
    ["完了|ゴール|成果|できたら", "flag"],
    ["評価|数字|基準|測る|テスト|成功", "bars"],
    ["計画|期間|予定|段階|広げる|定着|試す", "calendar"],
    ["速さ|時間|タイミング", "clock"],
    ["規程|出典|教材|勉強|本", "book"],
    ["質問|相談|声|共有|説明|伝え", "bubble"],
    ["くり返|使い回|改善|振り返", "loop"],
    ["材料|資料|文書|メモ|指示|依頼|手順|テンプレート|形式", "paper"],
    ["AI|エージェント|Codex", "ai"],
    ["人|先生|自分|学生|担当|チーム|読み手", "person"],
]


def main():
    scenes = {k: {"svg": v[0], "chip": v[1], "title": v[2], "cap": v[3]} for k, v in SCENES.items()}
    out = ROOT / "data" / "figures.js"
    out.write_text(
        "// scripts/build_figures.py が生成（手で編集しない）\n"
        "window.SCENES = " + json.dumps(scenes, ensure_ascii=False) + ";\n"
        "window.DICONS = " + json.dumps(ICONS, ensure_ascii=False) + ";\n"
        "window.DICON_RULES = " + json.dumps(ICON_RULES, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    cards = "".join(
        f'<div class="card" style="margin:10px 0"><div class="kicker">{k}</div><div class="scene"><div class="scene-box">{v[0]}</div>'
        f'<div class="metacap"><span class="metachip">{v[1]}</span><b>{v[2]}</b><span>{v[3]}</span></div></div></div>'
        for k, v in SCENES.items()
    )
    icons = "".join(
        f'<div style="text-align:center;width:90px"><div style="width:56px;height:56px;margin:0 auto">{svg}</div><div class="muted">{name}</div></div>'
        for name, svg in ICONS.items()
    )
    (ROOT / "figures-preview.html").write_text(
        '<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="style.css"><title>figures preview</title>'
        '<main class="app" style="padding-bottom:40px"><h1 class="h1">アイコン</h1>'
        f'<div class="card" style="display:flex;flex-wrap:wrap;gap:10px">{icons}</div>'
        f'<h1 class="h1" style="margin-top:20px">シーン</h1><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:10px">{cards}</div></main>',
        encoding="utf-8",
    )
    print(f"scenes: {len(scenes)}  icons: {len(ICONS)}  -> {out}")


if __name__ == "__main__":
    main()
