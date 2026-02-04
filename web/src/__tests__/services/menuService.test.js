import axios from 'axios';
import { getCategories, getMenus, getMenuDetail } from '../../services/menuService';

jest.mock('axios');

describe('menuService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('getCategories', () => {
    it('should fetch all categories', async () => {
      const mockCategories = [
        { id: 'c1', name: '메인요리' },
        { id: 'c2', name: '사이드' }
      ];
      axios.get.mockResolvedValue({ data: mockCategories });

      const result = await getCategories();

      expect(axios.get).toHaveBeenCalledWith('http://localhost:8001/menus/categories');
      expect(result).toEqual(mockCategories);
    });
  });

  describe('getMenus', () => {
    it('should fetch all menus without filters', async () => {
      const mockMenus = [{ id: 'm1', name: '김치찌개' }];
      axios.get.mockResolvedValue({ data: mockMenus });

      const result = await getMenus();

      expect(axios.get).toHaveBeenCalledWith('http://localhost:8001/menus', { params: {} });
      expect(result).toEqual(mockMenus);
    });

    it('should fetch menus with category filter', async () => {
      const mockMenus = [{ id: 'm1', name: '김치찌개', categoryId: 'c1' }];
      axios.get.mockResolvedValue({ data: mockMenus });

      const result = await getMenus('c1');

      expect(axios.get).toHaveBeenCalledWith('http://localhost:8001/menus', {
        params: { categoryId: 'c1' }
      });
      expect(result).toEqual(mockMenus);
    });

    it('should fetch menus with serving size filter', async () => {
      const mockMenus = [{ id: 'm1', name: '김치찌개', servingSize: '2인분' }];
      axios.get.mockResolvedValue({ data: mockMenus });

      const result = await getMenus(null, '2인분');

      expect(axios.get).toHaveBeenCalledWith('http://localhost:8001/menus', {
        params: { servingSize: '2인분' }
      });
      expect(result).toEqual(mockMenus);
    });
  });

  describe('getMenuDetail', () => {
    it('should fetch menu details', async () => {
      const mockMenu = { id: 'm1', name: '김치찌개', description: '맛있는 김치찌개' };
      axios.get.mockResolvedValue({ data: mockMenu });

      const result = await getMenuDetail('m1');

      expect(axios.get).toHaveBeenCalledWith('http://localhost:8001/menus/m1');
      expect(result).toEqual(mockMenu);
    });
  });
});
