from apps.core.redis import redis_client


def get_product_views_count(product_slug: str) -> int:
    client = redis_client()
    if client.exists(product_slug):
        return int(client.get(product_slug))
    return 0


def set_product_view_count(product_slug: str, count_value: int) -> None:
    client = redis_client()
    client.set(product_slug, count_value)


def increment_product_view_counter(product_slug: str) -> int:
    client = redis_client()
    if client.exists(product_slug):
        client.incr(product_slug)
    else:
        client.set(product_slug, 1)
    return int(client.get(product_slug))
