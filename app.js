(function () {
  'use strict';

  var KEY = 'ai-shigoto-progress-v1';
  var view = document.getElementById('view');
  var topbar = document.getElementById('topbar');
  var tabsEl = document.getElementById('tabs');
  var toastEl = document.getElementById('toast');

  // 保存できない環境（プライベートブラウズ等）でも表示は壊さない
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || { done: {}, quiz: {}, last: null }; }
    catch (e) { return { done: {}, quiz: {}, last: null }; }
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} }
  var state = load();

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function toast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add('on');
    clearTimeout(toast.t);
    toast.t = setTimeout(function () { toastEl.classList.remove('on'); }, 1800);
  }

  var ICONS = {
    home: '<path d="M4 11l8-7 8 7v8a1 1 0 0 1-1 1h-5v-6h-4v6H5a1 1 0 0 1-1-1z"/>',
    learn: '<path d="M4 5.5A1.5 1.5 0 0 1 5.5 4H11v16H5.5A1.5 1.5 0 0 1 4 18.5zM13 4h5.5A1.5 1.5 0 0 1 20 5.5v13a1.5 1.5 0 0 1-1.5 1.5H13z"/>',
    guide: '<circle cx="12" cy="12" r="8.5"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    glossary: '<path d="M6 4h10a2 2 0 0 1 2 2v14H8a2 2 0 0 1-2-2z"/><path d="M6 18a2 2 0 0 1 2-2h10M10 8h5M10 11h3"/>'
  };
  function icon(name) {
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + ICONS[name] + '</svg>';
  }
  var LOGO = '<svg viewBox="0 0 24 24" fill="none"><path d="M5 7a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-5l-4 3.5V16H7a2 2 0 0 1-2-2z" fill="#fff"/><path d="M12 7.2l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z" fill="#1D8AA6"/></svg>';

  var TABS = [
    { id: 'home', label: 'ホーム', href: '#/' },
    { id: 'learn', label: '講座', href: '#/learn' },
    { id: 'guide', label: '受講ガイド', href: '#/guide' },
    { id: 'glossary', label: '用語集', href: '#/glossary' }
  ];

  function readyLessons() {
    var list = [];
    COURSES.forEach(function (c) {
      c.lessons.forEach(function (l) { if (LESSONS[l.id]) list.push(l.id); });
    });
    return list;
  }
  function courseOf(lessonId) {
    for (var i = 0; i < COURSES.length; i++) {
      for (var j = 0; j < COURSES[i].lessons.length; j++) {
        if (COURSES[i].lessons[j].id === lessonId) return { course: COURSES[i], index: j };
      }
    }
    return null;
  }
  function courseProgress(c) {
    var ready = c.lessons.filter(function (l) { return LESSONS[l.id]; });
    var done = ready.filter(function (l) { return state.done[l.id]; });
    return { ready: ready.length, done: done.length, total: c.lessons.length };
  }
  function nextLesson() {
    var ids = readyLessons();
    if (state.last && LESSONS[state.last] && !state.done[state.last]) return state.last;
    for (var i = 0; i < ids.length; i++) if (!state.done[ids[i]]) return ids[i];
    return ids[0];
  }

  function renderChrome(tab, back) {
    var ids = readyLessons();
    var doneCount = ids.filter(function (id) { return state.done[id]; }).length;
    if (back) {
      topbar.innerHTML = '<button class="back" aria-label="戻る" data-back="' + esc(back.href) + '">‹</button>' +
        '<div class="brand">' + esc(back.title) + '<small>無料AIスクール 日本語ガイド</small></div>';
    } else {
      topbar.innerHTML = '<div class="logo">' + LOGO + '</div>' +
        '<div class="brand">無料AIスクール 日本語ガイド<small>試作版・非公式</small></div>' +
        '<span class="chip">完了 ' + doneCount + ' / ' + ids.length + '</span>';
    }
    tabsEl.innerHTML = TABS.map(function (t) {
      return '<a class="tab" href="' + t.href + '"' + (t.id === tab ? ' aria-current="page"' : '') + '>' + icon(t.id) + '<span>' + t.label + '</span></a>';
    }).join('');
  }

  function courseCard(c) {
    var p = courseProgress(c);
    var pct = p.ready ? Math.round(p.done / p.total * 100) : 0;
    var status = p.ready === 0 ? '<span class="badge soon">準備中</span>'
      : (p.done === p.ready && p.ready === p.total ? '<span class="badge done">修了</span>' : '<span class="muted">' + p.done + ' / ' + p.total + ' レッスン</span>');
    return '<a class="card course" href="#/course/' + c.id + '">' +
      '<div class="num">' + c.no + '</div><div style="flex:1">' +
      '<h3>' + esc(c.title) + '</h3><p>' + esc(c.desc) + '</p>' +
      '<div class="meta"><div class="bar"><i style="width:' + pct + '%"></i></div>' + status + '</div></div></a>';
  }

  function coursesByGroup() {
    return GROUPS.map(function (g) {
      var list = COURSES.filter(function (c) { return c.group === g.id; });
      return '<div class="sec-title">' + esc(g.name) + '<span class="grp-sub">' + esc(g.desc) + '</span></div>' + list.map(courseCard).join('');
    }).join('');
  }

  function foot() {
    return '<p class="foot">このアプリは個人が作成した非公式の学習教材で、OpenAI および OpenAI Academy とは関係ありません。' +
      '外部サイトの内容・動画の権利は、それぞれの提供元にあります。掲載情報は ' + esc(GUIDE.updated) + ' 時点のものです。</p>';
  }

  function pageHome() {
    renderChrome('home');
    var ids = readyLessons();
    var doneCount = ids.filter(function (id) { return state.done[id]; }).length;
    var nxt = nextLesson();
    var started = doneCount > 0 || state.last;
    view.innerHTML =
      '<section class="hero"><div class="ring"></div>' +
      '<div class="kicker" style="color:rgba(255,255,255,.75)">無料・日本語・スマホで学べる</div>' +
      '<h1 class="h1">AIに「仕事を任せられる人」になる</h1>' +
      '<p>指示の出し方やエージェントへの任せ方から、チームでの導入・教育・開発まで。1レッスン10分前後で、ChatGPTで試しながら進めます。</p>' +
      '<div class="hero-stats"><div><b>' + doneCount + '</b><span>完了レッスン</span></div>' +
      '<div><b>' + COURSES.length + '</b><span>コース</span></div>' +
      '<div><b>' + GUIDE.cats.reduce(function (n, c) { return n + c.courses.length; }, 0) + '</b><span>公式コースの受講ガイド</span></div></div>' +
      '<a class="btn" href="#/lesson/' + nxt + '">' + (started ? '続きから学ぶ' : '最初のレッスンを始める') + ' →</a></section>' +
      coursesByGroup() +
      '<div class="sec-title">公式の無料コースも受けたい人へ</div>' +
      '<a class="card course" href="#/guide"><div class="num">' + icon('guide') + '</div><div style="flex:1">' +
      '<h3>OpenAI Academy の受講ガイド</h3><p>英語の公式コースを、日本語で受講するための手順と、どのコースから始めるかの目安をまとめています。</p></div></a>' +
      foot();
  }

  function pageLearn() {
    renderChrome('learn');
    view.innerHTML = '<h1 class="h1">講座</h1><p class="lead">まずは「仕事でAIを使う」の3コースから。そのあとは、立場に合わせて選んでください。1レッスン10分前後で、途中でやめても進み具合は残ります。</p>' +
      coursesByGroup() + foot();
  }

  function pageCourse(id) {
    var c = COURSES.filter(function (x) { return x.id === id; })[0];
    if (!c) return pageLearn();
    renderChrome('learn', { href: '#/learn', title: 'コース' + c.no });
    var p = courseProgress(c);
    view.innerHTML = '<div class="kicker">コース' + c.no + '</div><h1 class="h1">' + esc(c.title) + '</h1>' +
      '<p class="lead">' + esc(c.desc) + '</p>' +
      '<div class="goal"><b>このコースで身につくこと</b><br>' + esc(c.outcome) + '</div>' +
      '<div class="card" style="margin-top:16px">' + c.lessons.map(function (l, i) {
        var ready = !!LESSONS[l.id];
        var done = state.done[l.id];
        return '<a class="lesson-row' + (ready ? '' : ' off') + '" href="#/lesson/' + l.id + '">' +
          '<span class="dot' + (done ? ' ok' : '') + '">' + (done ? '✓' : i + 1) + '</span>' +
          '<span class="t">' + esc(l.title) + '</span>' +
          (ready ? '<span class="muted">' + l.min + '分</span>' : '<span class="badge soon">準備中</span>') + '</a>';
      }).join('') + '</div>' +
      (p.ready ? '<p class="muted" style="margin-top:10px">' + p.done + ' / ' + p.total + ' レッスン完了</p>' : '') + foot();
  }

  function videoBlock(v) {
    if (!v) return '';
    var src = 'https://player.vimeo.com/video/' + encodeURIComponent(v.id) + '?dnt=1&title=0&byline=0&portrait=0&texttrack=ja-x-autogen';
    return '<h2>動画で見る</h2><p>' + v.note + '</p>' +
      '<div class="video"><iframe src="' + src + '" title="' + esc(v.title) + '" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe></div>' +
      '<p class="muted">字幕が英語のときは、プレーヤーの「CC」から「日本語 (自動生成)」を選んでください。表示されない場合は <a href="https://vimeo.com/' + encodeURIComponent(v.id) + '" target="_blank" rel="noopener">Vimeoで開く</a></p>';
  }

  function officialFor(id, c) {
    return OFFICIAL.lessons[id] || OFFICIAL.courses[c.id];
  }

  function officialBlock(id, c) {
    var o = officialFor(id, c);
    if (!o) return '';
    var items = o.items || [];
    var hasVideo = items.some(function (it) { return it.video; });
    var heading = hasVideo ? '公式の動画で学ぶ' : (o.type === 'player' ? '公式レッスンで学ぶ' : '公式コースで学ぶ');
    var label = hasVideo ? '公式コースで動画を見る（要サインイン）'
      : (o.type === 'player' ? '公式コースで読む（要サインイン）' : '公式コースを開く（要サインイン）');
    var list = items.length
      ? '<p style="margin:6px 0 4px">公式コース「' + esc(o.name) + '」の、次のレッスンで同じテーマを学べます。</p><ul class="offlist">' +
        items.map(function (it) {
          return '<li><b>' + esc(it.lesson) + '</b>' + (it.video ? ' <span class="badge ai">動画あり</span>' : '') +
            '<span class="sub">' + esc(it.module) + '</span></li>';
        }).join('') + '</ul>'
      : '<p style="margin:6px 0 12px">このテーマに対応する公式コース「' + esc(o.name) + '」を開きます。</p>';
    return '<h2>' + heading + '</h2><div class="card offcard">' +
      '<div class="kicker">OpenAI Academy（英語・要サインイン）</div>' + list +
      '<a class="btn wide" href="' + esc(o.url) + '" target="_blank" rel="noopener">' + label + ' ↗</a>' +
      '<details><summary>' + (hasVideo ? '日本語字幕の出し方' : '日本語で読むコツ') + '</summary><ol>' +
      '<li>初めて開くときは、コースページで「Enroll now（登録する）」を押し、ChatGPT のアカウントでサインインします。</li>' +
      (items.length ? '<li>コースの画面が開いたら、レッスンの一覧から上のレッスン名を選びます。</li>' : '') +
      (hasVideo
        ? '<li>動画プレーヤーの「CC」（字幕）ボタンを押し、「日本語 (自動生成)」があれば選びます。自動生成なので、専門用語は訳がずれることがあります。</li>' +
          '<li>日本語が選べない動画もあります。そのときは英語字幕をオンにして、このアプリの解説と<a href="#/glossary">用語集</a>を手がかりに見てください。</li>'
        : '<li>ページの文章は、ブラウザの翻訳機能（Chrome なら右クリック →「日本語に翻訳」）で日本語にできます。</li>') +
      '</ol></details></div>';
  }

  function quizBlock(id, quiz) {
    var saved = state.quiz[id] || {};
    return '<h2>確認クイズ</h2><div class="quiz">' + quiz.map(function (q, qi) {
      var answered = saved[qi] !== undefined;
      return '<div class="q" data-q="' + qi + '"><div class="q-t">Q' + (qi + 1) + '. ' + esc(q.q) + '</div>' +
        q.opts.map(function (o, oi) {
          var cls = '';
          if (answered && oi === q.a) cls = ' right';
          else if (answered && oi === saved[qi]) cls = ' wrong';
          return '<button class="opt' + cls + '" data-o="' + oi + '"' + (answered ? ' disabled' : '') + '>' + esc(o) + '</button>';
        }).join('') +
        '<div class="explain"' + (answered ? '' : ' hidden') + '>' + (answered ? (saved[qi] === q.a ? '⭕ 正解。' : '❌ 正解は「' + esc(q.opts[q.a]) + '」。') + esc(q.ex) : '') + '</div></div>';
    }).join('') + '</div>';
  }

  function pageLesson(id) {
    var L = LESSONS[id];
    var where = courseOf(id);
    if (!L || !where) return pageLearn();
    var c = where.course;
    state.last = id; save();
    renderChrome('learn', { href: '#/course/' + c.id, title: 'コース' + c.no + '・レッスン' + (where.index + 1) });
    var readyIds = c.lessons.map(function (l) { return l.id; }).filter(function (x) { return LESSONS[x]; });
    var pos = readyIds.indexOf(id);
    var prev = readyIds[pos - 1], next = readyIds[pos + 1];
    var nextCourse = COURSES.filter(function (x, i) { return i > COURSES.indexOf(c) && x.group === c.group; })[0];
    var nextCourseFirst = nextCourse && nextCourse.lessons.filter(function (l) { return LESSONS[l.id]; })[0];
    view.innerHTML =
      '<div class="kicker">コース' + c.no + '　' + esc(c.title) + '</div>' +
      '<h1 class="h1">' + esc(L.title) + '</h1><p class="muted">所要 ' + L.min + ' 分</p>' +
      '<div class="goal"><b>このレッスンのゴール</b><br>' + esc(L.goal) + '</div>' +
      '<article class="body">' + L.body +
      '<h2>ChatGPTで試してみる</h2><p>' + L.prompt.lead + '</p>' +
      '<div class="prompt"><div class="prompt-head"><span>' + esc(L.prompt.label) + '</span><button class="copy" data-copy="1">コピー</button></div><pre>' + esc(L.prompt.text) + '</pre></div>' +
      videoBlock(L.video) + officialBlock(id, c) + quizBlock(id, L.quiz) +
      '<h2>次の一歩</h2><div class="card"><p style="margin:0">' + L.next.text + '</p>' +
      (L.next.href && L.next.href !== (officialFor(id, c) || {}).url ? '<p style="margin:10px 0 0"><a class="btn sub" href="' + esc(L.next.href) + '" target="_blank" rel="noopener">' + esc(L.next.label) + ' ↗</a></p>' : '') + '</div>' +
      '</article>' +
      '<div style="margin-top:18px">' + (state.done[id]
        ? '<button class="btn sub wide" data-undone="1">✓ 完了済み（未完了に戻す）</button>'
        : '<button class="btn wide" data-done="1">このレッスンを完了にする</button>') + '</div>' +
      '<div class="pager">' +
      (prev ? '<a class="btn sub" href="#/lesson/' + prev + '">← 前へ</a>' : '<a class="btn sub" href="#/course/' + c.id + '">コース一覧</a>') +
      (next ? '<a class="btn" href="#/lesson/' + next + '">次へ →</a>'
        : nextCourseFirst ? '<a class="btn" href="#/lesson/' + nextCourseFirst.id + '">次のコースへ →</a>'
        : '<a class="btn" href="#/course/' + c.id + '">コースに戻る</a>') +
      '</div>' + foot();

    view.querySelector('[data-copy]').addEventListener('click', function () { copyText(L.prompt.text); });
    view.querySelectorAll('.q').forEach(function (qEl) {
      qEl.querySelectorAll('.opt').forEach(function (btn) {
        btn.addEventListener('click', function () { answer(id, L, qEl, +qEl.dataset.q, +btn.dataset.o); });
      });
    });
    var d = view.querySelector('[data-done]');
    if (d) d.addEventListener('click', function () { setDone(id, true); });
    var u = view.querySelector('[data-undone]');
    if (u) u.addEventListener('click', function () { setDone(id, false); });
  }

  function answer(id, L, qEl, qi, oi) {
    var q = L.quiz[qi];
    state.quiz[id] = state.quiz[id] || {};
    state.quiz[id][qi] = oi;
    qEl.querySelectorAll('.opt').forEach(function (b, i) {
      b.disabled = true;
      if (i === q.a) b.classList.add('right');
      else if (i === oi) b.classList.add('wrong');
    });
    var ex = qEl.querySelector('.explain');
    ex.hidden = false;
    ex.textContent = (oi === q.a ? '⭕ 正解。' : '❌ 正解は「' + q.opts[q.a] + '」。') + q.ex;
    var allAnswered = L.quiz.every(function (_, i) { return state.quiz[id][i] !== undefined; });
    if (allAnswered && !state.done[id]) { setDone(id, true); return; }
    save();
  }

  function setDone(id, v) {
    if (v) state.done[id] = true; else delete state.done[id];
    save();
    var y = window.scrollY;
    route();
    window.scrollTo(0, y);
    toast(v ? 'レッスン完了！' : '未完了に戻しました');
  }

  function copyText(text) {
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); toast('コピーしました'); } catch (e) { toast('コピーできませんでした'); }
      document.body.removeChild(ta);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { toast('コピーしました'); }, fallback);
    } else { fallback(); }
  }

  function pageGuide() {
    renderChrome('guide');
    var h = GUIDE.howto;
    view.innerHTML = '<h1 class="h1">OpenAI Academy 受講ガイド</h1>' +
      '<p class="lead">' + h.lead + '</p>' +
      '<div class="sec-title">受講のしかた</div><div class="card body"><ol class="steps">' +
      h.steps.map(function (s) { return '<li>' + s + '</li>'; }).join('') + '</ol>' +
      h.notes.map(function (n) { return '<div class="note warn"><span class="nt">' + esc(n.t) + '</span>' + n.d + '</div>'; }).join('') + '</div>' +
      '<div class="sec-title">日本語で受講するコツ</div><div class="card body">' +
      h.tips.map(function (t) { return '<p><strong>' + esc(t.t) + '</strong><br>' + t.d + '</p>'; }).join('') + '</div>' +
      '<div class="sec-title">コース一覧（' + GUIDE.updated + ' 時点）</div>' +
      GUIDE.cats.map(function (cat) {
        return '<div class="cat"><h2>' + esc(cat.name) + '</h2><p class="muted" style="margin-bottom:8px">' + esc(cat.desc) + '</p>' +
          cat.courses.map(function (c) {
            return '<div class="card gcourse"><h3>' + esc(c.ja) + '<span class="en">' + esc(c.en) + '</span></h3>' +
              '<p>' + esc(c.desc) + '</p>' + (c.meta ? '<p class="muted">' + esc(c.meta) + '</p>' : '') +
              '<div class="links"><a href="' + esc(c.url) + '" target="_blank" rel="noopener">公式ページを開く（英語）↗</a>' +
              (c.lesson ? '　·　<a href="#/course/' + c.lesson + '">このアプリの関連コース</a>' : '') + '</div></div>';
          }).join('') + '</div>';
      }).join('') + foot();
  }

  function pageGlossary() {
    renderChrome('glossary');
    view.innerHTML = '<h1 class="h1">用語集</h1><p class="lead">講座や公式コースに出てくる言葉を、ひとことで。</p>' +
      '<input class="search" type="search" placeholder="用語をさがす（例: プロンプト）" aria-label="用語をさがす" style="margin-top:14px">' +
      '<div class="card" style="margin-top:12px" id="terms"></div>' + foot();
    var input = view.querySelector('.search');
    var box = view.querySelector('#terms');
    function draw() {
      var k = input.value.trim().toLowerCase();
      var hit = GLOSSARY.filter(function (g) {
        return !k || (g.term + g.read + g.desc).toLowerCase().indexOf(k) !== -1;
      });
      box.innerHTML = hit.length ? hit.map(function (g) {
        return '<div class="term"><b>' + esc(g.term) + '</b>' + (g.read ? ' <span class="muted">' + esc(g.read) + '</span>' : '') + '<p>' + esc(g.desc) + '</p></div>';
      }).join('') : '<p class="muted">見つかりませんでした。</p>';
    }
    input.addEventListener('input', draw);
    draw();
  }

  function route() {
    var parts = (location.hash.replace(/^#\/?/, '') || '').split('/');
    var name = parts[0];
    if (name === 'learn') pageLearn();
    else if (name === 'course') pageCourse(parts[1]);
    else if (name === 'lesson') pageLesson(parts[1]);
    else if (name === 'guide') pageGuide();
    else if (name === 'glossary') pageGlossary();
    else pageHome();
    var h1 = view.querySelector('.h1');
    document.title = (h1 && name ? h1.textContent + '｜' : '') + '無料AIスクール 日本語ガイド';
  }

  topbar.addEventListener('click', function (e) {
    var b = e.target.closest('[data-back]');
    if (b) location.hash = b.getAttribute('data-back');
  });
  window.addEventListener('hashchange', function () { route(); window.scrollTo(0, 0); });
  route();
})();
