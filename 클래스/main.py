
#Cart 클래스 사용하고 싶다.
#from 모듈이름 import 클래스이름
from lib.cart import Cart

cart=Cart()
cart.add_item("딸기")
cart.add_item("카레")

print(cart.get_items())