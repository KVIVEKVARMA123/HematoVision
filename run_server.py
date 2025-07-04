#!/usr/bin/env python3
"""
HematoVision Server Launcher
Simple script to start the HematoVision web application
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required Python packages are installed"""
    required_packages = ['flask', 'pillow', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:")
        for package in missing_packages:
            print(f"  - {package}")
        print("\nInstall them using:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def main():
    print("=" * 60)
    print("🔬 HematoVision - Blood Cell Classification System")
    print("=" * 60)
    print()
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("✅ All dependencies found")
    print("🚀 Starting HematoVision server...")
    print()
    print("📱 Open your browser and navigate to:")
    print("   http://localhost:5000")
    print()
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        # Start Flask server
        from flask_server import app
        app.run(debug=False, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
