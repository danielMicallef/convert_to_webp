# JPG to WebP Converter

A Python command-line tool that batch converts PNG/JPG/JPEG images to WebP format with customizable quality settings.

## Why WebP?

WebP is a modern image format developed by Google that provides superior compression for web-based applications:

### 🚀 **Reduced File Sizes**
- **25-35% smaller** than JPEG files at equivalent quality levels
- **26% smaller** than PNG files for images with transparency
- Advanced compression algorithms reduce bandwidth usage significantly

### ⚡ **Faster Loading Times**
- Smaller file sizes mean faster download speeds
- Reduced server bandwidth consumption
- Better user experience, especially on mobile networks
- Improved Core Web Vitals scores for SEO

### 📱 **Modern Web Compatibility**
- Supported by all major browsers (Chrome, Firefox, Safari, Edge)
- Native support in modern web frameworks
- Perfect for responsive web design and progressive web apps

### 🎯 **Perfect for Web Applications**
- Ideal for e-commerce product images
- Great for blog post thumbnails and hero images
- Excellent for social media platforms
- Reduces hosting costs due to lower bandwidth usage

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Install Dependencies

#### Recommended: Using uv (fastest)
```bash
uv add typer pillow
```

#### Alternative: Using Poetry
```bash
poetry add typer pillow
```

#### Traditional: Using pip
```bash
pip install typer pillow
```

## Usage

### Basic Syntax
```bash
python jpg_to_webp.py [PATH] [OPTIONS]
```

### Parameters
- `PATH`: Directory containing JPG files to convert (required)
- `--quality, -q`: WebP quality level 1-100 (optional, default: 80)

### Examples

#### 1. Convert all JPG files in a directory (default quality)
```bash
python jpg_to_webp.py ./images
```

#### 2. Convert with high quality (90/100)
```bash
python jpg_to_webp.py ./photos --quality 90
```

#### 3. Convert with maximum compression (lower quality for smaller files)
```bash
python jpg_to_webp.py ./thumbnails -q 60
```

#### 4. Convert files in current directory
```bash
python jpg_to_webp.py .
```

#### 5. Convert files in a specific project folder
```bash
python jpg_to_webp.py /home/user/website/assets/images --quality 85
```

### Real-World Usage Examples

#### Web Development
```bash
# Convert product images for an e-commerce site
python jpg_to_webp.py ./src/assets/products -q 80

# Convert blog post images
python jpg_to_webp.py ./content/blog/images --quality 75
```

#### Batch Processing
```bash
# Process multiple directories
python jpg_to_webp.py ./images/gallery1 -q 85
python jpg_to_webp.py ./images/gallery2 -q 85
python jpg_to_webp.py ./images/thumbnails -q 70
```

## Output

The script provides detailed feedback during conversion:

```
Found 15 JPG file(s) in ./images
✓ Converted: photo1.jpg → photo1.webp
✓ Converted: image2.JPG → image2.webp
✓ Converted: picture3.jpeg → picture3.webp
...

Conversion complete!
Successfully converted: 15 files
```

## Features

- ✅ **Batch Processing**: Converts all JPG/JPEG files in a directory
- ✅ **File Replacement**: Automatically overwrites existing WebP files
- ✅ **Multiple Extensions**: Supports .jpg, .jpeg, .JPG, .JPEG
- ✅ **Quality Control**: Adjustable compression quality (1-100)
- ✅ **Error Handling**: Graceful error reporting for problematic files
- ✅ **Progress Tracking**: Real-time conversion feedback
- ✅ **Format Compatibility**: Handles RGBA images properly

## Quality Guidelines

Choose the right quality setting for your use case:

| Use Case | Recommended Quality | File Size | Visual Quality |
|----------|-------------------|-----------|----------------|
| Thumbnails | 60-70 | Smallest | Good for small images |
| Web Images | 75-85 | Balanced | Excellent for most websites |
| High-Quality Photos | 85-95 | Larger | Near-lossless quality |
| Archive/Print | 95-100 | Largest | Maximum quality |

## Supported File Types

**Input formats:**
- `.jpg`
- `.jpeg` 
- `.JPG`
- `.JPEG`
- `.png`
- `.PNG`

**Output format:**
- `.webp`

## Error Handling

The script handles common issues gracefully:
- Invalid image files are skipped with error messages
- Corrupted images are reported but don't stop the batch process
- Permission errors are clearly reported
- Missing directories are validated before processing

## Performance Benefits

### Before WebP Conversion
```
photo1.jpg - 2.5 MB
photo2.jpg - 1.8 MB
photo3.jpg - 3.2 MB
Total: 7.5 MB
```

### After WebP Conversion (Quality 80)
```
photo1.webp - 1.8 MB (-28%)
photo2.webp - 1.3 MB (-28%)
photo3.webp - 2.3 MB (-28%)
Total: 5.4 MB (28% reduction)
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.
