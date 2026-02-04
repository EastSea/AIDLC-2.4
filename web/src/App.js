import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/customer/*" element={<div>Customer App</div>} />
        <Route path="/admin/*" element={<div>Admin App</div>} />
        <Route path="/" element={<div>Table Order Service</div>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
