import arxiv

def fetch_arxiv_articles(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    return [{"title": result.title, "summary": result.summary, "url": result.entry_id} for result in search.results()]
