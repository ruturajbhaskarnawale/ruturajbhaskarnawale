import os
import sys

def generate_info_card(output_path="info-card.svg"):
    is_static = os.environ.get("STATIC") == "1"

    width = 490
    height = 530

    card_data = [
        ("USER", "ruturajbhaskarnawale (Ruturaj Nawale)"),
        ("ROLE", "Production AI Engineer (CV, OCR, LLMs)"),
        ("EDUCATION", "B.Sc Computer Science | SGPA: 9.40"),
        ("EXPERIENCE", "AI Engineer @ Jode Technologies"),
        ("SPECIALTY", "Deepfake Detection & Document AI (KYC)"),
        ("STACK", "PyTorch, FastAPI, LayoutLMv3, OpenCV, ViT"),
        ("PUBLICATIONS", "National Conf. on Robotics & AI (2025)"),
        ("LOCATION", "Navi Mumbai, Maharashtra, India"),
        ("PORTFOLIO", "ruturaj-nawale-portfolio.vercel.app"),
        ("STATUS", ">> Open for High-Impact AI & ML Roles")
    ]

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .title-bar { fill: #161b22; }')
    svg_lines.append('    .dot-red { fill: #ff5f56; }')
    svg_lines.append('    .dot-yellow { fill: #ffbd2e; }')
    svg_lines.append('    .dot-green { fill: #27c93f; }')
    svg_lines.append('    .title-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 12px; fill: #8b949e; font-weight: 600; }')
    svg_lines.append('    .prompt-user { fill: #58a6ff; font-weight: bold; }')
    svg_lines.append('    .prompt-at { fill: #8b949e; }')
    svg_lines.append('    .prompt-host { fill: #bc8cff; font-weight: bold; }')
    svg_lines.append('    .prompt-sep { fill: #8b949e; }')
    svg_lines.append('    .key { fill: #79c0ff; font-weight: 600; font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11.5px; }')
    svg_lines.append('    .val { fill: #c9d1d9; font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11.5px; }')
    svg_lines.append('    .separator { stroke: #30363d; stroke-width: 1px; }')

    if not is_static:
        svg_lines.append('    .animate-line { opacity: 0; animation: fadeInSlide 0.4s ease-out forwards; }')
        svg_lines.append('    @keyframes fadeInSlide {')
        svg_lines.append('      from { opacity: 0; transform: translateY(6px); }')
        svg_lines.append('      to { opacity: 1; transform: translateY(0); }')
        svg_lines.append('    }')
    else:
        svg_lines.append('    .animate-line { opacity: 1; }')

    svg_lines.append('  </style>')

    # Card background and header
    svg_lines.append(f'  <rect class="bg" width="{width}" height="{height}" rx="8" />')
    svg_lines.append(f'  <path class="title-bar" d="M 0 8 A 8 8 0 0 1 8 0 L {width-8} 0 A 8 8 0 0 1 {width} 8 L {width} 32 L 0 32 Z" />')
    svg_lines.append('  <circle class="dot-red" cx="16" cy="16" r="5" />')
    svg_lines.append('  <circle class="dot-yellow" cx="32" cy="16" r="5" />')
    svg_lines.append('  <circle class="dot-green" cx="48" cy="16" r="5" />')
    svg_lines.append(f'  <text class="title-text" x="{width/2}" y="20" text-anchor="middle">neofetch --ai-engineer ruturajbhaskarnawale</text>')

    y = 56
    stagger_delay = 0.1

    # Prompt Header
    anim_style = f'style="animation-delay: {round(stagger_delay, 2)}s;"' if not is_static else ''
    svg_lines.append(f'  <g class="animate-line" {anim_style}>')
    svg_lines.append(f'    <text x="20" y="{y}" class="val">')
    svg_lines.append('      <tspan class="prompt-user">ruturaj</tspan>')
    svg_lines.append('      <tspan class="prompt-at">@</tspan>')
    svg_lines.append('      <tspan class="prompt-host">ai-workstation</tspan>')
    svg_lines.append('      <tspan class="prompt-sep">-----------------------------</tspan>')
    svg_lines.append('    </text>')
    svg_lines.append('  </g>')

    y += 28
    stagger_delay += 0.1

    # Key / Value lines
    for key, val in card_data:
        anim_style = f'style="animation-delay: {round(stagger_delay, 2)}s;"' if not is_static else ''
        svg_lines.append(f'  <g class="animate-line" {anim_style}>')
        svg_lines.append(f'    <text x="20" y="{y}">')
        svg_lines.append(f'      <tspan class="key">{key.ljust(11)}:</tspan> ')
        svg_lines.append(f'      <tspan class="val">{val.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</tspan>')
        svg_lines.append('    </text>')
        svg_lines.append('  </g>')
        y += 30
        stagger_delay += 0.08

    # Separator rule
    anim_style = f'style="animation-delay: {round(stagger_delay, 2)}s;"' if not is_static else ''
    y += 6
    svg_lines.append(f'  <g class="animate-line" {anim_style}>')
    svg_lines.append(f'    <line x1="20" y1="{y}" x2="{width - 20}" y2="{y}" class="separator" />')
    svg_lines.append('  </g>')

    y += 26
    stagger_delay += 0.08

    # Color Palette blocks
    colors = ["#21262d", "#ff7b72", "#7ee787", "#ffa657", "#79c0ff", "#d2a8ff", "#a5d6ff", "#f0f6fc"]
    svg_lines.append(f'  <g class="animate-line" style="animation-delay: {round(stagger_delay, 2)}s;">')
    svg_lines.append(f'    <g transform="translate(20, {y})">')
    for i, c in enumerate(colors):
        svg_lines.append(f'      <rect x="{i*30}" y="0" width="24" height="14" fill="{c}" rx="2" />')
    svg_lines.append('    </g>')
    svg_lines.append('  </g>')

    svg_lines.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Successfully generated info card SVG: '{output_path}'")

if __name__ == "__main__":
    generate_info_card("info-card.svg")
