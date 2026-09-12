(function () {
  var base = 'https://academy.openai.com/public/courses/';
  // type: 'lesson' は受講者から受け取った動画つきレッスンのURL、'course' は公開のコースページ
  window.OFFICIAL = {
    courses: {
      c1: { name: 'AI Foundations', type: 'lesson', url: 'https://academy.openai.com/learning-path/ai-foundations-dnq5w/learn/ai-foundations-juzjs/lessons/ai-foundations-8dlkt' },
      c2: { name: 'Applied AI Foundations', type: 'course', url: base + 'applied-ai-foundations-szsmv' },
      c3: { name: 'Agents and Workflows', type: 'course', url: base + 'agents-and-workflows-y0qoc' },
      c4: { name: 'AI Leadership', type: 'course', url: base + 'ai-leadership-kaf7k' },
      c5: { name: 'AI for Educators', type: 'course', url: base + 'ai-for-educators-lc8j1' },
      c6: { name: 'AI for College Students', type: 'course', url: base + 'ai-for-college-students-gxgmr' },
      c7: { name: 'Get Started with Codex', type: 'course', url: base + 'get-started-with-codex-jkhsq' },
      c8: { name: 'Scope AI Solutions', type: 'course', url: base + 'scope-ai-solutions-kjplw' }
    },
    lessons: {
      '7-3': { name: 'Extend Codex Workflows', type: 'course', url: base + 'extend-codex-workflows-4e61p' },
      '7-4': { name: 'Scale Codex Across Teams and Systems', type: 'course', url: base + 'scale-codex-across-teams-and-systems-jr83a' },
      '8-2': { name: 'Build with Retrieval-Augmented Generation', type: 'course', url: base + 'build-with-retrieval-augmented-generation-2v6xg' },
      '8-3': { name: 'Evaluate AI Applications', type: 'course', url: base + 'evaluate-ai-applications-pxds7' },
      '8-4': { name: 'Optimize AI Application Performance', type: 'course', url: base + 'optimize-ai-application-performance-1k50h' }
    }
  };
})();
