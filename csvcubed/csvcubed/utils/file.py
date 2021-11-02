"""
File
----

Utilities for files.
"""
import shutil
from pathlib import Path
from typing import Iterable


def copy_files_to_directory_with_structure(
    files: Iterable[Path], common_parent: Path, to_dir: Path
) -> None:
    """
    Copies :obj:`files` into :obj:`to_dir` retaining the directory structure below :obj:`common_parent`.
    """
    for file in files:
        relative_dir_structure = file.relative_to(common_parent)
        abs_out_file_path = to_dir / relative_dir_structure

        _ensure_dir_structure_exists(abs_out_file_path.parent)
        shutil.copy(file, abs_out_file_path)


def _ensure_dir_structure_exists(dir_path: Path) -> None:
    if not dir_path.exists():
        _ensure_dir_structure_exists(dir_path.parent)
        dir_path.mkdir()