# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dbscan-swa.py'],
             pathex=['/100T/ganr/DBSCAN-SWA/bin'],
             binaries=[],
             datas=[],
             hiddenimports=['sklearn.cluster', 'sklearn.ensemble', 'sklearn.ensemble.RandomForestClassifier', 'sklearn.svm', 'sklearn.utils._cython_blas', 'sklearn.neighbors.typedefs', 'sklearn.neighbors.quad_tree', 'sklearn.tree._utils'],
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
          name='dbscan-swa',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
