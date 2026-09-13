# -*- coding: utf-8 -*-
"""レッスンのたとえ話イラストと、図解ボックスのアイコンを生成する。

スタイルv2（~/.claude/skills/research/references/illust-style-guide.md）の部品で組み、
記号だけに頼らないよう、登場人物と小物には日本語のラベルを添える（2026-09-13 ユーザー指定）。
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
    ground_v2, dashed_arc, wrap, magnifier_v2,
)

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME_Y = 187  # 足元の名札の高さ（地面は y=172）


def _tw(text, size):
    return sum(size * 0.62 if ord(ch) < 128 else size for ch in text)


def tag(x, y, text, tone="plain", size=10.5):
    """角丸の名札ラベル。x,yは中心。"""
    fill, stroke, ink = {
        "plain": ("var(--paper)", "var(--line)", "var(--ink)"),
        "you": ("var(--brand-soft)", "var(--brand)", "var(--ink)"),
        "ai": ("var(--accent-soft)", "var(--accent)", "var(--ink)"),
        "ng": ("var(--ng-soft)", "var(--ng)", "var(--ng)"),
    }[tone]
    w, h = _tw(text, size) + 14, size + 8
    return (f'<g><rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{h / 2:.1f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
            f'<text x="{x}" y="{y + size * 0.36:.1f}" text-anchor="middle" font-size="{size}" font-weight="800" '
            f'fill="{ink}" font-family="var(--head)">{text}</text></g>')


def say(x, y, text, dx=0, size=10.5):
    """文字入りの吹き出し。x,yはしっぽの先。dxで本体だけ左右にずらす。"""
    w, h = _tw(text, size) + 18, size + 12
    cx, top = x + dx, y - h - 7
    return (f'<g style="filter:drop-shadow(0 1px 1px rgba(42,38,32,.12))">'
            f'<rect x="{cx - w / 2:.1f}" y="{top:.1f}" width="{w:.1f}" height="{h:.1f}" rx="7" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.5"/>'
            f'<path d="M{x - 5},{top + h - 0.8:.1f} L{x},{y} L{x + 5},{top + h - 0.8:.1f}" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<rect x="{x - 4}" y="{top + h - 2.6:.1f}" width="8" height="3.2" fill="var(--paper)"/>'
            f'<text x="{cx}" y="{top + h / 2 + size * 0.36:.1f}" text-anchor="middle" font-size="{size}" font-weight="800" '
            f'fill="var(--ink)" font-family="var(--head)">{text}</text></g>')


def you(x, text="あなた"):
    return tag(x, NAME_Y, text, "you")


def ai(x, text="AI"):
    return tag(x, NAME_Y, text, "ai")


def scene(*parts):
    return wrap(ground_v2(14, 286, 172) + "".join(parts), vb="8 20 284 178")


# id: (svg, チップ, 見出し, キャプション)。コースごとに同じ具体例の場面で描く（figure-patterns A1）
SCENES = {
    # コース1: お詫びメール
    "1-1": (scene(desk_v2(196, 172, w=78), laptop_v2(192, 144, w=40), calendar_v2(254, 62, marks=2),
                  tag(252, 90, "新しい予定"), bot_v2(140, 172), say(140, 120, "納品日は？", dx=-8),
                  person_v2(64, 172, face="smile"), you(64), ai(140)),
            "たとえるなら", "筆がとても速い、新人の相棒", "文章は速くて上手。でも、昨日決まった納品日は知らない"),
    "1-2": (scene(person_v2(78, 172, face="smile", wave=True), recipe_card_v2(150, 116, rot=-6, dense=False),
                  tag(150, 148, "指示の4つ"), bot_v2(220, 172), sparkle(246, 108), you(78), ai(220)),
            "たとえるなら", "頼み方で、出来上がりが変わる", "ゴール・読み手・形式・条件の4つをそろえて渡す"),
    "1-3": (scene(person_v2(62, 172, face="smile"), desk_v2(166, 172, w=70), card_box_v2(150, 150, w=34, h=20),
                  paper_v2(186, 144, rot=5), tag(168, 110, "事実・参考・状況"), bot_v2(250, 172), you(62), ai(250)),
            "たとえるなら", "材料を箱に分けて渡す", "事実・参考・状況を、指示とは分けて渡す"),
    "1-4": (scene(bot_v2(62, 172), envelope_v2(146, 160, s=1.2, sealed=False), tag(146, 124, "送る前"),
                  magnifier_v2(196, 118, s=1.05), tag(214, 84, "3つを確認"), person_v2(244, 172, face="smile"),
                  ai(62), you(244)),
            "たとえるなら", "送る前に、虫眼鏡で見直す", "事実・目的・責任の3つを確かめてから送る"),
    # コース2: 営業週報
    "2-1": (scene(calendar_v2(66, 60, marks=4), tag(66, 90, "毎週月曜"), desk_v2(166, 172, w=82),
                  paper_v2(148, 144), paper_v2(186, 144, rot=4), tag(166, 110, "営業週報"),
                  person_v2(252, 172, face="trouble"), you(252)),
            "この場面", "毎週やってくる、同じ仕事", "回数が多く、形の決まった作業から選ぶ"),
    "2-2": (scene(person_v2(38, 172, face="smile"), crate_v2(96, 172, w=26, h=20), dashed_arc(112, 146, 140, 146),
                  crate_v2(152, 172, w=26, h=20), dashed_arc(168, 146, 196, 146), crate_v2(208, 172, w=26, h=20),
                  bot_v2(262, 172), you(38), tag(96, NAME_Y, "手順1"), tag(152, NAME_Y, "手順2"),
                  tag(208, NAME_Y, "手順3"), ai(262)),
            "たとえるなら", "レシピのように、1手順ずつ", "材料 → 作業 → 出来上がり、を小さく分ける"),
    "2-3": (scene(bot_v2(46, 172), gate_v2(118, 172, 1, w=48, h=56), person_v2(180, 172, face="smile"),
                  gate_v2(244, 172, 2, w=48, h=56), ai(46), tag(118, NAME_Y, "確認1"),
                  you(180), tag(244, NAME_Y, "確認2")),
            "たとえるなら", "要所に、チェックポイント", "全部ではなく、2〜3か所で人が確かめる"),
    "2-4": (scene(corkboard_v2(150, 64, w=62, h=42), tag(150, 98, "週報テンプレート"),
                  person_v2(88, 172, face="smile", wave=True), bot_v2(212, 172), sparkle(196, 40), you(88), ai(212)),
            "たとえるなら", "うまくいった型を、掲示板に", "変わる所だけ空けたテンプレートを育てる"),
    # コース3: 競合3社の調査
    "3-1": (scene(person_v2(40, 172, face="smile"), say(40, 106, "要約して", dx=8), bot_v2(96, 172),
                  tag(68, NAME_Y, "チャット：1往復"), bot_v2(208, 172), tab_v2(244, 86, w=30, h=22),
                  tab_v2(264, 112, w=30, h=22, tint=True), tag(248, 60, "自分で調べる"),
                  tag(222, NAME_Y, "エージェント：丸ごと", "ai")),
            "たとえるなら", "1往復か、用事を丸ごとか", "エージェントは、自分で調べて・まとめて・作る"),
    "3-2": (scene(person_v2(64, 172, face="smile", wave=True), blueprint_v2(150, 172, w=58, h=42),
                  tag(150, 110, "任せる前の4つ"), bot_v2(226, 172), tag(250, 84, "NGも決める", "ng"),
                  you(64), ai(226)),
            "たとえるなら", "出発前の、打ち合わせ", "完了の条件・材料・禁止・途中の確認を渡す"),
    "3-3": (scene(person_v2(56, 172, face="smile"), say(56, 106, "3社だけに戻して", dx=22), bot_v2(176, 172),
                  stop_mark_v2(250, 94, r=13), tag(244, 124, "危険なら止める", "ng"), you(56), ai(176)),
            "たとえるなら", "途中で、声をかける", "ずれたら直し、危ない操作の前では止める"),
    "3-4": (scene(bot_v2(60, 172), paper_v2(112, 172, rot=-4), tag(112, 146, "比較表"),
                  magnifier_v2(192, 118, s=1.05), tag(214, 86, "出典を確認"), person_v2(240, 172, face="smile"),
                  ai(60), you(240)),
            "たとえるなら", "持ち帰った成果を、点検する", "形・出どころ・操作の3つを確かめてから使う"),
    # コース4: 総務の社内問い合わせ
    "4-1": (scene(person_v2(62, 172, face="smile", wave=True), desk_v2(156, 172, w=72), envelope_v2(142, 146, s=0.8),
                  envelope_v2(172, 146, s=0.8, rot=8), tag(156, 112, "社内の問い合わせ"), flag_star_v2(246, 172),
                  you(62, "リーダー"), tag(246, NAME_Y, "最初の1つ")),
            "たとえるなら", "小さく始める、最初の一歩", "効果が大きく、進めやすい業務を1つ選ぶ"),
    "4-2": (scene(corkboard_v2(146, 60, w=62, h=42), tag(146, 94, "ルールは1枚"), padlock_v2(200, 52, s=0.8),
                  tag(236, 52, "個人情報", "ng"), person_v2(92, 172, face="smile"), person_v2(146, 172, face="smile"),
                  bot_v2(210, 172), you(119, "チーム"), ai(210)),
            "たとえるなら", "みんなで守る、1枚のルール", "入れてよい情報・確かめる人・相談先を決める"),
    "4-3": (scene(person_v2(40, 172, face="smile"), gate_v2(110, 172, 1, w=42, h=50, level=0),
                  gate_v2(184, 172, 2, w=46, h=58, level=1), gate_v2(256, 172, 3, w=50, h=66, level=3),
                  you(40, "チーム"), tag(110, NAME_Y, "試す"), tag(184, NAME_Y, "広げる"), tag(256, NAME_Y, "定着させる")),
            "たとえるなら", "試す → 広げる → 定着させる", "段階ごとに、期間と見る数字を決める"),
    "4-4": (scene(person_v2(64, 172, face="wow", wave=True), person_v2(116, 172, face="smile"),
                  person_v2(162, 172, face="smile"), bot_v2(214, 172), ribbon_badge_v2(256, 96, s=0.9),
                  tag(252, 66, "成功を共有"), you(64, "推進役"), tag(139, NAME_Y, "メンバー"), ai(214)),
            "たとえるなら", "うまくいったことを、分け合う", "推進役・実務での研修・定期的な振り返り"),
    # コース5: 中2理科「電流と電圧」
    "5-1": (scene(board_v2(150, 118, w=112, h=58), tag(150, 92, "電流と電圧"), person_v2(70, 172, face="smile"),
                  bot_v2(226, 172), paper_v2(270, 172, rot=6), tag(268, 142, "下書き"), you(70, "先生"), ai(226)),
            "たとえるなら", "下ごしらえはAI、味見は先生", "例題やプリントの下書きはAI、ねらいと正確さは先生"),
    "5-2": (scene(person_v2(40, 172, face="smile"), desk_row_v2(174, 172, n=3, gap=56), you(40, "先生"),
                  tag(118, NAME_Y, "基本"), tag(174, NAME_Y, "標準"), tag(230, NAME_Y, "発展"), sparkle(262, 70)),
            "たとえるなら", "同じねらいを、3つの段で", "基本・標準・発展と、やさしい日本語の版"),
    "5-3": (scene(usage_log_v2(150, 84, w=66, h=48), tag(150, 122, "評価の基準表"), person_v2(76, 172, face="smile"),
                  bot_v2(224, 172), padlock_v2(250, 60, s=0.7), tag(250, 88, "個人情報NG", "ng"),
                  you(76, "先生"), ai(224)),
            "たとえるなら", "ものさしを、先にそろえる", "基準表の下書きはAI、成績を決めるのは先生"),
    "5-4": (scene(schoolgate_v2(208, 172, w=66, h=74), person_v2(64, 172, face="smile"),
                  person_v2(116, 172, face="smile", scale=0.85), say(116, 118, "使っていい？", dx=14),
                  you(64, "先生"), tag(116, NAME_Y, "生徒"), tag(208, NAME_Y, "学校の方針")),
            "たとえるなら", "校門をくぐる前に、ルールを", "学校の方針と、年齢の条件を先に確かめる"),
    # コース6: 大学2年のレポート
    "6-1": (scene(person_v2(54, 172, face="smile"), desk_v2(116, 172, w=60), book_v2(116, 144, w=34),
                  bot_v2(200, 172), say(200, 120, "一緒に考えよう"), stop_mark_v2(262, 132, r=11),
                  tag(258, 154, "代筆はNG", "ng"), you(54, "学生"), ai(200)),
            "たとえるなら", "先生役・壁打ち相手・添削役", "代わりに書かせて、そのまま出すのはNG"),
    "6-2": (scene(person_v2(86, 172, face="wow"), say(86, 106, "こう理解したよ", dx=10), bot_v2(192, 172),
                  book_v2(254, 172, w=34), you(86, "学生"), ai(192), tag(254, NAME_Y, "確認問題")),
            "たとえるなら", "自分の理解から、話しはじめる", "たとえ話や確認問題で、一歩ずつ教わる"),
    "6-3": (scene(bot_v2(54, 172), say(54, 120, "この本が参考に", dx=24), person_v2(144, 172, face="smile"),
                  magnifier_v2(174, 116, s=1.0), shelf_v2(240, 172, w=62, h=44), ai(54), you(144, "学生"),
                  tag(240, NAME_Y, "図書館で確認")),
            "たとえるなら", "本棚で、出典を確かめる", "AIが挙げた本が、本当にあるとは限らない"),
    "6-4": (scene(calendar_v2(72, 60, marks=3), tag(72, 90, "学習計画"), person_v2(150, 172, face="wow", wave=True),
                  alarm_clock_v2(238, 172), ribbon_badge_v2(248, 70, s=0.8), tag(248, 98, "できた！"),
                  you(150, "学生"), say(150, 106, "毎日少しずつ")),
            "たとえるなら", "毎日の、小さな練習", "練習問題と計画で、自分で判断する力を育てる"),
    # コース7: 備品貸し出しアプリに検索機能
    "7-1": (scene(person_v2(62, 172, face="smile", wave=True), desk_v2(174, 172, w=84), monitor_v2(160, 144, w=40, h=28),
                  laptop_v2(200, 144, w=30), tag(174, 100, "アプリのコード"), bot_v2(254, 172),
                  you(62), ai(254, "Codex")),
            "たとえるなら", "コードを読める、新しい仲間", "読む・書く・直す・テストするを、続けて進める"),
    "7-2": (scene(person_v2(66, 172, face="smile"), recipe_card_v2(122, 118, rot=-6, dense=True), tag(122, 150, "依頼メモ"),
                  bot_v2(184, 172), corkboard_v2(248, 66, w=56, h=40), tag(248, 98, "AGENTS.md"),
                  you(66), ai(184, "Codex")),
            "たとえるなら", "依頼メモと、共通ルールの掲示板", "4つを入れた依頼と、約束事は AGENTS.md に"),
    "7-3": (scene(person_v2(62, 172, face="smile"), key_v2(92, 112, rot=-25, s=1.2), tag(120, 88, "権限"),
                  bot_v2(166, 172), server_v2(244, 172, w=40, h=56), padlock_v2(244, 94, s=0.9),
                  you(62), ai(166, "Codex"), tag(244, NAME_Y, "本番環境")),
            "たとえるなら", "鍵を渡す範囲を、決めておく", "確認のタイミング・作業範囲・ネットワークは狭く始める"),
    "7-4": (scene(bot_v2(54, 172), tab_v2(116, 84, w=36, h=26), tag(116, 60, "変更前"),
                  tab_v2(176, 84, w=36, h=26, tint=True), tag(176, 60, "変更後"), magnifier_v2(146, 110, s=1.0),
                  tag(146, 154, "差分を見る"), person_v2(248, 172, face="smile"), ai(54, "Codex"), you(248)),
            "たとえるなら", "差分を見てから、取り込む", "差分・テスト・説明を確かめ、小さく取り込む"),
    # コース8: 社内規程に答えるAIチャット
    "8-1": (scene(person_v2(70, 172, face="trouble"), desk_v2(160, 172, w=72), envelope_v2(144, 146, s=0.8),
                  envelope_v2(174, 146, s=0.8, rot=8), tag(160, 110, "月200件の質問"), bot_v2(246, 172),
                  you(70, "総務"), ai(246)),
            "この場面", "毎月200件の、同じような質問", "誰の・どんな困りごとか、AIに向くかを先に決める"),
    "8-2": (scene(shelf_v2(62, 172, w=62, h=44), book_v2(132, 172, w=36), bot_v2(190, 172),
                  say(190, 120, "第5条によると", dx=12), person_v2(260, 172, face="smile"),
                  tag(62, NAME_Y, "規程"), tag(132, NAME_Y, "該当ページ"), ai(190), you(260, "社員")),
            "たとえるなら", "本棚から該当ページを探して答える", "探す → 渡す → 答える → 出典を示す"),
    "8-3": (scene(board_v2(150, 124, w=110, h=62), tag(150, 72, "テスト結果"),
                  bars_v2(116, 118, vals=(10, 18, 14, 26), bw=9, gap=6),
                  person_v2(56, 172, face="smile"), bot_v2(244, 172), you(56), ai(244)),
            "たとえるなら", "毎回、同じテストで測る", "テスト質問集と合格の条件を、先に作る"),
    "8-4": (scene(tag(96, 70, "① 指示"), dashed_arc(126, 66, 142, 66, lift=6), tag(170, 70, "② 検索"),
                  dashed_arc(200, 66, 216, 66, lift=6), tag(248, 70, "③ モデル"),
                  tag(150, 116, "変えたら毎回テスト"), bot_v2(70, 172), person_v2(236, 172, face="smile"),
                  ai(70), you(236)),
            "たとえるなら", "1つずつ変えて、そのたび測る", "指示 → 検索 → モデルの順に、変えるたびテスト"),
}


def icon(inner, vb="0 0 70 70"):
    return f'<svg viewBox="{vb}" width="100%" height="100%" aria-hidden="true">{inner}</svg>'


def centered(part, dx=0, dy=0, s=1.0):
    return f'<g transform="translate({dx},{dy}) scale({s})">{part}</g>'


# 図解ボックスの見出し語 → アイコン＋ひとことラベル（記号だけで意味を読ませない）
ICONS = {
    "stop": (icon(stop_mark_v2(35, 35, r=20)), "NG"),
    "key": (icon(key_v2(35, 18, rot=-30, s=1.25)), "権限"),
    "lock": (icon(padlock_v2(35, 38, s=1.5)), "秘密"),
    "check": (icon(magnifier_v2(31, 29, s=1.25)), "確認"),
    "wifi": (icon(wifi_v2(35, 52, s=1.6)), "ネット"),
    "ai": (icon(bot_v2(35, 62)), "AI"),
    "person": (icon(person_v2(35, 68), vb="0 0 70 74"), "人"),
    "paper": (icon(centered(paper_v2(35, 50, rot=-4), -18, -22, 1.5)), "資料"),
    "calendar": (icon(calendar_v2(35, 36, w=42, h=38, marks=3)), "計画"),
    "clock": (icon(clock_v2(35, 36, r=22, hh=10, mm=10)), "時間"),
    "bars": (icon(bars_v2(14, 58, vals=(14, 26, 20, 38), bw=9, gap=4)), "数字"),
    "book": (icon(centered(book_v2(35, 50, w=50), -8, -14, 1.25)), "規程・本"),
    "flag": (icon(centered(flag_star_v2(35, 60), -30, -34, 1.9)), "ゴール"),
    "bubble": (icon(speech_bubble_v2(35, 54, s=1.1)), "相談"),
    "loop": (icon(loop_icon_v2(35, 35, r=20)), "くり返し"),
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
    icons = {k: {"svg": v[0], "label": v[1]} for k, v in ICONS.items()}
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
        f'<div class="dbox" style="width:150px"><span class="dicon"><span class="dicon-svg">{svg}</span><em>{label}</em></span>'
        f'<div class="dt">{name}</div></div>'
        for name, (svg, label) in ICONS.items()
    )
    (ROOT / "figures-preview.html").write_text(
        '<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="style.css"><title>figures preview</title>'
        '<main class="app body" style="padding-bottom:40px"><h1 class="h1">アイコン</h1>'
        f'<div style="display:flex;flex-wrap:wrap;gap:10px">{icon_cells}</div>'
        f'<h1 class="h1" style="margin-top:20px">シーン</h1><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:10px">{cards}</div></main>',
        encoding="utf-8",
    )
    print(f"scenes: {len(scenes)}  icons: {len(icons)}  -> {out}")


if __name__ == "__main__":
    main()
