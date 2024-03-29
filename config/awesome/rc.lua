pcall(require, "luarocks.loader")

require("awful.autofocus")
require("awful.hotkeys_popup.keys")

local gears = require("gears")
local awful = require("awful")
local wibox = require("wibox")
local beautiful = require("beautiful")
local naughty = require("naughty")
local menubar = require("menubar")
local hotkeys_popup = require("awful.hotkeys_popup")
require("awful.hotkeys_popup.keys")
local debian = pcall(require, "debian.menu")
local has_fdo, freedesktop = pcall(require, "freedesktop")
local autostart = require("util/autostart")
local lain = require("lain")
local dpi = require("beautiful.xresources").apply_dpi
local vicious = require("vicious")
local markup = lain.util.markup
local separators = lain.util.separators

if awesome.startup_errors then
  naughty.notify(
    {
      preset = naughty.config.presets.critical,
      title = "Oops, there were errors during startup!",
      text = awesome.startup_errors,
    }
  )
end

do
  local in_error = false
  awesome.connect_signal(
    "debug::error", function(err)
      -- Make sure we don't go into an endless error loop
      if in_error then return end
      in_error = true

      naughty.notify(
        {
          preset = naughty.config.presets.critical,
          title = "Oops, an error happened!",
          text = tostring(err),
        }
      )
      in_error = false
    end
  )
end

local chosen_theme = "powerarrow-dark"

local terminal = os.getenv("TERMINAL") or "urxvtc" 
local editor = os.getenv("EDITOR") or "editor"
local editor_cmd = terminal .. " -e " .. editor

local modkey = "Mod4"
local altkey = "Mod1"

awful.util.terminal = terminal

awful.layout.layouts = {
  awful.layout.suit.fair,
  awful.layout.suit.fair.horizontal,
  awful.layout.suit.max,
  awful.layout.suit.floating,
  awful.layout.suit.spiral.dwindle,
}

myawesomemenu = {
  {
    "hotkeys",
    function() hotkeys_popup.show_help(nil, awful.screen.focused()) end,
  },
  {"manual", terminal .. " -e man awesome"},
  {"edit config", editor_cmd .. " " .. awesome.conffile},
  {"restart", awesome.restart},
  {"quit", function() awesome.quit() end},
}

local menu_awesome = {"awesome", myawesomemenu, beautiful.awesome_icon}
local menu_terminal = {"open terminal", terminal}

lain.layout.termfair.nmaster           = 3
lain.layout.termfair.ncol              = 1
lain.layout.termfair.center.nmaster    = 3
lain.layout.termfair.center.ncol       = 1
lain.layout.cascade.tile.offset_x      = dpi(2)
lain.layout.cascade.tile.offset_y      = dpi(32)
lain.layout.cascade.tile.extra_padding = dpi(5)
lain.layout.cascade.tile.nmaster       = 5
lain.layout.cascade.tile.ncol          = 2

beautiful.init(string.format('%s/.config/awesome/themes/%s/theme.lua', os.getenv('HOME'), chosen_theme))
beautiful.font = 'SauceCodePro Nerd Font Mono 9'
-- beautiful.bg_normal = '#808080'
beautiful.bg_focus = '#666666'
beautiful.tasklist_bg_normal = beautiful.bg_normal
beautiful.tasklist_bg_focus = beautiful.bg_normal
beautiful.tasklist_fg_focus = '#ff0000'
beautiful.bg_systray = beautiful.bg_focus

if has_fdo then
  mymainmenu = freedesktop.menu.build(
    {before = {menu_awesome}, after = {menu_terminal}}
  )
else
  mymainmenu = awful.menu(
    {
      items = {
        menu_awesome,
        {"Debian", debian.menu.Debian_menu.Debian},
        menu_terminal,
      },
    }
  )
end

mylauncher = awful.widget.launcher(
  {image = beautiful.awesome_icon, menu = mymainmenu}
)

menubar.utils.terminal = terminal -- Set the terminal for applications that require it
mykeyboardlayout = awful.widget.keyboardlayout()
mytextclock = wibox.widget.textclock()

-- Separators 
local spr     = wibox.widget.textbox(' ')
local spr2    = wibox.container.background(wibox.widget.textbox(' '), beautiful.bg_focus)
local arrl_dl = separators.arrow_left(beautiful.bg_focus, "alpha")
local arrl_ld = separators.arrow_left("alpha", beautiful.bg_focus)

-- Widgets
local clockicon = wibox.widget.imagebox(beautiful.widget_clock)
local clock = awful.widget.watch(
    "date +'%a %d %b %R'", 60,
    function(widget, stdout)
        widget:set_markup(" " .. markup.font(beautiful.font, stdout))
    end
)
-- Calendar
beautiful.cal = lain.widget.cal({
    attach_to = { clock },
    notification_preset = {
        font = "Terminus 10",
        fg   = beautiful.fg_normal,
        bg   = beautiful.bg_normal,
    }
})

local taglist_buttons = gears.table.join(
  awful.button({}, 1, function(t) t:view_only() end), awful.button(
    {modkey}, 1,
    function(t)
      if client.focus then client.focus:move_to_tag(t) end
    end
  ),
  awful.button({}, 3, awful.tag.viewtoggle), awful.button(
    {modkey}, 3,
    function(t)
      if client.focus then client.focus:toggle_tag(t) end
    end
  ),
  awful.button({}, 4, function(t) awful.tag.viewnext(t.screen) end),
  awful.button({}, 5, function(t) awful.tag.viewprev(t.screen) end)
)

local tasklist_buttons = gears.table.join(
  awful.button(
    {}, 1, function(c)
      if c == client.focus then
        c.minimized = true
      else
        c:emit_signal("request::activate", "tasklist", {raise = true})
      end
    end
  ),
  awful.button(
    {}, 3, function() awful.menu.client_list({theme = {width = 250}}) end
  ),
  awful.button({}, 4, function() awful.client.focus.byidx(1) end),
  awful.button({}, 5, function() awful.client.focus.byidx(-1) end)
)

local function set_wallpaper(s)
  if beautiful.wallpaper then
    local wallpaper = beautiful.wallpaper
    -- If wallpaper is a function, call it with the screen
    if type(wallpaper) == "function" then wallpaper = wallpaper(s) end
    gears.wallpaper.maximized(wallpaper, s, true)
  end
end

screen.connect_signal("property::geometry", set_wallpaper)

awful.screen.connect_for_each_screen(
  function(s)
    set_wallpaper(s)
    awful.tag(
      {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"}, s,
      awful.layout.layouts[1]
    )
    s.quake = lain.util.quake(
    {
      app = '/usr/bin/urxvt',
        argname = "-title %s",
        extra = "-name QuakeDD",
        visible = true,
        height = 0.9,
        width = 0.9,
        horiz = "center",
        vert = "center",
        border = 2,
      }
    )
    s.mypromptbox = awful.widget.prompt()
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(
      gears.table.join(
        awful.button(
          {}, 1, function() awful.layout.inc(1) end
        ), awful.button(
          {}, 3, function() awful.layout.inc(-1) end
        ), awful.button(
          {}, 4, function() awful.layout.inc(1) end
        ), awful.button(
          {}, 5, function() awful.layout.inc(-1) end
        )
      )
    )
    s.mytaglist = awful.widget.taglist {
      screen = s,
      filter = awful.widget.taglist.filter.all,
      buttons = taglist_buttons,
    }
    s.mytasklist = awful.widget.tasklist {
      screen = s,
      filter = awful.widget.tasklist.filter.currenttags,
      buttons = tasklist_buttons,
    }
    s.mywibox = awful.wibar({
      position = "top",
      screen = s,
      height = dpi(18),
      fg = beautiful.fg_normal,
      bg = beautiful.bg_normal,
    })
    s.mywibox:setup{
      { -- Left widgets
        layout = wibox.layout.fixed.horizontal,
        wibox.container.background(mylauncher, beautiful.bg_focus),
				spr,
        s.mytaglist,
				spr,
        wibox.container.background(s.mypromptbox, beautiful.bg_focus),
      },
      s.mytasklist, -- Middle widget
      { -- Right widgets
        layout = wibox.layout.fixed.horizontal,
        spr,
				arrl_ld,
        wibox.container.background(mykeyboardlayout, beautiful.bg_focus),
				wibox.container.background(spr, beautiful.bg_focus),
				wibox.widget.systray(),
				arrl_dl,
				clock,
				spr,
				arrl_ld,
				wibox.container.background(spr, beautiful.bg_focus),
        wibox.container.background(s.mylayoutbox, beautiful.bg_focus),
				wibox.container.background(spr, beautiful.bg_focus),
      },
      bg = '#ff0000',
      layout = wibox.layout.align.horizontal,
    }
  end
)
root.buttons(
  gears.table.join(
    awful.button({}, 3, function() mymainmenu:toggle() end),
    awful.button({}, 4, awful.tag.viewnext),
    awful.button({}, 5, awful.tag.viewprev)
  )
)
globalkeys = gears.table.join(
  awful.key(
    {modkey}, "s", hotkeys_popup.show_help,
    {description = "show help", group = "awesome"}
  ),
  awful.key(
    {modkey}, "Left", awful.tag.viewprev,
    {description = "view previous", group = "tag"}
  ),
  awful.key(
    {modkey}, "Right", awful.tag.viewnext,
    {description = "view next", group = "tag"}
  ),
  awful.key(
    {modkey}, "Escape", awful.tag.history.restore,
    {description = "go back", group = "tag"}
  ),
  awful.key(
    {modkey}, "j", function() awful.client.focus.byidx(1) end,
    {description = "focus next by index", group = "client"}
  ),
  awful.key(
    {modkey}, "k", function() awful.client.focus.byidx(-1) end,
    {description = "focus previous by index", group = "client"}
  ),
  awful.key(
    {modkey}, "w", function() mymainmenu:show() end,
    {description = "show main menu", group = "awesome"}
  ), -- Layout manipulation
  awful.key(
    {modkey, "Shift"}, "j", function() awful.client.swap.byidx(1) end,
    {description = "swap with next client by index", group = "client"}
  ),
  awful.key(
    {modkey, "Shift"}, "k", function() awful.client.swap.byidx(-1) end,
    {
      description = "swap with previous client by index",
      group = "client",
    }
  ),
  awful.key(
    {modkey, "Control"}, "j", function()
      awful.screen.focus_relative(1)
    end, {description = "focus the next screen", group = "screen"}
  ),
  awful.key(
    {modkey, "Control"}, "k",
    function() awful.screen.focus_relative(-1) end,
    {description = "focus the previous screen", group = "screen"}
  ),
  awful.key(
    {modkey}, "u", awful.client.urgent.jumpto,
    {description = "jump to urgent client", group = "client"}
  ),
  awful.key(
    {modkey}, "Tab", function()
      awful.client.focus.history.previous()
      if client.focus then client.focus:raise() end
    end, {description = "go back", group = "client"}
  ), -- Standard program
  awful.key(
    {altkey}, "Tab", function() awful.spawn('rofi -show windowcd -modi windowcd') end,
    {description = "open programs", group = "client"}
  ),
  awful.key(
    {altkey, "Shift"}, "Tab", function() awful.spawn('rofi -show window -modi window') end,
    {description = "open programs", group = "client"}
  ),
  awful.key(
    {modkey}, "Return", function() awful.spawn(terminal) end,
    {description = "open a terminal", group = "launcher"}
  ),
--  awful.key(
--    {modkey}, "r", function() awful.spawn('xfreerpdui') end,
--    {description = "open xfreerpdui", group = "launcher"}
--  ),
  awful.key(
    {modkey, "Control"}, "r", awesome.restart,
    {description = "reload awesome", group = "awesome"}
  ),
  awful.key(
    {modkey, "Shift"}, "q", awesome.quit,
    {description = "quit awesome", group = "awesome"}
  ),
  awful.key(
    {modkey}, "l", function() awful.tag.incmwfact(0.05) end,
    {description = "increase master width factor", group = "layout"}
  ),
  awful.key(
    {modkey}, "h", function() awful.tag.incmwfact(-0.05) end,
    {description = "decrease master width factor", group = "layout"}
  ),
  awful.key(
    {modkey, "Shift"}, "h",
    function() awful.tag.incnmaster(1, nil, true) end, {
      description = "increase the number of master clients",
      group = "layout",
    }
  ),
  awful.key(
    {modkey, "Shift"}, "l",
    function() awful.tag.incnmaster(-1, nil, true) end, {
      description = "decrease the number of master clients",
      group = "layout",
    }
  ),
  awful.key(
    {modkey, "Control"}, "h",
    function() awful.tag.incncol(1, nil, true) end,
    {description = "increase the number of columns", group = "layout"}
  ),
  awful.key(
    {modkey, "Control"}, "l",
    function() awful.tag.incncol(-1, nil, true) end,
    {description = "decrease the number of columns", group = "layout"}
  ),
  awful.key(
    {modkey}, "space", function() awful.spawn('rofi -show drun -modi drun') end,
    {description = "start program", group = "layout"}
  ),
  awful.key(
    {modkey, "Shift"}, "space", function() awful.layout.inc(-1) end,
    {description = "select previous", group = "layout"}
  ),
  awful.key(
    {modkey, "Control"}, "n", function()
      local c = awful.client.restore()
      -- Focus restored client
      if c then
        c:emit_signal(
          "request::activate", "key.unminimize", {raise = true}
        )
      end
    end, {description = "restore minimized", group = "client"}
  ), -- Prompt
  awful.key(
    {modkey}, "r", function()
      awful.screen.focused().mypromptbox:run()
    end, {description = "run prompt", group = "launcher"}
  ),
  awful.key(
    {modkey}, "x", function()
      awful.prompt.run {
        prompt = "Run Lua code: ",
        textbox = awful.screen.focused().mypromptbox.widget,
        exe_callback = awful.util.eval,
        history_path = awful.util.get_cache_dir() .. "/history_eval",
      }
    end, {description = "lua execute prompt", group = "awesome"}
  ), -- Menubar
  awful.key(
    {modkey}, "p", function() menubar.show() end,
    {description = "show the menubar", group = "launcher"}
  ),
  awful.key(
    {any}, "F12", function() awful.screen.focused().quake:toggle() end,
    {description = "dropdown application", group = "launcher"}
  )
)

clientkeys = gears.table.join(
  awful.key(
    {modkey}, "f", function(c)
      c.fullscreen = not c.fullscreen
      c:raise()
    end, {description = "toggle fullscreen", group = "client"}
  ),
  awful.key(
    {modkey, "Shift"}, "c", function(c) c:kill() end,
    {description = "close", group = "client"}
  ),
  awful.key(
    {modkey, "Control"}, "space", awful.client.floating.toggle,
    {description = "toggle floating", group = "client"}
  ),
  awful.key(
    {modkey, "Control"}, "Return",
    function(c) c:swap(awful.client.getmaster()) end,
    {description = "move to master", group = "client"}
  ),
  awful.key(
    {modkey}, "o", function(c) c:move_to_screen() end,
    {description = "move to screen", group = "client"}
  ),
  awful.key(
    {modkey}, "t", function(c) c.ontop = not c.ontop end,
    {description = "toggle keep on top", group = "client"}
  ),
  awful.key(
    {modkey}, "n", function(c)
      c.minimized = true
    end, {description = "minimize", group = "client"}
  ),
  awful.key(
    {modkey}, "m", function(c)
      c.maximized = not c.maximized
      c:raise()
    end, {description = "(un)maximize", group = "client"}
  ),
  awful.key(
    {modkey, "Control"}, "m", function(c)
      c.maximized_vertical = not c.maximized_vertical
      c:raise()
    end, {description = "(un)maximize vertically", group = "client"}
  ),
  awful.key(
    {modkey, "Shift"}, "m", function(c)
      c.maximized_horizontal = not c.maximized_horizontal
      c:raise()
    end, {description = "(un)maximize horizontally", group = "client"}
  )
)

for i = 1, 12 do
  globalkeys = gears.table.join(
    globalkeys, -- View tag only.
    awful.key(
      {modkey}, "#" .. i + 9, function()
        local screen = awful.screen.focused()
        local tag = screen.tags[i]
        if tag then tag:view_only() end
      end, {description = "view tag #" .. i, group = "tag"}
    ), -- Toggle tag display.
    awful.key(
      {modkey, "Control"}, "#" .. i + 9, function()
        local screen = awful.screen.focused()
        local tag = screen.tags[i]
        if tag then awful.tag.viewtoggle(tag) end
      end, {description = "toggle tag #" .. i, group = "tag"}
    ), -- Move client to tag.
    awful.key(
      {modkey, "Shift"}, "#" .. i + 9, function()
        if client.focus then
          local tag = client.focus.screen.tags[i]
          if tag then client.focus:move_to_tag(tag) end
        end
      end,
      {
        description = "move focused client to tag #" .. i,
        group = "tag",
      }
    ), -- Toggle tag on focused client.
    awful.key(
      {modkey, "Control", "Shift"}, "#" .. i + 9, function()
        if client.focus then
          local tag = client.focus.screen.tags[i]
          if tag then client.focus:toggle_tag(tag) end
        end
      end, {
        description = "toggle focused client on tag #" .. i,
        group = "tag",
      }
    )
  )
end

clientbuttons = gears.table.join(
  awful.button(
    {}, 1, function(c)
      c:emit_signal("request::activate", "mouse_click", {raise = true})
    end
  ),
  awful.button(
    {modkey}, 1, function(c)
      c:emit_signal("request::activate", "mouse_click", {raise = true})
      awful.mouse.client.move(c)
    end
  ),
  awful.button(
    {modkey}, 3, function(c)
      c:emit_signal("request::activate", "mouse_click", {raise = true})
      awful.mouse.client.resize(c)
    end
  )
)

root.keys(globalkeys)

awful.rules.rules = {
  {
    rule = {},
    properties = {
      border_width = beautiful.border_width,
      border_color = beautiful.border_normal,
      focus = awful.client.focus.filter,
      raise = true,
      keys = clientkeys,
      buttons = clientbuttons,
      screen = awful.screen.preferred,
      placement = awful.placement.no_overlap +
      awful.placement.no_offscreen,
    },
  }, -- Floating clients.
  {
    rule_any = {
      instance = {
        "DTA", -- Firefox addon DownThemAll.
        "copyq", -- Includes session name in class.
        "pinentry",
      },
      class = {
        "Arandr",
        "Blueman-manager",
        "Gpick",
        "Kruler",
        "MessageWin", -- kalarm.
        "Sxiv",
        "Tor Browser", -- Needs a fixed window size to avoid fingerprinting by screen size.
        "Wpa_gui",
        "veromix",
        "xtightvncviewer",
      },
      name = {
        "Event Tester", -- xev.
      },
      role = {
        "AlarmWindow", -- Thunderbird's calendar.
        "ConfigManager", -- Thunderbird's about:config.
        "pop-up", -- e.g. Google Chrome's (detached) Developer Tools.
      },
    },
    properties = {floating = true},
  }, -- Do NOT add titlebars to normal clients and dialogs
  {
    rule_any = {type = {"normal", "dialog"}},
    properties = {titlebars_enabled = false},
  },
}

client.connect_signal(
  "manage", function(c)
    if awesome.startup and not c.size_hints.user_position and
      not c.size_hints.program_position then
      awful.placement.no_offscreen(c)
    end
  end
)

client.connect_signal(
  "request::titlebars", function(c)
    local buttons = gears.table.join(
      awful.button(
        {}, 1, function()
          c:emit_signal(
            "request::activate", "titlebar", {raise = true}
          )
          awful.mouse.client.move(c)
        end
      ),
      awful.button(
        {}, 3, function()
          c:emit_signal(
            "request::activate", "titlebar", {raise = true}
          )
          awful.mouse.client.resize(c)
        end
      )
    )
    awful.titlebar(c):setup{
      { -- Left
        awful.titlebar.widget.iconwidget(c),
        buttons = buttons,
        layout = wibox.layout.fixed.horizontal,
      },
      { -- Middle
        { -- Title
          align = "center",
          widget = awful.titlebar.widget.titlewidget(c),
      },
      buttons = buttons,
      layout = wibox.layout.flex.horizontal,
      },
      { -- Right
        awful.titlebar.widget.floatingbutton(c),
        awful.titlebar.widget.maximizedbutton(c),
        awful.titlebar.widget.stickybutton(c),
        awful.titlebar.widget.ontopbutton(c),
        awful.titlebar.widget.closebutton(c),
        layout = wibox.layout.fixed.horizontal(),
      },
      layout = wibox.layout.align.horizontal,
    }
  end
)

client.connect_signal(
  "mouse::enter", function(c)
    c:emit_signal("request::activate", "mouse_enter", {raise = false})
  end
)

client.connect_signal(
  "focus", function(c) c.border_color = beautiful.border_focus end
)
client.connect_signal(
  "unfocus", function(c) c.border_color = beautiful.border_normal end
)

autorun = true
autorunApps = {
  "/usr/bin/conky",
  "/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1",
  "/usr/libexec/polkit-gnome-authentication-agent-1",
  "/usr/lib/notification-daemon/notification-daemon",
  "/usr/libexec/notification-daemon",
  "/usr/bin/urxvtd -o -q",
  "/usr/bin/kdeconnect-indicator",
}
if autorun then
  for app = 1, #autorunApps do
    autostart(autorunApps[app])
  end
end
