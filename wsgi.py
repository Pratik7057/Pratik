# -*- coding: utf-8 -*-
"""
Radha API - wsgi file for Gunicorn deployment
This file is needed for Render.com deployment
"""

from main import app

# Gunicorn entry point
if __name__ == "__main__":
    # This block will not be executed by Gunicorn
    pass
