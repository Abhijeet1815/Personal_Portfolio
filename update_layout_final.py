import re

file_path = "/Users/abhijeetsharma/Desktop/Personal_Portfolio/portfolio (2).html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .ferb-banner-overlay
old_ferb_css = """.ferb-banner-overlay {
  position: absolute;
  top: 15%;
  left: 50%;
  transform: translateX(-50%);
  background: var(--orange);
  color: #fff;
  padding: 1.2rem 2.5rem;
  border-radius: 40px;
  font-family: 'Fredoka One', cursive;
  font-size: clamp(0.9rem, 2.5vw, 1.8rem);
  text-align: center;
  width: auto;
  max-width: 80%;
  letter-spacing: 0.05em;
  box-shadow: 0 10px 25px rgba(255, 107, 53, 0.4);
  z-index: 10;
}
.ferb-banner-overlay::before {
  content: '';
  position: absolute;
  background: var(--orange);
  border-radius: 50%;
  width: 24px;
  height: 24px;
  bottom: -20px;
  left: 65%;
  box-shadow: 0 5px 15px rgba(255,107,53,0.3);
}
.ferb-banner-overlay::after {
  content: '';
  position: absolute;
  background: var(--orange);
  border-radius: 50%;
  width: 14px;
  height: 14px;
  bottom: -40px;
  left: 68%;
  box-shadow: 0 5px 15px rgba(255,107,53,0.3);
}"""
new_ferb_css = """.ferb-banner-overlay {
  position: absolute;
  top: 0;
  left: 0;
  background: var(--navy2);
  color: #fff;
  padding: 1.2rem 0;
  font-family: 'Fredoka One', cursive;
  font-size: clamp(1.5rem, 4vw, 3rem);
  text-align: center;
  width: 100%;
  letter-spacing: 0.05em;
  z-index: 10;
  white-space: nowrap;
}"""
content = content.replace(old_ferb_css, new_ferb_css)

# 2. Update about-scene CSS
old_about_css = """.about-scene-wrap{
  position:absolute;top:0;bottom:0;left:0;right:0;height:100%;
  opacity:1;
  background-position:80% center;
  background-size:cover;
  background-image:url('Phineas_and_Ferb_under_tree.jpeg');
  background-size:cover;background-position:center top;
  pointer-events:none;
}"""
new_about_css = """.about-scene-bg{
  width:100%;
  display:block;
  height:auto;
}
#about{
  position:relative;
  overflow:hidden;
  display:flex;
  align-items:center;
}"""
content = content.replace(old_about_css, new_about_css)

# 3. Extract and replace the old `#about` section HTML
# The section string to extract:
# <!-- CONTACT (Tree Image) -->
# <section id="about" style="position:relative;overflow:hidden;">
# ...
# </section>
# It ends right before <!-- PROJECTS -->

start_idx = content.find("<!-- CONTACT (Tree Image) -->")
end_idx = content.find("<!-- PROJECTS -->")

if start_idx != -1 and end_idx != -1:
    about_section = content[start_idx:end_idx]
    
    # We remove it from its current position
    content = content[:start_idx] + content[end_idx:]
    
    # Now we modify about_section to use the new img and positioning
    about_section = about_section.replace('<div class="about-scene-wrap"></div>', '<img class="about-scene-bg" src="Phineas_and_Ferb_under_tree.jpeg" alt="Phineas and Ferb under tree" />')
    about_section = about_section.replace('<div class="section-inner">', '<div class="section-inner" style="position:absolute; inset:0; display:flex; align-items:center; width:100%; max-width:1100px; padding:2rem; margin:0 auto; z-index:2;">')
    about_section = about_section.replace('<section id="about" style="position:relative;overflow:hidden;">', '<section id="about" style="padding:0; margin:0;">')

    # Insert it right before <footer>
    footer_idx = content.find("<footer>")
    if footer_idx != -1:
        content = content[:footer_idx] + about_section + "\n" + content[footer_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied.")
