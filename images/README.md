# Krishna Yoga Website Images

## Image Optimization Guide

Due to network restrictions in the build environment, images cannot be automatically downloaded from Unsplash. However, the website is already optimized to use CDN-hosted images with aggressive caching and compression.

### Current Optimization

All images use these optimizations:
- **Quality**: 75-80 (optimal balance between size and quality)
- **Format**: WebP auto-conversion via Unsplash CDN
- **Lazy Loading**: Built into HTML
- **Responsive Sizing**: Appropriate dimensions for each use case

### To Download Images Locally

Run the provided `download_images.py` script from a local environment (not in a restricted network):

```bash
python3 download_images.py
```

This will download all 12 optimized images to the `images/` directory.

### Image Inventory

| Filename | Purpose | Dimensions | Source |
|----------|---------|------------|--------|
| hero-yoga-class.jpg | Hero section background | 1600x1067 | Unsplash |
| about-studio.jpg | About section | 800x533 | Unsplash |
| class-hatha.jpg | Hatha Yoga class card | 600x400 | Unsplash |
| class-vinyasa.jpg | Vinyasa Flow class card | 600x400 | Unsplash |
| class-ashtanga.jpg | Ashtanga Yoga class card | 600x400 | Unsplash |
| class-restorative.jpg | Restorative Yoga class card | 600x400 | Unsplash |
| class-pranayama.jpg | Pranayama class card | 600x400 | Unsplash |
| class-meditation.jpg | Meditation class card | 600x400 | Unsplash |
| instructor-priya.jpg | Priya Sharma profile | 400x400 | Unsplash |
| instructor-ananya.jpg | Ananya Desai profile | 400x400 | Unsplash |
| instructor-rajesh.jpg | Rajesh Kumar profile | 400x400 | Unsplash |
| instructor-meera.jpg | Meera Patel profile | 400x400 | Unsplash |

### Performance Benefits

**Current CDN Setup:**
- Global CDN distribution
- Automatic WebP conversion
- Browser caching
- ~30-50KB per image (optimized)

**Total Page Weight:** ~500KB (all images combined)

### Alternative: Local Hosting

After downloading images locally, update `index.html` to reference local paths:

```html
<!-- Change from: -->
<img src="https://images.unsplash.com/..." />

<!-- To: -->
<img src="images/hero-yoga-class.jpg" />
```

### Further Optimization Options

If hosting locally, consider:
1. Convert to WebP format for 25-35% smaller file sizes
2. Use `<picture>` elements for responsive images
3. Implement progressive JPEGs
4. Use image sprites for smaller assets
