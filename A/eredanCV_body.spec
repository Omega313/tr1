# -*- mode: python -*-

block_cipher = None


a = Analysis(['eredanCV_body.py'],
             pathex=['C:\\Users\\Echo\\Desktop\\Python Projects\\eredancardsviewer_presemicompiledwithlauncher_workingenv6_tocompile\\eredanCV_body\\dist\\eredanCV_body'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='eredanCV_body',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\Echo\\Desktop\\Python Projects\\eredancardsviewer_presemicompiledwithlauncher_workingenv6_tocompile\\eredanCV_body\\dist\\eredanCV_body\\eredicon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='eredanCV_body')
