(function () {
  var base = 'https://academy.openai.com/public/courses/';
  var AIF_PLAYER = 'https://academy.openai.com/learning-path/ai-foundations-dnq5w/learn/ai-foundations-juzjs/lessons/ai-foundations-8dlkt';
  // type: 'player' は公式の受講画面（要サインイン）、'course' は公開のコースページ。
  // レッスン名（英語）は受講画面の表示どおり。ja・topic・note は目次として自前で書いた短い説明（2026-09-13 時点）。
  var AIF = {
    m1: 'Module 1: Introduction', m2: 'Module 2: Large Language Models', m3: 'Module 3: Prompting and Evaluation',
    m4: 'Module 4: Add Context', m5: 'Module 5: Responsible Use'
  };
  window.OFFICIAL = {
    courses: {
      c1: { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m1, lesson: '1.1 Welcome to AI Foundations', ja: 'ようこそ', topic: 'コースの目的と進め方', video: true }
      ] },
      c2: { name: 'Applied AI Foundations', type: 'course', url: base + 'applied-ai-foundations-szsmv' },
      c3: { name: 'Agents and Workflows', type: 'course', url: base + 'agents-and-workflows-y0qoc' },
      c4: { name: 'AI Leadership', type: 'course', url: base + 'ai-leadership-kaf7k' },
      c5: { name: 'AI for Educators', type: 'course', url: base + 'ai-for-educators-lc8j1' },
      c6: { name: 'AI for College Students', type: 'course', url: base + 'ai-for-college-students-gxgmr' },
      c7: { name: 'Get Started with Codex', type: 'course', url: base + 'get-started-with-codex-jkhsq' },
      c8: { name: 'Scope AI Solutions', type: 'course', url: base + 'scope-ai-solutions-kjplw' }
    },
    lessons: {
      '1-1': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m1, lesson: '1.1 Welcome to AI Foundations', ja: 'ようこそ', topic: 'コースの目的と進め方', video: true },
        { module: AIF.m2, lesson: '2.2 What LLMs can do', ja: 'LLM にできること', topic: '得意なことと、仕組みからくる限界', video: false },
        { module: AIF.m2, lesson: '2.5 Why AI needs human review', ja: '人の確認が必要な理由', topic: 'もっともらしい間違いへの備え', video: false }
      ] },
      '1-5': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m2, lesson: '2.3 How models are trained', ja: 'モデルの学習のされ方', topic: '作られる段階と、AIの「学ぶ」の意味', video: false }
      ] },
      '1-6': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m2, lesson: '2.1 What is AI?', ja: 'AIとは', topic: 'ChatGPT でできることの全体像', video: true },
        { module: AIF.m4, lesson: '4.3 Use files', ja: 'ファイルを使う', topic: '資料を渡して任せる', video: false },
        { module: AIF.m4, lesson: '4.5 Save useful preferences', ja: 'よく使う設定を保存する', topic: '毎回の前提を覚えさせる', video: false }
      ] },
      '1-2': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m3, lesson: '3.1 Why clear instructions matter', ja: '明確な指示が大事な理由', topic: 'あいまいな頼み方で起きること', video: true },
        { module: AIF.m3, lesson: '3.2 Task, Concept, and Expectation', ja: '依頼を組み立てる3つの要素', topic: '何を・どんな前提で・どう仕上げるか', video: false }
      ] },
      '1-3': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m4, lesson: '4.1 Why context matters', ja: '文脈が大事な理由', topic: '指示だけでは足りないとき', video: false },
        { module: AIF.m4, lesson: '4.2 What context to add', ja: '足す文脈の選び方', topic: '必要な情報だけを選ぶ', video: false }
      ] },
      '1-7': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m2, lesson: '2.4 Know when to use trusted sources', ja: '信頼できる情報源を使う場面', topic: '正確さが要る情報の扱い', video: false },
        { module: AIF.m4, lesson: '4.4 Use search', ja: '検索を使う', topic: '新しい情報を調べて使う', video: false }
      ] },
      '1-4': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m3, lesson: '3.3 Review the output', ja: '出力を見直す', topic: '観点を決めて読み直す', video: false },
        { module: AIF.m3, lesson: '3.4 Improve the output', ja: '出力を良くする', topic: '直してもらう頼み方', video: false }
      ] },
      '1-8': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: AIF.m5, lesson: '5.1 Use ChatGPT responsibly', ja: '責任を持って使う', topic: '使う前に考えること', video: true },
        { module: AIF.m5, lesson: '5.2 Share information carefully', ja: '情報を慎重に共有する', topic: '渡す情報を減らす', video: false },
        { module: AIF.m5, lesson: '5.3 Keep yourself in the loop', ja: '自分が判断に関わり続ける', topic: '影響に合わせた確認', video: false }
      ] },
      '7-3': { name: 'Extend Codex Workflows', type: 'course', url: base + 'extend-codex-workflows-4e61p' },
      '7-4': { name: 'Scale Codex Across Teams and Systems', type: 'course', url: base + 'scale-codex-across-teams-and-systems-jr83a' },
      '8-2': { name: 'Build with Retrieval-Augmented Generation', type: 'course', url: base + 'build-with-retrieval-augmented-generation-2v6xg' },
      '8-3': { name: 'Evaluate AI Applications', type: 'course', url: base + 'evaluate-ai-applications-pxds7' },
      '8-4': { name: 'Optimize AI Application Performance', type: 'course', url: base + 'optimize-ai-application-performance-1k50h' }
    },
    // 受講ガイドに出す「受講画面の目次」
    toc: {
      aif: { name: 'AI Foundations', url: AIF_PLAYER, updated: '2026年9月13日', modules: [
        { name: AIF.m1, ja: '導入', note: 'コースの進め方', lessons: [
          { t: '1.1 Welcome to AI Foundations', ja: 'ようこそ', video: true },
          { t: '1.2 Learn with ChatGPT', ja: 'ChatGPT で学ぶ' },
          { t: '1.3 Check-in', ja: '振り返り' }
        ] },
        { name: AIF.m2, ja: '大規模言語モデル', note: 'AI と LLM の基本と、その限界', lessons: [
          { t: '2.1 What is AI?', ja: 'AIとは', video: true },
          { t: '2.2 What LLMs can do', ja: 'LLM にできること' },
          { t: '2.3 How models are trained', ja: 'モデルの学習のされ方' },
          { t: '2.4 Know when to use trusted sources', ja: '信頼できる情報源を使う場面' },
          { t: '2.5 Why AI needs human review', ja: '人の確認が必要な理由' },
          { t: '2.6 Check-in', ja: '振り返り' }
        ] },
        { name: AIF.m3, ja: '指示と評価', note: '指示の組み立て方と、出力の見直し方', lessons: [
          { t: '3.1 Why clear instructions matter', ja: '明確な指示が大事な理由', video: true },
          { t: '3.2 Task, Concept, and Expectation', ja: '依頼を組み立てる3つの要素' },
          { t: '3.3 Review the output', ja: '出力を見直す' },
          { t: '3.4 Improve the output', ja: '出力を良くする' },
          { t: '3.5 Check your knowledge', ja: '理解度チェック' },
          { t: '3.6 Check-in', ja: '振り返り' }
        ] },
        { name: AIF.m4, ja: '文脈を足す', note: 'ファイル・検索・保存した設定の使い方', lessons: [
          { t: '4.1 Why context matters', ja: '文脈が大事な理由' },
          { t: '4.2 What context to add', ja: '足す文脈の選び方' },
          { t: '4.3 Use files', ja: 'ファイルを使う' },
          { t: '4.4 Use search', ja: '検索を使う' },
          { t: '4.5 Save useful preferences', ja: 'よく使う設定を保存する' },
          { t: '4.6 Check-in', ja: '振り返り' }
        ] },
        { name: AIF.m5, ja: '責任ある使い方', note: '安全に使うための確認', lessons: [
          { t: '5.1 Use ChatGPT responsibly', ja: '責任を持って使う', video: true },
          { t: '5.2 Share information carefully', ja: '情報を慎重に共有する' },
          { t: '5.3 Keep yourself in the loop', ja: '自分が判断に関わり続ける' },
          { t: '5.4 Make a responsible choice', ja: '責任ある選び方' },
          { t: '5.5 Check-in', ja: '振り返り' }
        ] },
        { name: 'Recap', ja: 'まとめ', note: '', lessons: [
          { t: 'Conclusion and feedback', ja: 'まとめとフィードバック' }
        ] }
      ] }
    }
  };
})();
