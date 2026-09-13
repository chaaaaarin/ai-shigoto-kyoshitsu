# -*- coding: utf-8 -*-
"""レッスンのたとえ話イラストと、図解ボックスのアイコンを生成する。

スタイルv2（~/.claude/skills/research/references/illust-style-guide.md）の部品で組む。
文字のラベルで意味を補わず、記号そのものを一目で分かる形（*_pict_v2 / *_ground_v2）で描く（2026-09-13 ユーザー指定）。
data/figures.js を書き出す。生成済みの SVG は手で直さず、このスクリプトを直して再実行する。

    python3 scripts/build_figures.py            # data/figures.js と figures-preview.html を作る
"""
import json
import pathlib
import sys

sys.path.insert(0, "/Users/karin/.claude/skills/research/references")
from svg_parts_v2 import (  # noqa: E402
    person_v2, bot_v2, desk_v2, laptop_v2, envelope_v2, monitor_v2, board_v2, server_v2,
    ribbon_badge_v2, alarm_clock_v2, gate_v2, magnifier_v2, sparkle, cloud, ground_v2, dashed_arc, wrap,
    book_pict_v2, doc_pict_v2, ng_pict_v2, check_pict_v2, chart_pict_v2, flag_pict_v2, loop_pict_v2,
    bubble_pict_v2, question_pict_v2, calendar_pict_v2, clock_pict_v2, key_pict_v2, lock_pict_v2,
    wifi_pict_v2, robot_pict_v2, person_pict_v2, folder_pict_v2, browser_pict_v2,
    bookshelf_ground_v2, stairs_ground_v2, step_ground_v2, school_ground_v2,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
NG = "var(--ng)"


def scene(*parts):
    return wrap(ground_v2(14, 286, 172) + "".join(parts), vb="8 26 284 156")


def divider(x, y1=58, y2=166):
    """左右の比べる場面を分ける点線。"""
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="var(--line)" stroke-width="2" stroke-dasharray="4,6" stroke-linecap="round"/>'


# id: (svg, チップ, 見出し, キャプション)。コースごとに同じ具体例の場面で描く（figure-patterns A1）
SCENES = {
    # コース1: お詫びメール
    "1-1": (scene(desk_v2(200, 172, w=80), laptop_v2(194, 144, w=40), calendar_pict_v2(262, 64, 0.9),
                  bot_v2(136, 172), question_pict_v2(160, 96, 0.8), person_v2(62, 172, face="smile")),
            "たとえるなら", "筆がとても速い、新人の相棒", "文章は速くて上手。でも、昨日決まった納品日は知らない"),
    "1-2": (scene(person_v2(74, 172, face="smile", wave=True), dashed_arc(100, 128, 196, 128, lift=34),
                  doc_pict_v2(148, 98, 0.9), sparkle(176, 72), bot_v2(222, 172)),
            "たとえるなら", "頼み方で、出来上がりが変わる", "ゴール・読み手・形式・条件の4つをそろえて渡す"),
    "1-3": (scene(person_v2(58, 172, face="smile"), desk_v2(166, 172, w=76), folder_pict_v2(148, 128, 0.8),
                  doc_pict_v2(190, 126, 0.72), bot_v2(252, 172)),
            "たとえるなら", "材料をフォルダにまとめて渡す", "事実・参考・状況を、指示とは分けて渡す"),
    "1-4": (scene(bot_v2(56, 172), envelope_v2(136, 160, s=1.3), magnifier_v2(178, 116, s=1.15),
                  person_v2(238, 172, face="smile")),
            "たとえるなら", "送る前に、虫眼鏡で見直す", "事実・目的・責任の3つを確かめてから送る"),
    # コース2: 営業週報
    "2-1": (scene(calendar_pict_v2(66, 66, 1.0), desk_v2(166, 172, w=86), doc_pict_v2(148, 124, 0.78),
                  doc_pict_v2(186, 124, 0.78), loop_pict_v2(250, 64, 0.95), person_v2(252, 172, face="trouble")),
            "この場面", "毎週やってくる、同じ仕事", "回数が多く、形の決まった作業から選ぶ"),
    "2-2": (scene(person_v2(34, 172, face="smile"), step_ground_v2(92, 172, 1), dashed_arc(112, 146, 132, 146, lift=8),
                  step_ground_v2(150, 172, 2), dashed_arc(170, 146, 190, 146, lift=8), step_ground_v2(208, 172, 3),
                  bot_v2(264, 172)),
            "たとえるなら", "レシピのように、1手順ずつ", "材料 → 作業 → 出来上がり、を小さく分ける"),
    "2-3": (scene(bot_v2(44, 172), gate_v2(116, 172, 1, w=48, h=56), check_pict_v2(116, 80, 0.62),
                  person_v2(180, 172, face="smile"), gate_v2(244, 172, 2, w=48, h=56), check_pict_v2(244, 80, 0.62)),
            "たとえるなら", "要所に、チェックポイント", "全部ではなく、2〜3か所で人が確かめる"),
    "2-4": (scene(person_v2(84, 172, face="smile", wave=True), doc_pict_v2(146, 84, 0.95), loop_pict_v2(188, 70, 0.72),
                  bot_v2(222, 172), sparkle(116, 58)),
            "たとえるなら", "うまくいった型を、何度も使う", "変わる所だけ空けたテンプレートを育てる"),
    # コース3: 競合3社の調査
    "3-1": (scene(person_v2(40, 172, face="smile"), bubble_pict_v2(62, 98, 0.72), bot_v2(98, 172), divider(150),
                  bot_v2(206, 172), browser_pict_v2(244, 70, 0.7), browser_pict_v2(262, 98, 0.7, highlight=True)),
            "たとえるなら", "1往復か、用事を丸ごとか", "エージェントは、自分で調べて・まとめて・作る"),
    "3-2": (scene(person_v2(64, 172, face="smile", wave=True), check_pict_v2(146, 108, 1.05),
                  bot_v2(224, 172), ng_pict_v2(262, 80, 0.6, NG)),
            "たとえるなら", "出発前の、打ち合わせ", "完了の条件・材料・禁止・途中の確認を渡す"),
    "3-3": (scene(person_v2(56, 172, face="smile"), bubble_pict_v2(80, 98, 0.72), bot_v2(176, 172),
                  ng_pict_v2(246, 112, 0.85, NG)),
            "たとえるなら", "途中で、声をかける", "ずれたら直し、危ない操作の前では止める"),
    "3-4": (scene(bot_v2(56, 172), doc_pict_v2(104, 142, 0.72), magnifier_v2(182, 116, s=1.1),
                  person_v2(238, 172, face="smile"), sparkle(264, 94)),
            "たとえるなら", "持ち帰った成果を、点検する", "形・出どころ・操作の3つを確かめてから使う"),
    # コース4: 総務の社内問い合わせ
    "4-1": (scene(person_v2(58, 172, face="smile", wave=True), desk_v2(154, 172, w=80), envelope_v2(130, 146, s=0.75),
                  envelope_v2(156, 146, s=0.8), envelope_v2(182, 146, s=0.75, rot=8), flag_pict_v2(248, 150, 0.95)),
            "たとえるなら", "小さく始める、最初の一歩", "効果が大きく、進めやすい業務を1つ選ぶ"),
    "4-2": (scene(doc_pict_v2(146, 70, 0.95), lock_pict_v2(190, 62, 0.62), person_v2(92, 172, face="smile"),
                  person_v2(146, 172, face="smile"), bot_v2(210, 172)),
            "たとえるなら", "みんなで守る、1枚のルール", "入れてよい情報・確かめる人・相談先を決める"),
    "4-3": (scene(person_v2(38, 172, face="smile"), gate_v2(108, 172, 1, w=42, h=50, level=0),
                  gate_v2(180, 172, 2, w=46, h=58, level=1), gate_v2(254, 172, 3, w=50, h=66, level=3)),
            "たとえるなら", "試す → 広げる → 定着させる", "段階ごとに、期間と見る数字を決める"),
    "4-4": (scene(person_v2(62, 172, face="wow", wave=True), person_v2(112, 172, face="smile"),
                  person_v2(160, 172, face="smile"), bot_v2(210, 172), ribbon_badge_v2(256, 96, s=1.0), sparkle(242, 60)),
            "たとえるなら", "うまくいったことを、分け合う", "推進役・実務での研修・定期的な振り返り"),
    # コース5: 中2理科「電流と電圧」
    "5-1": (scene(board_v2(150, 118, w=112, h=58), person_v2(70, 172, face="smile"), bot_v2(222, 172),
                  doc_pict_v2(264, 136, 0.68)),
            "たとえるなら", "下ごしらえはAI、味見は先生", "例題やプリントの下書きはAI、ねらいと正確さは先生"),
    "5-2": (scene(person_v2(44, 172, face="smile"), stairs_ground_v2(178, 172, 1.05), sparkle(250, 76)),
            "たとえるなら", "同じねらいを、3つの段で", "基本・標準・発展と、やさしい日本語の版"),
    "5-3": (scene(check_pict_v2(150, 84, 1.05), person_v2(76, 172, face="smile"), bot_v2(224, 172),
                  lock_pict_v2(262, 70, 0.6)),
            "たとえるなら", "ものさしを、先にそろえる", "基準表の下書きはAI、成績を決めるのは先生"),
    "5-4": (scene(school_ground_v2(214, 172, 1.0), person_v2(62, 172, face="smile"),
                  person_v2(114, 172, face="smile", scale=0.85), bubble_pict_v2(136, 104, 0.6), cloud(52, 46, 0.8)),
            "たとえるなら", "校門をくぐる前に、ルールを", "学校の方針と、年齢の条件を先に確かめる"),
    # コース6: 大学2年のレポート
    "6-1": (scene(person_v2(52, 172, face="smile"), desk_v2(114, 172, w=62), book_pict_v2(114, 128, 0.6),
                  bot_v2(194, 172), bubble_pict_v2(218, 98, 0.66), doc_pict_v2(262, 132, 0.62), ng_pict_v2(262, 132, 0.58, NG)),
            "たとえるなら", "先生役・壁打ち相手・添削役", "代わりに書かせて、そのまま出すのはNG"),
    "6-2": (scene(person_v2(84, 172, face="wow"), bubble_pict_v2(106, 98, 0.72), bot_v2(190, 172),
                  book_pict_v2(250, 154, 0.7), sparkle(132, 56)),
            "たとえるなら", "自分の理解から、話しはじめる", "たとえ話や確認問題で、一歩ずつ教わる"),
    "6-3": (scene(bot_v2(52, 172), question_pict_v2(76, 98, 0.66), person_v2(140, 172, face="smile"),
                  magnifier_v2(170, 116, s=1.0), bookshelf_ground_v2(240, 172, 1.0)),
            "たとえるなら", "本棚で、出典を確かめる", "AIが挙げた本が、本当にあるとは限らない"),
    "6-4": (scene(calendar_pict_v2(72, 66, 0.95), person_v2(150, 172, face="wow", wave=True),
                  alarm_clock_v2(238, 172), ribbon_badge_v2(252, 74, s=0.85)),
            "たとえるなら", "毎日の、小さな練習", "練習問題と計画で、自分で判断する力を育てる"),
    # コース7: 備品貸し出しアプリに検索機能
    "7-1": (scene(person_v2(60, 172, face="smile", wave=True), desk_v2(176, 172, w=88), monitor_v2(160, 144, w=42, h=30),
                  laptop_v2(204, 144, w=30), bot_v2(258, 172)),
            "たとえるなら", "コードを読める、新しい仲間", "読む・書く・直す・テストするを、続けて進める"),
    "7-2": (scene(person_v2(64, 172, face="smile"), doc_pict_v2(118, 108, 0.85), bot_v2(184, 172),
                  check_pict_v2(250, 76, 0.85)),
            "たとえるなら", "依頼メモと、共通の約束事リスト", "4つを入れた依頼と、約束事は AGENTS.md に"),
    "7-3": (scene(person_v2(60, 172, face="smile"), key_pict_v2(96, 110, 0.8), bot_v2(168, 172),
                  server_v2(244, 172, w=40, h=56), lock_pict_v2(244, 94, 0.62)),
            "たとえるなら", "鍵を渡す範囲を、決めておく", "確認のタイミング・作業範囲・ネットワークは狭く始める"),
    "7-4": (scene(bot_v2(52, 172), browser_pict_v2(116, 80, 0.72), dashed_arc(136, 72, 160, 72, lift=8),
                  browser_pict_v2(180, 80, 0.72, highlight=True), magnifier_v2(150, 120, s=0.95),
                  person_v2(246, 172, face="smile")),
            "たとえるなら", "差分を見てから、取り込む", "差分・テスト・説明を確かめ、小さく取り込む"),
    # コース8: 社内規程に答えるAIチャット
    "8-1": (scene(person_v2(64, 172, face="trouble"), desk_v2(158, 172, w=82), envelope_v2(132, 146, s=0.75),
                  envelope_v2(158, 146, s=0.8), envelope_v2(184, 146, s=0.75, rot=8), bot_v2(248, 172)),
            "この場面", "毎月200件の、同じような質問", "誰の・どんな困りごとか、AIに向くかを先に決める"),
    "8-2": (scene(bookshelf_ground_v2(62, 172, 1.0), book_pict_v2(126, 154, 0.72), bot_v2(186, 172),
                  bubble_pict_v2(210, 98, 0.72), person_v2(258, 172, face="smile")),
            "たとえるなら", "本棚から該当ページを探して答える", "探す → 渡す → 答える → 出典を示す"),
    "8-3": (scene(board_v2(150, 124, w=110, h=62), chart_pict_v2(150, 94, 0.9),
                  person_v2(56, 172, face="smile"), bot_v2(244, 172)),
            "たとえるなら", "毎回、同じテストで測る", "テスト質問集と合格の条件を、先に作る"),
    "8-4": (scene(bot_v2(64, 172), loop_pict_v2(128, 80, 1.0), chart_pict_v2(186, 80, 0.85),
                  person_v2(242, 172, face="smile")),
            "たとえるなら", "1つずつ変えて、そのたび測る", "指示 → 検索 → モデルの順に、変えるたびテスト"),
}


def icon(inner, vb="0 0 70 70"):
    return f'<svg viewBox="{vb}" width="100%" height="100%" aria-hidden="true">{inner}</svg>'


# 図解ボックスの見出し語 → アイコン（figure-patterns A5: 同じ絵は全ページで同じ意味。形だけで伝わる記号にする）
ICONS = {
    "stop": icon(ng_pict_v2(35, 35, 1.25, NG)),
    "key": icon(key_pict_v2(35, 36, 1.1)),
    "lock": icon(lock_pict_v2(35, 37, 1.25)),
    "check": icon(check_pict_v2(35, 36, 1.15)),
    "wifi": icon(wifi_pict_v2(35, 32, 1.2)),
    "ai": icon(robot_pict_v2(35, 38, 1.2)),
    "person": icon(person_pict_v2(35, 35, 1.2)),
    "paper": icon(doc_pict_v2(35, 35, 1.2)),
    "calendar": icon(calendar_pict_v2(35, 37, 1.2)),
    "clock": icon(clock_pict_v2(35, 35, 1.25)),
    "bars": icon(chart_pict_v2(35, 35, 1.2)),
    "book": icon(book_pict_v2(37, 34, 1.15)),
    "flag": icon(flag_pict_v2(35, 33, 1.2)),
    "bubble": icon(bubble_pict_v2(37, 33, 1.25)),
    "loop": icon(loop_pict_v2(35, 35, 1.5)),
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
    icons = {k: {"svg": v} for k, v in ICONS.items()}
    out = ROOT / "data" / "figures.js"
    out.write_text(
        "// scripts/build_figures.py が生成（手で編集しない）\n"
        "window.SCENES = " + json.dumps(scenes, ensure_ascii=False) + ";\n"
        "window.DICONS = " + json.dumps(icons, ensure_ascii=False) + ";\n"
        "window.DICON_RULES = " + json.dumps(ICON_RULES, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    cards = "".join(
        f'<div class="card" style="margin:10px 0"><div class="kicker">{k}</div><div class="scene"><div class="scene-box">{v[0]}</div>'
        f'<div class="metacap"><span class="metachip">{v[1]}</span><b>{v[2]}</b><span>{v[3]}</span></div></div></div>'
        for k, v in SCENES.items()
    )
    icon_cells = "".join(
        f'<div class="card icon-demo" style="width:120px;text-align:center;padding:10px">'
        f'<div style="width:72px;height:72px;margin:0 auto">{svg}</div><div class="muted">{name}</div></div>'
        for name, svg in ICONS.items()
    )
    (ROOT / "figures-preview.html").write_text(
        '<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="style.css"><title>figures preview</title>'
        '<main class="app" style="padding-bottom:40px"><h1 class="h1">アイコン</h1>'
        f'<div style="display:flex;flex-wrap:wrap;gap:10px">{icon_cells}</div>'
        f'<h1 class="h1" style="margin-top:20px">シーン</h1><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:10px">{cards}</div></main>',
        encoding="utf-8",
    )
    print(f"scenes: {len(scenes)}  icons: {len(icons)}  -> {out}")


if __name__ == "__main__":
    main()
