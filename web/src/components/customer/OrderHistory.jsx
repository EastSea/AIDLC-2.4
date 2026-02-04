import React, { useEffect, useState } from 'react';
import { useAuth } from '../../hooks/useAuth';
import { useOrders } from '../../hooks/useOrders';
import { subscribeOrderStatus } from '../../services/sseService';
import StaffCallButton from './StaffCallButton';

/**
 * Order history component
 * @param {Object} props
 * @param {string} props.sessionId - Session ID
 */
const OrderHistory = () => {
  const { user } = useAuth();
  const { orders, loading, refetch } = useOrders(user?.sessionId);
  const [liveOrders, setLiveOrders] = useState([]);

  useEffect(() => {
    setLiveOrders(orders);
  }, [orders]);

  useEffect(() => {
    if (!user?.tableId) return;

    const eventSource = subscribeOrderStatus(user.tableId, (data) => {
      setLiveOrders((prev) =>
        prev.map((order) =>
          order.id === data.orderId ? { ...order, status: data.status } : order
        )
      );
    });

    return () => eventSource.close();
  }, [user?.tableId]);

  const getStatusBadge = (status) => {
    const badges = {
      pending: '대기중',
      preparing: '조리중',
      completed: '완료',
    };
    return badges[status] || status;
  };

  if (loading) return <div>로딩 중...</div>;

  return (
    <div className="order-history">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h2>주문 내역</h2>
        {user?.tableId && <StaffCallButton tableId={user.tableId} />}
      </div>
      
      {liveOrders.length === 0 ? (
        <div>주문 내역이 없습니다</div>
      ) : (
        liveOrders.map((order) => (
          <div key={order.id} className="order-item">
            <h3>주문 #{order.orderNumber}</h3>
            <span className={`status-badge ${order.status}`}>
              {getStatusBadge(order.status)}
            </span>
            <div className="order-items">
              {order.items.map((item, idx) => (
                <div key={idx}>
                  {item.menuName} x {item.quantity}
                </div>
              ))}
            </div>
            <p>총 금액: {order.totalAmount.toLocaleString()}원</p>
            <p>주문 시간: {new Date(order.createdAt).toLocaleString()}</p>
          </div>
        ))
      )}
    </div>
  );
};

export default OrderHistory;
