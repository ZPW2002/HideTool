# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['hidetool.py', 'json_flask.py', 'json_response.py', 'tools.py'],
    pathex=['D:\\Programs\\webview\\python-flask'],
    binaries=[],
    datas=[
        ('D:\\Programs\\webview\\python-flask\\data', 'data'), 
        ('D:\\Programs\\webview\\python-flask\\static', 'static'), 
        ('D:\\Programs\\webview\\python-flask\\templates', 'templates')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='HideTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\Programs\\webview\\python-flask\\static\\favicon.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='HideTool',
)
