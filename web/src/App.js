import { BrowserRouter, Routes, Route } from 'react-router-dom';

// Customer components
import CustomerLogin from './components/customer/CustomerLogin';
import MenuBrowser from './components/customer/MenuBrowser';
import MenuDetail from './components/customer/MenuDetail';
import Cart from './components/customer/Cart';
import OrderHistory from './components/customer/OrderHistory';

// Admin components
import AdminLogin from './components/admin/AdminLogin';
import AdminDashboard from './components/admin/AdminDashboard';
import MenuManagement from './components/admin/MenuManagement';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Customer routes */}
        <Route path="/" element={<MenuBrowser />} />
        <Route path="/login" element={<CustomerLogin />} />
        <Route path="/menu/:menuId" element={<MenuDetail />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/orders" element={<OrderHistory />} />
        
        {/* Admin routes */}
        <Route path="/admin/login" element={<AdminLogin />} />
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/admin/menus" element={<MenuManagement />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
