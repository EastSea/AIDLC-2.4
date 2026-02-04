import '@testing-library/jest-dom';

// Mock EventSource for SSE tests
global.EventSource = class EventSource {
  constructor(url) {
    this.url = url;
    this.readyState = 1;
  }
  close() {
    this.readyState = 2;
  }
  addEventListener() {}
  removeEventListener() {}
};

// Mock localStorage
const localStorageMock = {
  getItem: jest.fn(),
  setItem: jest.fn(),
  removeItem: jest.fn(),
  clear: jest.fn(),
};
global.localStorage = localStorageMock;
