# Contributing to imgdedup

Thanks for your interest in imgdedup! Here's how you can help.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/dedup-image.git
   cd dedup-image
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Making Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Test your changes:
   ```bash
   python imgdedup.py --help
   python imgdedup.py ./test_folder --dry-run
   ```
4. Commit with a clear message:
   ```bash
   git commit -m "Add feature: description"
   ```
5. Push and create a Pull Request

## Pull Request Process

- Describe what your PR does
- Link any related issues
- GitHub Actions will automatically test your code
- A maintainer will review and merge

## Code Style

- Keep it simple and readable
- Use descriptive variable names
- Add comments for complex logic
- Follow PEP 8 where reasonable

## Reporting Issues

Found a bug? Please create an issue with:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Your OS and Python version

## Building for Windows

To build your own Windows .exe:

```bash
pip install PyInstaller
build_exe.bat  # Windows
```

The executable will be in `releases/imgdedup.exe`

---

Happy coding! 🚀
