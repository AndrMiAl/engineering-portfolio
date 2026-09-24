// Sanitized portfolio example — simplified pagination logic.

export function paginate(totalHeight, pageHeight) {
  if (totalHeight <= 0 || pageHeight <= 0) return [];

  const pages = [];
  for (let top = 0; top < totalHeight; top += pageHeight) {
    pages.push({
      top,
      bottom: Math.min(top + pageHeight, totalHeight),
    });
  }
  return pages;
}
