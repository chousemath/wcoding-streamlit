#!/bin/bash

echo "# wcoding-streamlit" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:chousemath/wcoding-streamlit.git
git push -u origin main
