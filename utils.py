import sys, os, sublime, subprocess, shlex;

RUBY_SYNTAX_FILES = [
  'Ruby.sublime-syntax',
  'Ruby on Rails.sublime-syntax',
  'RSpec.sublime-syntax'
]

class Utils(object):

  @staticmethod
  def get_ruby_executable():
    p=subprocess.Popen(" if [ -f $HOME/.rvm/bin/rvm-auto-ruby ]; then echo $HOME/.rvm/bin/rvm-auto-ruby; fi", stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out.decode('utf-8').rstrip()

  @staticmethod
  def is_ruby_file(settings):
    syntax_file = settings.get('syntax')
    if syntax_file == None:
      return False

    for syntax in RUBY_SYNTAX_FILES:
      if syntax_file.endswith(syntax):
        return True

    return False


  @staticmethod
  def current_project_folder():
    project = sublime.active_window().project_data()
    project_base_path = os.path.dirname(sublime.active_window().project_file_name() or '')
    if not (project is None):
      if 'folders' in project:
        folders = project['folders']
        if len(folders) > 0:
          first_folder = folders[0]
          if 'path' in first_folder:
            path = first_folder['path']
            return (path if os.path.isabs(path) else os.path.join(project_base_path, path)) or ''
    return ''

  @staticmethod
  def get_marks(view, offense_dict):
    marks = []
    for line in offense_dict.keys():
      pt = view.text_point(line - 1, 0)
      marks.append(view.line(pt))
    return marks

  @staticmethod
  def get_offense_diff(rubocop_offenses, diff_line_numbers):
    diff_offenses = {}
    for offense in rubocop_offenses:
      line = int(offense['location']['line'])
      if line in diff_line_numbers:
        if diff_offenses.get(line) !=  None:
          diff_offenses[line].append(offense['message'])
        else:
          diff_offenses[line] = [offense['message']]
    return diff_offenses