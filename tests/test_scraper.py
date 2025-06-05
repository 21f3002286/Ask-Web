from scraper import text_scraper

def test_text_scraper_returns_tuple():
    url = "https://www.healthline.com/nutrition/10-health-benefits-of-apples"
    result = text_scraper(url)
    assert result is not None, "Should return a result"
    assert isinstance(result, tuple), "Should return a tuple"
    assert len(result) == 3, "Should return (title, url, content)"