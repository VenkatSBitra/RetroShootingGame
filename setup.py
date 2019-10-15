import cx_Freeze
from cx_Freeze import *

setup(
    name = "Shooter_Game",
    options = {"build.exe": {"packages": ['pygame', 'random'], "zip_include_packages": ["*"], "zip_exclude_packages": ['scipy', 'numpy']},},
    executables = [
        Executable("Game_Basic.py",),
        Executable("Player.py",),
        Executable("Bullet.py",),
        Executable("Enemy.py",),

        
        ]
    
    
    
    )