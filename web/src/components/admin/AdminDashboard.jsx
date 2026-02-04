import React, { useEffect, useState } from 'react';
import { getAdminOrders, updateOrderStatus, deleteOrder } from '../../services/adminOrderService';
import { subscribeAdminOrders } from '../../services/sseService';
import { useAuth } from '../../hooks/useAuth';
import OrderCard from './OrderCard';

/**
 * Admin dashboard component
 */
const AdminDashboard = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();

  useEffect(() => {
    fetchOrders();
  }, []);

  useEffect(() => {
    if (!user?.token) return;

    const eventSource = subscribeAdminOrders(user.token, (data) => {
      if (data.type === 'new_order') {
        setOrders((prev) => [data.order, ...prev]);
      } else if (data.type === 'order_updated') {
        setOrders((prev) =>
          prev.map((order) =>
            order.id === data.order.id ? data.order : order
          )
        );
      }
    });

    return () => eventSource.close();
  }, [user?.token]);

  const fetchOrders = async () => {
    try {
      const data = await getAdminOrders();
      setOrders(data);
    } catch (err) {
      console.error('Failed to fetch orders:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleStatusChange = async (orderId, newStatus) => {
    try {
      await updateOrderStatus(orderId, newStatus);
      setOrders((prev) =>
        prev.map((order) =>
          order.id === orderId ? { ...order, status: newStatus } : order
        )
      );
    } catch (err) {
      alert('상태 변경 실패: ' + (err.response?.data?.message || err.message));
    }
  };

  const handleDelete = async (orderId) => {
    if (!window.confirm('정말 삭제하시겠습니까?')) return;

    try {
      await deleteOrder(orderId);
      setOrders((prev) => prev.filter((order) => order.id !== orderId));
    } catch (err) {
      alert('삭제 실패: ' + (err.response?.data?.message || err.message));
    }
  };

  if (loading) return <div>로딩 중...</div>;

  return (
    <div className="admin-dashboard">
      <h2>주문 관리</h2>
      
      {orders.length === 0 ? (
        <div>주문이 없습니다</div>
      ) : (
        <div className="orders-grid">
          {orders.map((order) => (
            <OrderCard
              key={order.id}
              order={order}
              onStatusChange={handleStatusChange}
              onDelete={handleDelete}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default AdminDashboard;
