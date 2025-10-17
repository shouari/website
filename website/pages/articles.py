

# import reflex as rx
# from website.content.dummy_articles import dummy_articles

# # on crée un dictionnaire indexé par slug
# articles = {a["slug"]: a for a in dummy_articles}

# @rx.page(route="/article")
# def article_detail() -> rx.Component:
#     slug = rx.router.get_query_param("slug")
#     article = articles.get(slug, None)

#     if article is None:
#         return rx.center(
#             rx.text("Article introuvable.", size="5", weight="bold"),
#             padding="5rem"
#         )

#     return rx.box(
#         rx.heading(article["title"], size="8", margin_bottom="1rem"),
#         rx.text(article["date"], size="2", color="gray", margin_bottom="2rem"),
#         rx.markdown(article["content"], font_size="1.05rem", max_width="800px"),
#         padding="2rem",
#         align="center",
#     )
