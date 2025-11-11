#!/usr/bin/env python3
"""
Krishna Yoga - Local Image Setup Script
Downloads all images from Unsplash and updates HTML to use local paths
"""

import os
import sys
import requests
import shutil
from pathlib import Path

# Image mapping: local filename -> Unsplash URL
IMAGES = {
    'hero-yoga-class.jpg': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1600&q=75&fm=jpg&fit=crop',
    'about-studio.jpg': 'https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&q=75&fm=jpg&fit=crop',
    'class-hatha.jpg': 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&q=75&fm=jpg&fit=crop',
    'class-vinyasa.jpg': 'https://images.unsplash.com/photo-1588286840104-8957b019727f?w=600&q=75&fm=jpg&fit=crop',
    'class-ashtanga.jpg': 'https://images.unsplash.com/photo-1545389336-cf090694435e?w=600&q=75&fm=jpg&fit=crop',
    'class-restorative.jpg': 'https://images.unsplash.com/photo-1593810450967-f9c42742e326?w=600&q=75&fm=jpg&fit=crop',
    'class-pranayama.jpg': 'https://images.unsplash.com/photo-1602192509154-0b900ee1f851?w=600&q=75&fm=jpg&fit=crop',
    'class-meditation.jpg': 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=600&q=75&fm=jpg&fit=crop',
    'instructor-priya.jpg': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&q=75&fm=jpg&fit=crop',
    'instructor-ananya.jpg': 'https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=75&fm=jpg&fit=crop',
    'instructor-rajesh.jpg': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=75&fm=jpg&fit=crop',
    'instructor-meera.jpg': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=75&fm=jpg&fit=crop',
}

# URL replacements for HTML
URL_REPLACEMENTS = {
    'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1600&q=75&fm=jpg&fit=crop': 'images/hero-yoga-class.jpg',
    'https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&q=75&fm=jpg&fit=crop': 'images/about-studio.jpg',
    'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&q=75&fm=jpg&fit=crop': 'images/class-hatha.jpg',
    'https://images.unsplash.com/photo-1588286840104-8957b019727f?w=600&q=75&fm=jpg&fit=crop': 'images/class-vinyasa.jpg',
    'https://images.unsplash.com/photo-1545389336-cf090694435e?w=600&q=75&fm=jpg&fit=crop': 'images/class-ashtanga.jpg',
    'https://images.unsplash.com/photo-1593810450967-f9c42742e326?w=600&q=75&fm=jpg&fit=crop': 'images/class-restorative.jpg',
    'https://images.unsplash.com/photo-1602192509154-0b900ee1f851?w=600&q=75&fm=jpg&fit=crop': 'images/class-pranayama.jpg',
    'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=600&q=75&fm=jpg&fit=crop': 'images/class-meditation.jpg',
    'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&q=75&fm=jpg&fit=crop': 'images/instructor-priya.jpg',
    'https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=75&fm=jpg&fit=crop': 'images/instructor-ananya.jpg',
    'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=75&fm=jpg&fit=crop': 'images/instructor-rajesh.jpg',
    'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=75&fm=jpg&fit=crop': 'images/instructor-meera.jpg',
}

MIN_FILE_SIZE = 10000  # 10KB minimum to verify actual image downloaded

def download_images():
    """Download all images from Unsplash"""
    print("=" * 60)
    print("Krishna Yoga - Downloading Images")
    print("=" * 60)
    print()

    # Create images directory
    images_dir = Path('images')
    images_dir.mkdir(exist_ok=True)
    print(f"✓ Images directory: {images_dir.absolute()}")
    print()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    downloaded = []
    failed = []

    total = len(IMAGES)
    for i, (filename, url) in enumerate(IMAGES.items(), 1):
        filepath = images_dir / filename
        print(f"[{i}/{total}] Downloading {filename}...")

        try:
            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code == 200:
                # Save the file
                with open(filepath, 'wb') as f:
                    f.write(response.content)

                # Verify file size
                file_size = filepath.stat().st_size

                if file_size < MIN_FILE_SIZE:
                    print(f"    ✗ FAILED - File too small ({file_size} bytes)")
                    print(f"    This usually means the download was blocked (403 error)")
                    failed.append(filename)
                    filepath.unlink()  # Delete the bad file
                else:
                    size_kb = file_size / 1024
                    print(f"    ✓ SUCCESS - {size_kb:.1f} KB")
                    downloaded.append(filename)
            else:
                print(f"    ✗ FAILED - HTTP {response.status_code}")
                failed.append(filename)

        except Exception as e:
            print(f"    ✗ FAILED - {e}")
            failed.append(filename)

        print()

    # Summary
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"✓ Successfully downloaded: {len(downloaded)}/{total}")
    print(f"✗ Failed: {len(failed)}/{total}")

    if failed:
        print("\nFailed images:")
        for filename in failed:
            print(f"  - {filename}")

    print()

    return len(failed) == 0

def update_html():
    """Update index.html to use local image paths"""
    html_file = Path('index.html')

    if not html_file.exists():
        print("✗ ERROR: index.html not found")
        return False

    print("=" * 60)
    print("Updating HTML")
    print("=" * 60)
    print()

    # Create backup
    backup_file = Path('index.html.backup')
    shutil.copy(html_file, backup_file)
    print(f"✓ Backup created: {backup_file}")

    # Read HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Replace URLs
    replacements_made = 0
    for old_url, new_path in URL_REPLACEMENTS.items():
        count = html_content.count(old_url)
        if count > 0:
            html_content = html_content.replace(old_url, new_path)
            replacements_made += count
            print(f"✓ Replaced {count}x: {old_url[:50]}...")

    # Write updated HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print()
    print(f"✓ Total replacements: {replacements_made}")
    print(f"✓ Updated: {html_file}")
    print()

    return True

def verify_setup():
    """Verify all images exist and HTML is updated"""
    print("=" * 60)
    print("Verification")
    print("=" * 60)
    print()

    images_dir = Path('images')
    all_good = True

    # Check all image files exist
    print("Checking image files:")
    for filename in IMAGES.keys():
        filepath = images_dir / filename
        if filepath.exists():
            size_kb = filepath.stat().st_size / 1024
            print(f"  ✓ {filename} ({size_kb:.1f} KB)")
        else:
            print(f"  ✗ {filename} MISSING")
            all_good = False

    print()

    # Check HTML uses local paths
    html_file = Path('index.html')
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    print("Checking HTML references:")
    cdn_count = html_content.count('https://images.unsplash.com/')
    local_count = html_content.count('images/')

    print(f"  CDN URLs remaining: {cdn_count}")
    print(f"  Local paths: {local_count}")

    if cdn_count > 0:
        print("  ⚠ WARNING: Some CDN URLs still present")
    else:
        print("  ✓ All images use local paths")

    print()

    return all_good and cdn_count == 0

def main():
    """Main execution"""
    print()

    # Step 1: Download images
    if not download_images():
        print("=" * 60)
        print("ERROR: Some images failed to download")
        print("=" * 60)
        print()
        print("This is likely due to network restrictions (403 Forbidden).")
        print("The website will continue using CDN images.")
        print()
        print("To use local images, run this script from a computer")
        print("with unrestricted internet access.")
        print()
        sys.exit(1)

    # Step 2: Update HTML
    if not update_html():
        print("✗ ERROR: Failed to update HTML")
        sys.exit(1)

    # Step 3: Verify
    if not verify_setup():
        print("✗ ERROR: Verification failed")
        print("Restoring from backup...")
        shutil.copy('index.html.backup', 'index.html')
        print("✓ Restored index.html from backup")
        sys.exit(1)

    # Success!
    print("=" * 60)
    print("SUCCESS! ✓")
    print("=" * 60)
    print()
    print("All images downloaded and HTML updated successfully!")
    print("The website now uses local images.")
    print()
    print("Next steps:")
    print("1. Open index.html in your browser to verify")
    print("2. Delete index.html.backup if everything looks good")
    print("3. Commit and push the changes to git")
    print()

if __name__ == '__main__':
    main()
