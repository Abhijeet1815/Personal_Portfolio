import re

file_path = "/Users/abhijeetsharma/Desktop/Personal_Portfolio/portfolio (2).html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Reverse 1: .ferb-banner-overlay
new_ferb = """.ferb-banner-overlay {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
  background: var(--orange);
  color: #fff;
  padding: 1rem 2rem;
  border-radius: 20px;
  font-family: 'Fredoka One', cursive;
  font-size: clamp(1rem, 2.5vw, 1.8rem);
  text-align: center;
  white-space: nowrap;
  box-shadow: 0 10px 25px rgba(255, 107, 53, 0.4);
  z-index: 10;
}"""
old_ferb = """.ferb-banner-overlay {
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
content = content.replace(new_ferb, old_ferb)

# Reverse 2: hero image stretch
new_hero_img = """.hero-lab-img{
  text-align: center;
}
.hero-lab-img img{
  max-width:100%;
  display:inline-block;
  height:auto;
}"""
old_hero_img = """.hero-lab-img img{
  width:100%;
  display:block;
  height:auto;
}"""
# Note: In the original file, before fix_css, .hero-lab-img { width:100%; line-height:0; position:relative; } was there.
# fix_css.py replaced `.hero-lab-img img{...}` but also added `.hero-lab-img{ text-align: center; }`.
# Let's just use string replacement.
content = content.replace(new_hero_img, old_hero_img)

# Reverse 3: hero intro bg stretch
new_hero_intro = """.hero-intro-bg{
  max-width:100%;
  display:inline-block;
  height:auto;
}
#hero-intro {
  text-align: center;
}"""
old_hero_intro = """.hero-intro-bg{
  width:100%;
  display:block;
  height:auto;
}"""
content = content.replace(new_hero_intro, old_hero_intro)

# Reverse 4: about scene bg stretch
new_about = """.about-scene-bg{
  max-width:100%;
  display:inline-block;
  height:auto;
}
#about{
  position:relative;
  overflow:hidden;
  display:flex;
  align-items:center;
  justify-content:center;
  text-align: center;
}"""
old_about = """.about-scene-bg{
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
content = content.replace(new_about, old_about)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted CSS fixes.")
