from setuptools import setup
setup(
    entry_points={
        "console_scripts": [
            "yaml-sorter = pre_commit_hooks.yaml_sorter:main",
        ],
    }
)
