import os
import sys
import numpy as np
from PIL import Image

RAMP = " .`:-=+*cs#%@"  # bright (sparse) -> dark (dense)

def image_to_ascii(image_path, width=100, height=53):
    if not os.path.exists(image_path):
        print(f"Error: Prepped image '{image_path}' not found.")
        sys.exit(1)

    img = Image.open(image_path).convert("L")
    img_resized = img.resize((width, height), Image.Resampling.LANCZOS)
    arr = np.array(img_resized)

    # Map 0-255 brightness to RAMP indices
    # 255 (white) -> index 0 (' '), 0 (black) -> index len(RAMP)-1 ('@')
    ramp_len = len(RAMP)
    normalized = arr / 255.0
    indices = np.clip((1.0 - normalized) * (ramp_len - 1), 0, ramp_len - 1).astype(int)

    ascii_rows = []
    for r in range(height):
        row_str = "".join(RAMP[idx] for idx in indices[r])
        ascii_rows.append(row_str)

    return ascii_rows

def generate_ascii_svg(ascii_rows, output_path="avi-ascii.svg"):
    num_rows = len(ascii_rows)
    num_cols = len(ascii_rows[0]) if num_rows > 0 else 100

    char_width = 6.0
    char_height = 10.0
    font_size = 9.0

    svg_width = int(num_cols * char_width + 20)
    svg_height = int(num_rows * char_height + 20)

    total_anim_duration = 3.5  # seconds for full printout
    row_dur = total_anim_duration / num_rows

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: #0d1117; }')
    svg_lines.append('    .ascii-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; font-size: 9px; fill: #8b949e; white-space: pre; }')
    svg_lines.append('    .cursor { fill: #58a6ff; }')
    svg_lines.append('  </style>')

    # Background rect
    svg_lines.append(f'  <rect class="bg" width="{svg_width}" height="{svg_height}" rx="6" />')

    # Clip-path definitions for row wiping
    svg_lines.append('  <defs>')
    for r in range(num_rows):
        y_pos = 10 + r * char_height
        svg_lines.append(f'    <clipPath id="clip-row-{r}">')
        svg_lines.append(f'      <rect x="10" y="{y_pos - 1}" width="0" height="{char_height + 2}">')
        start_time = round(r * row_dur, 3)
        svg_lines.append(f'        <animate attributeName="width" from="0" to="{svg_width - 20}" begin="{start_time}s" dur="{round(row_dur, 3)}s" fill="freeze" calcMode="linear" />')
        svg_lines.append('      </rect>')
        svg_lines.append('    </clipPath>')
    svg_lines.append('  </defs>')

    # Rows of text with clip-path
    for r, row_str in enumerate(ascii_rows):
        y_pos = 18 + r * char_height
        # Escape xml entities
        escaped_row = row_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg_lines.append(f'  <g clip-path="url(#clip-row-{r})">')
        svg_lines.append(f'    <text x="10" y="{y_pos}" class="ascii-text">{escaped_row}</text>')
        svg_lines.append('  </g>')

    # Animated block cursor riding row by row
    svg_lines.append('  <!-- Typing cursor indicator -->')
    for r in range(num_rows):
        y_pos = 10 + r * char_height
        start_time = round(r * row_dur, 3)
        dur = round(row_dur, 3)
        svg_lines.append(f'  <rect class="cursor" y="{y_pos}" width="6" height="{char_height}" opacity="0">')
        svg_lines.append(f'    <animate attributeName="x" from="10" to="{svg_width - 16}" begin="{start_time}s" dur="{dur}s" fill="freeze" />')
        svg_lines.append(f'    <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.01;0.99;1" begin="{start_time}s" dur="{dur}s" fill="freeze" />')
        svg_lines.append('  </rect>')

    svg_lines.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Successfully generated ASCII SVG: '{output_path}'")

if __name__ == "__main__":
    image_file = sys.argv[1] if len(sys.argv) > 1 else "source-prepped.png"
    if not os.path.exists(image_file):
        # Check if source photo exists, run prep_photo first
        if os.path.exists("Ruturaj_Passport_photo.png"):
            from prep_photo import prep_photo
            prep_photo("Ruturaj_Passport_photo.png", "source-prepped.png")
            image_file = "source-prepped.png"
        else:
            print(f"Error: {image_file} does not exist.")
            sys.exit(1)

    rows = image_to_ascii(image_file, width=100, height=53)
    generate_ascii_svg(rows, "avi-ascii.svg")
