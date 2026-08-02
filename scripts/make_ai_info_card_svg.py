import os
import sys

def generate_ai_info_card_svg(output_path="ai-info-card.svg"):
    width = 860
    height = 380

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .header-bar { fill: #161b22; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 16px; fill: #58a6ff; font-weight: 700; }')
    svg_lines.append('    .subtitle { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #8b949e; }')
    svg_lines.append('    .card-box { fill: #161b22; stroke: #30363d; stroke-width: 1.5px; rx: 6px; }')
    svg_lines.append('    .card-title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 12px; fill: #79c0ff; font-weight: 600; }')
    svg_lines.append('    .card-sub { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 10px; fill: #c9d1d9; }')
    svg_lines.append('    .badge-bg { fill: #21262d; rx: 4px; }')
    svg_lines.append('    .badge-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 10px; fill: #7ee787; font-weight: 600; }')
    svg_lines.append('    .stat-val { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 18px; fill: #58a6ff; font-weight: 700; }')
    svg_lines.append('    .stat-lbl { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9.5px; fill: #8b949e; }')
    svg_lines.append('  </style>')

    # Outer Container
    svg_lines.append(f'  <rect class="bg" width="{width}" height="{height}" rx="8" />')

    # Top Header Banner
    svg_lines.append(f'  <rect class="header-bar" x="0" y="0" width="{width}" height="65" rx="8" />')
    svg_lines.append('  <text class="title" x="24" y="28">RUTURAJ BHASKAR NAWALE</text>')
    svg_lines.append('  <text class="subtitle" x="24" y="48">Production AI Engineer | Computer Vision, Document AI (OCR) &amp; Deepfake Detection | SGPA: 9.40</text>')

    # Stats Highlights (4 Columns across top)
    stats = [
        {"val": "9.40 SGPA", "lbl": "B.Sc Computer Science"},
        {"val": "4 Platforms", "lbl": "Production AI Systems"},
        {"val": "Robotics &amp; AI", "lbl": "Conference Publication"},
        {"val": "1,668+", "lbl": "GitHub Contributions"}
    ]

    for i, st in enumerate(stats):
        x = 540 + i * 78
        svg_lines.append(f'  <text class="stat-val" x="{x}" y="28" text-anchor="middle">{st["val"]}</text>')
        svg_lines.append(f'  <text class="stat-lbl" x="{x}" y="45" text-anchor="middle">{st["lbl"]}</text>')

    # 4 Key AI Platform Cards
    projects = [
        {
            "x": 20, "y": 80, "w": 395, "h": 130,
            "title": "[1] DEEPFAKE DETECTION &amp; MEDIA AUTHENTICITY",
            "desc": "Multi-model ensemble (EfficientNet + ViT + XceptionNet + InsightFace) for frame-level facial artifact analysis &amp; temporal anomaly detection.",
            "tech": "PyTorch • FastAPI • OpenCV • ViT • RetinaFace"
        },
        {
            "x": 445, "y": 80, "w": 395, "h": 130,
            "title": "[2] MERCHANT KYC &amp; INTELLIGENT FRAUD PREVENTION",
            "desc": "LayoutLMv3 + TrOCR document parsing, ArcFace biometric face matching, key-value extraction, &amp; image forensics for document tampering.",
            "tech": "LayoutLMv3 • PaddleOCR • ArcFace • XGBoost"
        },
        {
            "x": 20, "y": 225, "w": 395, "h": 130,
            "title": "[3] AI 5V BANKING RECONCILIATION PLATFORM",
            "desc": "High-throughput UPI/NPCI/CBS transaction stream ingestion, Isolation Forest &amp; XGBoost anomaly detection, with 5 executive KPI dashboards.",
            "tech": "FastAPI • Polars • Isolation Forest • Prophet"
        },
        {
            "x": 445, "y": 225, "w": 395, "h": 130,
            "title": "[4] 360 DEGREE MERCHANT INTELLIGENCE &amp; RISK ENGINE",
            "desc": "Automated crawling across WHOIS/DNS/SSL, GSTIN/CIN validation, social media discovery, &amp; tech fingerprinting into structured JSON with AI risk score.",
            "tech": "Playwright • Selenium • BeautifulSoup • FastAPI"
        }
    ]

    for p in projects:
        svg_lines.append(f'  <rect class="card-box" x="{p["x"]}" y="{p["y"]}" width="{p["w"]}" height="{p["h"]}" rx="6" />')
        svg_lines.append(f'  <text class="card-title" x="{p["x"] + 14}" y="{p["y"] + 24}">{p["title"]}</text>')
        svg_lines.append(f'  <line x1="{p["x"] + 14}" y1="{p["y"] + 32}" x2="{p["x"] + p["w"] - 14}" y2="{p["y"] + 32}" stroke="#30363d" stroke-width="1" />')

        # Split description into 2 lines if needed
        words = p["desc"].split()
        line1 = " ".join(words[:len(words)//2])
        line2 = " ".join(words[len(words)//2:])

        svg_lines.append(f'  <text class="card-sub" x="{p["x"] + 14}" y="{p["y"] + 52}">{line1}</text>')
        svg_lines.append(f'  <text class="card-sub" x="{p["x"] + 14}" y="{p["y"] + 68}">{line2}</text>')

        # Tech Badge at bottom of card
        svg_lines.append(f'  <rect class="badge-bg" x="{p["x"] + 14}" y="{p["y"] + 88}" width="{p["w"] - 28}" height="24" />')
        svg_lines.append(f'  <text class="badge-text" x="{p["x"] + 24}" y="{p["y"] + 104}">STACK: {p["tech"]}</text>')

    svg_lines.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Successfully generated AI Info Card SVG: '{output_path}'")

if __name__ == "__main__":
    generate_ai_info_card_svg("ai-info-card.svg")
