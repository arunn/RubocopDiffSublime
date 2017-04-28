import sublime, sublime_plugin, json
from RubocopDiff.utils import Utils;

class Listeners(sublime_plugin.EventListener):
  def on_post_save_async(self, view):
    view.run_command("set_mark")
  
  def on_load_async(self, view):
    view.run_command("set_mark")
  
  def on_hover(self, view, point, hover_zone):
    if hover_zone != sublime.HOVER_GUTTER:
      return
    if view.is_popup_visible():
      return

    offense_dict_str = view.settings().get("rubocop_diff")
    if offense_dict_str == None:
      return
    entry = self.get_offense_entry(view, point, offense_dict_str)
    if entry == None:
      return

    popup_content = self.get_complete_html(entry)
    view.show_popup(popup_content, sublime.HIDE_ON_MOUSE_MOVE_AWAY, point, 512, 100)

  def get_offense_entry(self, view, point, offense_dict_str):
    offense_dict = json.loads(offense_dict_str)
    hovered_line = view.rowcol(point)[0]
    return offense_dict.get(str(hovered_line + 1))

  def get_offense_html(self, offense_dict_entry):
    str = ""
    for entry in offense_dict_entry:
      str += "<p>. " + entry + "</p>"
    return str

  def get_complete_html(self, entry):
    offense_html = self.get_offense_html(entry)
    html = """
        <body id=rubocop-diff>
            <style>
                p {
                  margin: 2px 0;
                }
                div {
                  padding: 0;
                  margin: 0;
                }
            </style>
            <div>%s</div>
        </body>
    """ % (offense_html)

    return html