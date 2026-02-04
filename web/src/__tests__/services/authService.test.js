import axios from 'axios';
import { loginTable, loginAdmin } from '../../services/authService';

jest.mock('axios');

describe('authService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('loginTable', () => {
    it('should login table successfully', async () => {
      const mockResponse = {
        data: { token: 'table-token', tableId: 't1', sessionId: 's1' }
      };
      axios.post.mockResolvedValue(mockResponse);

      const result = await loginTable('STORE01', 5, 'pass123');

      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:8001/auth/table/login',
        { storeCode: 'STORE01', tableNumber: 5, password: 'pass123' }
      );
      expect(result).toEqual(mockResponse.data);
    });

    it('should throw error on invalid credentials', async () => {
      axios.post.mockRejectedValue(new Error('Invalid credentials'));

      await expect(loginTable('STORE01', 5, 'wrong')).rejects.toThrow('Invalid credentials');
    });
  });

  describe('loginAdmin', () => {
    it('should login admin successfully', async () => {
      const mockResponse = {
        data: { token: 'admin-token', storeId: 'st1', userId: 'u1' }
      };
      axios.post.mockResolvedValue(mockResponse);

      const result = await loginAdmin('STORE01', 'admin', 'pass123');

      expect(axios.post).toHaveBeenCalledWith(
        'http://localhost:8001/auth/admin/login',
        { storeCode: 'STORE01', username: 'admin', password: 'pass123' }
      );
      expect(result).toEqual(mockResponse.data);
    });
  });
});
