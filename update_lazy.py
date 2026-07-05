import re

with open('index.html', 'r') as f:
    content = f.read()

# Don't lazy load the hero image or the agent P image that might be in the corner, 
# but definitely do it for Phineas, Doofenshmirtz, poems, project logos, etc.
imgs_to_lazy = [
    './Phineas.jpeg',
    'Grandmaster_ferb.png',
    'Couch-Critic.png',
    'Doofenshmirtz_Evil_Inc..jpeg',
    'Doofenshmirtz.jpeg',
    './poem1.jpg',
    './poem2.jpg',
    './poem3.jpg',
    './poem4.jpg',
    './rollercoaster.png'
]

for img in imgs_to_lazy:
    # Handle cases where it might already have loading="lazy" to avoid duplicates
    if f'src="{img}"' in content and f'loading="lazy" src="{img}"' not in content:
        content = content.replace(f'src="{img}"', f'loading="lazy" src="{img}"')

with open('index.html', 'w') as f:
    f.write(content)

print("Lazy loading added successfully.")
