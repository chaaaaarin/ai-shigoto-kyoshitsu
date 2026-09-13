(function () {
  var base = 'https://academy.openai.com/public/courses/';
  var AIF_PLAYER = 'https://academy.openai.com/learning-path/ai-foundations-dnq5w/learn/ai-foundations-juzjs/lessons/ai-foundations-8dlkt';
  // type: 'player' は受講画面（要サインイン）＋コース内で見るレッスン名、'course' は公開のコースページ。
  // items の lesson/module は受講者が受講画面から控えた名前（2026-09-13 時点）。
  window.OFFICIAL = {
    courses: {
      c1: { name: 'AI Foundations', type: 'player', url: AIF_PLAYER,
            items: [{ module: 'Module 1: Introduction', lesson: '1.1 Welcome to AI Foundations', video: true }] },
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
        { module: 'Module 1: Introduction', lesson: '1.1 Welcome to AI Foundations', video: true },
        { module: 'Module 2: Large Language Models', lesson: '2.1 What is AI?', video: true }
      ] },
      '1-2': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: 'Module 3: Prompting and Evaluation', lesson: '3.1 Why clear instructions matter', video: true }
      ] },
      '1-3': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: 'Module 4: Add Context', lesson: '4.1 Why context matters', video: false },
        { module: 'Module 4: Add Context', lesson: '4.2 What context to add', video: false }
      ] },
      '1-4': { name: 'AI Foundations', type: 'player', url: AIF_PLAYER, items: [
        { module: 'Module 3: Prompting and Evaluation', lesson: '3.3 Review the output', video: false },
        { module: 'Module 5: Responsible Use', lesson: '5.1 Use ChatGPT responsibly', video: true }
      ] },
      '7-3': { name: 'Extend Codex Workflows', type: 'course', url: base + 'extend-codex-workflows-4e61p' },
      '7-4': { name: 'Scale Codex Across Teams and Systems', type: 'course', url: base + 'scale-codex-across-teams-and-systems-jr83a' },
      '8-2': { name: 'Build with Retrieval-Augmented Generation', type: 'course', url: base + 'build-with-retrieval-augmented-generation-2v6xg' },
      '8-3': { name: 'Evaluate AI Applications', type: 'course', url: base + 'evaluate-ai-applications-pxds7' },
      '8-4': { name: 'Optimize AI Application Performance', type: 'course', url: base + 'optimize-ai-application-performance-1k50h' }
    }
  };
})();
