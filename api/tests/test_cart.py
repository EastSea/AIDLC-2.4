import pytest

class TestCartGet:
    """장바구니 조회 테스트"""
    
    def test_get_empty_cart(self, client, test_data):
        """빈 장바구니 조회"""
        session_id = test_data["session"].id
        response = client.get(f"/api/customer/cart?session_id={session_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert data["session_id"] == session_id
        assert data["items"] == []
        assert data["total"] == 0

class TestCartAdd:
    """장바구니 추가 테스트"""
    
    def test_add_item_to_cart(self, client, test_data):
        """장바구니에 메뉴 추가"""
        session_id = test_data["session"].id
        payload = {
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 2
        }
        response = client.post("/api/customer/cart", json=payload)
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 1
        assert data["items"][0]["menu_id"] == "menu-1"
        assert data["items"][0]["quantity"] == 2
        assert data["items"][0]["unit_price"] == 10000
        assert data["items"][0]["subtotal"] == 20000
        assert data["total"] == 20000
    
    def test_add_multiple_items(self, client, test_data):
        """여러 메뉴 추가"""
        session_id = test_data["session"].id
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1
        })
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-2",
            "quantity": 2
        })
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 2
        assert data["total"] == 50000  # 10000 + 40000
    
    def test_add_duplicate_item_increases_quantity(self, client, test_data):
        """동일 메뉴 재추가 시 수량 증가"""
        session_id = test_data["session"].id
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 2
        })
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1
        })
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 1
        assert data["items"][0]["quantity"] == 3
        assert data["total"] == 30000
    
    def test_add_item_with_options(self, client, test_data):
        """옵션이 있는 메뉴 추가"""
        session_id = test_data["session"].id
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1,
            "options": "매운맛"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert data["items"][0]["options"] == "매운맛"
    
    def test_add_same_menu_different_options(self, client, test_data):
        """동일 메뉴 + 다른 옵션은 별도 항목"""
        session_id = test_data["session"].id
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1,
            "options": "매운맛"
        })
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1,
            "options": "순한맛"
        })
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 2
    
    def test_add_invalid_menu(self, client, test_data):
        """존재하지 않는 메뉴 추가"""
        session_id = test_data["session"].id
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "invalid-menu",
            "quantity": 1
        })
        
        assert response.status_code == 404
        assert "Menu not found" in response.json()["detail"]

class TestCartUpdate:
    """장바구니 수량 변경 테스트"""
    
    def test_update_item_quantity(self, client, test_data):
        """수량 변경"""
        session_id = test_data["session"].id
        
        add_response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 2
        })
        item_id = add_response.json()["items"][0]["id"]
        
        response = client.patch(f"/api/customer/cart/{item_id}", json={"quantity": 5})
        
        assert response.status_code == 200
        data = response.json()
        assert data["items"][0]["quantity"] == 5
        assert data["total"] == 50000
    
    def test_update_invalid_item(self, client, test_data):
        """존재하지 않는 항목 수정"""
        response = client.patch("/api/customer/cart/invalid-id", json={"quantity": 5})
        
        assert response.status_code == 404
        assert "Cart item not found" in response.json()["detail"]

class TestCartDelete:
    """장바구니 삭제 테스트"""
    
    def test_delete_item(self, client, test_data):
        """항목 삭제"""
        session_id = test_data["session"].id
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1
        })
        
        add_response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-2",
            "quantity": 1
        })
        item_id = add_response.json()["items"][1]["id"]
        
        response = client.delete(f"/api/customer/cart/{item_id}")
        
        assert response.status_code == 200
        data = response.json()
        assert len(data["items"]) == 1
        assert data["items"][0]["menu_id"] == "menu-1"
    
    def test_delete_invalid_item(self, client, test_data):
        """존재하지 않는 항목 삭제"""
        response = client.delete("/api/customer/cart/invalid-id")
        
        assert response.status_code == 404
        assert "Cart item not found" in response.json()["detail"]
    
    def test_clear_cart(self, client, test_data):
        """장바구니 비우기"""
        session_id = test_data["session"].id
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 1
        })
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-2",
            "quantity": 1
        })
        
        response = client.delete(f"/api/customer/cart?session_id={session_id}")
        
        assert response.status_code == 200
        assert response.json()["success"] is True
        
        # 비운 후 조회
        get_response = client.get(f"/api/customer/cart?session_id={session_id}")
        assert get_response.json()["items"] == []
        assert get_response.json()["total"] == 0

class TestCartCalculation:
    """장바구니 계산 테스트"""
    
    def test_total_calculation(self, client, test_data):
        """총액 계산 검증"""
        session_id = test_data["session"].id
        
        client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 3
        })
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-2",
            "quantity": 2
        })
        
        data = response.json()
        expected_total = (10000 * 3) + (20000 * 2)
        assert data["total"] == expected_total
    
    def test_subtotal_calculation(self, client, test_data):
        """항목별 소계 계산 검증"""
        session_id = test_data["session"].id
        
        response = client.post("/api/customer/cart", json={
            "session_id": session_id,
            "menu_id": "menu-1",
            "quantity": 4
        })
        
        data = response.json()
        assert data["items"][0]["subtotal"] == 40000
