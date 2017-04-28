import sys, json, subprocess, shlex;
from RubocopDiffSublime.utils import Utils;

class RubocopRunner(object):
  def __init__(self):
    self.rubocop_config_file = ''
    self.chdir = None

  def run_cmd(self, file_name):
    p=subprocess.Popen(shlex.split(Utils.get_ruby_executable() + " -S rubocop '"+ file_name +"' --format json"), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=Utils.current_project_folder())
    out, err = p.communicate()
    json_offenses = json.loads(out.decode('utf-8'))['files'][0]['offenses']
    return json_offenses

  def get_ruby_executable(self):
    p=subprocess.Popen(" if [ -f $HOME/.rvm/bin/rvm-auto-ruby ]; then echo $HOME/.rvm/bin/rvm-auto-ruby; fi", stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    return out.decode('utf-8').rstrip()