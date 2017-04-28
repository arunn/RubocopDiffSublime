import sublime, sublime_plugin, json
from RubocopDiff.git_diff_lines import GitDiffLines;
from RubocopDiff.utils import Utils;
from RubocopDiff.rubocop_runner import RubocopRunner;
class SetMarkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      view = self.view
      file_name = view.file_name()
      if Utils.is_ruby_file(view.settings()):
        lines = GitDiffLines().get_diff_lines(file_name)
        if not lines:
          return
        rubocop_offenses = RubocopRunner().run_cmd(file_name)
        offense_dict = Utils.get_offense_diff(rubocop_offenses, lines)
        marks = Utils.get_marks(view, offense_dict)
        
        offense_dict_str = json.dumps(offense_dict)
        view.settings().set("rubocop_diff", offense_dict_str)
        view.add_regions("rubocop_marks", marks, "keyword", "arrow_right", sublime.DRAW_EMPTY | sublime.DRAW_NO_OUTLINE | sublime.DRAW_NO_FILL | sublime.DRAW_SQUIGGLY_UNDERLINE | sublime.HIDE_ON_MINIMAP)