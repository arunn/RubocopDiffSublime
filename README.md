# RubocopDiffSublime

Sublime Text 3 plugin for rubocop on git diff

## What does it do?

It runs rubocop on the git diff of the active view file and shows gutter icons and squiggly underlines on the error lines. 
When hovered on the gutter icon, it shows the error messages for the lines in a popup. 

## Screenshot

<img width="933" alt="screen shot 2017-04-28 at 8 45 06 am" src="https://cloud.githubusercontent.com/assets/389262/25512994/673603f6-2bef-11e7-8f42-5f1d03c5dac6.png">

## Manual Installation

1. Go to the sublime text folder. 
    * Windows: %APPDATA%\Sublime Text 3
    * OS X: ~/Library/Application Support/Sublime Text 3
    * Linux: ~/.config/sublime-text-3

2. Go to packages folder

3. Run the git clone command inside the packages directory: 

`git clone git@github.com:arunn/RubocopDiffSublime.git "RubocopDiffSublime"`

4. Restart Sublime Text.


## Caveats

When there are other icons present in the gutter(for ex: GitGutter), RubocopDiffSublime's icons and popups may not be shown. This can be fixed if the plugin provides configuration regarding it. Add the following to the GitGutter.settings file for GitGutter plugin. 

`"protected_regions": [`

`"sublimelinter-warning-gutter-marks",`

`"sublimelinter-error-gutter-marks",`

`"bookmarks",`

`"rubocop_marks"`
`],`

`"enable_hover_diff_popup": false`

## Credits

[pderichs/sublime_rubocop](https://github.com/pderichs/sublime_rubocop)

Sam Mello for giving the best possible writeup for sublime plugin creation(https://cnpagency.com/blog/creating-sublime-text-3-plugins-part-1/)

Sublime API Reference(https://www.sublimetext.com/docs/3/api_reference.html)
