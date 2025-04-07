class Route:
    """Base class for all routes."""

    def generate_url(self):
        raise NotImplementedError(
            "You should implement this method in subclasses.")


class HomeRoute(Route):
    """Route for the homepage."""

    def generate_url(self):
        return "/home"


class AboutRoute(Route):
    """Route for the about page."""

    def generate_url(self):
        return "/about"


class ContactRoute(Route):
    """Route for the contact page."""

    def generate_url(self):
        return "/contact"


class ProductRoute(Route):
    """Route for the product page with an optional product ID."""

    def __init__(self, product_id=None):
        self.product_id = product_id

    def generate_url(self):
        if self.product_id:
            return f"/product/{self.product_id}"
        return "/product"


class RouteFactory:
    """Factory class to generate different routes."""

    @staticmethod
    def create_route(route_type, **kwargs):
        if route_type == 'home':
            return HomeRoute()
        if route_type == 'about':
            return AboutRoute()
        if route_type == 'contact':
            return ContactRoute()
        if route_type == 'product':
            product_id = kwargs.get('product_id', None)
            return ProductRoute(product_id)
        raise ValueError(f"Route type '{route_type}' is not recognized.")

# Client code


def main():
    # Simulate user input
    route_type = input(
        "Enter route type (home, about, contact, product): ").lower()

    if route_type == 'product':
        product_id = input("Enter product ID (optional): ")
        product_id = product_id if product_id else None
        route = RouteFactory.create_route(route_type, product_id=product_id)
    else:
        route = RouteFactory.create_route(route_type)

    print(f"Generated URL: {route.generate_url()}")


if __name__ == "__main__":
    main()
