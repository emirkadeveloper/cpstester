import random
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import NumericProperty, StringProperty, BooleanProperty
from kivy.metrics import dp
from kivy.storage.jsonstore import JsonStore  # Импортируем для сохранения

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton, MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

# Размер окна для ПК
Window.size = (360, 800)


class MenuCard(MDCard):
    text = StringProperty("")
    icon = StringProperty("android")
    subtext = StringProperty("")


KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

# ---- Стили ----

<HUDCapsule@MDCard>:
    size_hint: None, None
    size: "90dp", "60dp"
    radius: [20]
    md_bg_color: app.theme_cls.bg_darkest
    elevation: 0
    padding: "5dp"
    orientation: "vertical"

<MenuCard>:
    padding: "12dp"
    size_hint: None, None
    size: "145dp", "160dp"
    radius: [28]
    # ТЕНИ УБРАНЫ (Flat Design)
    elevation: 0
    ripple_behavior: True
    orientation: "vertical"
    md_bg_color: app.theme_cls.bg_dark if app.theme_cls.theme_style == "Dark" else [0.95, 0.95, 0.95, 1]
    spacing: "10dp"
    
    Widget:
        size_hint_y: 0.1
    
    MDIcon:
        icon: root.icon
        halign: "center"
        font_size: "56sp"
        theme_text_color: "Custom"
        text_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5}
        size_hint_y: None
        height: "60dp"
    
    MDBoxLayout:
        orientation: "vertical"
        adaptive_height: True
        
        MDLabel:
            text: root.text
            halign: "center"
            theme_text_color: "Primary"
            bold: True
            font_style: "H6"
            adaptive_height: True
            
        MDLabel:
            text: root.subtext
            halign: "center"
            theme_text_color: "Hint"
            font_style: "Caption"
            adaptive_height: True

    Widget:
        size_hint_y: 0.1

# ---- Экраны ----
ScreenManager:
    transition: FadeTransition()
    MenuScreen:
    FreeClickerScreen:
    TimeSelectScreen:
    TimedGameScreen:
    OsuGameScreen:
    SettingsScreen:

<MenuScreen>:
    name: "menu"
    
    MDBoxLayout:
        orientation: "vertical"
        padding: "24dp"
        spacing: "20dp"

        # Заголовок и Автор
        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: "120dp"
            spacing: "0dp"
            
            MDLabel:
                text: "CPS TESTER"
                halign: "center"
                font_style: "H3"
                bold: True
                theme_text_color: "Primary"
                pos_hint: {"center_x": .5}
                size_hint_y: 0.7
            
            # Автор под заголовком
            MDLabel:
                text: "By EmirkaDev"
                halign: "center"
                font_style: "Subtitle1"
                theme_text_color: "Hint"
                size_hint_y: 0.3
                valign: "top"

        # Сетка меню
        MDGridLayout:
            cols: 2
            spacing: "20dp"
            adaptive_height: True
            adaptive_width: True
            pos_hint: {"center_x": .5, "center_y": .5}
            
            MenuCard:
                icon: "mouse"
                text: "Free Click"
                subtext: "Unlimited"
                on_release: app.change_screen("free_clicker")
            
            MenuCard:
                icon: "timer-outline"
                text: "Timed"
                subtext: "Challenge"
                on_release: app.change_screen("time_select")
            
            MenuCard:
                icon: "bullseye"
                text: "Precision"
                subtext: "OSU Mode"
                on_release: app.change_screen("osu_game")
                
            MenuCard:
                icon: "cog"
                text: "Settings"
                subtext: "Theme & UI"
                on_release: app.change_screen("settings")

        # Распорка, чтобы версия была в самом низу
        Widget: 

        # Версия в самом низу
        MDLabel:
            text: "v1.0"
            halign: "center"
            font_style: "Overline"
            theme_text_color: "Hint"
            size_hint_y: None
            height: "20dp"

<FreeClickerScreen>:
    name: "free_clicker"
    
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"top": 0.98, "left": 0.02}
        on_release: app.change_screen("menu")
        theme_text_color: "Primary"

    MDBoxLayout:
        orientation: "vertical"
        padding: "30dp"
        spacing: "30dp"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDLabel:
            text: "FREE MODE"
            halign: "center"
            font_style: "Overline"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            font_size: "16sp"
            size_hint_y: None
            height: "30dp"
        
        MDLabel:
            text: str(root.clicks)
            halign: "center"
            font_style: "H1"
            bold: True
            theme_text_color: "Primary"
            font_size: "100sp"

        Widget:
            size_hint_y: 0.1

        MDFloatingActionButton:
            id: click_btn
            icon: "cursor-default-click"
            type: "large"
            icon_size: "64sp"
            pos_hint: {"center_x": .5}
            md_bg_color: app.theme_cls.primary_color
            text_color: 1, 1, 1, 1
            elevation: 0
            on_release: root.on_click()

<TimeSelectScreen>:
    name: "time_select"
    
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"top": 0.98, "left": 0.02}
        on_release: app.change_screen("menu")
        
    MDBoxLayout:
        orientation: "vertical"
        padding: "30dp"
        spacing: "20dp"
        
        MDLabel:
            text: "Select Duration"
            halign: "center"
            font_style: "H4"
            bold: True
            size_hint_y: 0.15

        ScrollView:
            MDGridLayout:
                cols: 1
                adaptive_height: True
                spacing: "15dp"
                padding: "10dp"
                
                MDFillRoundFlatButton:
                    text: "1 SECOND"
                    font_size: "18sp"
                    size_hint_x: 1
                    height: "60dp"
                    radius: [15]
                    on_release: root.start_game(1)
                MDFillRoundFlatButton:
                    text: "5 SECONDS"
                    font_size: "18sp"
                    size_hint_x: 1
                    height: "60dp"
                    radius: [15]
                    on_release: root.start_game(5)
                MDFillRoundFlatButton:
                    text: "10 SECONDS"
                    font_size: "18sp"
                    size_hint_x: 1
                    height: "60dp"
                    radius: [15]
                    on_release: root.start_game(10)
                MDFillRoundFlatButton:
                    text: "30 SECONDS"
                    font_size: "18sp"
                    size_hint_x: 1
                    height: "60dp"
                    radius: [15]
                    on_release: root.start_game(30)
                MDFillRoundFlatButton:
                    text: "60 SECONDS"
                    font_size: "18sp"
                    size_hint_x: 1
                    height: "60dp"
                    radius: [15]
                    on_release: root.start_game(60)

<TimedGameScreen>:
    name: "timed_game"
    
    MDBoxLayout:
        orientation: "vertical"
        padding: "10dp"
        spacing: "30dp"
        
        # HUD Top
        MDBoxLayout:
            orientation: "horizontal"
            adaptive_height: True
            spacing: "10dp"
            pos_hint: {"center_x": .5}
            padding: "10dp"

            HUDCapsule:
                MDLabel:
                    text: "TIME"
                    halign: "center"
                    font_style: "Overline"
                    theme_text_color: "Hint"
                MDLabel:
                    text: str(round(root.time_left, 1))
                    halign: "center"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Primary"

            HUDCapsule:
                MDLabel:
                    text: "CLICKS"
                    halign: "center"
                    font_style: "Overline"
                    theme_text_color: "Hint"
                MDLabel:
                    text: str(root.clicks)
                    halign: "center"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
            
            HUDCapsule:
                MDLabel:
                    text: "CPS"
                    halign: "center"
                    font_style: "Overline"
                    theme_text_color: "Hint"
                MDLabel:
                    text: root.current_cps
                    halign: "center"
                    font_style: "H6"
                    bold: True
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.accent_color

        MDLabel:
            text: "TAP TO START" if not root.game_active else "GO!"
            halign: "center"
            font_style: "H4"
            bold: True
            size_hint_y: 0.2
            opacity: 1 if root.time_left > 0 else 0
            theme_text_color: "Custom"
            text_color: app.theme_cls.accent_color if not root.game_active else app.theme_cls.primary_color

        MDFloatingActionButton:
            id: game_btn
            icon: "fingerprint"
            type: "large"
            icon_size: "80sp"
            pos_hint: {"center_x": .5}
            md_bg_color: app.theme_cls.primary_color
            text_color: 1, 1, 1, 1
            elevation: 0
            on_release: root.on_click()
            
    MDIconButton:
        icon: "close"
        pos_hint: {"top": 0.98, "right": 0.98}
        on_release: root.stop_game()

<OsuGameScreen>:
    name: "osu_game"
    
    FloatLayout:
        id: game_area
        
        MDCard:
            size_hint: None, None
            size: "200dp", "60dp"
            pos_hint: {"top": 0.95, "center_x": 0.5}
            radius: [30]
            md_bg_color: app.theme_cls.bg_darkest
            elevation: 0
            
            MDBoxLayout:
                padding: "15dp"
                spacing: "20dp"
                
                MDBoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: "TIME"
                        font_style: "Overline"
                        halign: "center"
                        theme_text_color: "Hint"
                    MDLabel:
                        text: str(round(root.time_left, 1))
                        halign: "center"
                        font_style: "Subtitle1"
                        bold: True
                        
                MDSeparator:
                    orientation: "vertical"
                    
                MDBoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: "SCORE"
                        font_style: "Overline"
                        halign: "center"
                        theme_text_color: "Hint"
                    MDLabel:
                        text: str(root.score)
                        halign: "center"
                        font_style: "Subtitle1"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.accent_color

        MDIconButton:
            icon: "close"
            pos_hint: {"top": 0.98, "right": 0.98}
            on_release: root.stop_game()

        MDFloatingActionButton:
            id: target_circle
            icon: "target"
            md_bg_color: app.theme_cls.accent_color
            text_color: 1, 1, 1, 1
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            opacity: 0
            elevation: 0
            on_release: root.on_target_click()

<SettingsScreen>:
    name: "settings"
    
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"top": 0.98, "left": 0.02}
        on_release: app.change_screen("menu")
        
    MDBoxLayout:
        orientation: "vertical"
        padding: "24dp"
        spacing: "20dp"
        
        MDLabel:
            text: "Settings"
            halign: "center"
            font_style: "H4"
            bold: True
            size_hint_y: None
            height: "60dp"
        
        MDCard:
            padding: "20dp"
            spacing: "10dp"
            size_hint_y: None
            height: "80dp"
            radius: [24]
            ripple_behavior: False
            elevation: 0
            md_bg_color: app.theme_cls.bg_dark if app.theme_cls.theme_style == "Dark" else [0.95, 0.95, 0.95, 1]
            
            MDIcon:
                icon: "theme-light-dark"
                theme_text_color: "Primary"
                size_hint_x: None
                width: "40dp"
                pos_hint: {"center_y": .5}
            
            MDLabel:
                text: "Dark Mode"
                font_style: "H6"
                pos_hint: {"center_y": .5}
            
            MDSwitch:
                active: app.theme_cls.theme_style == "Dark"
                on_active: app.toggle_theme(self.active)
                pos_hint: {"center_y": .5}

        MDLabel:
            text: "ACCENT COLOR"
            font_style: "Overline"
            size_hint_y: None
            height: "40dp"
            halign: "center"
            theme_text_color: "Hint"

        ScrollView:
            MDGridLayout:
                id: color_grid
                cols: 4
                adaptive_height: True
                spacing: "15dp"
                padding: "10dp"
'''


class MenuScreen(Screen):
    pass


class FreeClickerScreen(Screen):
    clicks = NumericProperty(0)

    def on_enter(self):
        self.clicks = 0

    def on_click(self):
        self.clicks += 1
        self.animate_btn()

    def animate_btn(self):
        btn = self.ids.click_btn
        anim = Animation(icon_size=58, d=0.05) + Animation(icon_size=64, d=0.05)
        anim.start(btn)


class TimeSelectScreen(Screen):
    def start_game(self, duration):
        game_screen = MDApp.get_running_app().root.get_screen('timed_game')
        game_screen.setup_game(duration)
        MDApp.get_running_app().change_screen('timed_game')


class TimedGameScreen(Screen):
    clicks = NumericProperty(0)
    time_left = NumericProperty(0)
    current_cps = StringProperty("0.0")
    duration = 0
    event = None
    game_active = BooleanProperty(False)
    result_dialog = None

    def setup_game(self, duration):
        self.duration = duration
        self.time_left = duration
        self.clicks = 0
        self.current_cps = "0.0"
        self.game_active = False
        self.result_dialog = None
        if self.event:
            self.event.cancel()

    def start_timer(self):
        self.game_active = True
        self.event = Clock.schedule_interval(self.update_time, 0.1)

    def update_time(self, dt):
        if not self.game_active: 
            return
            
        self.time_left -= dt
        if self.time_left <= 0:
            self.time_left = 0
            self.finish_game()

    def on_click(self):
        if self.time_left == 0 and self.clicks > 0:
            return

        if not self.game_active:
            self.start_timer()
            self.clicks += 1
            self.update_live_cps()
        else:
            self.clicks += 1
            self.update_live_cps()

        btn = self.ids.game_btn
        anim = Animation(icon_size=74, d=0.03) + Animation(icon_size=80, d=0.03)
        anim.start(btn)
        
    def update_live_cps(self):
        elapsed = self.duration - self.time_left
        if elapsed > 0.1:
            cps = self.clicks / elapsed
            self.current_cps = str(round(cps, 1))

    def finish_game(self):
        if not self.game_active:
            return
            
        self.game_active = False
        if self.event:
            self.event.cancel()

        dur = self.duration if self.duration > 0 else 1
        cps = round(self.clicks / dur, 2)
        
        if not self.result_dialog:
            self.show_dialog(f"Time's up!\nClicks: {self.clicks}\nCPS: {cps}")

    def stop_game(self):
        if self.event:
            self.event.cancel()
        self.game_active = False
        MDApp.get_running_app().change_screen('menu')

    def show_dialog(self, text):
        self.result_dialog = MDDialog(
            title="RESULT",
            text=text,
            radius=[24, 24, 24, 24],
            auto_dismiss=False,  
            buttons=[
                MDFlatButton(
                    text="MENU",
                    theme_text_color="Custom",
                    text_color=MDApp.get_running_app().theme_cls.primary_color,
                    on_release=lambda x: self.close_dialog(self.result_dialog)
                ),
                MDFillRoundFlatButton(
                    text="RETRY",
                    on_release=lambda x: self.retry(self.result_dialog)
                ),
            ],
        )
        self.result_dialog.open()

    def close_dialog(self, dialog):
        dialog.dismiss()
        self.result_dialog = None
        MDApp.get_running_app().change_screen('menu')

    def retry(self, dialog):
        dialog.dismiss()
        self.result_dialog = None
        self.setup_game(self.duration)


class OsuGameScreen(Screen):
    score = NumericProperty(0)
    time_left = NumericProperty(30)
    event = None
    target_locked = BooleanProperty(False)

    def on_enter(self):
        self.score = 0
        self.time_left = 30
        self.ids.target_circle.opacity = 1
        self.move_target()
        if self.event:
            self.event.cancel()
        self.event = Clock.schedule_interval(self.update, 0.1)

    def update(self, dt):
        self.time_left -= dt
        if self.time_left <= 0:
            self.time_left = 0
            self.finish_game()

    def move_target(self):
        x = random.uniform(0.15, 0.85)
        y = random.uniform(0.15, 0.85)

        target = self.ids.target_circle
        target.pos_hint = {"center_x": x, "center_y": y}
        self.target_locked = False
        
        target.opacity = 0
        anim = Animation(opacity=1, duration=0.15)
        anim.start(target)

    def on_target_click(self):
        if self.time_left <= 0 or self.target_locked:
            return
            
        self.target_locked = True
        self.score += 1
        target = self.ids.target_circle
        anim = Animation(opacity=0, duration=0.05)
        anim.bind(on_complete=lambda *args: self.move_target())
        anim.start(target)

    def finish_game(self):
        if self.event:
            self.event.cancel()
        self.ids.target_circle.opacity = 0
        self.show_dialog(f"Game Over!\nFinal Score: {self.score}")

    def stop_game(self):
        if self.event:
            self.event.cancel()
        MDApp.get_running_app().change_screen('menu')

    def show_dialog(self, text):
        dialog = MDDialog(
            title="OSU RESULT",
            text=text,
            radius=[24, 24, 24, 24],
            auto_dismiss=False,
            buttons=[
                MDFlatButton(text="MENU", 
                             theme_text_color="Custom",
                             text_color=MDApp.get_running_app().theme_cls.primary_color,
                             on_release=lambda x: self.close_dialog(dialog))
            ]
        )
        dialog.open()

    def close_dialog(self, dialog):
        dialog.dismiss()
        MDApp.get_running_app().change_screen('menu')


class SettingsScreen(Screen):
    def on_enter(self):
        grid = self.ids.color_grid
        if not grid.children:
            colors = ['DeepPurple', 'Red', 'Pink', 'Purple', 'Indigo', 'Blue',
                      'Teal', 'Green', 'Orange', 'DeepOrange', 'Brown', 'BlueGray']
            for color in colors:
                btn = MDFloatingActionButton(
                    icon="palette",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    md_bg_color=MDApp.get_running_app().theme_cls.colors[color]['500'],
                    elevation=0,
                    size_hint=(None, None),
                    size=("56dp", "56dp")
                )
                btn.bind(on_release=lambda x, c=color: self.set_color(c))
                grid.add_widget(btn)

    def set_color(self, color_name):
        # Вызываем метод App для сохранения
        MDApp.get_running_app().change_palette(color_name)


class CPSTesterApp(MDApp):
    store = None

    def build(self):
        self.title = "CPS Tester"
        
        # 1. Инициализация хранилища
        self.store = JsonStore("app_settings.json")

        # 2. Загрузка темы
        if self.store.exists('theme'):
            self.theme_cls.theme_style = self.store.get('theme')['style']
        else:
            self.theme_cls.theme_style = "Dark" # Значение по умолчанию

        # 3. Загрузка цвета
        if self.store.exists('palette'):
            self.theme_cls.primary_palette = self.store.get('palette')['color']
        else:
            self.theme_cls.primary_palette = "DeepPurple" # Значение по умолчанию

        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name

    def toggle_theme(self, is_dark):
        new_style = "Dark" if is_dark else "Light"
        self.theme_cls.theme_style = new_style
        # Сохранение темы
        self.store.put('theme', style=new_style)

    def change_palette(self, color_name):
        self.theme_cls.primary_palette = color_name
        # Сохранение цвета
        self.store.put('palette', color=color_name)


if __name__ == '__main__':
    CPSTesterApp().run()