(function () {
  var base = 'https://academy.openai.com/public/courses/';
  window.GUIDE = {
    updated: '2026年9月13日',
    howto: {
      lead: 'OpenAI Academy（オープンエーアイ・アカデミー）は、OpenAI が無料で公開している英語の学習サイトです。日本語で受講するための手順と、どのコースから始めるかの目安をまとめました。',
      steps: [
        '<a href="https://academy.openai.com/pages/courses" target="_blank" rel="noopener">公式のコース一覧</a>を開きます。見るだけならサインインは要りません。',
        '受けたいコースを選び、コースページの「Enroll now（登録する）」を押します。',
        'ChatGPT のアカウントでサインインします。受講は無料です。',
        'コースを始めます。進み具合は自動で保存されるので、途中でやめても続きから再開できます。'
      ],
      notes: [
        { t: 'サインインするアカウントは、先に決めておく', d: '進み具合と修了証は、サインインしたアカウントのメールアドレスに結びつきます。あとから別のアカウントとまとめることはできません。' },
        { t: '修了証は「資格」ではありません', d: 'コースを終えた記録として発行されるもので、OpenAI の公式な認定資格ではありません。コースによっては、確認テストで一定の点数を取ることが修了の条件です（例: AI Foundations は80%以上）。' }
      ],
      tips: [
        { t: 'ページは、ブラウザの翻訳機能で日本語にする', d: 'Chrome なら、ページの何もない所を右クリックして「日本語に翻訳」を選びます。Safari や Edge も、アドレスバー付近の翻訳ボタンから切り替えられます。' },
        { t: '動画は、自動生成の日本語字幕を使う', d: '動画プレーヤーの「CC」ボタンから「日本語 (自動生成)」を選びます。自動生成なので専門用語は訳がずれることがあり、日本語字幕が無い動画もあります。' },
        { t: '英語のまま出てくる言葉は、用語集で確認する', d: 'このアプリの<a href="#/glossary">用語集</a>に、公式コースによく出てくる言葉をまとめています。' },
        { t: '先にこのアプリの講座で「型」をつかむ', d: '同じテーマを日本語で先に学んでおくと、英語のコースでも話の流れを追いやすくなります。' }
      ]
    },
    faq: [
      { q: '公式コースの受講に、お金はかかりますか？', a: '2026年9月時点では、受講は無料です。ChatGPT のアカウントでサインインして受講します。このサイトも無料です。' },
      { q: '英語が苦手でも受けられますか？', a: 'ページはブラウザの翻訳機能で、動画は自動生成の日本語字幕で見られます（字幕がない動画もあります）。先にこのサイトで同じテーマを日本語で学んでおくと、話の流れを追いやすくなります。' },
      { q: 'どのコースから始めればいいですか？', a: '仕事でAIを使うなら、AI Foundations から始めるのが目安です。立場ごとのおすすめは、<a href="#/">ホームのコース診断</a>で確かめられます。' },
      { q: '修了証は資格として使えますか？', a: 'コースを終えた記録で、OpenAI の公式な認定資格ではありません。学習の区切りや、社内での共有に使うものと考えるのが正確です。' },
      { q: '途中でやめても大丈夫ですか？', a: '公式コースは、進み具合が自動で保存されます。このサイトの進み具合は、使っている端末のブラウザに保存されます（別の端末には引き継がれません）。' },
      { q: 'このサイトは、公式教材の翻訳ですか？', a: 'いいえ。このサイトの講座は、同じテーマを独自に解説したオリジナルの教材です。公式の教材や動画は、公式サイトで受講してください。' }
    ],
    cats: [
      {
        name: '仕事でAIを使う', en: 'Apply AI at Work',
        desc: 'はじめてAIを仕事に使う人向け。基本から、くり返し作業の手順化、エージェントへの任せ方まで、上から順に進みます。',
        courses: [
          { ja: 'AIの基礎', en: 'AI Foundations', url: base + 'ai-foundations-dnq5w', lesson: 'c1', toc: 'aif', meta: '所要 約70分／確認テストあり',
            desc: 'AI・大規模言語モデル・ChatGPT の基本と、指示の出し方、材料の渡し方、答えの確かめ方、責任ある使い方を、自分の実際の仕事を題材に練習します。' },
          { ja: '応用・AIの基礎', en: 'Applied AI Foundations', url: base + 'applied-ai-foundations-szsmv', lesson: 'c2', meta: '所要 約80分',
            desc: '1回きりの指示から一歩進んで、作業をステップに分け、AIが役立つ所と人が確認する所を決めて、くり返し使える流れにします。' },
          { ja: 'エージェントとワークフロー', en: 'Agents and Workflows', url: base + 'agents-and-workflows-y0qoc', lesson: 'c3', meta: '所要 約90分',
            desc: '段取りのある作業をエージェントに任せる方法を学びます。材料の渡し方、結果の確認と改善、うまくいったやり方の再利用を練習します。' }
        ]
      },
      {
        name: 'AIで作る', en: 'Build with AI',
        desc: '開発者向け。Codex（コーデックス）と OpenAI の API（エーピーアイ）を使って、AIの仕組みを設計・構築・評価・公開します。下の説明はコース名と公式の分類から要点をまとめたもので、詳しい中身は公式ページで確認してください。',
        courses: [
          { ja: 'AIで解く課題を決める', en: 'Scope AI Solutions', url: base + 'scope-ai-solutions-kjplw', lesson: 'c8', desc: 'AIで何を解決するのか、どこまでを対象にするのかを決める段階を扱います。' },
          { ja: 'AIアプリを評価する', en: 'Evaluate AI Applications', url: base + 'evaluate-ai-applications-pxds7', lesson: 'c8', desc: 'AIを組み込んだアプリの出来をどう測り、改善につなげるかを扱います。' },
          { ja: 'エージェント型の仕組みを設計して作る', en: 'Design and Build Agentic Systems', url: base + 'design-and-build-agentic-systems-k5uke', lesson: 'c8', desc: '自分で判断して動くエージェント型の仕組みを、設計から構築まで扱います。' },
          { ja: '検索と組み合わせたAIを作る', en: 'Build with Retrieval-Augmented Generation', url: base + 'build-with-retrieval-augmented-generation-2v6xg', lesson: 'c8', desc: '手元の文書などを検索し、その内容をもとに答えるAI（RAG＝ラグ）の作り方を扱います。' },
          { ja: 'AIアプリの性能を上げる', en: 'Optimize AI Application Performance', url: base + 'optimize-ai-application-performance-1k50h', lesson: 'c8', desc: 'AIアプリの性能を改善する方法を扱います。' },
          { ja: 'Codex を始める', en: 'Get Started with Codex', url: base + 'get-started-with-codex-jkhsq', lesson: 'c7', desc: 'OpenAI のコーディング用AIエージェント Codex を使い始めるための入門です。' },
          { ja: 'Codex の使い方を広げる', en: 'Extend Codex Workflows', url: base + 'extend-codex-workflows-4e61p', lesson: 'c7', desc: 'Codex を日々の開発の流れに組み込み、使い方を広げていきます。' },
          { ja: 'Codex をチームと仕組みに広げる', en: 'Scale Codex Across Teams and Systems', url: base + 'scale-codex-across-teams-and-systems-jr83a', lesson: 'c7', desc: 'Codex を個人の道具から、チームや組織の仕組みへ広げていきます。' }
        ]
      },
      {
        name: 'AI活用を率いる', en: 'Lead AI Adoption',
        desc: 'リーダー向け。AI施策を1つ題材にして、組織で進めるための計画を作ります。',
        courses: [
          { ja: 'AIリーダーシップ', en: 'AI Leadership', url: base + 'ai-leadership-kaf7k', lesson: 'c4',
            desc: 'AI施策を1つ選び、事業の優先順位とのつなげ方、責任分担とルールづくり、ロードマップ、社内への定着までを考えて、AI戦略の下書きを作ります。' }
        ]
      },
      {
        name: '教える・学ぶ', en: 'Teach and Learn with AI',
        desc: '教育向け。勉強・授業・これからへの備えに、AIをどう使うかを学びます。',
        courses: [
          { ja: '教員のためのAI', en: 'AI for Educators', url: base + 'ai-for-educators-lc8j1', lesson: 'c5', desc: '授業づくりや生徒への指導に、AIをどう役立てるかを扱う教員向けのコースです。' },
          { ja: '大学生のためのAI', en: 'AI for College Students', url: base + 'ai-for-college-students-gxgmr', lesson: 'c6', desc: '勉強を進める、早く身につける、将来に備える、といった場面でのAIの使い方を扱う大学生向けのコースです。' }
        ]
      }
    ]
  };
})();
