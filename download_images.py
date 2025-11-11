#!/usr/bin/env python3
import requests
import sys

images = {
    'hero-yoga-class.jpg': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1600&q=75&auto=format&fit=crop',
    'about-studio.jpg': 'https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&q=75&auto=format&fit=crop',
    'class-hatha.jpg': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&q=75&auto=format&fit=crop',
    'class-vinyasa.jpg': 'https://images.unsplash.com/photo-1588286840104-8957b019727f?w=600&q=75&auto=format&fit=crop',
    'class-ashtanga.jpg': 'https://images.unsplash.com/photo-1545389336-cf090694435e?w=600&q=75&auto=format&fit=crop',
    'class-restorative.jpg': 'https://images.unsplash.com/photo-1593810450967-f9c42742e326?w=600&q=75&auto=format&fit=crop',
    'class-pranayama.jpg': 'https://images.unsplash.com/photo-1602192509154-0b900ee1f851?w=600&q=75&auto=format&fit=crop',
    'class-meditation.jpg': 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=600&q=75&auto=format&fit=crop',
    'instructor-priya.jpg': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&q=75&auto=format&fit=crop',
    'instructor-ananya.jpg': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=75&auto=format&fit=crop',
    'instructor-rajesh.jpg': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=75&auto=format&fit=crop',
    'instructor-meera.jpg': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=75&auto=format&fit=crop',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print("Downloading images...")
for filename, url in images.items():
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(f'images/{filename}', 'wb') as f:
                f.write(response.content)
            print(f"✓ {filename} ({len(response.content)} bytes)")
        else:
            print(f"✗ {filename} - Status: {response.status_code}")
    except Exception as e:
        print(f"✗ {filename} - Error: {e}")

print("\nDone!")
