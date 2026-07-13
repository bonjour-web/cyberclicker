[app]
title = CyberClicker
package.name = cyberclicker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11.10,kivy==2.3.0,cython==0.29.36,jnius==1.6.0

orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
