import os
import sys

def generate_ai_info_card_svg(output_path="ai-info-card.svg"):
    width = 860
    height = 420

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .header-bar { fill: #161b22; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 15px; fill: #58a6ff; font-weight: 700; }')
    svg_lines.append('    .subtitle { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 10.5px; fill: #8b949e; }')
    svg_lines.append('    .card-box { fill: #161b22; stroke: #30363d; stroke-width: 1.5px; rx: 6px; }')
    svg_lines.append('    .card-title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11.5px; fill: #79c0ff; font-weight: 600; }')
    svg_lines.append('    .card-sub { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9.5px; fill: #c9d1d9; }')
    svg_lines.append('    .badge-bg { fill: #21262d; rx: 4px; }')
    svg_lines.append('    .badge-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9.5px; fill: #7ee787; font-weight: 600; }')
    svg_lines.append('    .stat-val { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 14px; fill: #58a6ff; font-weight: 700; }')
    svg_lines.append('    .stat-lbl { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9px; fill: #8b949e; }')
    svg_lines.append('  </style>')

    # Outer Background
    svg_lines.append(f'  <rect class="bg" width="{width}" height="{height}" rx="8" />')

    # Header Banner
    svg_lines.append(f'  <rect class="header-bar" x="0" y="0" width="{width}" height="70" rx="8" />')
    svg_lines.append('  <text class="title" x="20" y="28">RUTURAJ BHASKAR NAWALE</text>')
    svg_lines.append('  <text class="subtitle" x="20" y="50">Production AI Engineer | Computer Vision, Document AI (OCR) &amp; Deepfake Detection</text>')

    # Stat Badges (Right side of header with spacious offsets)
    stats = [
        {"x": 450, "val": "9.40 SGPA", "lbl": "B.Sc CS"},
        {"x": 550, "val": "4 AI Systems", "lbl": "Production"},
        {"x": 665, "val": "Robotics &amp; AI", "lbl": "Conference '25"},
        {"x": 780, "val": "1,668+", "lbl": "Contributions"}
    ]

    for st in stats:
        svg_lines.append(f'  <text class="stat-val" x="{st["x"]}" y="30" text-anchor="middle">{st["val"]}</text>')
        svg_lines.append(f'  <text class="stat-lbl" x="{st["x"]}" y="48" text-anchor="middle">{st["lbl"]}</text>')

    # 4 Project Cards with padded layout
    projects = [
        {
            "x": 20, "y": 85, "w": 395, "h": 150,
            "title": "[1] DEEPFAKE DETECTION &amp; AUTHENTICITY",
            "desc1": "Multi-model ensemble (EfficientNet, ViT, XceptionNet)",
            "desc2": "for frame-level facial artifact analysis &amp; anomalies.",
            "tech": "STACK: PyTorch • FastAPI • OpenCV • ViT • RetinaFace"
        },
        {
            "x": 445, "y": 85, "w": 395, "h": 150,
            "title": "[2] MERCHANT KYC &amp; FRAUD PREVENTION",
            "desc1": "LayoutLMv3 + TrOCR document parsing, ArcFace face",
            "desc2": "matching, key-value extraction &amp; metadata forensics.",
            "tech": "STACK: LayoutLMv3 • PaddleOCR • ArcFace • XGBoost"
        },
        {
            "x": 20, "y": 250, "w": 395, "h": 150,
            "title": "[3] AI 5V BANKING RECONCILIATION PLATFORM",
            "desc1": "High-throughput UPI/NPCI/CBS transaction stream",
            "desc2": "ingestion with Isolation Forest &amp; XGBoost anomaly AI.",
            "tech": "STACK: FastAPI • Polars • Isolation Forest • Prophet"
        },
        {
            "x": 445, "y": 250, "w": 395, "h": 150,
            "title": "[4] 360 MERCHANT INTELLIGENCE &amp; RISK ENGINE",
            "desc1": "Automated crawling across WHOIS/DNS/SSL &amp; GSTIN",
            "desc2": "validation into structured JSON with AI risk score.",
            "tech": "STACK: Playwright • Selenium • BeautifulSoup • FastAPI"
        }
    ]

    for p in projects:
        svg_lines.append(f'  <rect class="card-box" x="{p["x"]}" y="{p["y"]}" width="{p["w"]}" height="{p["h"]}" rx="6" />')
        svg_lines.append(f'  <text class="card-title" x="{p["x"] + 14}" y="{p["y"] + 26}">{p["title"]}</text>')
        svg_lines.append(f'  <line x1="{p["x"] + 14}" y1="{p["y"] + 36}" x2="{p["x"] + p["w"] - 14}" y2="{p["y"] + 36}" stroke="#30363d" stroke-width="1" />')

        svg_lines.append(f'  <text class="card-sub" x="{p["x"] + 14}" y="{p["y"] + 58}">{p["desc1"]}</text>')
        svg_lines.append(f'  <text class="card-sub" x="{p["x"] + 14}" y="{p["y"] + 76}">{p["desc2"]}</text>')

        # Tech Badge at bottom of card
        svg_lines.append(f'  <rect class="badge-bg" x="{p["x"] + 14}" y="{p["y"] + 104}" width="{p["w"] - 28}" height="28" />')
        svg_lines.append(f'  <text class="badge-text" x="{p["x"] + 24}" y="{p["y"] + 122}">{p["tech"]}</text>')

    svg_lines.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Successfully generated AI Info Card SVG: '{output_path}'")

if __name__ == "__main__":
    generate_ai_info_card_svg("ai-info-card.svg")
