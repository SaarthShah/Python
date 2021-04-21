from pathlib import Path
path=Path("directoy1")
path.mkdir()
print(path.exists())
path.rmdir()
print(path.exists())