"""
Sports Intelligence Platform

File: loader.py
Author: Syed Faran Ali

Description:
Dynamic module loader.
"""

from importlib import import_module


class ModuleLoader:
    """Loads application modules dynamically."""

    @staticmethod
    def load(module_name: str):
        """Load a module page."""

        module = import_module(
            f"modules.{module_name}.page"
        )

        return module