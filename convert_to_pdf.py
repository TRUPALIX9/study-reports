#!/usr/bin/env python3
"""
Script to convert the L04-Submission.md to PDF using markdown and weasyprint.
Install dependencies: pip install markdown weasyprint
"""

import markdown
import weasyprint
import os

def convert_markdown_to_pdf():
    # Read the markdown file
    with open('L04-Submission.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(markdown_content, extensions=['codehilite', 'tables'])
    
    # Add CSS for better formatting
    css = """
    <style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    h1, h2, h3 {
        color: #333;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
    code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 3px;
    }
    pre {
        background-color: #f4f4f4;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    .mermaid {
        text-align: center;
        margin: 20px 0;
    }
    </style>
    """
    
    # Combine HTML with CSS
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>L04 Submission</title>
        {css}
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    # Convert to PDF
    pdf_path = 'L04-Submission.pdf'
    weasyprint.HTML(string=full_html).write_pdf(pdf_path)
    
    print(f"✅ PDF created successfully: {pdf_path}")

if __name__ == "__main__":
    convert_markdown_to_pdf()
