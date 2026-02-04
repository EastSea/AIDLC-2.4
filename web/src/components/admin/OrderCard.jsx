import React from 'react';

/**
 * Order card component for admin
 * @param {Object} props
 * @param {Object} props.order - Order data
 * @param {Function} props.onStatusChange - Status change callback
 * @param {Function} props.onDelete - Delete callback
 */
const OrderCard = ({ order, onStatusChange, onDelete }) => {
  return (
    <div className="order-card">
      <h3>주문 #{order.orderNumber}</h3>
      <p>테이블: {order.tableNumber}</p>
      
      <div className="order-items">
        {order.items.map((item, idx) => (
          <div key={idx}>
            {item.menuName} x {item.quantity}
          </div>
        ))}
      </div>
      
      <p>총 금액: {order.totalAmount.toLocaleString()}원</p>
      <p>주문 시간: {new Date(order.createdAt).toLocaleString()}</p>
      
      <div className="status-controls">
        <select
          value={order.status}
          onChange={(e) => onStatusChange(order.id, e.target.value)}
        >
          <option value="pending">대기중</option>
          <option value="preparing">조리중</option>
          <option value="completed">완료</option>
        </select>
      </div>
      
      <button onClick={() => onDelete(order.id)} className="delete-btn">
        삭제
      </button>
    </div>
  );
};

export default OrderCard;
