import os
import sys
import json
from datetime import datetime

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap_svg(json_path="data/contributions.json", output_path="contrib-heatmap.svg"):
    if not os.path.exists(json_path):
        print(f"Error: Contribution data file '{json_path}' not found.")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    if not days:
        print("Error: No day data found in json.")
        sys.exit(1)

    total_contribs = data.get("total_contributions", 0)
    current_streak = data.get("current_streak", 0)
    longest_streak = data.get("longest_streak", 0)

    # Sort days chronologically
    days_sorted = sorted(days, key=lambda x: x["date"])

    # Group into weeks (53 weeks x 7 days)
    # Align day 0 = Sunday or Monday
    weeks = []
    current_week = []

    # Pad first week if starting mid-week
    first_date = datetime.strptime(days_sorted[0]["date"], "%Y-%m-%d")
    # Python weekday: 0=Mon, 6=Sun. GitHub calendar starts on Sunday (weekday 6 -> 0)
    gh_weekday = (first_date.weekday() + 1) % 7

    for _ in range(gh_weekday):
        current_week.append(None)

    for day in days_sorted:
        current_week.append(day)
        if len(current_week) == 7:
            weeks.append(current_week)
            current_week = []

    if current_week:
        while len(current_week) < 7:
            current_week.append(None)
        weeks.append(current_week)

    # Ensure max 53 weeks
    weeks = weeks[-53:]

    # SVG layout specs
    svg_width = 860
    svg_height = 210
    grid_x_offset = 45
    grid_y_offset = 55
    box_size = 11
    box_gap = 3

    svg_lines = []
    svg_lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1px; }')
    svg_lines.append('    .header-title { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 13px; fill: #58a6ff; font-weight: 600; }')
    svg_lines.append('    .month-text, .day-label { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 10px; fill: #8b949e; }')
    svg_lines.append('    .footer-text { font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace; font-size: 11px; fill: #8b949e; }')
    svg_lines.append('    .highlight { fill: #39d353; font-weight: 600; }')
    svg_lines.append('    .day-box { opacity: 0; animation: diagSlideDown 0.35s ease-out forwards; }')
    svg_lines.append('    @keyframes diagSlideDown {')
    svg_lines.append('      from { opacity: 0; transform: translateY(-6px) scale(0.85); }')
    svg_lines.append('      to { opacity: 1; transform: translateY(0) scale(1); }')
    svg_lines.append('    }')
    svg_lines.append('  </style>')

    # Background card
    svg_lines.append(f'  <rect class="bg" width="{svg_width}" height="{svg_height}" rx="8" />')

    # Title header
    username = data.get("username", "ruturajbhaskarnawale")
    svg_lines.append(f'  <text class="header-title" x="20" y="30">contrib-heatmap --user {username}</text>')

    # Month headers
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    last_month = None
    for w_idx, week in enumerate(weeks):
        # Check first non-None day in week to place month label
        valid_day = next((d for d in week if d is not None), None)
        if valid_day:
            m_str = datetime.strptime(valid_day["date"], "%Y-%m-%d").strftime("%b")
            if m_str != last_month:
                x_pos = grid_x_offset + w_idx * (box_size + box_gap)
                svg_lines.append(f'    <text class="month-text" x="{x_pos}" y="45">{m_str}</text>')
                last_month = m_str

    # Day labels (Mon, Wed, Fri)
    day_labels = [("Mon", 1), ("Wed", 3), ("Fri", 5)]
    for lbl, row_idx in day_labels:
        y_pos = grid_y_offset + row_idx * (box_size + box_gap) + 9
        svg_lines.append(f'  <text class="day-label" x="15" y="{y_pos}">{lbl}</text>')

    # Render day boxes with diagonal animation delay
    for w_idx, week in enumerate(weeks):
        x_pos = grid_x_offset + w_idx * (box_size + box_gap)
        for d_idx, day in enumerate(week):
            if day is None:
                continue

            y_pos = grid_y_offset + d_idx * (box_size + box_gap)
            level = day.get("level", 0)
            color = PALETTE[min(level, len(PALETTE) - 1)]

            # Diagonal animation index = w_idx + d_idx
            delay = round((w_idx + d_idx) * 0.015, 3)
            date_str = day.get("date", "")
            count = day.get("count", 0)

            svg_lines.append(
                f'  <rect class="day-box" x="{x_pos}" y="{y_pos}" width="{box_size}" height="{box_size}" fill="{color}" rx="2" '
                f'style="animation-delay: {delay}s;">'
                f'<title>{count} contributions on {date_str}</title></rect>'
            )

    # Footer stats & Legend
    footer_y = svg_height - 18
    svg_lines.append(f'  <text class="footer-text" x="20" y="{footer_y}">')
    svg_lines.append(f'    <tspan class="highlight">{total_contribs:,}</tspan> contributions in the last year')
    svg_lines.append(f'    <tspan dx="15">Streak: </tspan><tspan class="highlight">{current_streak} days</tspan>')
    svg_lines.append(f'    <tspan dx="15">Longest: </tspan><tspan class="highlight">{longest_streak} days</tspan>')
    svg_lines.append('  </text>')

    # Legend Less -> More on right side of footer
    legend_start_x = svg_width - 165
    svg_lines.append(f'  <g transform="translate({legend_start_x}, {footer_y - 10})">')
    svg_lines.append('    <text class="month-text" x="0" y="9">Less</text>')
    for i, c in enumerate(PALETTE):
        svg_lines.append(f'    <rect x="{30 + i * 14}" y="0" width="11" height="11" fill="{c}" rx="2" />')
    svg_lines.append(f'    <text class="month-text" x="{30 + len(PALETTE) * 14 + 5}" y="9">More</text>')
    svg_lines.append('  </g>')

    svg_lines.append('</svg>')

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print(f"Successfully generated heatmap SVG: '{output_path}'")

if __name__ == "__main__":
    json_path = sys.argv[1] if len(sys.argv) > 1 else "data/contributions.json"
    if not os.path.exists(json_path):
        from fetch_contributions import fetch_contributions
        data = fetch_contributions("ruturajbhaskarnawale")
        os.makedirs("data", exist_ok=True)
        with open("data/contributions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        json_path = "data/contributions.json"

    render_heatmap_svg(json_path, "contrib-heatmap.svg")
