[app]

title = ExterAndroid
package.name = exterandroid
package.domain = org.exterandroid

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,atlas

version = 0.1

requirements = python3==3.11.9,hostpython3==3.11.9,kivy

orientation = portrait

fullscreen = 0

android.archs = arm64-v8a


[buildozer]

log_level = 2


[android]

android.api = 35
android.minapi = 21
