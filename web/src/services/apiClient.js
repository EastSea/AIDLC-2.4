import axios from 'axios';

/**
 * Create configured axios instance
 * @returns {AxiosInstance} Axios instance with base URL and interceptors
 */
export const createApiClient = () => {
  const client = axios.create({
    baseURL: 'http://localhost:8001',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  // Request interceptor for auth token
  client.interceptors.request.use(
    (config) => {
      const tableAuth = localStorage.getItem('tableAuth');
      const adminAuth = localStorage.getItem('adminAuth');
      
      if (tableAuth) {
        const { token } = JSON.parse(tableAuth);
        config.headers.Authorization = `Bearer ${token}`;
      } else if (adminAuth) {
        const { token } = JSON.parse(adminAuth);
        config.headers.Authorization = `Bearer ${token}`;
      }
      
      return config;
    },
    (error) => Promise.reject(error)
  );

  return client;
};
