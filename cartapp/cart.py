from django.contrib.sessions.models import Session


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart-session")
        if "cart-session" not in self.session:
            cart = self.session["cart-session"] = {}
        else:
            self.cart = cart
