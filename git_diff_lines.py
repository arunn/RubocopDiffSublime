import sys, json, subprocess, shlex, re, sublime, sublime_plugin;
from RubocopDiffSublime.utils import Utils;

class GitDiffLines(object):
  def __init__(self):
    return None

  def get_diff_lines(self, file_name):
    normal_diff_line_numbers = self.get_diff(file_name, "")
    staged_diff_line_numbers = self.get_diff(file_name, "--cached")
    return normal_diff_line_numbers + staged_diff_line_numbers

  def get_diff(self, file_name, options):
    p=subprocess.Popen(shlex.split("git diff --unified=0 --no-ext-diff "+ options + " '"+ file_name +"'"), 
      shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=Utils.current_project_folder())
    return self.get_line_numbers(p)

  def get_line_numbers(self, p):
    out, err = p.communicate()
    lines_in_diff_output = out.decode('utf-8').splitlines()
    diff_line_numbers = []
    for line in lines_in_diff_output:
      match=re.match("\A@@ -[0-9]+(,[0-9]+)? \+([0-9]+)(,[0-9]+)? @@", line)
      if match:
        if match.group(3) != ",0": # A line has been deleted from the code. We do not need to worry.
          starting_line_number = int(match.group(2))
          total_line_changes = 1
          if match.group(3) != None:
            total_line_changes = int(match.group(3)[1:])
          lines_to_be_added = list(range(starting_line_number, starting_line_number + total_line_changes))
          diff_line_numbers += lines_to_be_added
    return diff_line_numbers