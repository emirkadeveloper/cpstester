[app]

title = CPS Tester
package.name = cpstester
package.domain = org.emirkadev
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,pillow,sdl2_ttf
orientation = portrait
fullscreen = 0
android.presplash_color = #121212
# icon.filename = %(source.dir)s/icon.png
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.private_storage = True

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.debug_artifact = apk

[buildozer]

log_level = 2

warn_on_root = 1
