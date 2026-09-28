"""Shared fixtures for the Wikipedia E2E suite."""
import pytest

from pages.article_page import ArticlePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage

# Registers the PM-friendly reporter (see reporting/pm_report.py)
pytest_plugins = ["reporting.pm_report"]

# Wikipedia's bot policy asks automated clients to identify themselves.
USER_AGENT = (
    "Mozilla/5.0 (compatible; PortfolioE2E/1.0; "
    "+https://github.com/himanshu888-art/wikipedia-e2e-suite)"
)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 900},
        "locale": "en-US",
        "user_agent": USER_AGENT,
    }


@pytest.fixture
def article(page) -> ArticlePage:
    return ArticlePage(page)


@pytest.fixture
def search(page) -> SearchPage:
    return SearchPage(page)


@pytest.fixture
def login(page) -> LoginPage:
    return LoginPage(page)
