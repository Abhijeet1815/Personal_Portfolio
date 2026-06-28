import re

file_path = "/Users/abhijeetsharma/Desktop/Personal_Portfolio/portfolio (2).html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix .ferb-banner-overlay
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
content = content.replace(old_ferb, new_ferb)

# 2. Fix hero image stretch
old_hero_img = """.hero-lab-img img{
  width:100%;
  display:block;
  height:auto;
}"""
new_hero_img = """.hero-lab-img{
  text-align: center;
}
.hero-lab-img img{
  max-width:100%;
  display:inline-block;
  height:auto;
}"""
content = content.replace(old_hero_img, new_hero_img)

# 3. Fix hero intro bg stretch
old_hero_intro = """.hero-intro-bg{
  width:100%;
  display:block;
  height:auto;
}"""
new_hero_intro = """.hero-intro-bg{
  max-width:100%;
  display:inline-block;
  height:auto;
}
#hero-intro {
  text-align: center;
}"""
content = content.replace(old_hero_intro, new_hero_intro)

# 4. Fix about scene bg stretch
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
content = content.replace(old_about, new_about)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied.")
