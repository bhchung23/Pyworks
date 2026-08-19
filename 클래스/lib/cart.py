#
class Cart:
    def __init__(self):
        self.items=[] #장바구니가 비어있음

    #아이템 추가 매서드  
    def add_item(self, item):
        self.items.append(item)

    #아이템 검색 매서드
    def get_items(self):
        return f"장바구니:{self.items}"

    #아이템 제거 매서드
    def remove_item(self, item):
        if item in self.items: #없는거 삭제하면 오류나니까 왼쪽 if문 사용
            self.items.remove(item)
if __name__=="__main__":
    cart=Cart()
    cart.add_item("여름바지")
    cart.add_item("손수건")
    cart.add_item("양말")

#item 삭제
    cart.remove_item("양말") #있는거 삭제, 장바구니:['여름바지', '손수건']
    cart.remove_item("반팔티") #없는거 삭제하면 오류나니까 위 if문 사용

#아이템 조회
    print(cart.get_items())
