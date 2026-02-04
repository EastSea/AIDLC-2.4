import { createApiClient } from '../../services/apiClient';

describe('apiClient', () => {
  describe('createApiClient', () => {
    it('should create axios instance with base URL', () => {
      const client = createApiClient();
      
      expect(client).toBeDefined();
      expect(client.defaults.baseURL).toBe('http://localhost:8001');
    });

    it('should have request interceptor for auth token', () => {
      const client = createApiClient();
      
      expect(client.interceptors.request.handlers.length).toBeGreaterThan(0);
    });
  });
});
