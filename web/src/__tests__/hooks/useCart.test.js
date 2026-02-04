import { renderHook, act } from '@testing-library/react';
import { useCart } from '../../hooks/useCart';

describe('useCart', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('should add item to cart', () => {
    const { result } = renderHook(() => useCart());
    
    act(() => {
      result.current.addItem({ id: 'm1', name: '김치찌개', price: 8000 });
    });

    expect(result.current.items).toHaveLength(1);
    expect(result.current.items[0].quantity).toBe(1);
  });

  it('should increment quantity for duplicate item', () => {
    const { result } = renderHook(() => useCart());
    const menu = { id: 'm1', name: '김치찌개', price: 8000 };
    
    act(() => {
      result.current.addItem(menu);
      result.current.addItem(menu);
    });

    expect(result.current.items).toHaveLength(1);
    expect(result.current.items[0].quantity).toBe(2);
  });

  it('should calculate total amount', () => {
    const { result } = renderHook(() => useCart());
    
    act(() => {
      result.current.addItem({ id: 'm1', name: '김치찌개', price: 8000 });
      result.current.addItem({ id: 'm2', name: '된장찌개', price: 7000 });
    });

    expect(result.current.totalAmount).toBe(15000);
  });

  it('should persist cart to localStorage', () => {
    const { result } = renderHook(() => useCart());
    const setItemSpy = jest.spyOn(Storage.prototype, 'setItem');
    
    act(() => {
      result.current.addItem({ id: 'm1', name: '김치찌개', price: 8000 });
    });

    expect(setItemSpy).toHaveBeenCalled();
    setItemSpy.mockRestore();
  });
});
