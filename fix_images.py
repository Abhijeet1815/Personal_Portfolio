import re

file_path = "/Users/abhijeetsharma/Desktop/Personal_Portfolio/portfolio.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Lab (Phineas.jpeg)
content = re.sub(
    r'<img src="data:image/[^"]+base64,[^"]+" alt="Hello — Phineas and Ferb in the lab" />',
    '<img src="Phineas.jpeg" alt="Hello — Phineas and Ferb in the lab" />',
    content
)

# 2. Hero Intro BG (City.jpeg) - in CSS .hero-intro-bg
content = re.sub(
    r'\.hero-intro-bg\{\s*background-image:url\(\'data:image/[^\']+\'\);',
    ".hero-intro-bg{\n  background-image:url('City.jpeg');",
    content
)

# 3. About Scene Wrap (Phineas_and_Ferb_under_tree.jpeg) - in CSS .about-scene-wrap
content = re.sub(
    r'\.about-scene-wrap\{\s*position:absolute;[^}]*background-image:url\(\'data:image/[^\']+\'\);',
    lambda m: m.group(0).replace(re.search(r'url\(\'data:image/[^\']+\'\)', m.group(0)).group(0), "url('Phineas_and_Ferb_under_tree.jpeg')"),
    content
)

# 4. About Image Panel (P&F.jpeg) - in HTML
content = re.sub(
    r'<img src="data:image/[^"]+" alt="The gang in class" />',
    '<img src="P&F.jpeg" alt="The gang in class" />',
    content
)

# 5. Contact Section (Doofenshmirtz_Evil_Inc..jpeg) - in CSS .contact-overlay
content = re.sub(
    r'\.contact-overlay\{\s*position:absolute;[^}]*background-image:url\(\'data:image/[^\']+\'\);',
    lambda m: m.group(0).replace(re.search(r'url\(\'data:image/[^\']+\'\)', m.group(0)).group(0), "url('Doofenshmirtz_Evil_Inc..jpeg')"),
    content
)

# 6. Perry Easter Egg (AgentP.png) - at the bottom
content = re.sub(
    r'<img class="perry-corner" src="data:image/[^"]+"',
    '<img class="perry-corner" src="AgentP.png"',
    content
)

# 7. Hero Chars (hero-chars) - just remove the src to make it clean, or remove the tag
content = re.sub(
    r'<img class="hero-chars" src="data:image/[^"]+" alt="Phineas, Ferb and Perry in the backyard" />',
    '',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images replaced.")
