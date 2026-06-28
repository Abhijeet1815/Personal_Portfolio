import re

file_path = "/Users/abhijeetsharma/Desktop/Personal_Portfolio/portfolio.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace base64 strings with filenames
# Image 1: Hero Lab (Phineas.jpeg) - usually around line 118
# It's an <img> tag.
content = re.sub(r'<img src="data:image/[^"]+base64,[^"]+" alt="Hello — Phineas and Ferb in the lab" />', '<img src="Phineas.jpeg" alt="Hello — Phineas and Ferb in the lab" />', content)

# Image 2: Hero Intro BG (City.jpeg) - in CSS .hero-intro-bg
content = re.sub(r'background-image:url\(\'data:image/[^\']+\'\);', "background-image:url('City.jpeg');", content, count=1)

# Image 3: About Scene Wrap (Phineas_and_Ferb_under_tree.jpeg) - in CSS .about-scene-wrap
content = re.sub(r'background-image:url\(\'data:image/[^\']+\'\);', "background-image:url('Phineas_and_Ferb_under_tree.jpeg');", content, count=1)

# Image 4: About Image Panel (P&F.jpeg) - in HTML
content = re.sub(r'<img src="data:image/[^"]+" alt="The gang in class" />', '<img src="P&F.jpeg" alt="The gang in class" />', content)

# Image 5: Contact Section (Doofenshmirtz_Evil_Inc..jpeg) - in CSS #contact
content = re.sub(r'background-image:url\(\'data:image/[^\']+\'\);', "background-image:url('Doofenshmirtz_Evil_Inc..jpeg');", content, count=1)

# Image 6: Perry Easter Egg (AgentP.png) - at the bottom
content = re.sub(r'<img class="perry-corner" src="data:image/[^"]+"', '<img class="perry-corner" src="AgentP.png"', content)


# Now inject the Doofenshmirtz panel beside the coding profile
# The user wants it beside the coding profile, like in portfolio (2).html
# We find the <div class="coding-grid"> and wrap it in a flex container

coding_grid_match = re.search(r'<div class="coding-grid">([\s\S]*?)</div>\n  </div>\n</section>', content)
if coding_grid_match:
    old_coding_section = """    <div class="coding-grid">"""
    
    new_coding_section = """    <div style="display:flex;gap:2.5rem;align-items:flex-start;">
      <div class="coding-grid" style="flex:1;">"""
    
    content = content.replace(old_coding_section, new_coding_section)
    
    # We need to close the flex container and add the doof panel after the coding grid finishes
    # In the original, the closing tags were:
    #       </div>
    #     </div>
    #   </div>
    # </section>
    # Actually, the grid closes at `</div>` before `</div>` (section-inner).
    old_end = """      </div>
    </div>
  </div>
</section>"""
    new_end = """      </div>
      </div><!-- /coding-grid -->
      <div class="doof-panel reveal" style="flex-shrink:0;width:260px;position:sticky;top:90px;align-self:flex-start;">
        <img src="Doofenshmirtz.jpeg" alt="Doofenshmirtz with his latest inator" style="width:100%;filter:drop-shadow(0 8px 24px rgba(0,0,0,0.2));border-radius:16px;" />
        <div style="margin-top:0.8rem;background:rgba(123,45,139,0.08);border:1.5px solid rgba(123,45,139,0.2);border-radius:12px;padding:0.8rem 1rem;font-size:0.82rem;color:#5a4070;font-weight:700;text-align:center;font-family:'Fredoka One',cursive;">
          "I too have ratings, Perry the Platypus!"
        </div>
      </div>
    </div><!-- /flex wrapper -->
  </div>
</section>"""
    content = content.replace(old_end, new_end)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done updating portfolio.html")
