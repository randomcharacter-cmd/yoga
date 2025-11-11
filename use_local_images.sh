#!/bin/bash

# Script to update index.html to use local images

echo "Updating index.html to use local images..."

# Backup the original file
cp index.html index.html.backup

# Replace all image URLs with local paths
sed -i \
    -e 's|https://images.unsplash.com/photo-1544367567-0f2fcb009e0b[^"]*|images/hero-yoga-class.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1599901860904-17e6ed7083a0[^"]*|images/about-studio.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1506126613408-eca07ce68773[^"]*|images/class-hatha.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1588286840104-8957b019727f[^"]*|images/class-vinyasa.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1545389336-cf090694435e[^"]*|images/class-ashtanga.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1593810450967-f9c42742e326[^"]*|images/class-restorative.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1602192509154-0b900ee1f851[^"]*|images/class-pranayama.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1571902943202-507ec2618e8f[^"]*|images/class-meditation.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1573496359142-b8d87734a5a2[^"]*|images/instructor-priya.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1580489944761-15a19d654956[^"]*|images/instructor-ananya.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d[^"]*|images/instructor-rajesh.jpg|g' \
    -e 's|https://images.unsplash.com/photo-1494790108377-be9c29b29330[^"]*|images/instructor-meera.jpg|g' \
    index.html

echo "✓ Updated index.html to use local images"
echo "✓ Backup saved as index.html.backup"
echo ""
echo "To revert: mv index.html.backup index.html"
