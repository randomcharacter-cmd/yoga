#!/bin/bash

# Krishna Yoga Image Setup Script
# Run this script locally to download and optimize all images

echo "==================================="
echo "Krishna Yoga - Image Setup"
echo "==================================="
echo ""

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "Error: Please run this script from the yoga website root directory"
    exit 1
fi

# Create images directory if it doesn't exist
mkdir -p images

echo "Downloading optimized images from Unsplash..."
echo ""

# Array of images to download
declare -A images
images["hero-yoga-class.jpg"]="https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1600&q=75&fm=jpg"
images["about-studio.jpg"]="https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&q=75&fm=jpg"
images["class-hatha.jpg"]="https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600&q=75&fm=jpg"
images["class-vinyasa.jpg"]="https://images.unsplash.com/photo-1588286840104-8957b019727f?w=600&q=75&fm=jpg"
images["class-ashtanga.jpg"]="https://images.unsplash.com/photo-1545389336-cf090694435e?w=600&q=75&fm=jpg"
images["class-restorative.jpg"]="https://images.unsplash.com/photo-1593810450967-f9c42742e326?w=600&q=75&fm=jpg"
images["class-pranayama.jpg"]="https://images.unsplash.com/photo-1602192509154-0b900ee1f851?w=600&q=75&fm=jpg"
images["class-meditation.jpg"]="https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=600&q=75&fm=jpg"
images["instructor-priya.jpg"]="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&q=75&fm=jpg"
images["instructor-ananya.jpg"]="https://images.unsplash.com/photo-1580489944761-15a19d654956?w=400&q=75&fm=jpg"
images["instructor-rajesh.jpg"]="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=75&fm=jpg"
images["instructor-meera.jpg"]="https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&q=75&fm=jpg"

# Download each image
count=0
total=${#images[@]}

for filename in "${!images[@]}"; do
    ((count++))
    url="${images[$filename]}"
    echo "[$count/$total] Downloading $filename..."

    curl -L -A "Mozilla/5.0" -o "images/$filename" "$url" 2>/dev/null

    if [ $? -eq 0 ] && [ -f "images/$filename" ] && [ $(stat -f%z "images/$filename" 2>/dev/null || stat -c%s "images/$filename" 2>/dev/null) -gt 1000 ]; then
        size=$(du -h "images/$filename" | cut -f1)
        echo "   ✓ Downloaded successfully ($size)"
    else
        echo "   ✗ Download failed"
        rm -f "images/$filename"
    fi
    echo ""
done

echo "==================================="
echo "Download complete!"
echo ""
echo "To use local images, update index.html:"
echo "  sed -i 's|https://images.unsplash.com/photo-1544367567-0f2fcb009e0b[^\"]*|images/hero-yoga-class.jpg|g' index.html"
echo ""
echo "Or run: bash use_local_images.sh"
echo "==================================="
