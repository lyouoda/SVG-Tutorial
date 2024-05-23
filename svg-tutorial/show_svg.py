import os
import sys

if len(sys.argv) == 1:
    print(
        f"Usage: {sys.argv[0]} [dir1] [dir2] ...\n"
    )
    sys.exit(-1)

folders: list[str] = sys.argv[1:]
svg_files: list[str] = [
    f'<img class="svg" src="{os.path.join(folder, file)}" />'
    if file.endswith(".svg") else f"<h2>{folder}</h2>"
    for folder in folders
    for file in [folder]+os.listdir(folder)
]

code = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SVG Tutorial</title>
    <style>
        svg,
        .svg {{
            padding: 0.5em;
            width: 35px;
            border-radius: 10px;
        }}

        svg line {{
            stroke-linecap: round;
        }}

        svg:hover,
        .svg:hover {{
            background-color: rgb(213, 214, 205);
        }}
    </style>
</head>
<body>
    <h1>Show SVG file</h1>
{"    " + "\n    ".join(svg_files)}
</body>
</html>"""

print(code)
