# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

mod = "mod4"
terminal = "mate-terminal" #guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),

    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),

    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
#    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),

#    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),

#    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),

#    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes

#    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
#    Key([mod], "r", lazy.spawncmd(),
#        desc="Spawn a command using a prompt widget"),


    ### Raccourcis persos

    Key([mod, "control"], "Up",
	lazy.layout.grow(),
	lazy.layout.increase_nmaster(),
	desc='Expand window (MonadTall), increase number in master pane (Tile)'
	),

	Key([mod, "control"], "Down",
	lazy.layout.shrink(),
	lazy.layout.decrease_nmaster(),
    desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
	),

    Key([mod], "e",
    lazy.spawn("pcmanfm"),
    desc='File manager'
    ),
    Key([mod, "shift"], "r",
    lazy.restart(),
    desc='Restart Qtile'
    ),

	Key([mod], "z",
    lazy.spawn("vivaldi"),
    desc='Lancer Vivaldi'
    ),

    Key([mod, "shift"], "z",
    lazy.spawn("./Téléchargements/waterfox/waterfox"),
    desc='Lancer Waterfox'
    ),

    Key([mod], "i",
    lazy.spawn("geany .config/qtile/config.py"),
    desc='Ouvrir le fichier de config'
    ),

    Key([], "XF86MonBrightnessDown",
    lazy.spawn("xbacklight -dec 10"),
    desc='Diminuer la luminosité'
    ),

    Key([], "XF86MonBrightnessUp",
    lazy.spawn("xbacklight -inc 10"),
    desc='Augmenter la luminosité'
    ),

    Key([], "XF86AudioRaiseVolume",
    lazy.spawn("amixer set 'Master' 10%+"),
    desc='Augmenter la luminosité'
    ),

    Key([], "XF86AudioLowerVolume",
    lazy.spawn("amixer set 'Master' 10%-"),
    desc='Augmenter la luminosité'
    ),

    Key([], "XF86AudioMute",
    lazy.spawn("amixer -q set Master toggle"),
    desc='Augmenter la luminosité'
    ),

    Key([mod], "l",
    lazy.spawn("slock"),
    ),

    Key([mod, "shift"], "s",
    lazy.spawn("flameshot gui"),
    ),

    Key([mod], "r",
    lazy.spawn("synapse"),
    ),

    Key([mod, "shift"], "f",
    lazy.window.toggle_floating(),
    desc='toggle floating'
    ),

    Key([mod], "m",
	lazy.layout.maximize(),
	desc='toggle window between minimum and maximum sizes'
	),

	Key([mod], "f",
	lazy.window.toggle_fullscreen(),
	desc='toggle fullscreen'
	),

	Key([mod], "v",
	lazy.spawn("virt-viewer -c qemu:///system"),
	desc='Open virt-viewer'
	),





    ### GROUPS KEYBINDINGS

	Key([mod], "F1",
    lazy.group["1"].toscreen()
    ),

    Key([mod], "F2",
    lazy.group["2"].toscreen()
    ),

    Key([mod], "F3",
    lazy.group["3"].toscreen()
    ),

    Key([mod], "F4",
    lazy.group["4"].toscreen()
    ),

    Key([mod], "F5",
    lazy.group["5"].toscreen()
    ),

    Key([mod,"shift"], "F1",
    lazy.window.togroup("1")
    ),

    Key([mod,"shift"], "F2",
    lazy.window.togroup("2")
    ),

    Key([mod,"shift"], "F3",
    lazy.window.togroup("3")
    ),

    Key([mod,"shift"], "F4",
    lazy.window.togroup("4")
    ),

    Key([mod,"shift"], "F5",
    lazy.window.togroup("5")
    ),


]

groups = [Group("1", layout='monadtall', label='⬤'),
          Group("2", layout='monadtall', label='⬤'),
          Group("3", layout='monadtall', label='⬤'),
          Group("4", layout='monadtall', label='⬤'),
          Group("5", layout='monadtall', label='⬤'),]


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Bsp(**layout_theme),
]

colors = [
    ["#2e3440", "#2e3440"],  # background
    ["#d8dee9", "#d8dee9"],  # foreground
    ["#3b4252", "#3b4252"],  # background lighter
    ["#bf616a", "#bf616a"],  # red
    ["#a3be8c", "#a3be8c"],  # green
    ["#ebcb8b", "#ebcb8b"],  # yellow
    ["#81a1c1", "#81a1c1"],  # blue
    ["#b48ead", "#b48ead"],  # magenta
    ["#88c0d0", "#88c0d0"],  # cyan
    ["#e5e9f0", "#e5e9f0"],  # white
    ["#4c566a", "#4c566a"],  # grey
    ["#d08770", "#d08770"],  # orange
    ["#8fbcbb", "#8fbcbb"],  # super cyan
    ["#5e81ac", "#5e81ac"],  # super blue
    ["#242831", "#242831"],  # super dark background
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[8],
    "highlight_method": "block",
    "this_current_screen_border": colors[0],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[0],
    "other_screen_border": colors[0],
    "foreground": colors[1],
    # "background": colors[14],
    "urgent_border": colors[3],
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(),
				widget.GroupBox(
					font="verdana bold",
					**group_box_settings,
					fontsize=12
					),
				widget.Sep(
				linewidth=0,
				foreground=colors[2],
				padding=20,
				size_percent=40,
                ),
                widget.WindowName(
                font = "verdana bold"
                ),
                widget.Systray(),
				widget.Sep(
				linewidth=0,
				foreground=colors[2],
				padding=20,
				size_percent=40,
                ),
                widget.Volume(
                foreground = colors[1],
                background = colors[0],
                fmt = 'Vol: {}',
                padding = 5,
                font = "verdana bold"
                ),
                widget.ThermalSensor(
                foreground = colors[1],
                background = colors[0],
                threshold = 90,
                fmt = 'Temp: {}',
                padding = 5,
                font = "verdana bold"
                ),
                widget.TextBox(
				"🔋",
				foreground = colors[2]
				),
                widget.Battery(
                foreground = colors[1],
                background = colors[0],
                padding = 5,
                font = "verdana bold"
                ),
                widget.TextBox(
				"📅",
				foreground = colors[2]
				),
                widget.Clock(
                foreground = colors[1],
                background = colors[0],
                format = " %A %d %B - %H:%M ",
                font = "verdana bold"
                ),

            ],
            size=20,
            background = colors[0],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

wmname = "LG3D"
