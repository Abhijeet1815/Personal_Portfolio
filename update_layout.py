import re

file_path = "/Users/abhijeetsharma/Desktop/Personal_Portfolio/portfolio (2).html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Margin Collapse (Top white space)
content = content.replace('<section id="hero" style="padding:0;margin:0;">', '<section id="hero" style="padding:0;margin:0;padding-top:64px;overflow:hidden;">')
content = content.replace('  margin-top:64px; /* navbar(64) */\n', '')

# 2. Thought Bubble CSS
old_ferb_banner_css = """.ferb-banner-overlay {
  position: absolute;
  bottom: 8%;
  left: 50%;
  transform: translateX(-50%);
  font-family: 'Fredoka One', cursive;
  font-size: clamp(1rem, 3vw, 2.5rem);
  color: #fff;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.8), -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
  text-align: center;
  width: 90%;
  letter-spacing: 0.05em;
  z-index: 10;
}"""
new_ferb_banner_css = """.ferb-banner-overlay {
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
content = content.replace(old_ferb_banner_css, new_ferb_banner_css)

# 3. CSS for Hero-Intro
old_hero_intro_css = """/* HERO INTRO — backyard bg with text */
#hero-intro{
  position:relative;
  overflow:hidden;
  min-height:60vh;
  display:flex;align-items:center;
}
.hero-intro-bg{
  position:absolute;inset:0;
  background-image:url('City.jpeg');
  background-size:cover;
  background-position:center;
}
.hero-intro-overlay{
  position:absolute;inset:0;
  background:linear-gradient(
    to right,
    rgba(255,249,240,0.97) 0%,
    rgba(255,249,240,0.92) 42%,
    rgba(255,249,240,0.55) 65%,
    rgba(255,249,240,0) 100%
  );
}
.hero-intro-content{
  position:relative;z-index:2;
  width:100%;max-width:1200px;
  margin:0 auto;
  padding:3.5rem 3rem;
}"""
new_hero_intro_css = """/* HERO INTRO */
#hero-intro{
  position:relative;
  overflow:hidden;
  display:flex;
  align-items:center;
}
.hero-intro-bg{
  width:100%;
  display:block;
  height:auto;
}
.hero-intro-content{
  position:absolute;z-index:2;
  inset:0;
  display:flex;align-items:center;
  width:100%;max-width:1100px;
  margin:0 auto;
  padding:2rem;
}"""
content = content.replace(old_hero_intro_css, new_hero_intro_css)

# 4. Hero-Intro HTML Replacement
old_hero_intro_html = """<!-- HERO: PART B - Backyard with intro text -->
<section id="hero-intro">
  <div class="hero-intro-bg"></div>
  <div class="hero-intro-overlay"></div>
  <div class="hero-intro-content">
    <div class="hero-left reveal">
      <div class="hero-top-label">B.Tech ECE · IIITA · Class of 2028</div>
      <div class="hero-tagline">"Another day, another invention."</div>
      <h1 class="hero-title">
        Hi, I'm<br>
        <span class="orange">Abhijeet</span>
      </h1>
      <p class="hero-sub">
        Building chess engines, ML systems, and everything in between —
        because every day in Danville is too short to sit still.
      </p>
      <div class="hero-btns">
        <a href="#projects" class="btn btn-primary">⚗️ See My Projects</a>
        <a href="#coding" class="btn btn-ghost">📈 Coding Profiles</a>
      </div>
    </div>
  </div>
</section>"""

# We extract about_text_html exactly as it was.
about_text_html = """      <div class="about-text reveal" style="max-width:600px;">
        <div class="s-label">📋 Origin Story</div>
        <h2 class="s-title">Hi I'm <em>Abhijeet</em><span class="dot">.</span></h2>
        <p>
          I'm <strong>Abhijeet Sharma</strong> — a B.Tech ECE student at <strong>IIITA</strong> with a 8.13 CGPA. Like any good day in Danville, I wake up with a plan and a whiteboard full of ideas — except mine tend to involve bitboards and cosine similarity instead of roller coasters.
        </p>
        <p>
          From C++ chess engines with alpha-beta pruning to ML recommendation pipelines — I build things that are fast, clever, and ship before lunch.
        </p>
        <p>
          I'm also a Senior Member of Sarasva (IIITA's Literary Society), where I've organized events like TEDx-IIITA and MUN-IIITA. Even Perry would be impressed.
        </p>

        <div class="about-tags">
          <span class="tag tag-o">C++ Systems</span>
          <span class="tag tag-t">Machine Learning</span>
          <span class="tag tag-o">Chess AI</span>
          <span class="tag tag-t">FastAPI</span>
          <span class="tag tag-g">Competitive Programming</span>
          <span class="tag tag-o">ECE @ IIITA</span>
        </div>

        <div class="stat-row">
          <div class="stat-box"><div class="stat-num">8.13</div><div class="stat-lbl">CGPA</div></div>
          <div class="stat-box"><div class="stat-num">400+</div><div class="stat-lbl">Problems Solved</div></div>
          <div class="stat-box"><div class="stat-num">Top 0.6%</div><div class="stat-lbl">JEE 2024</div></div>
          <div class="stat-box"><div class="stat-num">2★</div><div class="stat-lbl">CodeChef</div></div>
        </div>
      </div>"""

new_hero_intro_html = f"""<!-- HERO: PART B - Backyard with intro text -->
<section id="hero-intro" style="padding:0; margin:0;">
  <img class="hero-intro-bg" src="City.jpeg" alt="City Background" />
  <div class="hero-intro-content">
    <div class="hero-left reveal" style="width:100%;">
{about_text_html}
    </div>
  </div>
</section>"""
content = content.replace(old_hero_intro_html, new_hero_intro_html)


# 5. Tree Section -> Contact
old_about_html = """<!-- ABOUT -->
<section id="about">
  <div class="about-scene-wrap"></div>
  <div class="section-inner">
    <div class="about-grid">

      <div class="about-img-panel reveal" style="display: none;">
        <img src="P&F.jpeg" alt="The gang in class" />
      </div>

      <div class="about-text reveal">
        <div class="s-label">📋 Origin Story</div>
        <h2 class="s-title">Hi I'm <em>Abhijeet</em><span class="dot">.</span></h2>
        <p>
          I'm <strong>Abhijeet Sharma</strong> — a B.Tech ECE student at <strong>IIITA</strong> with a 8.13 CGPA. Like any good day in Danville, I wake up with a plan and a whiteboard full of ideas — except mine tend to involve bitboards and cosine similarity instead of roller coasters.
        </p>
        <p>
          From C++ chess engines with alpha-beta pruning to ML recommendation pipelines — I build things that are fast, clever, and ship before lunch.
        </p>
        <p>
          I'm also a Senior Member of Sarasva (IIITA's Literary Society), where I've organized events like TEDx-IIITA and MUN-IIITA. Even Perry would be impressed.
        </p>

        <div class="about-tags">
          <span class="tag tag-o">C++ Systems</span>
          <span class="tag tag-t">Machine Learning</span>
          <span class="tag tag-o">Chess AI</span>
          <span class="tag tag-t">FastAPI</span>
          <span class="tag tag-g">Competitive Programming</span>
          <span class="tag tag-o">ECE @ IIITA</span>
        </div>

        <div class="stat-row">
          <div class="stat-box"><div class="stat-num">8.13</div><div class="stat-lbl">CGPA</div></div>
          <div class="stat-box"><div class="stat-num">400+</div><div class="stat-lbl">Problems Solved</div></div>
          <div class="stat-box"><div class="stat-num">Top 0.6%</div><div class="stat-lbl">JEE 2024</div></div>
          <div class="stat-box"><div class="stat-num">2★</div><div class="stat-lbl">CodeChef</div></div>
        </div>
      </div>
    </div>
  </div>
</section>"""

new_about_contact_html = """<!-- CONTACT (Tree Image) -->
<section id="about" style="position:relative;overflow:hidden;">
  <div class="about-scene-wrap"></div>
  <div class="section-inner">
    <div class="about-grid" style="grid-template-columns:1fr;">
      <div class="about-text reveal" style="max-width:600px;">
        <div class="s-label">📡 Open Channel</div>
        <h2 class="s-title">Let's Build Something<span class="dot">.</span></h2>
        <p>Got a project idea, a collab, or just want to compare ratings? Every great invention starts with a conversation.</p>
        <div class="contact-links" style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:2rem;">
          <a href="mailto:iec2024022@iiita.ac.in" class="cl cl-email" style="display:inline-flex;align-items:center;gap:0.55rem;padding:0.8rem 1.6rem;border-radius:12px;font-weight:800;font-size:0.88rem;border:1.5px solid;background:var(--orange);color:#fff;border-color:var(--orange-light);transition:transform 0.2s,box-shadow 0.2s;">📧 Email Me</a>
          <a href="https://github.com/Abhijeet1815" target="_blank" class="cl cl-gh" style="display:inline-flex;align-items:center;gap:0.55rem;padding:0.8rem 1.6rem;border-radius:12px;font-weight:800;font-size:0.88rem;border:1.5px solid;background:#24292e;color:#fff;border-color:#444;transition:transform 0.2s,box-shadow 0.2s;">GitHub</a>
          <a href="https://linkedin.com/in/abhijeet-sharma-68a716321" target="_blank" class="cl cl-li" style="display:inline-flex;align-items:center;gap:0.55rem;padding:0.8rem 1.6rem;border-radius:12px;font-weight:800;font-size:0.88rem;border:1.5px solid;background:#0077b5;color:#fff;border-color:#005f8d;transition:transform 0.2s,box-shadow 0.2s;">LinkedIn</a>
        </div>
      </div>
    </div>
  </div>
</section>"""
content = content.replace(old_about_html, new_about_contact_html)

# 6. Remove Old Contact Section
old_contact_html = """<!-- CONTACT -->
<section id="contact">
  <div class="contact-overlay"></div>
  <div class="section-inner contact-inner">
    <div class="s-label reveal">📡 Open Channel</div>
    <h2 class="s-title reveal">Let's Build Something<span class="dot">.</span></h2>
    <p class="s-desc reveal">Got a project idea, a collab, or just want to compare ratings? Every great invention starts with a conversation.</p>
    <div class="contact-links reveal">
      <a href="mailto:iec2024022@iiita.ac.in" class="cl cl-email">📧 Email Me</a>
      <a href="https://github.com/Abhijeet1815" target="_blank" class="cl cl-gh">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
  GitHub
</a>
      <a href="https://linkedin.com/in/abhijeet-sharma-68a716321" target="_blank" class="cl cl-li">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
  LinkedIn
</a>
      <a href="https://codeforces.com/profile/abhijeet.sharma" target="_blank" class="cl cl-cf">⚡ Codeforces</a>
      <a href="https://leetcode.com/u/ferb01/" target="_blank" class="cl cl-lc">⚡ LeetCode</a>
    </div>
  </div>
</section>"""
content = content.replace(old_contact_html, '')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing.")
