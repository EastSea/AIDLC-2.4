import React, { useState } from 'react';
import { callStaff } from '../../services/staffService';

/**
 * Staff call button component
 * @param {Object} props
 * @param {string} props.tableId - Table ID
 */
const StaffCallButton = ({ tableId }) => {
  const [calling, setCalling] = useState(false);

  const handleCallStaff = async () => {
    setCalling(true);
    try {
      await callStaff(tableId);
      alert('직원을 호출했습니다');
    } catch (err) {
      alert('호출 실패: ' + (err.response?.data?.message || err.message));
    } finally {
      setCalling(false);
    }
  };

  return (
    <button
      className="staff-call-btn"
      onClick={handleCallStaff}
      disabled={calling}
    >
      {calling ? '호출 중...' : '직원 호출'}
    </button>
  );
};

export default StaffCallButton;
