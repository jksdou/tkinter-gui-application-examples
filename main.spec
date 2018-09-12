# -*- mode: python -*-

import os
block_cipher = None
APP_PATH = "/Users/douzhenjiang/Projects/tkinter-gui-application-examples"

a = Analysis(['main.py'],
            pathex=[
                os.path.join(APP_PATH, "components", '__init__.py'),
                os.path.join(APP_PATH, "lib", 'dbcontent.py'),
                os.path.join(APP_PATH, "lib", 'functions.py'),
                os.path.join(APP_PATH, "lib", 'global_variable.py'),
                os.path.join(APP_PATH, "lib", 'sqlite_helper.py'),
                os.path.join(APP_PATH, "pages", 'win_login.py'),
                os.path.join(APP_PATH, "pages", 'win_splah.py'),
                os.path.join(APP_PATH, "pages", 'win_user_edit.py'),
                os.path.join(APP_PATH, "pages", 'win_user_info.py'),
                os.path.join(APP_PATH, "pages", 'winAbout.py'),
                os.path.join(APP_PATH, "pages", 'winContentEdit.py'),
                os.path.join(APP_PATH, "pages", 'winContentInfo.py'),
                APP_PATH
            ],
            binaries=[],
            datas=[(os.path.join(APP_PATH, "data", 'database.db'), 'data')],
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='main.app',
             icon=None,
             bundle_identifier=None)
