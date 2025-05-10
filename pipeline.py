from core.analyze import analyze_sources
from core.enrich import enrich_articles
from core.preprocess import preprocess_articles
from core.report import generate_report
from core.sources import collect_sources

async def run_full_pipeline():
    sources = await collect_sources()
    preprocessed = preprocess_articles(sources)
    enriched = enrich_articles(preprocessed)
    report = generate_report(enriched)
    print(report)
