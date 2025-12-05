#!/bin/bash

echo "🧹 Limpiando residuos de compilación LaTeX en subdirectorios..."

# 1. Encuentra carpetas que contengan archivos .tex
dirs=$(find . -name '*.tex' -exec dirname {} \; | sort -u)

# 2. Ejecuta latexmk -c en cada carpeta
for dir in $dirs; do
  echo "→ Limpiando en: $dir"
  (cd "$dir" && latexmk -c > /dev/null 2>&1)
done

# 3. Borra residuos adicionales manualmente
echo "🗑️  Eliminando archivos: aux, log, out, toc, bbl, blg, fls, fdb_latexmk..."

find . -type f \( \
  -name '*.aux' -o \
  -name '*.log' -o \
  -name '*.out' -o \
  -name '*.toc' -o \
  -name '*.nav' -o \
  -name '*.snm' -o \
  -name '*.vrb' -o \
  -name '*.bbl' -o \
  -name '*.blg' -o \
  -name '*.fls' -o \
  -name '*.fdb_latexmk' -o \
  -name '*.synctex.gz' \
\) -delete

echo "✅ Limpieza completada."

