import markdown
import os

md_file = 'c:\\Users\\Gyanankur Baruah\\Downloads\\ai agents fp20\\docs\\PowerBI_Dashboard_Specification.md'
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

html_template = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{font-family: Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px;}}
table {{border-collapse: collapse; width: 100%; margin: 20px 0;}}
th, td {{border: 1px solid #ddd; padding: 12px; text-align: left;}}
th {{background-color: #4CAF50; color: white;}}
pre {{background-color: #f4f4f4; padding: 15px; overflow-x: auto;}}
code {{font-family: monospace;}}
</style>
</head>
<body>
{html}
</body>
</html>'''

html_file = 'c:\\Users\\Gyanankur Baruah\\Downloads\\ai agents fp20\\docs\\PowerBI_Dashboard_Specification.html'
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f'HTML saved to: {html_file}')
print('You can open this HTML file in a browser and print it to PDF')
