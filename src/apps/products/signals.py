from django import dispatch


product_viewed = dispatch.Signal(providing_args=["user"])
