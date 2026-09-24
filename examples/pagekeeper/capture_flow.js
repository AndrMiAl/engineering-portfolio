// Sanitized portfolio example — not production source.

export async function capturePage({ directCapture, scrollingCapture, preferDirect = true }) {
  if (preferDirect) {
    try {
      return await directCapture();
    } catch (error) {
      console.warn("Direct capture unavailable, using fallback", error);
    }
  }

  return scrollingCapture();
}

export function buildExportPlan({ format, pages }) {
  return {
    format,
    pageCount: pages.length,
    searchableText: format === "pdf",
    editable: format === "docx",
  };
}
