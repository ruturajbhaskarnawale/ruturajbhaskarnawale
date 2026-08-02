import os
import sys

def generate_ai_pipeline_svg(output_path="ai-pipeline.svg"):
    width = 860
    height = 260

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 13px; fill: #58a6ff; font-weight: 600; }')
    svg_lines.append('    .box { fill: #161b22; stroke: #30363d; stroke-width: 1.5px; rx: 6px; }')
    svg_lines.append('    .box-active { fill: #1c2128; stroke: #58a6ff; stroke-width: 2px; rx: 6px; }')
    svg_lines.append('    .node-title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #58a6ff; font-weight: 600; }')
    svg_lines.append('    .node-sub { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9.5px; fill: #8b949e; }')
    svg_lines.append('    .flow-line { stroke: #30363d; stroke-width: 2px; stroke-dasharray: 4; animation: dashFlow 2s linear infinite; }')
    svg_lines.append('    .pulse-dot { fill: #39d353; animation: pulse 1.5s ease-in-out infinite alternate; }')
    svg_lines.append('    .tag { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 9px; fill: #7ee787; font-weight: bold; }')
    svg_lines.append('    @keyframes dashFlow { from { stroke-dashoffset: 16; } to { stroke-dashoffset: 0; } }')
    svg_lines.append('    @keyframes pulse { from { opacity: 0.4; r: 3; } to { opacity: 1; r: 5; } }')
    svg_lines.append('  </style>')

    # Background
    svg_lines.append(f'  <rect class="bg" width="{width}" height="{height}" rx="8" />')

    # Title
    svg_lines.append('  <text class="title" x="20" y="30">🤖 MULTI-MODEL DEEPFAKE & DOCUMENT AI PIPELINE ARCHITECTURE</text>')

    # Pipeline Nodes
    nodes = [
        {"x": 20, "y": 60, "w": 145, "h": 140, "title": "1. Media Ingestion", "sub1": "Images / Video Streams", "sub2": "Frame Alignment", "sub3": "RetinaFace Detection", "color": "#79c0ff"},
        {"x": 190, "y": 60, "w": 155, "h": 140, "title": "2. Document AI & OCR", "sub1": "LayoutLMv3 Parsing", "sub2": "PaddleOCR + TrOCR", "sub3": "Key-Value Extraction", "color": "#d2a8ff"},
        {"x": 370, "y": 60, "w": 165, "h": 140, "title": "3. Deep Feature AI", "sub1": "EfficientNet & ViT", "sub2": "XceptionNet Traces", "sub3": "InsightFace Embeddings", "color": "#ffa657"},
        {"x": 560, "y": 60, "w": 140, "h": 140, "title": "4. Ensemble & Risk", "sub1": "Temporal Anomalies", "sub2": "XGBoost Classifier", "sub3": "Biometric Match", "color": "#ff7b72"},
        {"x": 725, "y": 60, "w": 115, "h": 140, "title": "5. Outcome", "sub1": "Authentic ✅", "sub2": "Deepfake ❌", "sub3": "Fraud Risk Score", "color": "#7ee787"},
    ]

    for n in nodes:
        svg_lines.append(f'  <rect class="box" x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="6" />')
        svg_lines.append(f'  <text class="node-title" x="{n["x"] + 12}" y="{n["y"] + 24}" fill="{n["color"]}">{n["title"]}</text>')
        svg_lines.append(f'  <line x1="{n["x"] + 12}" y1="{n["y"] + 32}" x2="{n["x"] + n["w"] - 12}" y2="{n["y"] + 32}" stroke="#30363d" stroke-width="1" />')
        svg_lines.append(f'  <text class="node-sub" x="{n["x"] + 12}" y="{n["y"] + 52}">• {n["sub1"]}</text>')
        svg_lines.append(f'  <text class="node-sub" x="{n["x"] + 12}" y="{n["y"] + 74}">• {n["sub2"]}</text>')
        svg_lines.append(f'  <text class="node-sub" x="{n["x"] + 12}" y="{n["y"] + 96}">• {n["sub3"]}</text>')

    # Connectors / Animated Flow Arrows
    for i in range(len(nodes) - 1):
        x1 = nodes[i]["x"] + nodes[i]["w"]
        y1 = nodes[i]["y"] + nodes[i]["h"] / 2
        x2 = nodes[i+1]["x"]
        y2 = nodes[i+1]["y"] + nodes[i+1]["h"] / 2

        svg_lines.append(f'  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="flow-line" stroke="#58a6ff" />')
        svg_lines.append(f'  <circle cx="{(x1 + x2)/2}" cy="{y1}" class="pulse-dot" />')

    # Footer status
    svg_lines.append(f'  <text class="node-sub" x="20" y="{height - 18}">⚡ Latency: &lt;150ms/frame | Real-Time Inference | End-to-End PyTorch &amp; FastAPI Pipeline</text>')

    svg_lines.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Successfully generated AI Pipeline SVG: '{output_path}'")

if __name__ == "__main__":
    generate_ai_pipeline_svg("ai-pipeline.svg")
