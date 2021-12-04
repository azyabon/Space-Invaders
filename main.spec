# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\down\Space Invaders'],
             binaries=[],
             datas=[('assets/aliens/alien1.png', 'Images'), ('assets/aliens/alien2.png', 'Images'), ('assets/aliens/alien3.png', 'Images'), ('assets/aliens/alien4.png', 'Images'),  ('assets/aliens/alien5.png', 'Images'), ('assets/bgc.jpg', 'Images'), ('assets/gameover.wav', 'Sounds'), ('assets/menu_move.mp3', 'Sounds'), ('assets/boom.mp3', 'Sounds'), ('assets/clash.mp3', 'Sounds'), ('assets/lifes.png', 'Images'), ('assets/shoot.mp3', 'Sounds'), ('assets/spaceship.png', 'Images')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
